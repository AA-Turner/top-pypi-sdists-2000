import asyncio
import aiofiles
import inspect
import logging
import math
from functools import partial
from io import BytesIO
from typing import Optional, Callable, BinaryIO, Dict, Any, Union
from abc import abstractmethod

from aiobotocore.context import with_current_context
from botocore.exceptions import ClientError
from botocore.useragent import register_feature_id
from boto3 import utils
from boto3.s3.transfer import S3TransferConfig, S3Transfer
from boto3.s3.inject import bucket_upload_file, bucket_download_file, bucket_copy, bucket_upload_fileobj, bucket_download_fileobj
from s3transfer.upload import UploadSubmissionTask
from s3transfer.copies import CopySubmissionTask

logger = logging.getLogger(__name__)


TransferCallback = Callable[[int], None]


class _AsyncBinaryIO:
    @abstractmethod
    async def seek(self, offset: int, whence: int = 0) -> int:
        pass

    @abstractmethod
    async def write(self, s: Union[bytes, bytearray]) -> int:
        pass


AnyFileObject = Union[_AsyncBinaryIO, BinaryIO]


def inject_s3_transfer_methods(class_attributes, **kwargs):
    utils.inject_attribute(class_attributes, 'upload_file', upload_file)
    utils.inject_attribute(class_attributes, 'download_file', download_file)
    utils.inject_attribute(class_attributes, 'copy', copy)
    utils.inject_attribute(class_attributes, 'upload_fileobj', upload_fileobj)
    utils.inject_attribute(
        class_attributes, 'download_fileobj', download_fileobj
    )


def inject_object_summary_methods(class_attributes, **kwargs):
    utils.inject_attribute(class_attributes, 'load', object_summary_load)


def inject_bucket_methods(class_attributes, **kwargs):
    utils.inject_attribute(class_attributes, 'load', bucket_load)
    utils.inject_attribute(class_attributes, 'upload_file', bucket_upload_file)
    utils.inject_attribute(
        class_attributes, 'download_file', bucket_download_file
    )
    utils.inject_attribute(class_attributes, 'copy', bucket_copy)
    utils.inject_attribute(
        class_attributes, 'upload_fileobj', bucket_upload_fileobj
    )
    utils.inject_attribute(
        class_attributes, 'download_fileobj', bucket_download_fileobj
    )


async def object_summary_load(self, *args, **kwargs):
    response = await self.meta.client.head_object(
        Bucket=self.bucket_name, Key=self.key
    )
    if 'ContentLength' in response:
        response['Size'] = response.pop('ContentLength')
    self.meta.data = response


@with_current_context(partial(register_feature_id, 'S3_TRANSFER'))
async def download_file(
    self,
    Bucket: str,
    Key: str,
    Filename: str,
    ExtraArgs: Optional[Dict[str, Any]] = None,
    Callback: Optional[TransferCallback] = None,
    Config: Optional[S3TransferConfig] = None
):
    """Download an S3 object to a file asynchronously.

    Usage::

        import aioboto3

        async with aioboto3.resource('s3') as s3:
            await s3.meta.client.download_file('mybucket', 'hello.txt', '/tmp/hello.txt')

    Similar behaviour as S3Transfer's download_file() method,
    except that parameters are capitalised.
    """
    async with aiofiles.open(Filename, 'wb') as fileobj:  # type: _AsyncBinaryIO
        await download_fileobj(
            self,
            Bucket,
            Key,
            fileobj,
            ExtraArgs=ExtraArgs,
            Callback=Callback,
            Config=Config
        )


