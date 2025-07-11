"""
Type annotations for s3 service Client.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_s3/client/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_s3.client import S3Client

    session = Session()
    client: S3Client = session.client("s3")
    ```
"""

from __future__ import annotations

import sys
from typing import Any, overload

from boto3.s3.transfer import TransferConfig
from botocore.client import BaseClient, ClientMeta
from botocore.errorfactory import BaseClientExceptions
from botocore.exceptions import ClientError as BotocoreClientError

from .paginator import (
    ListBucketsPaginator,
    ListDirectoryBucketsPaginator,
    ListMultipartUploadsPaginator,
    ListObjectsPaginator,
    ListObjectsV2Paginator,
    ListObjectVersionsPaginator,
    ListPartsPaginator,
)
from .type_defs import (
    AbortMultipartUploadOutputTypeDef,
    AbortMultipartUploadRequestTypeDef,
    CompleteMultipartUploadOutputTypeDef,
    CompleteMultipartUploadRequestTypeDef,
    CopyObjectOutputTypeDef,
    CopyObjectRequestTypeDef,
    CopySourceTypeDef,
    CreateBucketMetadataTableConfigurationRequestTypeDef,
    CreateBucketOutputTypeDef,
    CreateBucketRequestTypeDef,
    CreateMultipartUploadOutputTypeDef,
    CreateMultipartUploadRequestTypeDef,
    CreateSessionOutputTypeDef,
    CreateSessionRequestTypeDef,
    DeleteBucketAnalyticsConfigurationRequestTypeDef,
    DeleteBucketCorsRequestTypeDef,
    DeleteBucketEncryptionRequestTypeDef,
    DeleteBucketIntelligentTieringConfigurationRequestTypeDef,
    DeleteBucketInventoryConfigurationRequestTypeDef,
    DeleteBucketLifecycleRequestTypeDef,
    DeleteBucketMetadataTableConfigurationRequestTypeDef,
    DeleteBucketMetricsConfigurationRequestTypeDef,
    DeleteBucketOwnershipControlsRequestTypeDef,
    DeleteBucketPolicyRequestTypeDef,
    DeleteBucketReplicationRequestTypeDef,
    DeleteBucketRequestTypeDef,
    DeleteBucketTaggingRequestTypeDef,
    DeleteBucketWebsiteRequestTypeDef,
    DeleteObjectOutputTypeDef,
    DeleteObjectRequestTypeDef,
    DeleteObjectsOutputTypeDef,
    DeleteObjectsRequestTypeDef,
    DeleteObjectTaggingOutputTypeDef,
    DeleteObjectTaggingRequestTypeDef,
    DeletePublicAccessBlockRequestTypeDef,
    EmptyResponseMetadataTypeDef,
    FileobjTypeDef,
    GetBucketAccelerateConfigurationOutputTypeDef,
    GetBucketAccelerateConfigurationRequestTypeDef,
    GetBucketAclOutputTypeDef,
    GetBucketAclRequestTypeDef,
    GetBucketAnalyticsConfigurationOutputTypeDef,
    GetBucketAnalyticsConfigurationRequestTypeDef,
    GetBucketCorsOutputTypeDef,
    GetBucketCorsRequestTypeDef,
    GetBucketEncryptionOutputTypeDef,
    GetBucketEncryptionRequestTypeDef,
    GetBucketIntelligentTieringConfigurationOutputTypeDef,
    GetBucketIntelligentTieringConfigurationRequestTypeDef,
    GetBucketInventoryConfigurationOutputTypeDef,
    GetBucketInventoryConfigurationRequestTypeDef,
    GetBucketLifecycleConfigurationOutputTypeDef,
    GetBucketLifecycleConfigurationRequestTypeDef,
    GetBucketLifecycleOutputTypeDef,
    GetBucketLifecycleRequestTypeDef,
    GetBucketLocationOutputTypeDef,
    GetBucketLocationRequestTypeDef,
    GetBucketLoggingOutputTypeDef,
    GetBucketLoggingRequestTypeDef,
    GetBucketMetadataTableConfigurationOutputTypeDef,
    GetBucketMetadataTableConfigurationRequestTypeDef,
    GetBucketMetricsConfigurationOutputTypeDef,
    GetBucketMetricsConfigurationRequestTypeDef,
    GetBucketNotificationConfigurationRequestRequestTypeDef,
    GetBucketNotificationConfigurationRequestTypeDef,
    GetBucketOwnershipControlsOutputTypeDef,
    GetBucketOwnershipControlsRequestTypeDef,
    GetBucketPolicyOutputTypeDef,
    GetBucketPolicyRequestTypeDef,
    GetBucketPolicyStatusOutputTypeDef,
    GetBucketPolicyStatusRequestTypeDef,
    GetBucketReplicationOutputTypeDef,
    GetBucketReplicationRequestTypeDef,
    GetBucketRequestPaymentOutputTypeDef,
    GetBucketRequestPaymentRequestTypeDef,
    GetBucketTaggingOutputTypeDef,
    GetBucketTaggingRequestTypeDef,
    GetBucketVersioningOutputTypeDef,
    GetBucketVersioningRequestTypeDef,
    GetBucketWebsiteOutputTypeDef,
    GetBucketWebsiteRequestTypeDef,
    GetObjectAclOutputTypeDef,
    GetObjectAclRequestTypeDef,
    GetObjectAttributesOutputTypeDef,
    GetObjectAttributesRequestTypeDef,
    GetObjectLegalHoldOutputTypeDef,
    GetObjectLegalHoldRequestTypeDef,
    GetObjectLockConfigurationOutputTypeDef,
    GetObjectLockConfigurationRequestTypeDef,
    GetObjectOutputTypeDef,
    GetObjectRequestTypeDef,
    GetObjectRetentionOutputTypeDef,
    GetObjectRetentionRequestTypeDef,
    GetObjectTaggingOutputTypeDef,
    GetObjectTaggingRequestTypeDef,
    GetObjectTorrentOutputTypeDef,
    GetObjectTorrentRequestTypeDef,
    GetPublicAccessBlockOutputTypeDef,
    GetPublicAccessBlockRequestTypeDef,
    HeadBucketOutputTypeDef,
    HeadBucketRequestTypeDef,
    HeadObjectOutputTypeDef,
    HeadObjectRequestTypeDef,
    ListBucketAnalyticsConfigurationsOutputTypeDef,
    ListBucketAnalyticsConfigurationsRequestTypeDef,
    ListBucketIntelligentTieringConfigurationsOutputTypeDef,
    ListBucketIntelligentTieringConfigurationsRequestTypeDef,
    ListBucketInventoryConfigurationsOutputTypeDef,
    ListBucketInventoryConfigurationsRequestTypeDef,
    ListBucketMetricsConfigurationsOutputTypeDef,
    ListBucketMetricsConfigurationsRequestTypeDef,
    ListBucketsOutputTypeDef,
    ListBucketsRequestTypeDef,
    ListDirectoryBucketsOutputTypeDef,
    ListDirectoryBucketsRequestTypeDef,
    ListMultipartUploadsOutputTypeDef,
    ListMultipartUploadsRequestTypeDef,
    ListObjectsOutputTypeDef,
    ListObjectsRequestTypeDef,
    ListObjectsV2OutputTypeDef,
    ListObjectsV2RequestTypeDef,
    ListObjectVersionsOutputTypeDef,
    ListObjectVersionsRequestTypeDef,
    ListPartsOutputTypeDef,
    ListPartsRequestTypeDef,
    NotificationConfigurationDeprecatedResponseTypeDef,
    NotificationConfigurationResponseTypeDef,
    PutBucketAccelerateConfigurationRequestTypeDef,
    PutBucketAclRequestTypeDef,
    PutBucketAnalyticsConfigurationRequestTypeDef,
    PutBucketCorsRequestTypeDef,
    PutBucketEncryptionRequestTypeDef,
    PutBucketIntelligentTieringConfigurationRequestTypeDef,
    PutBucketInventoryConfigurationRequestTypeDef,
    PutBucketLifecycleConfigurationOutputTypeDef,
    PutBucketLifecycleConfigurationRequestTypeDef,
    PutBucketLifecycleRequestTypeDef,
    PutBucketLoggingRequestTypeDef,
    PutBucketMetricsConfigurationRequestTypeDef,
    PutBucketNotificationConfigurationRequestTypeDef,
    PutBucketNotificationRequestTypeDef,
    PutBucketOwnershipControlsRequestTypeDef,
    PutBucketPolicyRequestTypeDef,
    PutBucketReplicationRequestTypeDef,
    PutBucketRequestPaymentRequestTypeDef,
    PutBucketTaggingRequestTypeDef,
    PutBucketVersioningRequestTypeDef,
    PutBucketWebsiteRequestTypeDef,
    PutObjectAclOutputTypeDef,
    PutObjectAclRequestTypeDef,
    PutObjectLegalHoldOutputTypeDef,
    PutObjectLegalHoldRequestTypeDef,
    PutObjectLockConfigurationOutputTypeDef,
    PutObjectLockConfigurationRequestTypeDef,
    PutObjectOutputTypeDef,
    PutObjectRequestTypeDef,
    PutObjectRetentionOutputTypeDef,
    PutObjectRetentionRequestTypeDef,
    PutObjectTaggingOutputTypeDef,
    PutObjectTaggingRequestTypeDef,
    PutPublicAccessBlockRequestTypeDef,
    RenameObjectRequestTypeDef,
    RestoreObjectOutputTypeDef,
    RestoreObjectRequestTypeDef,
    SelectObjectContentOutputTypeDef,
    SelectObjectContentRequestTypeDef,
    UploadPartCopyOutputTypeDef,
    UploadPartCopyRequestTypeDef,
    UploadPartOutputTypeDef,
    UploadPartRequestTypeDef,
    WriteGetObjectResponseRequestTypeDef,
)
from .waiter import (
    BucketExistsWaiter,
    BucketNotExistsWaiter,
    ObjectExistsWaiter,
    ObjectNotExistsWaiter,
)

