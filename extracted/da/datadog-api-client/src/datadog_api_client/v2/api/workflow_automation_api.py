# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Any, Dict, Union

from datadog_api_client.api_client import ApiClient, Endpoint as _Endpoint
from datadog_api_client.configuration import Configuration
from datadog_api_client.model_utils import (
    UnsetType,
    unset,
)
from datadog_api_client.v2.model.create_workflow_response import CreateWorkflowResponse
from datadog_api_client.v2.model.create_workflow_request import CreateWorkflowRequest
from datadog_api_client.v2.model.get_workflow_response import GetWorkflowResponse
from datadog_api_client.v2.model.update_workflow_response import UpdateWorkflowResponse
from datadog_api_client.v2.model.update_workflow_request import UpdateWorkflowRequest
from datadog_api_client.v2.model.workflow_list_instances_response import WorkflowListInstancesResponse
from datadog_api_client.v2.model.workflow_instance_create_response import WorkflowInstanceCreateResponse
from datadog_api_client.v2.model.workflow_instance_create_request import WorkflowInstanceCreateRequest
from datadog_api_client.v2.model.worklflow_get_instance_response import WorklflowGetInstanceResponse
from datadog_api_client.v2.model.worklflow_cancel_instance_response import WorklflowCancelInstanceResponse


