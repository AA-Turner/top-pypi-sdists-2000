from ctypes import c_int
from enum import IntEnum
import json
from multiprocessing import Process
from multiprocessing import Value
import os
import time
from typing import Dict  # noqa:F401
from typing import List  # noqa:F401
from typing import Optional  # noqa:F401
from typing import Tuple  # noqa:F401
from urllib.parse import urljoin

from ddtrace.ext import ci
from ddtrace.ext.git import _build_git_packfiles_with_details
from ddtrace.ext.git import _extract_clone_defaultremotename_with_details
from ddtrace.ext.git import _extract_latest_commits_with_details
from ddtrace.ext.git import _extract_upstream_sha
from ddtrace.ext.git import _get_rev_list_with_details
from ddtrace.ext.git import _is_shallow_repository_with_details
from ddtrace.ext.git import _unshallow_repository
from ddtrace.ext.git import _unshallow_repository_with_details
from ddtrace.ext.git import extract_commit_sha
from ddtrace.ext.git import extract_git_version
from ddtrace.ext.git import extract_remote_url
from ddtrace.ext.git import extract_workspace_path
from ddtrace.internal.logger import get_logger
from ddtrace.internal.utils.retry import fibonacci_backoff_with_jitter
from ddtrace.settings._agent import config as agent_config
from ddtrace.settings._telemetry import config as telemetry_config
from ddtrace.trace import Tracer  # noqa: F401

from .. import telemetry
from ..utils.http import Response
from ..utils.http import get_connection
from ..utils.http import verify_url
from ..utils.time import StopWatch
from .constants import AGENTLESS_API_KEY_HEADER_NAME
from .constants import AGENTLESS_DEFAULT_SITE
from .constants import EVP_PROXY_AGENT_BASE_PATH
from .constants import EVP_SUBDOMAIN_HEADER_API_VALUE
from .constants import EVP_SUBDOMAIN_HEADER_NAME
from .constants import GIT_API_BASE_PATH
from .constants import REQUESTS_MODE
from .telemetry.constants import ERROR_TYPES
from .telemetry.constants import GIT_TELEMETRY_COMMANDS
from .telemetry.git import record_git_command
from .telemetry.git import record_objects_pack_data
from .telemetry.git import record_objects_pack_request
from .telemetry.git import record_search_commits


log = get_logger(__name__)

# this exists only for the purpose of mocking in tests
RESPONSE = None

# we're only interested in uploading .pack files
PACK_EXTENSION = ".pack"

DEFAULT_TIMEOUT = 20

DEFAULT_METADATA_UPLOAD_TIMEOUT = 120


class METADATA_UPLOAD_STATUS(IntEnum):
    PENDING = 0
    IN_PROCESS = 1
    SUCCESS = 2
    FAILED = 3
    UNNECESSARY = 4


FINISHED_METADATA_UPLOAD_STATUSES = [
    METADATA_UPLOAD_STATUS.FAILED,
    METADATA_UPLOAD_STATUS.SUCCESS,
    METADATA_UPLOAD_STATUS.UNNECESSARY,
]


