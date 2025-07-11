# -*- coding: utf-8 -*-
# Copyright 2025 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
from __future__ import annotations

from typing import MutableSequence

import proto  # type: ignore

from google.ads.googleads.v20.enums.types import access_role as gage_access_role
from google.ads.googleads.v20.enums.types import (
    response_content_type as gage_response_content_type,
)
from google.ads.googleads.v20.resources.types import customer as gagr_customer
from google.protobuf import field_mask_pb2  # type: ignore


__protobuf__ = proto.module(
    package="google.ads.googleads.v20.services",
    marshal="google.ads.googleads.v20",
    manifest={
        "MutateCustomerRequest",
        "CreateCustomerClientRequest",
        "CustomerOperation",
        "CreateCustomerClientResponse",
        "MutateCustomerResponse",
        "MutateCustomerResult",
        "ListAccessibleCustomersRequest",
        "ListAccessibleCustomersResponse",
    },
)


class MutateCustomerRequest(proto.Message):
    r"""Request message for
    [CustomerService.MutateCustomer][google.ads.googleads.v20.services.CustomerService.MutateCustomer].

    Attributes:
        customer_id (str):
            Required. The ID of the customer being
            modified.
        operation (google.ads.googleads.v20.services.types.CustomerOperation):
            Required. The operation to perform on the
            customer
        validate_only (bool):
            If true, the request is validated but not
            executed. Only errors are returned, not results.
        response_content_type (google.ads.googleads.v20.enums.types.ResponseContentTypeEnum.ResponseContentType):
            The response content type setting. Determines
            whether the mutable resource or just the
            resource name should be returned post mutation.
    """

    customer_id: str = proto.Field(
        proto.STRING,
        number=1,
    )
    operation: "CustomerOperation" = proto.Field(
        proto.MESSAGE,
        number=4,
        message="CustomerOperation",
    )
    validate_only: bool = proto.Field(
        proto.BOOL,
        number=5,
    )
    response_content_type: (
        gage_response_content_type.ResponseContentTypeEnum.ResponseContentType
    ) = proto.Field(
        proto.ENUM,
        number=6,
        enum=gage_response_content_type.ResponseContentTypeEnum.ResponseContentType,
    )


class CreateCustomerClientRequest(proto.Message):
    r"""Request message for
    [CustomerService.CreateCustomerClient][google.ads.googleads.v20.services.CustomerService.CreateCustomerClient].


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        customer_id (str):
            Required. The ID of the Manager under whom
            client customer is being created.
        customer_client (google.ads.googleads.v20.resources.types.Customer):
            Required. The new client customer to create.
            The resource name on this customer will be
            ignored.
        email_address (str):
            Email address of the user who should be
            invited on the created client customer.
            Accessible only to customers on the allow-list.

            This field is a member of `oneof`_ ``_email_address``.
        access_role (google.ads.googleads.v20.enums.types.AccessRoleEnum.AccessRole):
            The proposed role of user on the created
            client customer. Accessible only to customers on
            the allow-list.
        validate_only (bool):
            If true, the request is validated but not
            executed. Only errors are returned, not results.
    """

    customer_id: str = proto.Field(
        proto.STRING,
        number=1,
    )
    customer_client: gagr_customer.Customer = proto.Field(
        proto.MESSAGE,
        number=2,
        message=gagr_customer.Customer,
    )
    email_address: str = proto.Field(
        proto.STRING,
        number=5,
        optional=True,
    )
    access_role: gage_access_role.AccessRoleEnum.AccessRole = proto.Field(
        proto.ENUM,
        number=4,
        enum=gage_access_role.AccessRoleEnum.AccessRole,
    )
    validate_only: bool = proto.Field(
        proto.BOOL,
        number=6,
    )


class CustomerOperation(proto.Message):
    r"""A single update on a customer.

    Attributes:
        update (google.ads.googleads.v20.resources.types.Customer):
            Mutate operation. Only updates are supported
            for customer.
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            FieldMask that determines which resource
            fields are modified in an update.
    """

    update: gagr_customer.Customer = proto.Field(
        proto.MESSAGE,
        number=1,
        message=gagr_customer.Customer,
    )
    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=2,
        message=field_mask_pb2.FieldMask,
    )


class CreateCustomerClientResponse(proto.Message):
    r"""Response message for CreateCustomerClient mutate.

    Attributes:
        resource_name (str):
            The resource name of the newly created customer. Customer
            resource names have the form: ``customers/{customer_id}``.
        invitation_link (str):
            Link for inviting user to access the created
            customer. Accessible to allowlisted customers
            only.
    """

    resource_name: str = proto.Field(
        proto.STRING,
        number=2,
    )
    invitation_link: str = proto.Field(
        proto.STRING,
        number=3,
    )


class MutateCustomerResponse(proto.Message):
    r"""Response message for customer mutate.

    Attributes:
        result (google.ads.googleads.v20.services.types.MutateCustomerResult):
            Result for the mutate.
    """

    result: "MutateCustomerResult" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="MutateCustomerResult",
    )


class MutateCustomerResult(proto.Message):
    r"""The result for the customer mutate.

    Attributes:
        resource_name (str):
            Returned for successful operations.
        customer (google.ads.googleads.v20.resources.types.Customer):
            The mutated customer with only mutable fields after mutate.
            The fields will only be returned when response_content_type
            is set to "MUTABLE_RESOURCE".
    """

    resource_name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    customer: gagr_customer.Customer = proto.Field(
        proto.MESSAGE,
        number=2,
        message=gagr_customer.Customer,
    )


class ListAccessibleCustomersRequest(proto.Message):
    r"""Request message for
    [CustomerService.ListAccessibleCustomers][google.ads.googleads.v20.services.CustomerService.ListAccessibleCustomers].

    """


class ListAccessibleCustomersResponse(proto.Message):
    r"""Response message for
    [CustomerService.ListAccessibleCustomers][google.ads.googleads.v20.services.CustomerService.ListAccessibleCustomers].

    Attributes:
        resource_names (MutableSequence[str]):
            Resource name of customers directly
            accessible by the user authenticating the call.
    """

    resource_names: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=1,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