class WorkflowAutomationApi:
    """
    Datadog Workflow Automation allows you to automate your end-to-end processes by connecting Datadog with the rest of your tech stack. Build workflows to auto-remediate your alerts, streamline your incident and security processes, and reduce manual toil. Workflow Automation supports over 1,000+ OOTB actions, including AWS, JIRA, ServiceNow, GitHub, and OpenAI. Learn more in our Workflow Automation docs `here <https://docs.datadoghq.com/service_management/workflows/>`_.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient(Configuration())
        self.api_client = api_client

        self._cancel_workflow_instance_endpoint = _Endpoint(
            settings={
                "response_type": (WorklflowCancelInstanceResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/workflows/{workflow_id}/instances/{instance_id}/cancel",
                "operation_id": "cancel_workflow_instance",
                "http_method": "PUT",
                "version": "v2",
            },
            params_map={
                "workflow_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "workflow_id",
                    "location": "path",
                },
                "instance_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "instance_id",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._create_workflow_endpoint = _Endpoint(
            settings={
                "response_type": (CreateWorkflowResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/workflows",
                "operation_id": "create_workflow",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "body": {
                    "required": True,
                    "openapi_types": (CreateWorkflowRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._create_workflow_instance_endpoint = _Endpoint(
            settings={
                "response_type": (WorkflowInstanceCreateResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/workflows/{workflow_id}/instances",
                "operation_id": "create_workflow_instance",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "workflow_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "workflow_id",
                    "location": "path",
                },
                "body": {
                    "required": True,
                    "openapi_types": (WorkflowInstanceCreateRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._delete_workflow_endpoint = _Endpoint(
            settings={
                "response_type": None,
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/workflows/{workflow_id}",
                "operation_id": "delete_workflow",
                "http_method": "DELETE",
                "version": "v2",
            },
            params_map={
                "workflow_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "workflow_id",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["*/*"],
            },
            api_client=api_client,
        )

        self._get_workflow_endpoint = _Endpoint(
            settings={
                "response_type": (GetWorkflowResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/workflows/{workflow_id}",
                "operation_id": "get_workflow",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "workflow_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "workflow_id",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._get_workflow_instance_endpoint = _Endpoint(
            settings={
                "response_type": (WorklflowGetInstanceResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/workflows/{workflow_id}/instances/{instance_id}",
                "operation_id": "get_workflow_instance",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "workflow_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "workflow_id",
                    "location": "path",
                },
                "instance_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "instance_id",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._list_workflow_instances_endpoint = _Endpoint(
            settings={
                "response_type": (WorkflowListInstancesResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/workflows/{workflow_id}/instances",
                "operation_id": "list_workflow_instances",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "workflow_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "workflow_id",
                    "location": "path",
                },
                "page_size": {
                    "openapi_types": (int,),
                    "attribute": "page[size]",
                    "location": "query",
                },
                "page_number": {
                    "openapi_types": (int,),
                    "attribute": "page[number]",
                    "location": "query",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._update_workflow_endpoint = _Endpoint(
            settings={
                "response_type": (UpdateWorkflowResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/workflows/{workflow_id}",
                "operation_id": "update_workflow",
                "http_method": "PATCH",
                "version": "v2",
            },
            params_map={
                "workflow_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "workflow_id",
                    "location": "path",
                },
                "body": {
                    "required": True,
                    "openapi_types": (UpdateWorkflowRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

    def cancel_workflow_instance(
        self,
        workflow_id: str,
        instance_id: str,
    ) -> WorklflowCancelInstanceResponse:
        """Cancel a workflow instance.

        Cancels a specific execution of a given workflow. This API requires a `registered application key <https://docs.datadoghq.com/api/latest/action-connection/#register-a-new-app-key>`_.

        :param workflow_id: The ID of the workflow.
        :type workflow_id: str
        :param instance_id: The ID of the workflow instance.
        :type instance_id: str
        :rtype: WorklflowCancelInstanceResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["workflow_id"] = workflow_id

        kwargs["instance_id"] = instance_id

        return self._cancel_workflow_instance_endpoint.call_with_http_info(**kwargs)

    def create_workflow(
        self,
        body: CreateWorkflowRequest,
    ) -> CreateWorkflowResponse:
        """Create a Workflow.

        Create a new workflow, returning the workflow ID. This API requires a `registered application key <https://docs.datadoghq.com/api/latest/action-connection/#register-a-new-app-key>`_.

        :type body: CreateWorkflowRequest
        :rtype: CreateWorkflowResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["body"] = body

        return self._create_workflow_endpoint.call_with_http_info(**kwargs)

    def create_workflow_instance(
        self,
        workflow_id: str,
        body: WorkflowInstanceCreateRequest,
    ) -> WorkflowInstanceCreateResponse:
        """Execute a workflow.

        Execute the given workflow. This API requires a `registered application key <https://docs.datadoghq.com/api/latest/action-connection/#register-a-new-app-key>`_.

        :param workflow_id: The ID of the workflow.
        :type workflow_id: str
        :type body: WorkflowInstanceCreateRequest
        :rtype: WorkflowInstanceCreateResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["workflow_id"] = workflow_id

        kwargs["body"] = body

        return self._create_workflow_instance_endpoint.call_with_http_info(**kwargs)

    def delete_workflow(
        self,
        workflow_id: str,
    ) -> None:
        """Delete an existing Workflow.

        Delete a workflow by ID. This API requires a `registered application key <https://docs.datadoghq.com/api/latest/action-connection/#register-a-new-app-key>`_.

        :param workflow_id: The ID of the workflow.
        :type workflow_id: str
        :rtype: None
        """
        kwargs: Dict[str, Any] = {}
        kwargs["workflow_id"] = workflow_id

        return self._delete_workflow_endpoint.call_with_http_info(**kwargs)

    def get_workflow(
        self,
        workflow_id: str,
    ) -> GetWorkflowResponse:
        """Get an existing Workflow.

        Get a workflow by ID. This API requires a `registered application key <https://docs.datadoghq.com/api/latest/action-connection/#register-a-new-app-key>`_.

        :param workflow_id: The ID of the workflow.
        :type workflow_id: str
        :rtype: GetWorkflowResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["workflow_id"] = workflow_id

        return self._get_workflow_endpoint.call_with_http_info(**kwargs)

    def get_workflow_instance(
        self,
        workflow_id: str,
        instance_id: str,
    ) -> WorklflowGetInstanceResponse:
        """Get a workflow instance.

        Get a specific execution of a given workflow. This API requires a `registered application key <https://docs.datadoghq.com/api/latest/action-connection/#register-a-new-app-key>`_.

        :param workflow_id: The ID of the workflow.
        :type workflow_id: str
        :param instance_id: The ID of the workflow instance.
        :type instance_id: str
        :rtype: WorklflowGetInstanceResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["workflow_id"] = workflow_id

        kwargs["instance_id"] = instance_id

        return self._get_workflow_instance_endpoint.call_with_http_info(**kwargs)

    def list_workflow_instances(
        self,
        workflow_id: str,
        *,
        page_size: Union[int, UnsetType] = unset,
        page_number: Union[int, UnsetType] = unset,
    ) -> WorkflowListInstancesResponse:
        """List workflow instances.

        List all instances of a given workflow. This API requires a `registered application key <https://docs.datadoghq.com/api/latest/action-connection/#register-a-new-app-key>`_.

        :param workflow_id: The ID of the workflow.
        :type workflow_id: str
        :param page_size: Size for a given page. The maximum allowed value is 100.
        :type page_size: int, optional
        :param page_number: Specific page number to return.
        :type page_number: int, optional
        :rtype: WorkflowListInstancesResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["workflow_id"] = workflow_id

        if page_size is not unset:
            kwargs["page_size"] = page_size

        if page_number is not unset:
            kwargs["page_number"] = page_number

        return self._list_workflow_instances_endpoint.call_with_http_info(**kwargs)

    def update_workflow(
        self,
        workflow_id: str,
        body: UpdateWorkflowRequest,
    ) -> UpdateWorkflowResponse:
        """Update an existing Workflow.

        Update a workflow by ID. This API requires a `registered application key <https://docs.datadoghq.com/api/latest/action-connection/#register-a-new-app-key>`_.

        :param workflow_id: The ID of the workflow.
        :type workflow_id: str
        :type body: UpdateWorkflowRequest
        :rtype: UpdateWorkflowResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["workflow_id"] = workflow_id

        kwargs["body"] = body

        return self._update_workflow_endpoint.call_with_http_info(**kwargs)
