# This file was auto-generated by Fern from our API Definition.

import typing
import urllib.parse
from json.decoder import JSONDecodeError

from ...core.api_error import ApiError
from ...core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ...core.jsonable_encoder import jsonable_encoder
from ...core.remove_none_from_dict import remove_none_from_dict
from ...errors.unprocessable_entity_error import UnprocessableEntityError
from ...types.http_validation_error import HttpValidationError
from ...types.message import Message
from ...types.model_configuration import ModelConfiguration

try:
    import pydantic
    if pydantic.__version__.startswith("1."):
        raise ImportError
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore

# this is used as the default value for optional parameters
OMIT = typing.cast(typing.Any, ...)


class ResponsesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def generate_response(
        self,
        *,
        project_id: typing.Optional[str] = None,
        organization_id: typing.Optional[str] = None,
        messages: typing.List[Message],
        model_configuration: ModelConfiguration,
    ) -> typing.Any:
        """
        EXPERIMENTAL - SSE endpoint for basic response generation (dummy stream).

        Parameters:
            - project_id: typing.Optional[str].

            - organization_id: typing.Optional[str].

            - messages: typing.List[Message]. List of messages in the conversation

            - model_configuration: ModelConfiguration. Configuration for the model to use in the response
        ---
        from llama_cloud import ModelConfiguration, SupportedLlmModelNames
        from llama_cloud.client import LlamaCloud

        client = LlamaCloud(
            token="YOUR_TOKEN",
        )
        client.responses.generate_response(
            messages=[],
            model_configuration=ModelConfiguration(
                model_name=SupportedLlmModelNames.GPT_4_O,
            ),
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            "POST",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "api/v1/responses/generate"),
            params=remove_none_from_dict({"project_id": project_id, "organization_id": organization_id}),
            json=jsonable_encoder({"messages": messages, "model_configuration": model_configuration}),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(typing.Any, _response.json())  # type: ignore
        if _response.status_code == 422:
            raise UnprocessableEntityError(pydantic.parse_obj_as(HttpValidationError, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)


class AsyncResponsesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def generate_response(
        self,
        *,
        project_id: typing.Optional[str] = None,
        organization_id: typing.Optional[str] = None,
        messages: typing.List[Message],
        model_configuration: ModelConfiguration,
    ) -> typing.Any:
        """
        EXPERIMENTAL - SSE endpoint for basic response generation (dummy stream).

        Parameters:
            - project_id: typing.Optional[str].

            - organization_id: typing.Optional[str].

            - messages: typing.List[Message]. List of messages in the conversation

            - model_configuration: ModelConfiguration. Configuration for the model to use in the response
        ---
        from llama_cloud import ModelConfiguration, SupportedLlmModelNames
        from llama_cloud.client import AsyncLlamaCloud

        client = AsyncLlamaCloud(
            token="YOUR_TOKEN",
        )
        await client.responses.generate_response(
            messages=[],
            model_configuration=ModelConfiguration(
                model_name=SupportedLlmModelNames.GPT_4_O,
            ),
        )
        """
        _response = await self._client_wrapper.httpx_client.request(
            "POST",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "api/v1/responses/generate"),
            params=remove_none_from_dict({"project_id": project_id, "organization_id": organization_id}),
            json=jsonable_encoder({"messages": messages, "model_configuration": model_configuration}),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(typing.Any, _response.json())  # type: ignore
        if _response.status_code == 422:
            raise UnprocessableEntityError(pydantic.parse_obj_as(HttpValidationError, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)
