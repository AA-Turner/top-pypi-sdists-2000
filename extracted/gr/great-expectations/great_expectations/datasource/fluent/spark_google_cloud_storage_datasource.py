from __future__ import annotations

import logging
from typing import TYPE_CHECKING, Any, ClassVar, Dict, Literal, Type, Union

from great_expectations._docs_decorators import public_api
from great_expectations.compatibility import google, pydantic
from great_expectations.compatibility.typing_extensions import override
from great_expectations.core.util import GCSUrl
from great_expectations.datasource.fluent import _SparkFilePathDatasource
from great_expectations.datasource.fluent.config_str import (
    ConfigStr,
    _check_config_substitutions_needed,
)
from great_expectations.datasource.fluent.data_connector import (
    GoogleCloudStorageDataConnector,
)
from great_expectations.datasource.fluent.interfaces import TestConnectionError
from great_expectations.datasource.fluent.spark_datasource import SparkDatasourceError

if TYPE_CHECKING:
    from great_expectations.compatibility.google import Client
    from great_expectations.datasource.fluent.data_asset.path.spark.spark_asset import (
        SPARK_PATH_ASSET_UNION,
    )

logger = logging.getLogger(__name__)


class SparkGoogleCloudStorageDatasourceError(SparkDatasourceError):
    pass


@public_api
class SparkGoogleCloudStorageDatasource(_SparkFilePathDatasource):
    """
    SparkGoogleCloudStorageDatasource is a subclass of SparkDatasource which connects to
    Google Cloud Storage.
    """

    # class attributes
    data_connector_type: ClassVar[Type[GoogleCloudStorageDataConnector]] = (
        GoogleCloudStorageDataConnector
    )
    # these fields should not be passed to the execution engine
    _EXTRA_EXCLUDED_EXEC_ENG_ARGS: ClassVar[set] = {
        "bucket_or_name",
        "gcs_options",
        "max_results",
    }

    # instance attributes
    type: Literal["spark_gcs"] = "spark_gcs"

    # Google Cloud Storage specific attributes
    bucket_or_name: str
    gcs_options: Dict[str, Union[ConfigStr, Any]] = {}

    # on 3.11 the annotation must be type-checking import otherwise it will fail at import time
    _gcs_client: Union[Client, None] = pydantic.PrivateAttr(default=None)

    def _get_gcs_client(self) -> google.Client:
        gcs_client: Union[google.Client, None] = self._gcs_client
        if not gcs_client:
            # Validate that "google" libararies were successfully imported and attempt to create "gcs_client" handle.  # noqa: E501 # FIXME CoP
            if google.service_account and google.storage:
                try:
                    credentials: Union[google.Client, None] = (
                        None  # If configured with gcloud CLI / env vars
                    )
                    _check_config_substitutions_needed(
                        self,
                        self.gcs_options,
                        raise_warning_if_provider_not_present=True,
                    )
                    # pull in needed config substitutions using the `_config_provider`
                    # The `FluentBaseModel.dict()` call will do the config substitution on the serialized dict if a `config_provider` is passed  # noqa: E501 # FIXME CoP
                    gcs_options: dict = self.dict(config_provider=self._config_provider).get(
                        "gcs_options", {}
                    )

                    if "filename" in gcs_options:
                        filename: str = gcs_options.pop("filename")
                        credentials = google.service_account.Credentials.from_service_account_file(
                            filename=filename
                        )
                    elif "info" in gcs_options:
                        info: Any = gcs_options.pop("info")
                        credentials = google.service_account.Credentials.from_service_account_info(
                            info=info
                        )

                    gcs_client = google.storage.Client(credentials=credentials, **gcs_options)
                except Exception as e:
                    # Failure to create "gcs_client" is most likely due invalid "gcs_options" dictionary.  # noqa: E501 # FIXME CoP
                    raise SparkGoogleCloudStorageDatasourceError(  # noqa: TRY003 # FIXME CoP
                        f'Due to exception: "{e!r}", "gcs_client" could not be created.'
                    ) from e
            else:
                raise SparkGoogleCloudStorageDatasourceError(  # noqa: TRY003 # FIXME CoP
                    'Unable to create "SparkGoogleCloudStorageDatasource" due to missing google dependency.'  # noqa: E501 # FIXME CoP
                )

            self._gcs_client = gcs_client

        return gcs_client

    @override
    def test_connection(self, test_assets: bool = True) -> None:
        """Test the connection for the SparkGoogleCloudStorageDatasource.

        Args:
            test_assets: If assets have been passed to the SparkGoogleCloudStorageDatasource, whether to test them as well.

        Raises:
            TestConnectionError: If the connection test fails.
        """  # noqa: E501 # FIXME CoP
        try:
            # tests GCS connection
            _ = self._get_gcs_client()
        except Exception as e:
            raise TestConnectionError(  # noqa: TRY003 # FIXME CoP
                f"Attempt to connect to datasource failed with the following error message: {e!s}"
            ) from e

        # tests Spark connection, raising TestConnectionError
        super().test_connection()

        if self.assets and test_assets:
            for asset in self.assets:
                asset.test_connection()

    @override
    def _build_data_connector(
        self,
        data_asset: SPARK_PATH_ASSET_UNION,
        gcs_prefix: str = "",
        gcs_delimiter: str = "/",
        gcs_max_results: int = 1000,
        gcs_recursive_file_discovery: bool = False,
        **kwargs,
    ) -> None:
        """Builds and attaches the `GoogleCloudStorageDataConnector` to the asset."""
        if kwargs:
            raise TypeError(  # noqa: TRY003 # FIXME CoP
                f"_build_data_connector() got unexpected keyword arguments {list(kwargs.keys())}"
            )
        data_asset._data_connector = self.data_connector_type.build_data_connector(
            datasource_name=self.name,
            data_asset_name=data_asset.name,
            gcs_client=self._get_gcs_client(),
            bucket_or_name=self.bucket_or_name,
            prefix=gcs_prefix,
            delimiter=gcs_delimiter,
            max_results=gcs_max_results,
            recursive_file_discovery=gcs_recursive_file_discovery,
            file_path_template_map_fn=GCSUrl.OBJECT_URL_TEMPLATE.format,
            whole_directory_path_override=data_asset.get_whole_directory_path_override(),
        )

        # build a more specific `_test_connection_error_message`
        data_asset._test_connection_error_message = (
            self.data_connector_type.build_test_connection_error_message(
                data_asset_name=data_asset.name,
                bucket_or_name=self.bucket_or_name,
                prefix=gcs_prefix,
                delimiter=gcs_delimiter,
                recursive_file_discovery=gcs_recursive_file_discovery,
            )
        )