class CIVisibilityGitClient(object):
    def __init__(
        self,
        api_key,
        requests_mode=REQUESTS_MODE.AGENTLESS_EVENTS,
        tracer=None,
    ):
        # type: (str, int, Optional[Tracer]) -> None
        self._serializer = CIVisibilityGitClientSerializerV1(api_key)
        self._worker = None  # type: Optional[Process]
        self._response = RESPONSE
        self._requests_mode = requests_mode
        self._metadata_upload_status = Value(c_int, METADATA_UPLOAD_STATUS.PENDING, lock=True)

        if self._requests_mode == REQUESTS_MODE.EVP_PROXY_EVENTS:
            tracer_url = agent_config.trace_agent_url if tracer is None else tracer._agent_url
            self._base_url = urljoin(tracer_url, EVP_PROXY_AGENT_BASE_PATH + GIT_API_BASE_PATH)
        elif self._requests_mode == REQUESTS_MODE.AGENTLESS_EVENTS:
            self._base_url = urljoin(
                "https://api.{}".format(
                    os.getenv("DD_SITE", AGENTLESS_DEFAULT_SITE),
                ),
                GIT_API_BASE_PATH,
            )

    def _get_git_dir(self, cwd=None):
        # type: (Optional[str]) -> Optional[str]
        try:
            return extract_workspace_path(cwd=cwd)
        except (FileNotFoundError, ValueError):
            return None

    def upload_git_metadata(self, cwd=None):
        # type: (Optional[str]) -> None
        if not self._get_git_dir(cwd=cwd):
            log.debug("Missing .git directory; skipping git metadata upload")
            self._metadata_upload_status.value = METADATA_UPLOAD_STATUS.FAILED
            return

        self._tags = ci.tags(cwd=cwd)
        if self._worker is None:
            self._worker = Process(
                target=CIVisibilityGitClient._run_protocol,
                args=(self._serializer, self._requests_mode, self._base_url, self._metadata_upload_status),
                kwargs={"_tags": self._tags, "_response": self._response, "cwd": cwd, "log_level": log.level},
            )
            self._worker.start()
            log.debug("Upload git metadata to URL %s started with PID %s", self._base_url, self._worker.pid)
        else:
            log.debug("git metadata upload worker already started: %s", self._worker)

    def metadata_upload_finished(self):
        return self._metadata_upload_status.value in FINISHED_METADATA_UPLOAD_STATUSES

    def _wait_for_metadata_upload(self, timeout=DEFAULT_METADATA_UPLOAD_TIMEOUT):
        log.debug("Waiting up to %s seconds for git metadata upload to finish", timeout)
        if self._worker is None:
            log.debug("No git metadata upload worker started")
            return
        with StopWatch() as stopwatch:
            while not self.metadata_upload_finished():
                log.debug("Waited %s so far, status is %s", stopwatch.elapsed(), self._metadata_upload_status.value)
                if stopwatch.elapsed() >= timeout:
                    raise TimeoutError(
                        "Timed out waiting for git metadata upload to complete after %s seconds" % timeout
                    )

                if self._worker.exitcode is not None:
                    log.debug(
                        "git metadata process exited with exitcode %s but upload status is %s",
                        self._worker.exitcode,
                        self._metadata_upload_status.value,
                    )
                    raise ValueError("git metadata process exited with exitcode %s", self._worker.exitcode)

                self._worker.join(timeout=1)
                time.sleep(1)
        log.debug("git metadata upload completed, waited %s seconds", stopwatch.elapsed())

    def wait_for_metadata_upload_status(self):
        # type: () -> METADATA_UPLOAD_STATUS
        self._wait_for_metadata_upload()
        return self._metadata_upload_status.value  # type: ignore

    @classmethod
    def _run_protocol(
        cls,
        serializer,  # CIVisibilityGitClientSerializerV1
        requests_mode,  # int
        base_url,  # str
        _metadata_upload_status,  # METADATA_UPLOAD_STATUS
        _tags=None,  # Optional[Dict[str, str]]
        _response=None,  # Optional[Response]
        cwd=None,  # Optional[str]
        log_level=0,  # int
    ):
        # type: (...) -> None
        log.setLevel(log_level)
        _metadata_upload_status.value = METADATA_UPLOAD_STATUS.IN_PROCESS
        try:
            if _tags is None:
                _tags = {}
            repo_url = cls._get_repository_url(tags=_tags, cwd=cwd)

            # If all latest commits are known to our gitdb backend, assume that unshallowing is unnecessary
            latest_commits = cls._get_latest_commits(cwd=cwd)
            backend_commits = cls._search_commits(
                requests_mode, base_url, repo_url, latest_commits, serializer, _response
            )

            if backend_commits is None:
                log.debug("No initial backend commits found, returning early.")
                _metadata_upload_status.value = METADATA_UPLOAD_STATUS.FAILED
                return

            commits_not_in_backend = list(set(latest_commits) - set(backend_commits))

            if len(commits_not_in_backend) == 0:
                log.debug("All latest commits found in backend, skipping metadata upload")
                _metadata_upload_status.value = METADATA_UPLOAD_STATUS.UNNECESSARY
                return

            if cls._is_shallow_repository(cwd=cwd) and extract_git_version(cwd=cwd) >= (2, 27, 0):
                log.debug("Shallow repository detected on git > 2.27 detected, unshallowing")
                try:
                    cls._unshallow_repository(cwd=cwd)
                except ValueError:
                    log.warning("Failed to unshallow repository, continuing to send pack data", exc_info=True)

            latest_commits = cls._get_latest_commits(cwd=cwd)
            backend_commits = cls._search_commits(
                requests_mode, base_url, repo_url, latest_commits, serializer, _response
            )
            if backend_commits is None:
                log.debug("No backend commits found, returning early.")
                _metadata_upload_status.value = METADATA_UPLOAD_STATUS.FAILED
                return

            commits_not_in_backend = list(set(latest_commits) - set(backend_commits))

            rev_list = cls._get_filtered_revisions(
                excluded_commits=backend_commits, included_commits=commits_not_in_backend, cwd=cwd
            )
            if rev_list:
                log.debug("Building and uploading packfiles for revision list: %s", rev_list)
                with _build_git_packfiles_with_details(rev_list, cwd=cwd) as (packfiles_prefix, packfiles_details):
                    record_git_command(
                        GIT_TELEMETRY_COMMANDS.PACK_OBJECTS, packfiles_details.duration, packfiles_details.returncode
                    )
                    if packfiles_details.returncode == 0:
                        if cls._upload_packfiles(
                            requests_mode, base_url, repo_url, packfiles_prefix, serializer, _response, cwd=cwd
                        ):
                            _metadata_upload_status.value = METADATA_UPLOAD_STATUS.SUCCESS
                            return
                    _metadata_upload_status.value = METADATA_UPLOAD_STATUS.FAILED
                    log.warning("Failed to upload git metadata packfiles")
            else:
                log.debug("Revision list empty, no packfiles to build and upload")
                _metadata_upload_status.value = METADATA_UPLOAD_STATUS.SUCCESS
                record_objects_pack_data(0, 0)
        finally:
            telemetry_config.DEPENDENCY_COLLECTION = False
            telemetry.telemetry_writer.periodic(force_flush=True)

    @classmethod
    def _get_repository_url(cls, tags=None, cwd=None):
        # type: (Optional[Dict[str, str]], Optional[str]) -> str
        if tags is None:
            tags = {}
        result = tags.get(ci.git.REPOSITORY_URL, "")
        if not result:
            result = extract_remote_url(cwd=cwd)
        return result

    @classmethod
    def _get_latest_commits(cls, cwd=None):
        # type: (Optional[str]) -> List[str]
        latest_commits, stderr, duration, returncode = _extract_latest_commits_with_details(cwd=cwd)
        record_git_command(GIT_TELEMETRY_COMMANDS.GET_LOCAL_COMMITS, duration, returncode)
        if returncode == 0:
            return latest_commits.split("\n") if latest_commits else []
        raise ValueError(stderr)

    @classmethod
    def _search_commits(cls, requests_mode, base_url, repo_url, latest_commits, serializer, _response):
        # type: (int, str, str, List[str], CIVisibilityGitClientSerializerV1, Optional[Response]) -> Optional[List[str]]
        payload = serializer.search_commits_encode(repo_url, latest_commits)
        request_error = None
        with StopWatch() as stopwatch:
            try:
                try:
                    response = _response or cls._do_request(
                        requests_mode, base_url, "/search_commits", payload, serializer
                    )
                except TimeoutError:
                    request_error = ERROR_TYPES.TIMEOUT
                    log.warning("Timeout searching commits")
                    return None

                if response.status >= 400:
                    request_error = ERROR_TYPES.CODE_4XX if response.status < 500 else ERROR_TYPES.CODE_5XX
                    log.debug(
                        "Error searching commits, response status code: %s , response body: %s",
                        response.status,
                        response.body,
                    )
                    log.debug("Response body: %s", response.body)
                    return None

                try:
                    result = serializer.search_commits_decode(response.body)
                    return result
                except json.JSONDecodeError:
                    request_error = ERROR_TYPES.BAD_JSON
                    log.warning("Error searching commits, response not parsable: %s", response.body)
                    return None
            finally:
                record_search_commits(stopwatch.elapsed() * 1000, error=request_error)

    @classmethod
    @fibonacci_backoff_with_jitter(attempts=5, until=lambda result: isinstance(result, Response))
    def _do_request(cls, requests_mode, base_url, endpoint, payload, serializer, headers=None, timeout=DEFAULT_TIMEOUT):
        # type: (int, str, str, str, CIVisibilityGitClientSerializerV1, Optional[dict], int) -> Response
        url = "{}/repository{}".format(base_url, endpoint)
        _headers = {
            AGENTLESS_API_KEY_HEADER_NAME: serializer.api_key,
        }
        if requests_mode == REQUESTS_MODE.EVP_PROXY_EVENTS:
            _headers = {
                EVP_SUBDOMAIN_HEADER_NAME: EVP_SUBDOMAIN_HEADER_API_VALUE,
            }
        if headers is not None:
            _headers.update(headers)
        try:
            parsed_url = verify_url(url)
            url_path = parsed_url.path
            conn = get_connection(url, timeout=timeout)
            log.debug("Sending request: %s %s %s %s", "POST", url_path, payload, _headers)
            conn.request("POST", url_path, payload, _headers)
            resp = conn.getresponse()
            log.debug("Response status: %s", resp.status)
            result = Response.from_http_response(resp)
        finally:
            conn.close()
        return result

    @classmethod
    def _get_filtered_revisions(cls, excluded_commits, included_commits=None, cwd=None):
        # type: (List[str], Optional[List[str]], Optional[str]) -> str
        filtered_revisions, _, duration, returncode = _get_rev_list_with_details(
            excluded_commits, included_commits, cwd=cwd
        )
        record_git_command(GIT_TELEMETRY_COMMANDS.GET_OBJECTS, duration, returncode if returncode != 0 else None)
        return filtered_revisions

    @classmethod
    def _upload_packfiles(cls, requests_mode, base_url, repo_url, packfiles_prefix, serializer, _response, cwd=None):
        # type: (int, str, str, str, CIVisibilityGitClientSerializerV1, Optional[Response], Optional[str]) -> bool

        sha = extract_commit_sha(cwd=cwd)
        parts = packfiles_prefix.split("/")
        directory = "/".join(parts[:-1])
        rand = parts[-1]
        packfiles_uploaded_count = 0
        packfiles_uploaded_bytes = 0
        for filename in os.listdir(directory):
            if not filename.startswith(rand) or not filename.endswith(PACK_EXTENSION):
                continue
            file_path = os.path.join(directory, filename)
            content_type, payload = serializer.upload_packfile_encode(repo_url, sha, file_path)
            headers = {"Content-Type": content_type}
            with StopWatch() as stopwatch:
                error_type = None
                try:
                    response = _response or cls._do_request(
                        requests_mode, base_url, "/packfile", payload, serializer, headers=headers
                    )
                    if response.status == 204:
                        packfiles_uploaded_count += 1
                        packfiles_uploaded_bytes += len(payload)
                    elif response.status >= 400:
                        log.debug(
                            "Git packfile upload request for file %s (sizee: %s) failed with status: %s",
                            filename,
                            len(payload),
                            response.status,
                        )
                        error_type = ERROR_TYPES.CODE_4XX if response.status < 500 else ERROR_TYPES.CODE_5XX
                except ConnectionRefusedError:
                    error_type = ERROR_TYPES.NETWORK
                    log.debug("Git packfile upload request for file %s failed: connection refused", filename)
                except TimeoutError:
                    error_type = ERROR_TYPES.TIMEOUT
                    log.debug("Git packfile upload request for file %s (size: %s) timed out", filename, len(payload))
                finally:
                    duration = stopwatch.elapsed() * 1000  # StopWatch is in seconds
                    record_objects_pack_request(duration, error_type)

        record_objects_pack_data(packfiles_uploaded_count, packfiles_uploaded_bytes)
        log.debug(
            "Git packfiles upload succeeded, file count: %s, total size: %s",
            packfiles_uploaded_count,
            packfiles_uploaded_bytes,
        )

        return response.status == 204

    @classmethod
    def _is_shallow_repository(cls, cwd=None):
        # type () -> bool
        is_shallow_repository, duration, returncode = _is_shallow_repository_with_details(cwd=cwd)
        record_git_command(GIT_TELEMETRY_COMMANDS.CHECK_SHALLOW, duration, returncode if returncode != 0 else None)
        return is_shallow_repository

    @classmethod
    def _unshallow_repository(cls, cwd=None):
        # type () -> None
        with StopWatch() as stopwatch:
            error_exit_code = None
            try:
                remote, stderr, _, exit_code = _extract_clone_defaultremotename_with_details(cwd=cwd)
                if exit_code != 0:
                    error_exit_code = exit_code
                    log.debug("Failed to get default remote: %s", stderr)
                    return

                try:
                    CIVisibilityGitClient._unshallow_repository_to_local_head(remote, cwd=cwd)
                    return
                except ValueError as e:
                    log.debug("Could not unshallow repository to local head: %s", e)

                try:
                    CIVisibilityGitClient._unshallow_repository_to_upstream(remote, cwd=cwd)
                    return
                except ValueError as e:
                    log.debug("Could not unshallow to upstream: %s", e)

                log.debug("Unshallowing to default")
                _, unshallow_error, _, exit_code = _unshallow_repository_with_details(cwd=cwd, repo=remote)
                if exit_code == 0:
                    log.debug("Unshallowing to default successful")
                    return
                log.debug("Unshallowing failed: %s", unshallow_error)
                error_exit_code = exit_code
                return
            finally:
                duration = stopwatch.elapsed() * 1000  # StopWatch measures elapsed time in seconds
                record_git_command(GIT_TELEMETRY_COMMANDS.UNSHALLOW, duration, error_exit_code)

    @classmethod
    def _unshallow_repository_to_local_head(cls, remote, cwd=None):
        # type (str, Optional[str) -> None
        head = extract_commit_sha(cwd=cwd)
        log.debug("Unshallowing to local head %s", head)
        _unshallow_repository(cwd=cwd, repo=remote, refspec=head)
        log.debug("Unshallowing to local head successful")

    @classmethod
    def _unshallow_repository_to_upstream(cls, remote, cwd=None):
        # type (str, Optional[str) -> None
        upstream = _extract_upstream_sha(cwd=cwd)
        log.debug("Unshallowing to upstream %s", upstream)
        _unshallow_repository(cwd=cwd, repo=remote, refspec=upstream)
        log.debug("Unshallowing to upstream")