if sys.version_info >= (3, 9):
    from builtins import dict as Dict
    from builtins import list as List
    from builtins import type as Type
    from collections.abc import Callable, Mapping
else:
    from typing import Callable, Dict, List, Mapping, Type
if sys.version_info >= (3, 12):
    from typing import Literal, Unpack
else:
    from typing_extensions import Literal, Unpack


__all__ = ("S3Client",)


class Exceptions(BaseClientExceptions):
    BucketAlreadyExists: Type[BotocoreClientError]
    BucketAlreadyOwnedByYou: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    EncryptionTypeMismatch: Type[BotocoreClientError]
    IdempotencyParameterMismatch: Type[BotocoreClientError]
    InvalidObjectState: Type[BotocoreClientError]
    InvalidRequest: Type[BotocoreClientError]
    InvalidWriteOffset: Type[BotocoreClientError]
    NoSuchBucket: Type[BotocoreClientError]
    NoSuchKey: Type[BotocoreClientError]
    NoSuchUpload: Type[BotocoreClientError]
    ObjectAlreadyInActiveTierError: Type[BotocoreClientError]
    ObjectNotInActiveTierError: Type[BotocoreClientError]
    TooManyParts: Type[BotocoreClientError]


class S3Client(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.Client)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_s3/client/)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        S3Client exceptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.Client)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_s3/client/#exceptions)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3/client/can_paginate.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_s3/client/#can_paginate)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Mapping[str, Any] = ...,
        ExpiresIn: int = 3600,
        HttpMethod: str = ...,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3/client/generate_presigned_url.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_s3/client/#generate_presigned_url)
        """

    def abort_multipart_upload(
        self, **kwargs: Unpack[AbortMultipartUploadRequestTypeDef]
    ) -> AbortMultipartUploadOutputTypeDef:
        """
        This operation aborts a multipart upload.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3/client/abort_multipart_upload.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_s3/client/#abort_multipart_upload)
        """

    def complete_multipart_upload(
        self, **kwargs: Unpack[CompleteMultipartUploadRequestTypeDef]
    ) -> CompleteMultipartUploadOutputTypeDef:
        """
        Completes a multipart upload by assembling previously uploaded parts.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3/client/complete_multipart_upload.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_s3/client/#complete_multipart_upload)
        """

    def copy_object(self, **kwargs: Unpack[CopyObjectRequestTypeDef]) -> CopyObjectOutputTypeDef:
        """
        End of support notice: Beginning October 1, 2025, Amazon S3 will discontinue
        support for creating new Email Grantee Access Control Lists (ACL).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3/client/copy_object.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_s3/client/#copy_object)
        """

    def create_bucket(
        self, **kwargs: Unpack[CreateBucketRequestTypeDef]
    ) -> CreateBucketOutputTypeDef:
        """
        End of support notice: Beginning October 1, 2025, Amazon S3 will discontinue
        support for creating new Email Grantee Access Control Lists (ACL).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3/client/create_bucket.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_s3/client/#create_bucket)
        """

    def create_bucket_metadata_table_configuration(
        self, **kwargs: Unpack[CreateBucketMetadataTableConfigurationRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Creates a metadata table configuration for a general purpose bucket.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3/client/create_bucket_metadata_table_configuration.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_s3/client/#create_bucket_metadata_table_configuration)
        """

    def create_multipart_upload(
        self, **kwargs: Unpack[CreateMultipartUploadRequestTypeDef]
    ) -> CreateMultipartUploadOutputTypeDef:
        """
        End of support notice: Beginning October 1, 2025, Amazon S3 will discontinue
        support for creating new Email Grantee Access Control Lists (ACL).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3/client/create_multipart_upload.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_s3/client/#create_multipart_upload)
        """

    def create_session(
        self, **kwargs: Unpack[CreateSessionRequestTypeDef]
    ) -> CreateSessionOutputTypeDef:
        """
        Creates a session that establishes temporary security credentials to support
        fast authentication and authorization for the Zonal endpoint API operations on
        directory buckets.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3/client/create_session.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_s3/client/#create_session)
        """

    def delete_bucket(
        self, **kwargs: Unpack[DeleteBucketRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes the S3 bucket.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3/client/delete_bucket.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_s3/client/#delete_bucket)
        """

    def delete_bucket_analytics_configuration(
        self, **kwargs: Unpack[DeleteBucketAnalyticsConfigurationRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        This operation is not supported for directory buckets.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3/client/delete_bucket_analytics_configuration.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_s3/client/#delete_bucket_analytics_configuration)
        """

    def delete_bucket_cors(
        self, **kwargs: Unpack[DeleteBucketCorsRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        This operation is not supported for directory buckets.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3/client/delete_bucket_cors.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_s3/client/#delete_bucket_cors)
        """

    def delete_bucket_encryption(
        self, **kwargs: Unpack[DeleteBucketEncryptionRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        This implementation of the DELETE action resets the default encryption for the
        bucket as server-side encryption with Amazon S3 managed keys (SSE-S3).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3/client/delete_bucket_encryption.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_s3/client/#delete_bucket_encryption)
        """

    def delete_bucket_intelligent_tiering_configuration(
        self, **kwargs: Unpack[DeleteBucketIntelligentTieringConfigurationRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        This operation is not supported for directory buckets.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3/client/delete_bucket_intelligent_tiering_configuration.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_s3/client/#delete_bucket_intelligent_tiering_configuration)
        """

    def delete_bucket_inventory_configuration(
        self, **kwargs: Unpack[DeleteBucketInventoryConfigurationRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        This operation is not supported for directory buckets.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3/client/delete_bucket_inventory_configuration.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_s3/client/#delete_bucket_inventory_configuration)
        """

    def delete_bucket_lifecycle(
        self, **kwargs: Unpack[DeleteBucketLifecycleRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes the lifecycle configuration from the specified bucket.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3/client/delete_bucket_lifecycle.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_s3/client/#delete_bucket_lifecycle)
        """

    def delete_bucket_metadata_table_configuration(
        self, **kwargs: Unpack[DeleteBucketMetadataTableConfigurationRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes a metadata table configuration from a general purpose bucket.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3/client/delete_bucket_metadata_table_configuration.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_s3/client/#delete_bucket_metadata_table_configuration)
        """

    def delete_bucket_metrics_configuration(
        self, **kwargs: Unpack[DeleteBucketMetricsConfigurationRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        This operation is not supported for directory buckets.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3/client/delete_bucket_metrics_configuration.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_s3/client/#delete_bucket_metrics_configuration)
        """

    def delete_bucket_ownership_controls(
        self, **kwargs: Unpack[DeleteBucketOwnershipControlsRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        This operation is not supported for directory buckets.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3/client/delete_bucket_ownership_controls.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_s3/client/#delete_bucket_ownership_controls)
        """

    def delete_bucket_policy(
        self, **kwargs: Unpack[DeleteBucketPolicyRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes the policy of a specified bucket.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3/client/delete_bucket_policy.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_s3/client/#delete_bucket_policy)
        """

    def delete_bucket_replication(
        self, **kwargs: Unpack[DeleteBucketReplicationRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        This operation is not supported for directory buckets.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3/client/delete_bucket_replication.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_s3/client/#delete_bucket_replication)
        """

    def delete_bucket_tagging(
        self, **kwargs: Unpack[DeleteBucketTaggingRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        This operation is not supported for directory buckets.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3/client/delete_bucket_tagging.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_s3/client/#delete_bucket_tagging)
        """

    def delete_bucket_website(
        self, **kwargs: Unpack[DeleteBucketWebsiteRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        This operation is not supported for directory buckets.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3/client/delete_bucket_website.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_s3/client/#delete_bucket_website)
        """

    def delete_object(
        self, **kwargs: Unpack[DeleteObjectRequestTypeDef]
    ) -> DeleteObjectOutputTypeDef:
        """
        Removes an object from a bucket.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3/client/delete_object.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_s3/client/#delete_object)
        """

    def delete_object_tagging(
        self, **kwargs: Unpack[DeleteObjectTaggingRequestTypeDef]
    ) -> DeleteObjectTaggingOutputTypeDef:
        """
        This operation is not supported for directory buckets.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3/client/delete_object_tagging.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_s3/client/#delete_object_tagging)
        """

    def delete_objects(
        self, **kwargs: Unpack[DeleteObjectsRequestTypeDef]
    ) -> DeleteObjectsOutputTypeDef:
        """
        This operation enables you to delete multiple objects from a bucket using a
        single HTTP request.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3/client/delete_objects.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_s3/client/#delete_objects)
        """

    def delete_public_access_block(
        self, **kwargs: Unpack[DeletePublicAccessBlockRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        This operation is not supported for directory buckets.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3/client/delete_public_access_block.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_s3/client/#delete_public_access_block)
        """

    def get_bucket_accelerate_configuration(
        self, **kwargs: Unpack[GetBucketAccelerateConfigurationRequestTypeDef]
    ) -> GetBucketAccelerateConfigurationOutputTypeDef:
        """
        This operation is not supported for directory buckets.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3/client/get_bucket_accelerate_configuration.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_s3/client/#get_bucket_accelerate_configuration)
        """

    def get_bucket_acl(
        self, **kwargs: Unpack[GetBucketAclRequestTypeDef]
    ) -> GetBucketAclOutputTypeDef:
        """
        End of support notice: Beginning October 1, 2025, Amazon S3 will stop returning
        <code>DisplayName</code>.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3/client/get_bucket_acl.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_s3/client/#get_bucket_acl)
        """

    def get_bucket_analytics_configuration(
        self, **kwargs: Unpack[GetBucketAnalyticsConfigurationRequestTypeDef]
    ) -> GetBucketAnalyticsConfigurationOutputTypeDef:
        """
        This operation is not supported for directory buckets.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3/client/get_bucket_analytics_configuration.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_s3/client/#get_bucket_analytics_configuration)
        """

    def get_bucket_cors(
        self, **kwargs: Unpack[GetBucketCorsRequestTypeDef]
    ) -> GetBucketCorsOutputTypeDef:
        """
        This operation is not supported for directory buckets.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3/client/get_bucket_cors.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_s3/client/#get_bucket_cors)
        """

    def get_bucket_encryption(
        self, **kwargs: Unpack[GetBucketEncryptionRequestTypeDef]
    ) -> GetBucketEncryptionOutputTypeDef:
        """
        Returns the default encryption configuration for an Amazon S3 bucket.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3/client/get_bucket_encryption.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_s3/client/#get_bucket_encryption)
        """

    def get_bucket_intelligent_tiering_configuration(
        self, **kwargs: Unpack[GetBucketIntelligentTieringConfigurationRequestTypeDef]
    ) -> GetBucketIntelligentTieringConfigurationOutputTypeDef:
        """
        This operation is not supported for directory buckets.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3/client/get_bucket_intelligent_tiering_configuration.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_s3/client/#get_bucket_intelligent_tiering_configuration)
        """

    def get_bucket_inventory_configuration(
        self, **kwargs: Unpack[GetBucketInventoryConfigurationRequestTypeDef]
    ) -> GetBucketInventoryConfigurationOutputTypeDef:
        """
        This operation is not supported for directory buckets.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3/client/get_bucket_inventory_configuration.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_s3/client/#get_bucket_inventory_configuration)
        """

    def get_bucket_lifecycle(
        self, **kwargs: Unpack[GetBucketLifecycleRequestTypeDef]
    ) -> GetBucketLifecycleOutputTypeDef:
        """
        For an updated version of this API, see <a
        href="https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetBucketLifecycleConfiguration.html">GetBucketLifecycleConfiguration</a>.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3/client/get_bucket_lifecycle.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_s3/client/#get_bucket_lifecycle)
        """

    def get_bucket_lifecycle_configuration(
        self, **kwargs: Unpack[GetBucketLifecycleConfigurationRequestTypeDef]
    ) -> GetBucketLifecycleConfigurationOutputTypeDef:
        """
        Returns the lifecycle configuration information set on the bucket.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3/client/get_bucket_lifecycle_configuration.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_s3/client/#get_bucket_lifecycle_configuration)
        """

    def get_bucket_location(
        self, **kwargs: Unpack[GetBucketLocationRequestTypeDef]
    ) -> GetBucketLocationOutputTypeDef:
        """
        This operation is not supported for directory buckets.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3/client/get_bucket_location.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_s3/client/#get_bucket_location)
        """

    def get_bucket_logging(
        self, **kwargs: Unpack[GetBucketLoggingRequestTypeDef]
    ) -> GetBucketLoggingOutputTypeDef:
        """
        End of support notice: Beginning October 1, 2025, Amazon S3 will stop returning
        <code>DisplayName</code>.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3/client/get_bucket_logging.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_s3/client/#get_bucket_logging)
        """

    def get_bucket_metadata_table_configuration(
        self, **kwargs: Unpack[GetBucketMetadataTableConfigurationRequestTypeDef]
    ) -> GetBucketMetadataTableConfigurationOutputTypeDef:
        """
        Retrieves the metadata table configuration for a general purpose bucket.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3/client/get_bucket_metadata_table_configuration.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_s3/client/#get_bucket_metadata_table_configuration)
        """

    def get_bucket_metrics_configuration(
        self, **kwargs: Unpack[GetBucketMetricsConfigurationRequestTypeDef]
    ) -> GetBucketMetricsConfigurationOutputTypeDef:
        """
        This operation is not supported for directory buckets.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3/client/get_bucket_metrics_configuration.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_s3/client/#get_bucket_metrics_configuration)
        """

    def get_bucket_notification(
        self, **kwargs: Unpack[GetBucketNotificationConfigurationRequestTypeDef]
    ) -> NotificationConfigurationDeprecatedResponseTypeDef:
        """
        This operation is not supported for directory buckets.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3/client/get_bucket_notification.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_s3/client/#get_bucket_notification)
        """

    def get_bucket_notification_configuration(
        self, **kwargs: Unpack[GetBucketNotificationConfigurationRequestRequestTypeDef]
    ) -> NotificationConfigurationResponseTypeDef:
        """
        This operation is not supported for directory buckets.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3/client/get_bucket_notification_configuration.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_s3/client/#get_bucket_notification_configuration)
        """

    def get_bucket_ownership_controls(
        self, **kwargs: Unpack[GetBucketOwnershipControlsRequestTypeDef]
    ) -> GetBucketOwnershipControlsOutputTypeDef:
        """
        This operation is not supported for directory buckets.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3/client/get_bucket_ownership_controls.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_s3/client/#get_bucket_ownership_controls)
        """

    def get_bucket_policy(
        self, **kwargs: Unpack[GetBucketPolicyRequestTypeDef]
    ) -> GetBucketPolicyOutputTypeDef:
        """
        Returns the policy of a specified bucket.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3/client/get_bucket_policy.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_s3/client/#get_bucket_policy)
        """

    def get_bucket_policy_status(
        self, **kwargs: Unpack[GetBucketPolicyStatusRequestTypeDef]
    ) -> GetBucketPolicyStatusOutputTypeDef:
        """
        This operation is not supported for directory buckets.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3/client/get_bucket_policy_status.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_s3/client/#get_bucket_policy_status)
        """

    def get_bucket_replication(
        self, **kwargs: Unpack[GetBucketReplicationRequestTypeDef]
    ) -> GetBucketReplicationOutputTypeDef:
        """
        This operation is not supported for directory buckets.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3/client/get_bucket_replication.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_s3/client/#get_bucket_replication)
        """

    def get_bucket_request_payment(
        self, **kwargs: Unpack[GetBucketRequestPaymentRequestTypeDef]
    ) -> GetBucketRequestPaymentOutputTypeDef:
        """
        This operation is not supported for directory buckets.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3/client/get_bucket_request_payment.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_s3/client/#get_bucket_request_payment)
        """

    def get_bucket_tagging(
        self, **kwargs: Unpack[GetBucketTaggingRequestTypeDef]
    ) -> GetBucketTaggingOutputTypeDef:
        """
        This operation is not supported for directory buckets.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3/client/get_bucket_tagging.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_s3/client/#get_bucket_tagging)
        """

    def get_bucket_versioning(
        self, **kwargs: Unpack[GetBucketVersioningRequestTypeDef]
    ) -> GetBucketVersioningOutputTypeDef:
        """
        This operation is not supported for directory buckets.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3/client/get_bucket_versioning.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_s3/client/#get_bucket_versioning)
        """

    def get_bucket_website(
        self, **kwargs: Unpack[GetBucketWebsiteRequestTypeDef]
    ) -> GetBucketWebsiteOutputTypeDef:
        """
        This operation is not supported for directory buckets.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3/client/get_bucket_website.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_s3/client/#get_bucket_website)
        """

    def get_object(self, **kwargs: Unpack[GetObjectRequestTypeDef]) -> GetObjectOutputTypeDef:
        """
        Retrieves an object from Amazon S3.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3/client/get_object.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_s3/client/#get_object)
        """

    def get_object_acl(
        self, **kwargs: Unpack[GetObjectAclRequestTypeDef]
    ) -> GetObjectAclOutputTypeDef:
        """
        This operation is not supported for directory buckets.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3/client/get_object_acl.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_s3/client/#get_object_acl)
        """

    def get_object_attributes(
        self, **kwargs: Unpack[GetObjectAttributesRequestTypeDef]
    ) -> GetObjectAttributesOutputTypeDef:
        """
        Retrieves all of the metadata from an object without returning the object
        itself.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3/client/get_object_attributes.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_s3/client/#get_object_attributes)
        """

    def get_object_legal_hold(
        self, **kwargs: Unpack[GetObjectLegalHoldRequestTypeDef]
    ) -> GetObjectLegalHoldOutputTypeDef:
        """
        This operation is not supported for directory buckets.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3/client/get_object_legal_hold.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_s3/client/#get_object_legal_hold)
        """

    def get_object_lock_configuration(
        self, **kwargs: Unpack[GetObjectLockConfigurationRequestTypeDef]
    ) -> GetObjectLockConfigurationOutputTypeDef:
        """
        This operation is not supported for directory buckets.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3/client/get_object_lock_configuration.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_s3/client/#get_object_lock_configuration)
        """

    def get_object_retention(
        self, **kwargs: Unpack[GetObjectRetentionRequestTypeDef]
    ) -> GetObjectRetentionOutputTypeDef:
        """
        This operation is not supported for directory buckets.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3/client/get_object_retention.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_s3/client/#get_object_retention)
        """

    def get_object_tagging(
        self, **kwargs: Unpack[GetObjectTaggingRequestTypeDef]
    ) -> GetObjectTaggingOutputTypeDef:
        """
        This operation is not supported for directory buckets.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3/client/get_object_tagging.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_s3/client/#get_object_tagging)
        """

    def get_object_torrent(
        self, **kwargs: Unpack[GetObjectTorrentRequestTypeDef]
    ) -> GetObjectTorrentOutputTypeDef:
        """
        This operation is not supported for directory buckets.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3/client/get_object_torrent.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_s3/client/#get_object_torrent)
        """

    def get_public_access_block(
        self, **kwargs: Unpack[GetPublicAccessBlockRequestTypeDef]
    ) -> GetPublicAccessBlockOutputTypeDef:
        """
        This operation is not supported for directory buckets.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3/client/get_public_access_block.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_s3/client/#get_public_access_block)
        """

    def head_bucket(self, **kwargs: Unpack[HeadBucketRequestTypeDef]) -> HeadBucketOutputTypeDef:
        """
        You can use this operation to determine if a bucket exists and if you have
        permission to access it.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3/client/head_bucket.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_s3/client/#head_bucket)
        """

    def head_object(self, **kwargs: Unpack[HeadObjectRequestTypeDef]) -> HeadObjectOutputTypeDef:
        """
        The <code>HEAD</code> operation retrieves metadata from an object without
        returning the object itself.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3/client/head_object.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_s3/client/#head_object)
        """

    def list_bucket_analytics_configurations(
        self, **kwargs: Unpack[ListBucketAnalyticsConfigurationsRequestTypeDef]
    ) -> ListBucketAnalyticsConfigurationsOutputTypeDef:
        """
        This operation is not supported for directory buckets.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3/client/list_bucket_analytics_configurations.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_s3/client/#list_bucket_analytics_configurations)
        """

    def list_bucket_intelligent_tiering_configurations(
        self, **kwargs: Unpack[ListBucketIntelligentTieringConfigurationsRequestTypeDef]
    ) -> ListBucketIntelligentTieringConfigurationsOutputTypeDef:
        """
        This operation is not supported for directory buckets.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3/client/list_bucket_intelligent_tiering_configurations.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_s3/client/#list_bucket_intelligent_tiering_configurations)
        """

    def list_bucket_inventory_configurations(
        self, **kwargs: Unpack[ListBucketInventoryConfigurationsRequestTypeDef]
    ) -> ListBucketInventoryConfigurationsOutputTypeDef:
        """
        This operation is not supported for directory buckets.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3/client/list_bucket_inventory_configurations.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_s3/client/#list_bucket_inventory_configurations)
        """

    def list_bucket_metrics_configurations(
        self, **kwargs: Unpack[ListBucketMetricsConfigurationsRequestTypeDef]
    ) -> ListBucketMetricsConfigurationsOutputTypeDef:
        """
        This operation is not supported for directory buckets.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3/client/list_bucket_metrics_configurations.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_s3/client/#list_bucket_metrics_configurations)
        """

    def list_buckets(self, **kwargs: Unpack[ListBucketsRequestTypeDef]) -> ListBucketsOutputTypeDef:
        """
        End of support notice: Beginning October 1, 2025, Amazon S3 will stop returning
        <code>DisplayName</code>.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3/client/list_buckets.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_s3/client/#list_buckets)
        """

    def list_directory_buckets(
        self, **kwargs: Unpack[ListDirectoryBucketsRequestTypeDef]
    ) -> ListDirectoryBucketsOutputTypeDef:
        """
        Returns a list of all Amazon S3 directory buckets owned by the authenticated
        sender of the request.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3/client/list_directory_buckets.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_s3/client/#list_directory_buckets)
        """

    def list_multipart_uploads(
        self, **kwargs: Unpack[ListMultipartUploadsRequestTypeDef]
    ) -> ListMultipartUploadsOutputTypeDef:
        """
        End of support notice: Beginning October 1, 2025, Amazon S3 will stop returning
        <code>DisplayName</code>.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3/client/list_multipart_uploads.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_s3/client/#list_multipart_uploads)
        """

    def list_object_versions(
        self, **kwargs: Unpack[ListObjectVersionsRequestTypeDef]
    ) -> ListObjectVersionsOutputTypeDef:
        """
        End of support notice: Beginning October 1, 2025, Amazon S3 will stop returning
        <code>DisplayName</code>.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3/client/list_object_versions.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_s3/client/#list_object_versions)
        """

    def list_objects(self, **kwargs: Unpack[ListObjectsRequestTypeDef]) -> ListObjectsOutputTypeDef:
        """
        End of support notice: Beginning October 1, 2025, Amazon S3 will stop returning
        <code>DisplayName</code>.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3/client/list_objects.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_s3/client/#list_objects)
        """

    def list_objects_v2(
        self, **kwargs: Unpack[ListObjectsV2RequestTypeDef]
    ) -> ListObjectsV2OutputTypeDef:
        """
        Returns some or all (up to 1,000) of the objects in a bucket with each request.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3/client/list_objects_v2.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_s3/client/#list_objects_v2)
        """

    def list_parts(self, **kwargs: Unpack[ListPartsRequestTypeDef]) -> ListPartsOutputTypeDef:
        """
        End of support notice: Beginning October 1, 2025, Amazon S3 will stop returning
        <code>DisplayName</code>.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3/client/list_parts.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_s3/client/#list_parts)
        """

    def put_bucket_accelerate_configuration(
        self, **kwargs: Unpack[PutBucketAccelerateConfigurationRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        This operation is not supported for directory buckets.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3/client/put_bucket_accelerate_configuration.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_s3/client/#put_bucket_accelerate_configuration)
        """

    def put_bucket_acl(
        self, **kwargs: Unpack[PutBucketAclRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        End of support notice: Beginning October 1, 2025, Amazon S3 will discontinue
        support for creating new Email Grantee Access Control Lists (ACL).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3/client/put_bucket_acl.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_s3/client/#put_bucket_acl)
        """

    def put_bucket_analytics_configuration(
        self, **kwargs: Unpack[PutBucketAnalyticsConfigurationRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        This operation is not supported for directory buckets.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3/client/put_bucket_analytics_configuration.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_s3/client/#put_bucket_analytics_configuration)
        """

    def put_bucket_cors(
        self, **kwargs: Unpack[PutBucketCorsRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        This operation is not supported for directory buckets.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3/client/put_bucket_cors.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_s3/client/#put_bucket_cors)
        """

    def put_bucket_encryption(
        self, **kwargs: Unpack[PutBucketEncryptionRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        This operation configures default encryption and Amazon S3 Bucket Keys for an
        existing bucket.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3/client/put_bucket_encryption.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_s3/client/#put_bucket_encryption)
        """

    def put_bucket_intelligent_tiering_configuration(
        self, **kwargs: Unpack[PutBucketIntelligentTieringConfigurationRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        This operation is not supported for directory buckets.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3/client/put_bucket_intelligent_tiering_configuration.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_s3/client/#put_bucket_intelligent_tiering_configuration)
        """

    def put_bucket_inventory_configuration(
        self, **kwargs: Unpack[PutBucketInventoryConfigurationRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        This operation is not supported for directory buckets.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3/client/put_bucket_inventory_configuration.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_s3/client/#put_bucket_inventory_configuration)
        """

    def put_bucket_lifecycle(
        self, **kwargs: Unpack[PutBucketLifecycleRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        This operation is not supported for directory buckets.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3/client/put_bucket_lifecycle.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_s3/client/#put_bucket_lifecycle)
        """

    def put_bucket_lifecycle_configuration(
        self, **kwargs: Unpack[PutBucketLifecycleConfigurationRequestTypeDef]
    ) -> PutBucketLifecycleConfigurationOutputTypeDef:
        """
        Creates a new lifecycle configuration for the bucket or replaces an existing
        lifecycle configuration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3/client/put_bucket_lifecycle_configuration.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_s3/client/#put_bucket_lifecycle_configuration)
        """

    def put_bucket_logging(
        self, **kwargs: Unpack[PutBucketLoggingRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        End of support notice: Beginning October 1, 2025, Amazon S3 will discontinue
        support for creating new Email Grantee Access Control Lists (ACL).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3/client/put_bucket_logging.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_s3/client/#put_bucket_logging)
        """

    def put_bucket_metrics_configuration(
        self, **kwargs: Unpack[PutBucketMetricsConfigurationRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        This operation is not supported for directory buckets.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3/client/put_bucket_metrics_configuration.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_s3/client/#put_bucket_metrics_configuration)
        """

    def put_bucket_notification(
        self, **kwargs: Unpack[PutBucketNotificationRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        This operation is not supported for directory buckets.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3/client/put_bucket_notification.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_s3/client/#put_bucket_notification)
        """

    def put_bucket_notification_configuration(
        self, **kwargs: Unpack[PutBucketNotificationConfigurationRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        This operation is not supported for directory buckets.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3/client/put_bucket_notification_configuration.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_s3/client/#put_bucket_notification_configuration)
        """

    def put_bucket_ownership_controls(
        self, **kwargs: Unpack[PutBucketOwnershipControlsRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        This operation is not supported for directory buckets.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3/client/put_bucket_ownership_controls.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_s3/client/#put_bucket_ownership_controls)
        """

    def put_bucket_policy(
        self, **kwargs: Unpack[PutBucketPolicyRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Applies an Amazon S3 bucket policy to an Amazon S3 bucket.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3/client/put_bucket_policy.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_s3/client/#put_bucket_policy)
        """

    def put_bucket_replication(
        self, **kwargs: Unpack[PutBucketReplicationRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        This operation is not supported for directory buckets.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3/client/put_bucket_replication.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_s3/client/#put_bucket_replication)
        """

    def put_bucket_request_payment(
        self, **kwargs: Unpack[PutBucketRequestPaymentRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        This operation is not supported for directory buckets.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3/client/put_bucket_request_payment.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_s3/client/#put_bucket_request_payment)
        """

    def put_bucket_tagging(
        self, **kwargs: Unpack[PutBucketTaggingRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        This operation is not supported for directory buckets.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3/client/put_bucket_tagging.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_s3/client/#put_bucket_tagging)
        """

    def put_bucket_versioning(
        self, **kwargs: Unpack[PutBucketVersioningRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        This operation is not supported for directory buckets.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3/client/put_bucket_versioning.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_s3/client/#put_bucket_versioning)
        """

    def put_bucket_website(
        self, **kwargs: Unpack[PutBucketWebsiteRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        This operation is not supported for directory buckets.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3/client/put_bucket_website.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_s3/client/#put_bucket_website)
        """

    def put_object(self, **kwargs: Unpack[PutObjectRequestTypeDef]) -> PutObjectOutputTypeDef:
        """
        End of support notice: Beginning October 1, 2025, Amazon S3 will discontinue
        support for creating new Email Grantee Access Control Lists (ACL).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3/client/put_object.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_s3/client/#put_object)
        """

    def put_object_acl(
        self, **kwargs: Unpack[PutObjectAclRequestTypeDef]
    ) -> PutObjectAclOutputTypeDef:
        """
        This operation is not supported for directory buckets.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3/client/put_object_acl.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_s3/client/#put_object_acl)
        """

    def put_object_legal_hold(
        self, **kwargs: Unpack[PutObjectLegalHoldRequestTypeDef]
    ) -> PutObjectLegalHoldOutputTypeDef:
        """
        This operation is not supported for directory buckets.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3/client/put_object_legal_hold.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_s3/client/#put_object_legal_hold)
        """

    def put_object_lock_configuration(
        self, **kwargs: Unpack[PutObjectLockConfigurationRequestTypeDef]
    ) -> PutObjectLockConfigurationOutputTypeDef:
        """
        This operation is not supported for directory buckets.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3/client/put_object_lock_configuration.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_s3/client/#put_object_lock_configuration)
        """

    def put_object_retention(
        self, **kwargs: Unpack[PutObjectRetentionRequestTypeDef]
    ) -> PutObjectRetentionOutputTypeDef:
        """
        This operation is not supported for directory buckets.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3/client/put_object_retention.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_s3/client/#put_object_retention)
        """

    def put_object_tagging(
        self, **kwargs: Unpack[PutObjectTaggingRequestTypeDef]
    ) -> PutObjectTaggingOutputTypeDef:
        """
        This operation is not supported for directory buckets.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3/client/put_object_tagging.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_s3/client/#put_object_tagging)
        """

    def put_public_access_block(
        self, **kwargs: Unpack[PutPublicAccessBlockRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        This operation is not supported for directory buckets.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3/client/put_public_access_block.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_s3/client/#put_public_access_block)
        """

    def rename_object(self, **kwargs: Unpack[RenameObjectRequestTypeDef]) -> Dict[str, Any]:
        """
        Renames an existing object in a directory bucket that uses the S3 Express One
        Zone storage class.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3/client/rename_object.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_s3/client/#rename_object)
        """

    def restore_object(
        self, **kwargs: Unpack[RestoreObjectRequestTypeDef]
    ) -> RestoreObjectOutputTypeDef:
        """
        This operation is not supported for directory buckets.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3/client/restore_object.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_s3/client/#restore_object)
        """

    def select_object_content(
        self, **kwargs: Unpack[SelectObjectContentRequestTypeDef]
    ) -> SelectObjectContentOutputTypeDef:
        """
        This operation is not supported for directory buckets.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3/client/select_object_content.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_s3/client/#select_object_content)
        """

    def upload_part(self, **kwargs: Unpack[UploadPartRequestTypeDef]) -> UploadPartOutputTypeDef:
        """
        Uploads a part in a multipart upload.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3/client/upload_part.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_s3/client/#upload_part)
        """

    def upload_part_copy(
        self, **kwargs: Unpack[UploadPartCopyRequestTypeDef]
    ) -> UploadPartCopyOutputTypeDef:
        """
        Uploads a part by copying data from an existing object as data source.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3/client/upload_part_copy.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_s3/client/#upload_part_copy)
        """

    def write_get_object_response(
        self, **kwargs: Unpack[WriteGetObjectResponseRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        This operation is not supported for directory buckets.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3/client/write_get_object_response.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_s3/client/#write_get_object_response)
        """

    def copy(
        self,
        CopySource: CopySourceTypeDef,
        Bucket: str,
        Key: str,
        ExtraArgs: Dict[str, Any] | None = ...,
        Callback: Callable[..., Any] | None = ...,
        SourceClient: BaseClient | None = ...,
        Config: TransferConfig | None = ...,
    ) -> None:
        """
        Copy an object from one S3 location to another.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3/client/copy.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_s3/client/#copy)
        """

    def download_file(
        self,
        Bucket: str,
        Key: str,
        Filename: str,
        ExtraArgs: Dict[str, Any] | None = ...,
        Callback: Callable[..., Any] | None = ...,
        Config: TransferConfig | None = ...,
    ) -> None:
        """
        Download an object from S3 to a file.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3/client/download_file.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_s3/client/#download_file)
        """

    def download_fileobj(
        self,
        Bucket: str,
        Key: str,
        Fileobj: FileobjTypeDef,
        ExtraArgs: Dict[str, Any] | None = ...,
        Callback: Callable[..., Any] | None = ...,
        Config: TransferConfig | None = ...,
    ) -> None:
        """
        Download an object from S3 to a file-like object.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3/client/download_fileobj.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_s3/client/#download_fileobj)
        """

    def generate_presigned_post(
        self,
        Bucket: str,
        Key: str,
        Fields: Dict[str, Any] | None = ...,
        Conditions: List[Any] | Dict[str, Any] | None = ...,
        ExpiresIn: int = 3600,
    ) -> Dict[str, Any]:
        """
        Generate a presigned URL for POST requests.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3/client/generate_presigned_post.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_s3/client/#generate_presigned_post)
        """

    def upload_file(
        self,
        Filename: str,
        Bucket: str,
        Key: str,
        ExtraArgs: Dict[str, Any] | None = ...,
        Callback: Callable[..., Any] | None = ...,
        Config: TransferConfig | None = ...,
    ) -> None:
        """
        Upload a file to S3.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3/client/upload_file.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_s3/client/#upload_file)
        """

    def upload_fileobj(
        self,
        Fileobj: FileobjTypeDef,
        Bucket: str,
        Key: str,
        ExtraArgs: Dict[str, Any] | None = ...,
        Callback: Callable[..., Any] | None = ...,
        Config: TransferConfig | None = ...,
    ) -> None:
        """
        Upload a file-like object to S3.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3/client/upload_fileobj.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_s3/client/#upload_fileobj)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_buckets"]
    ) -> ListBucketsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_s3/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_directory_buckets"]
    ) -> ListDirectoryBucketsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_s3/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_multipart_uploads"]
    ) -> ListMultipartUploadsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_s3/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_object_versions"]
    ) -> ListObjectVersionsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_s3/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_objects"]
    ) -> ListObjectsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_s3/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_objects_v2"]
    ) -> ListObjectsV2Paginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_s3/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_parts"]
    ) -> ListPartsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_s3/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_waiter(  # type: ignore[override]
        self, waiter_name: Literal["bucket_exists"]
    ) -> BucketExistsWaiter:
        """
        Returns an object that can wait for some condition.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3/client/get_waiter.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_s3/client/#get_waiter)
        """

    @overload  # type: ignore[override]
    def get_waiter(  # type: ignore[override]
        self, waiter_name: Literal["bucket_not_exists"]
    ) -> BucketNotExistsWaiter:
        """
        Returns an object that can wait for some condition.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3/client/get_waiter.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_s3/client/#get_waiter)
        """

    @overload  # type: ignore[override]
    def get_waiter(  # type: ignore[override]
        self, waiter_name: Literal["object_exists"]
    ) -> ObjectExistsWaiter:
        """
        Returns an object that can wait for some condition.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3/client/get_waiter.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_s3/client/#get_waiter)
        """

    @overload  # type: ignore[override]
    def get_waiter(  # type: ignore[override]
        self, waiter_name: Literal["object_not_exists"]
    ) -> ObjectNotExistsWaiter:
        """
        Returns an object that can wait for some condition.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3/client/get_waiter.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_s3/client/#get_waiter)
        """