async def _download_part(self, bucket: str, key: str, extraArgs: Dict[str, str], headers: Dict[str, str], start: int, file: AnyFileObject, semaphore: asyncio.Semaphore, write_lock: asyncio.Lock,
                         callback=None, io_queue: Optional[asyncio.Queue] = None) -> None:
    async with semaphore:  # limit number of concurrent downloads
        response = await self.get_object(
            Bucket=bucket, Key=key, Range=headers['Range'], **extraArgs
        )
        content = await response['Body'].read()

        # If stream is not seekable, return the offset and data so it can be queued up to be written
        if io_queue:
            await io_queue.put((start, content))
        else:
            # Check if it's aiofiles file
            if inspect.iscoroutinefunction(file.seek) and inspect.iscoroutinefunction(file.write):
                # These operations need to happen sequentially, which is non-deterministic when dealing with event loops
                async with write_lock:
                    await file.seek(start)
                    await file.write(content)
            else:
                # Fallback to synchronous operations for file objects that are not async
                file.seek(start)
                file.write(content)

        # Call the wrapper callback with the number of bytes written, if provided
        if callback:
            try:
                callback(len(content))
            except:  # noqa: E722
                pass


@with_current_context(partial(register_feature_id, 'S3_TRANSFER'))
async def download_fileobj(
    self,
    Bucket: str,
    Key: str,
    Fileobj: AnyFileObject,
    ExtraArgs: Optional[Dict[str, Any]] = None,
    Callback: Optional[TransferCallback] = None,
    Config: Optional[S3TransferConfig] = None
):
    """Download an object from S3 to a file-like object.

    The file-like object must be in binary mode.

    This is a managed transfer which will perform a multipart download
    with asyncio if necessary.

    Usage::

        import boto3
        s3 = boto3.client('s3')

        async with aiofiles.open('filename', 'wb') as data:
            await s3.download_fileobj('mybucket', 'mykey', data)

    :type Fileobj: a file-like object
    :param Fileobj: A file-like object to download into. At a minimum, it must
        implement the `write` method and must accept bytes.

    :type Bucket: str
    :param Bucket: The name of the bucket to download from.

    :type Key: str
    :param Key: The name of the key to download from.

    :type ExtraArgs: dict
    :param ExtraArgs: Extra arguments that may be passed to the
        client operation.

    :type Callback: method
    :param Callback: A method which takes a number of bytes transferred to
        be periodically called during the download.

    :type Config: boto3.s3.transfer.TransferConfig
    :param Config: The transfer configuration to be used when performing the
        download.
    """

    Config = Config or S3TransferConfig()
    ExtraArgs = ExtraArgs or {}

    try:
        # Get object metadata to determine the total size
        head_response = await self.head_object(Bucket=Bucket, Key=Key, **ExtraArgs)
    except ClientError as err:
        if err.response['Error']['Code'] == 'NoSuchKey':
            # Convert to 404 so it looks the same when boto3.download_file fails
            raise ClientError({'Error': {'Code': '404', 'Message': 'Not Found'}}, 'HeadObject')
        raise

    # Semaphore to limit the number of concurrent downloads
    semaphore = asyncio.Semaphore(Config.max_request_concurrency)
    write_mutex = asyncio.Lock()

    total_size = head_response['ContentLength']
    total_parts = (total_size + Config.multipart_chunksize - 1) // Config.multipart_chunksize

    # Keep track of total downloaded bytes
    total_downloaded = 0

    def wrapper_callback(bytes_transferred):
        nonlocal total_downloaded
        total_downloaded += bytes_transferred
        if Callback:
            try:
                Callback(total_downloaded)
            except:  # noqa: E722
                pass

    is_seekable = hasattr(Fileobj, "seek")

    # This'll have around `semaphore` length items, somewhat more if writing is slow
    # TODO add limits so we dont fill up this list n blow out ram
    io_list = []

    # This should be Config.io_concurrency but as we're gathering all coro's we cant guarantee
    # that the co-routines will start in relative order so we could fill up the queue with the
    # x chunks and if we're not writing to a seekable stream then it'll deadlock.
    io_queue = asyncio.Queue()

    async def queue_reader():
        """
        Pretty much, get things off queue, add them to list
        Go through list, write things to file object in order
        """
        is_async = inspect.iscoroutinefunction(Fileobj.write)

        try:
            written_pos = 0
            while written_pos < total_size:
                io_list.append(await io_queue.get())

                # Stuff might be out of order in io_list
                # so spin until there's nothing to queue off
                done_nothing = False
                while not done_nothing:
                    done_nothing = True

                    indexes_to_remove = []
                    for index, (chunk_start, data) in enumerate(io_list):
                        if chunk_start == written_pos:
                            if is_async:
                                await Fileobj.write(data)
                            else:
                                Fileobj.write(data)

                            indexes_to_remove.append(index)
                            written_pos += len(data)
                            done_nothing = False

                    for index in reversed(indexes_to_remove):
                        io_list.pop(index)
        except asyncio.CancelledError:
            pass

    queue_reader_future = None
    if not is_seekable:
        queue_reader_future = asyncio.ensure_future(queue_reader())

    try:
        tasks = []
        for i in range(total_parts):
            start = i * Config.multipart_chunksize
            end = min(
                start + Config.multipart_chunksize, total_size
            )  # Ensure we don't go beyond the total size
            # Range headers, start at 0 so end which would be total_size, minus 1 = 0 indexed.
            headers = {'Range': f'bytes={start}-{end - 1}'}
            # Create a task for each part download
            tasks.append(
                _download_part(self, Bucket, Key, ExtraArgs, headers, start, Fileobj, semaphore, write_mutex, wrapper_callback, io_queue if not is_seekable else None)
            )

        # Run all the download tasks concurrently
        await asyncio.gather(*tasks)  # TODO might not be worth spamming the eventloop with 1000's of tasks, but deal with it when its a problem.

        if queue_reader_future:
            await queue_reader_future

        logger.debug(f'Downloaded file from {Bucket}/{Key}')

    except ClientError as e:
        raise Exception(
            f"Couldn't download file from {Bucket}/{Key}"
        ) from e