class CIVisibilityGitClientSerializerV1(object):
    def __init__(self, api_key):
        # type: (str) -> None
        self.api_key = api_key

    def search_commits_encode(self, repo_url, latest_commits):
        # type: (str, list[str]) -> str
        return json.dumps(
            {"meta": {"repository_url": repo_url}, "data": [{"id": sha, "type": "commit"} for sha in latest_commits]}
        )

    def search_commits_decode(self, payload):
        # type: (str) -> List[str]
        res = []  # type: List[str]
        try:
            if isinstance(payload, bytes):
                parsed = json.loads(payload.decode())
            else:
                parsed = json.loads(payload)
            return [item["id"] for item in parsed["data"] if item["type"] == "commit"]
        except KeyError:
            log.warning("Expected information not found in search_commits response", exc_info=True)
        except json.JSONDecodeError:
            log.warning("Unexpected decode error in search_commits response", exc_info=True)

        return res

    def upload_packfile_encode(self, repo_url, sha, file_path):
        # type: (str, str, str) -> Tuple[str, bytes]
        BOUNDARY = b"----------boundary------"
        CRLF = b"\r\n"
        body = []
        metadata = {"data": {"id": sha, "type": "commit"}, "meta": {"repository_url": repo_url}}
        body.extend(
            [
                b"--" + BOUNDARY,
                b'Content-Disposition: form-data; name="pushedSha"',
                b"Content-Type: application/json",
                b"",
                json.dumps(metadata).encode("utf-8"),
            ]
        )
        file_name = os.path.basename(file_path)
        f = open(file_path, "rb")
        file_content = f.read()
        f.close()
        body.extend(
            [
                b"--" + BOUNDARY,
                b'Content-Disposition: form-data; name="packfile"; filename="%s"' % file_name.encode("utf-8"),
                b"Content-Type: application/octet-stream",
                b"",
                file_content,
            ]
        )
        body.extend([b"--" + BOUNDARY + b"--", b""])
        return "multipart/form-data; boundary=%s" % BOUNDARY.decode("utf-8"), CRLF.join(body)