@with_current_context(partial(register_feature_id, 'S3_TRANSFER'))
async def upload_fileobj(
    self,
    Fileobj: AnyFileObject,
    Bucket: str,
    Key: str,
    ExtraArgs: Optional[Dict[str, Any]] = None,
    Callback: Optional[TransferCallback] = None,
    Config: Optional[S3TransferConfig] = None,
    Processing: Callable[[bytes], bytes] = None
):
    """Upload a file-like object to S3.

    The file-like object must be in binary mode.

    This is a managed transfer which will perform a multipart upload in
    multiple threads if necessary.

    Usage::

        import boto3
        s3 = boto3.client('s3')

        with open('filename', 'rb') as data:
            s3.upload_fileobj(data, 'mybucket', 'mykey')

    :type Fileobj: a file-like object
    :param Fileobj: A file-like object to upload. At a minimum, it must
        implement the `read` method, and must return bytes.

    :type Bucket: str
    :param Bucket: The name of the bucket to upload to.

    :type Key: str
    :param Key: The name of the key to upload to.

    :type ExtraArgs: dict
    :param ExtraArgs: Extra arguments that may be passed to the
        client operation.

    :type Callback: method
    :param Callback: A method which takes a number of bytes transferred to
        be periodically called during the upload.

    :type Config: boto3.s3.transfer.TransferConfig
    :param Config: The transfer configuration to be used when performing the
        upload.

    :type Processing: method
    :param Processing: A method which takes a bytes buffer and convert it
        by custom logic.
    """
    kwargs = ExtraArgs or {}
    upload_part_args = {k: v for k, v in kwargs.items() if k in UploadSubmissionTask.UPLOAD_PART_ARGS}
    complete_upload_args = {k: v for k, v in kwargs.items() if k in UploadSubmissionTask.COMPLETE_MULTIPART_ARGS}
    Config = Config or S3TransferConfig()

    async def fileobj_read(num_bytes: int) -> bytes:
        data = Fileobj.read(num_bytes)
        if inspect.isawaitable(data):
            data = await data
        else:
            await asyncio.sleep(0.0)  # Yield to the eventloop incase .read() took ages

        return data

    # So some streams might return less than Config.multipart_threshold on a read, but that might not be eof
    initial_data = b''
    while len(initial_data) < Config.multipart_threshold:
        new_data = await fileobj_read(Config.multipart_threshold)
        if new_data == b'':
            break
        initial_data += new_data

    if len(initial_data) < Config.multipart_threshold:
        # Do Processing hook here, else it'll happen during the multipart
        # upload loop too
        if Processing:
            initial_data = Processing(initial_data)

        # Do put_object
        await self.put_object(
            Bucket=Bucket,
            Key=Key,
            Body=initial_data,
            **kwargs
        )
        if Callback:
            if inspect.iscoroutinefunction(Callback):
                await Callback(len(initial_data))
            else:
                Callback(len(initial_data))
        return

    # File bigger than threshold, start multipart upload
    resp = await self.create_multipart_upload(Bucket=Bucket, Key=Key, **kwargs)
    upload_id = resp['UploadId']
    finished_parts = []
    expected_parts = 0
    io_queue = asyncio.Queue(maxsize=Config.max_io_queue_size)
    exception_event = asyncio.Event()
    exception = None
    sent_bytes = 0

    async def uploader() -> int:
        nonlocal sent_bytes
        nonlocal exception
        uploaded_parts = 0

        # Loop whilst no other co-routine has raised an exception
        while not exception:
            try:
                part_args = await io_queue.get()
            except asyncio.CancelledError:
                break

            # Submit part to S3
            try:
                resp = await self.upload_part(**part_args)
            except Exception as err:
                # Set the main exception variable to the current exception, trigger the exception event
                exception = err
                exception_event.set()
                # Exit the coro
                break

            # Success, add the result to the finished_parts, increment the sent_bytes

            finished_parts_kwargs = {}
            if 'ChecksumAlgorithm' in kwargs:
                for key in resp:
                    if key.startswith('Checksum'):
                        finished_parts_kwargs[key] = resp[key]
            finished_parts.append(
                {'ETag': resp['ETag'], 'PartNumber': part_args['PartNumber'], **finished_parts_kwargs})
            current_bytes = len(part_args['Body'])
            sent_bytes += current_bytes
            uploaded_parts += 1
            logger.debug('Uploaded part to S3')

            # Call the callback, if it blocks then not good :/
            if Callback:
                try:
                    if inspect.iscoroutinefunction(Callback):
                        await Callback(current_bytes)
                    else:
                        Callback(current_bytes)
                except:  # noqa: E722
                    pass

            # Mark task as done so .join() will work later on
            io_queue.task_done()

        # For testing return number of parts uploaded
        return uploaded_parts

    async def file_reader() -> None:
        nonlocal expected_parts
        nonlocal exception
        part = 0
        eof = False
        while not exception and not eof:
            part += 1
            multipart_payload = bytearray()
            if part == 1:  # Add in the initial data we've read to check if we've met the multipart threshold
                multipart_payload += initial_data

            loop_counter = 0
            while len(multipart_payload) < Config.multipart_chunksize:
                try:
                    # Handles if .read() returns anything that can be awaited
                    data = await fileobj_read(Config.io_chunksize)
                except Exception as err:
                    # Caught some random exception whilst reading from a file
                    exception = err
                    exception_event.set()

                    # shortcircuit upload logic
                    eof = True
                    multipart_payload = bytearray()
                    break

                if data == b'' and loop_counter > 0:  # End of file, handles uploading empty files
                    eof = True
                    break
                multipart_payload += data
                loop_counter += 1

            # If file has ended but chunk has some data in it, upload it,
            # else if file ended just after a chunk then exit
            # if the first part is b'' then upload it as we're uploading an empty
            # file
            if not multipart_payload and part != 1:
                break

            if Processing:
                multipart_payload = Processing(multipart_payload)

            await io_queue.put({'Body': multipart_payload, 'Bucket': Bucket, 'Key': Key,
                                'PartNumber': part, 'UploadId': upload_id, **upload_part_args})
            logger.debug('Added part to io_queue')
            expected_parts += 1

    file_reader_future = asyncio.ensure_future(file_reader())
    futures = [asyncio.ensure_future(uploader()) for _ in range(0, Config.max_request_concurrency)]

    # Wait for file reader to finish
    try:
        await file_reader_future
    except Exception as err:
        # if the file reader raises, we need to clean up the uploaders
        exception = err
        exception_event.set()
    # So by this point all of the file is read and in a queue

    # wait for either io queue is finished, or an exception has been raised
    _, pending = await asyncio.wait(
        {asyncio.create_task(io_queue.join()), asyncio.create_task(exception_event.wait())},
        return_when=asyncio.FIRST_COMPLETED
    )

    if exception_event.is_set() or len(finished_parts) != expected_parts:
        # An exception during upload or for some reason the finished parts dont match the expected parts, cancel upload
        await self.abort_multipart_upload(Bucket=Bucket, Key=Key, UploadId=upload_id)
        # Raise exception later after we've disposed of the pending co-routines
    else:
        # All io chunks from the queue have been successfully uploaded
        try:
            # Sort the finished parts as they must be in order
            finished_parts.sort(key=lambda item: item['PartNumber'])

            await self.complete_multipart_upload(
                Bucket=Bucket,
                Key=Key,
                UploadId=upload_id,
                MultipartUpload={'Parts': finished_parts},
                **complete_upload_args
            )
        except Exception as err:
            # We failed to complete the upload, try and abort, then return the orginal error
            exception = err
            try:
                await self.abort_multipart_upload(Bucket=Bucket, Key=Key, UploadId=upload_id)
            except:
                pass

    # Close either the Queue.join() coro, or the event.wait() coro
    for coro in pending:
        if not coro.done():
            coro.cancel()
            try:
                await coro
            except:
                pass

    # Cancel any remaining futures, though if successful they'll be done
    cancelled = []
    for future in futures:
        if not future.done():
            future.cancel()
            cancelled.append(future)
        else:
            uploaded_parts = future.result()
            logger.debug('Future uploaded {0} parts'.format(uploaded_parts))
    if cancelled:
        for uploaded_parts in await asyncio.gather(*cancelled, return_exceptions=True):
            if isinstance(uploaded_parts, int):
                logger.debug('Future uploaded {0} parts'.format(uploaded_parts))

    # Raise an exception now after everythings cleaned up
    if exception:
        raise exception


@with_current_context(partial(register_feature_id, 'S3_TRANSFER'))
async def upload_file(
    self,
    Filename: str,
    Bucket: str,
    Key: str,
    ExtraArgs: Optional[Dict[str, Any]] = None,
    Callback: Optional[TransferCallback] = None,
    Config: Optional[S3TransferConfig] = None
):
    """Upload a file to an S3 object.

    Usage::

        import boto3
        async with aioboto3.resource('s3') as s3:
            await s3.meta.client.upload_file('/tmp/hello.txt', 'mybucket', 'hello.txt')

    Similar behavior as S3Transfer's upload_file() method,
    except that parameters are capitalized.
    """
    async with aiofiles.open(Filename, 'rb') as open_file:
        await upload_fileobj(
            self,
            open_file,
            Bucket,
            Key,
            ExtraArgs=ExtraArgs,
            Callback=Callback,
            Config=Config
        )


@with_current_context(partial(register_feature_id, 'S3_TRANSFER'))
async def copy(
    self,
    CopySource: Dict[str, Any],
    Bucket: str,
    Key: str,
    ExtraArgs: Optional[Dict[str, Any]] = None,
    Callback: Optional[TransferCallback] = None,
    SourceClient=None,  # Should be aioboto3/aiobotocore client
    Config: Optional[S3TransferConfig] = None
):
    assert 'Bucket' in CopySource
    assert 'Key' in CopySource

    SourceClient = SourceClient or self
    Config = Config or S3TransferConfig()
    ExtraArgs = ExtraArgs or {}

    try:
        head_object_kwargs = {}
        for param, value in ExtraArgs.items():
            if param in CopySubmissionTask.EXTRA_ARGS_TO_HEAD_ARGS_MAPPING:
                head_object_kwargs[CopySubmissionTask.EXTRA_ARGS_TO_HEAD_ARGS_MAPPING[param]] = value

        # Get object metadata to determine the total size
        head_response = await SourceClient.head_object(Bucket=CopySource['Bucket'], Key=CopySource['Key'], **head_object_kwargs)
    except ClientError as err:
        if err.response['Error']['Code'] == 'NoSuchKey':
            # Convert to 404 so it looks the same when boto3.download_file fails
            raise ClientError({'Error': {'Code': '404', 'Message': 'Not Found'}}, 'HeadObject')
        raise

    # So CopyObject works up to 5GiB, but S3Transfer uses Config.MultipartThreshold which by default is 8MiB :unamused:
    if head_response['ContentLength'] < Config.multipart_threshold:
        await self.copy_object(CopySource=CopySource, Bucket=Bucket, Key=Key, **ExtraArgs)
        return

    # File is larger than 5GiB, do multipart copy
    create_multipart_kwargs = {k: v for k, v in ExtraArgs.items() if k not in CopySubmissionTask.CREATE_MULTIPART_ARGS_BLACKLIST}
    create_multipart_upload_resp = await self.create_multipart_upload(Bucket=Bucket, Key=Key, **create_multipart_kwargs)

    finished_parts = []
    total_size = 0

    sem = asyncio.Semaphore(Config.max_request_concurrency)

    async def uploader(size: int, part_args: Dict[str, Any]):
        nonlocal total_size

        async with sem:
            upload_part_response = await self.upload_part_copy(**part_args)

        finished_parts.append({'ETag': upload_part_response['CopyPartResult']['ETag'], 'PartNumber': part_args['PartNumber']})

        # Call the callback, if it blocks then not good :/
        if Callback:
            try:
                total_size += size
                Callback(total_size)
            except:  # noqa: E722
                pass

    num_parts = int(math.ceil(head_response['ContentLength'] / float(Config.multipart_chunksize)))

    tasks = []
    upload_kwargs = {k: v for k, v in ExtraArgs.items() if k in CopySubmissionTask.UPLOAD_PART_COPY_ARGS}
    upload_kwargs.update({'Bucket': Bucket, 'Key': Key, 'CopySource': CopySource, 'UploadId': create_multipart_upload_resp['UploadId']})
    for part_number in range(1, num_parts + 1):
        part_upload_kwargs = upload_kwargs.copy()
        part_upload_kwargs['PartNumber'] = part_number

        range_start = (part_number - 1) * Config.multipart_chunksize
        range_end = range_start + Config.multipart_chunksize - 1
        if part_number == num_parts:
            range_end = head_response['ContentLength'] - 1

        part_upload_kwargs['CopySourceRange'] = f'bytes={range_start}-{range_end}'

        tasks.append(uploader(range_end-range_start, part_upload_kwargs))

    try:
        await asyncio.gather(*tasks)

        assert len(finished_parts) == num_parts, "Number of finished upload parts does not match expected parts"

        finished_parts.sort(key=lambda item: item['PartNumber'])

        complete_upload_args = {k: v for k, v in ExtraArgs.items() if k in CopySubmissionTask.COMPLETE_MULTIPART_ARGS}
        await self.complete_multipart_upload(
            Bucket=Bucket,
            Key=Key,
            UploadId=create_multipart_upload_resp['UploadId'],
            MultipartUpload={'Parts': finished_parts},
            **complete_upload_args
        )

    except Exception as err:
        try:
            await self.abort_multipart_upload(Bucket=Bucket, Key=Key, UploadId=create_multipart_upload_resp['UploadId'])
        except Exception as err2:
            raise err2 from err
        raise err


async def bucket_load(self, *args, **kwargs):
    """
    Calls s3.Client.list_buckets() to update the attributes of the Bucket
    resource.
    """
    # The docstring above is phrased this way to match what the autogenerated
    # docs produce.

    # We can't actually get the bucket's attributes from a HeadBucket,
    # so we need to use a ListBuckets and search for our bucket.
    # However, we may fail if we lack permissions to ListBuckets
    # or the bucket is in another account. In which case, creation_date
    # will be None.
    self.meta.data = {}
    try:
        response = await self.meta.client.list_buckets()
        for bucket_data in response['Buckets']:
            if bucket_data['Name'] == self.name:
                self.meta.data = bucket_data
                break
    except ClientError as e:
        if not e.response.get('Error', {}).get('Code') == 'AccessDenied':
            raise
