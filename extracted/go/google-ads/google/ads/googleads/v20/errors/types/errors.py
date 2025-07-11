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

from google.ads.googleads.v20.common.types import policy
from google.ads.googleads.v20.common.types import value
from google.ads.googleads.v20.enums.types import resource_limit_type
from google.ads.googleads.v20.errors.types import (
    access_invitation_error as gage_access_invitation_error,
)
from google.ads.googleads.v20.errors.types import (
    account_budget_proposal_error as gage_account_budget_proposal_error,
)
from google.ads.googleads.v20.errors.types import (
    account_link_error as gage_account_link_error,
)
from google.ads.googleads.v20.errors.types import (
    ad_customizer_error as gage_ad_customizer_error,
)
from google.ads.googleads.v20.errors.types import ad_error as gage_ad_error
from google.ads.googleads.v20.errors.types import (
    ad_group_ad_error as gage_ad_group_ad_error,
)
from google.ads.googleads.v20.errors.types import (
    ad_group_bid_modifier_error as gage_ad_group_bid_modifier_error,
)
from google.ads.googleads.v20.errors.types import (
    ad_group_criterion_customizer_error as gage_ad_group_criterion_customizer_error,
)
from google.ads.googleads.v20.errors.types import (
    ad_group_criterion_error as gage_ad_group_criterion_error,
)
from google.ads.googleads.v20.errors.types import (
    ad_group_customizer_error as gage_ad_group_customizer_error,
)
from google.ads.googleads.v20.errors.types import (
    ad_group_error as gage_ad_group_error,
)
from google.ads.googleads.v20.errors.types import (
    ad_group_feed_error as gage_ad_group_feed_error,
)
from google.ads.googleads.v20.errors.types import (
    ad_parameter_error as gage_ad_parameter_error,
)
from google.ads.googleads.v20.errors.types import (
    ad_sharing_error as gage_ad_sharing_error,
)
from google.ads.googleads.v20.errors.types import adx_error as gage_adx_error
from google.ads.googleads.v20.errors.types import (
    asset_error as gage_asset_error,
)
from google.ads.googleads.v20.errors.types import (
    asset_group_asset_error as gage_asset_group_asset_error,
)
from google.ads.googleads.v20.errors.types import (
    asset_group_error as gage_asset_group_error,
)
from google.ads.googleads.v20.errors.types import (
    asset_group_listing_group_filter_error as gage_asset_group_listing_group_filter_error,
)
from google.ads.googleads.v20.errors.types import (
    asset_group_signal_error as gage_asset_group_signal_error,
)
from google.ads.googleads.v20.errors.types import (
    asset_link_error as gage_asset_link_error,
)
from google.ads.googleads.v20.errors.types import (
    asset_set_asset_error as gage_asset_set_asset_error,
)
from google.ads.googleads.v20.errors.types import (
    asset_set_error as gage_asset_set_error,
)
from google.ads.googleads.v20.errors.types import (
    asset_set_link_error as gage_asset_set_link_error,
)
from google.ads.googleads.v20.errors.types import (
    audience_error as gage_audience_error,
)
from google.ads.googleads.v20.errors.types import (
    audience_insights_error as gage_audience_insights_error,
)
from google.ads.googleads.v20.errors.types import (
    authentication_error as gage_authentication_error,
)
from google.ads.googleads.v20.errors.types import (
    authorization_error as gage_authorization_error,
)
from google.ads.googleads.v20.errors.types import (
    automatically_created_asset_removal_error as gage_automatically_created_asset_removal_error,
)
from google.ads.googleads.v20.errors.types import (
    batch_job_error as gage_batch_job_error,
)
from google.ads.googleads.v20.errors.types import (
    bidding_error as gage_bidding_error,
)
from google.ads.googleads.v20.errors.types import (
    bidding_strategy_error as gage_bidding_strategy_error,
)
from google.ads.googleads.v20.errors.types import (
    billing_setup_error as gage_billing_setup_error,
)
from google.ads.googleads.v20.errors.types import (
    brand_guidelines_migration_error as gage_brand_guidelines_migration_error,
)
from google.ads.googleads.v20.errors.types import (
    campaign_budget_error as gage_campaign_budget_error,
)
from google.ads.googleads.v20.errors.types import (
    campaign_conversion_goal_error as gage_campaign_conversion_goal_error,
)
from google.ads.googleads.v20.errors.types import (
    campaign_criterion_error as gage_campaign_criterion_error,
)
from google.ads.googleads.v20.errors.types import (
    campaign_customizer_error as gage_campaign_customizer_error,
)
from google.ads.googleads.v20.errors.types import (
    campaign_draft_error as gage_campaign_draft_error,
)
from google.ads.googleads.v20.errors.types import (
    campaign_error as gage_campaign_error,
)
from google.ads.googleads.v20.errors.types import (
    campaign_experiment_error as gage_campaign_experiment_error,
)
from google.ads.googleads.v20.errors.types import (
    campaign_feed_error as gage_campaign_feed_error,
)
from google.ads.googleads.v20.errors.types import (
    campaign_lifecycle_goal_error as gage_campaign_lifecycle_goal_error,
)
from google.ads.googleads.v20.errors.types import (
    campaign_shared_set_error as gage_campaign_shared_set_error,
)
from google.ads.googleads.v20.errors.types import (
    change_event_error as gage_change_event_error,
)
from google.ads.googleads.v20.errors.types import (
    change_status_error as gage_change_status_error,
)
from google.ads.googleads.v20.errors.types import (
    click_view_error as gage_click_view_error,
)
from google.ads.googleads.v20.errors.types import (
    collection_size_error as gage_collection_size_error,
)
from google.ads.googleads.v20.errors.types import (
    context_error as gage_context_error,
)
from google.ads.googleads.v20.errors.types import (
    conversion_action_error as gage_conversion_action_error,
)
from google.ads.googleads.v20.errors.types import (
    conversion_adjustment_upload_error as gage_conversion_adjustment_upload_error,
)
from google.ads.googleads.v20.errors.types import (
    conversion_custom_variable_error as gage_conversion_custom_variable_error,
)
from google.ads.googleads.v20.errors.types import (
    conversion_goal_campaign_config_error as gage_conversion_goal_campaign_config_error,
)
from google.ads.googleads.v20.errors.types import (
    conversion_upload_error as gage_conversion_upload_error,
)
from google.ads.googleads.v20.errors.types import (
    conversion_value_rule_error as gage_conversion_value_rule_error,
)
from google.ads.googleads.v20.errors.types import (
    conversion_value_rule_set_error as gage_conversion_value_rule_set_error,
)
from google.ads.googleads.v20.errors.types import (
    country_code_error as gage_country_code_error,
)
from google.ads.googleads.v20.errors.types import (
    criterion_error as gage_criterion_error,
)
from google.ads.googleads.v20.errors.types import (
    currency_code_error as gage_currency_code_error,
)
from google.ads.googleads.v20.errors.types import (
    currency_error as gage_currency_error,
)
from google.ads.googleads.v20.errors.types import (
    custom_audience_error as gage_custom_audience_error,
)
from google.ads.googleads.v20.errors.types import (
    custom_conversion_goal_error as gage_custom_conversion_goal_error,
)
from google.ads.googleads.v20.errors.types import (
    custom_interest_error as gage_custom_interest_error,
)
from google.ads.googleads.v20.errors.types import (
    customer_client_link_error as gage_customer_client_link_error,
)
from google.ads.googleads.v20.errors.types import (
    customer_customizer_error as gage_customer_customizer_error,
)
from google.ads.googleads.v20.errors.types import (
    customer_error as gage_customer_error,
)
from google.ads.googleads.v20.errors.types import (
    customer_feed_error as gage_customer_feed_error,
)
from google.ads.googleads.v20.errors.types import (
    customer_lifecycle_goal_error as gage_customer_lifecycle_goal_error,
)
from google.ads.googleads.v20.errors.types import (
    customer_manager_link_error as gage_customer_manager_link_error,
)
from google.ads.googleads.v20.errors.types import (
    customer_sk_ad_network_conversion_value_schema_error as gage_customer_sk_ad_network_conversion_value_schema_error,
)
from google.ads.googleads.v20.errors.types import (
    customer_user_access_error as gage_customer_user_access_error,
)
from google.ads.googleads.v20.errors.types import (
    customizer_attribute_error as gage_customizer_attribute_error,
)
from google.ads.googleads.v20.errors.types import (
    data_link_error as gage_data_link_error,
)
from google.ads.googleads.v20.errors.types import (
    database_error as gage_database_error,
)
from google.ads.googleads.v20.errors.types import date_error as gage_date_error
from google.ads.googleads.v20.errors.types import (
    date_range_error as gage_date_range_error,
)
from google.ads.googleads.v20.errors.types import (
    distinct_error as gage_distinct_error,
)
from google.ads.googleads.v20.errors.types import enum_error as gage_enum_error
from google.ads.googleads.v20.errors.types import (
    experiment_arm_error as gage_experiment_arm_error,
)
from google.ads.googleads.v20.errors.types import (
    experiment_error as gage_experiment_error,
)
from google.ads.googleads.v20.errors.types import (
    extension_feed_item_error as gage_extension_feed_item_error,
)
from google.ads.googleads.v20.errors.types import (
    extension_setting_error as gage_extension_setting_error,
)
from google.ads.googleads.v20.errors.types import (
    feed_attribute_reference_error as gage_feed_attribute_reference_error,
)
from google.ads.googleads.v20.errors.types import feed_error as gage_feed_error
from google.ads.googleads.v20.errors.types import (
    feed_item_error as gage_feed_item_error,
)
from google.ads.googleads.v20.errors.types import (
    feed_item_set_error as gage_feed_item_set_error,
)
from google.ads.googleads.v20.errors.types import (
    feed_item_set_link_error as gage_feed_item_set_link_error,
)
from google.ads.googleads.v20.errors.types import (
    feed_item_target_error as gage_feed_item_target_error,
)
from google.ads.googleads.v20.errors.types import (
    feed_item_validation_error as gage_feed_item_validation_error,
)
from google.ads.googleads.v20.errors.types import (
    feed_mapping_error as gage_feed_mapping_error,
)
from google.ads.googleads.v20.errors.types import (
    field_error as gage_field_error,
)
from google.ads.googleads.v20.errors.types import (
    field_mask_error as gage_field_mask_error,
)
from google.ads.googleads.v20.errors.types import (
    function_error as gage_function_error,
)
from google.ads.googleads.v20.errors.types import (
    function_parsing_error as gage_function_parsing_error,
)
from google.ads.googleads.v20.errors.types import (
    geo_target_constant_suggestion_error as gage_geo_target_constant_suggestion_error,
)
from google.ads.googleads.v20.errors.types import (
    header_error as gage_header_error,
)
from google.ads.googleads.v20.errors.types import id_error as gage_id_error
from google.ads.googleads.v20.errors.types import (
    identity_verification_error as gage_identity_verification_error,
)
from google.ads.googleads.v20.errors.types import (
    image_error as gage_image_error,
)
from google.ads.googleads.v20.errors.types import (
    internal_error as gage_internal_error,
)
from google.ads.googleads.v20.errors.types import (
    invoice_error as gage_invoice_error,
)
from google.ads.googleads.v20.errors.types import (
    keyword_plan_ad_group_error as gage_keyword_plan_ad_group_error,
)
from google.ads.googleads.v20.errors.types import (
    keyword_plan_ad_group_keyword_error as gage_keyword_plan_ad_group_keyword_error,
)
from google.ads.googleads.v20.errors.types import (
    keyword_plan_campaign_error as gage_keyword_plan_campaign_error,
)
from google.ads.googleads.v20.errors.types import (
    keyword_plan_campaign_keyword_error as gage_keyword_plan_campaign_keyword_error,
)
from google.ads.googleads.v20.errors.types import (
    keyword_plan_error as gage_keyword_plan_error,
)
from google.ads.googleads.v20.errors.types import (
    keyword_plan_idea_error as gage_keyword_plan_idea_error,
)
from google.ads.googleads.v20.errors.types import (
    label_error as gage_label_error,
)
from google.ads.googleads.v20.errors.types import (
    language_code_error as gage_language_code_error,
)
from google.ads.googleads.v20.errors.types import (
    list_operation_error as gage_list_operation_error,
)
from google.ads.googleads.v20.errors.types import (
    manager_link_error as gage_manager_link_error,
)
from google.ads.googleads.v20.errors.types import (
    media_bundle_error as gage_media_bundle_error,
)
from google.ads.googleads.v20.errors.types import (
    media_file_error as gage_media_file_error,
)
from google.ads.googleads.v20.errors.types import (
    media_upload_error as gage_media_upload_error,
)
from google.ads.googleads.v20.errors.types import (
    merchant_center_error as gage_merchant_center_error,
)
from google.ads.googleads.v20.errors.types import (
    multiplier_error as gage_multiplier_error,
)
from google.ads.googleads.v20.errors.types import (
    mutate_error as gage_mutate_error,
)
from google.ads.googleads.v20.errors.types import (
    new_resource_creation_error as gage_new_resource_creation_error,
)
from google.ads.googleads.v20.errors.types import (
    not_allowlisted_error as gage_not_allowlisted_error,
)
from google.ads.googleads.v20.errors.types import (
    not_empty_error as gage_not_empty_error,
)
from google.ads.googleads.v20.errors.types import null_error as gage_null_error
from google.ads.googleads.v20.errors.types import (
    offline_user_data_job_error as gage_offline_user_data_job_error,
)
from google.ads.googleads.v20.errors.types import (
    operation_access_denied_error as gage_operation_access_denied_error,
)
from google.ads.googleads.v20.errors.types import (
    operator_error as gage_operator_error,
)
from google.ads.googleads.v20.errors.types import (
    partial_failure_error as gage_partial_failure_error,
)
from google.ads.googleads.v20.errors.types import (
    payments_account_error as gage_payments_account_error,
)
from google.ads.googleads.v20.errors.types import (
    policy_finding_error as gage_policy_finding_error,
)
from google.ads.googleads.v20.errors.types import (
    policy_validation_parameter_error as gage_policy_validation_parameter_error,
)
from google.ads.googleads.v20.errors.types import (
    policy_violation_error as gage_policy_violation_error,
)
from google.ads.googleads.v20.errors.types import (
    product_link_error as gage_product_link_error,
)
from google.ads.googleads.v20.errors.types import (
    product_link_invitation_error as gage_product_link_invitation_error,
)
from google.ads.googleads.v20.errors.types import (
    query_error as gage_query_error,
)
from google.ads.googleads.v20.errors.types import (
    quota_error as gage_quota_error,
)
from google.ads.googleads.v20.errors.types import (
    range_error as gage_range_error,
)
from google.ads.googleads.v20.errors.types import (
    reach_plan_error as gage_reach_plan_error,
)
from google.ads.googleads.v20.errors.types import (
    recommendation_error as gage_recommendation_error,
)
from google.ads.googleads.v20.errors.types import (
    recommendation_subscription_error as gage_recommendation_subscription_error,
)
from google.ads.googleads.v20.errors.types import (
    region_code_error as gage_region_code_error,
)
from google.ads.googleads.v20.errors.types import (
    request_error as gage_request_error,
)
from google.ads.googleads.v20.errors.types import (
    resource_access_denied_error as gage_resource_access_denied_error,
)
from google.ads.googleads.v20.errors.types import (
    resource_count_limit_exceeded_error as gage_resource_count_limit_exceeded_error,
)
from google.ads.googleads.v20.errors.types import (
    search_term_insight_error as gage_search_term_insight_error,
)
from google.ads.googleads.v20.errors.types import (
    setting_error as gage_setting_error,
)
from google.ads.googleads.v20.errors.types import (
    shareable_preview_error as gage_shareable_preview_error,
)
from google.ads.googleads.v20.errors.types import (
    shared_criterion_error as gage_shared_criterion_error,
)
from google.ads.googleads.v20.errors.types import (
    shared_set_error as gage_shared_set_error,
)
from google.ads.googleads.v20.errors.types import (
    shopping_product_error as gage_shopping_product_error,
)
from google.ads.googleads.v20.errors.types import (
    size_limit_error as gage_size_limit_error,
)
from google.ads.googleads.v20.errors.types import (
    smart_campaign_error as gage_smart_campaign_error,
)
from google.ads.googleads.v20.errors.types import (
    string_format_error as gage_string_format_error,
)
from google.ads.googleads.v20.errors.types import (
    string_length_error as gage_string_length_error,
)
from google.ads.googleads.v20.errors.types import (
    third_party_app_analytics_link_error as gage_third_party_app_analytics_link_error,
)
from google.ads.googleads.v20.errors.types import (
    time_zone_error as gage_time_zone_error,
)
from google.ads.googleads.v20.errors.types import (
    url_field_error as gage_url_field_error,
)
from google.ads.googleads.v20.errors.types import (
    user_data_error as gage_user_data_error,
)
from google.ads.googleads.v20.errors.types import (
    user_list_customer_type_error as gage_user_list_customer_type_error,
)
from google.ads.googleads.v20.errors.types import (
    user_list_error as gage_user_list_error,
)
from google.ads.googleads.v20.errors.types import (
    video_campaign_error as gage_video_campaign_error,
)
from google.ads.googleads.v20.errors.types import (
    youtube_video_registration_error as gage_youtube_video_registration_error,
)
from google.protobuf import duration_pb2  # type: ignore


__protobuf__ = proto.module(
    package="google.ads.googleads.v20.errors",
    marshal="google.ads.googleads.v20",
    manifest={
        "GoogleAdsFailure",
        "GoogleAdsError",
        "ErrorCode",
        "ErrorLocation",
        "ErrorDetails",
        "PolicyViolationDetails",
        "PolicyFindingDetails",
        "QuotaErrorDetails",
        "ResourceCountDetails",
    },
)


class GoogleAdsFailure(proto.Message):
    r"""Describes how a GoogleAds API call failed. It's returned
    inside google.rpc.Status.details when a call fails.

    Attributes:
        errors (MutableSequence[google.ads.googleads.v20.errors.types.GoogleAdsError]):
            The list of errors that occurred.
        request_id (str):
            The unique ID of the request that is used for
            debugging purposes.
    """

    errors: MutableSequence["GoogleAdsError"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="GoogleAdsError",
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=2,
    )


class GoogleAdsError(proto.Message):
    r"""GoogleAds-specific error.

    Attributes:
        error_code (google.ads.googleads.v20.errors.types.ErrorCode):
            An enum value that indicates which error
            occurred.
        message (str):
            A human-readable description of the error.
        trigger (google.ads.googleads.v20.common.types.Value):
            The value that triggered the error.
        location (google.ads.googleads.v20.errors.types.ErrorLocation):
            Describes the part of the request proto that
            caused the error.
        details (google.ads.googleads.v20.errors.types.ErrorDetails):
            Additional error details, which are returned
            by certain error codes. Most error codes do not
            include details.
    """

    error_code: "ErrorCode" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="ErrorCode",
    )
    message: str = proto.Field(
        proto.STRING,
        number=2,
    )
    trigger: value.Value = proto.Field(
        proto.MESSAGE,
        number=3,
        message=value.Value,
    )
    location: "ErrorLocation" = proto.Field(
        proto.MESSAGE,
        number=4,
        message="ErrorLocation",
    )
    details: "ErrorDetails" = proto.Field(
        proto.MESSAGE,
        number=5,
        message="ErrorDetails",
    )


class ErrorCode(proto.Message):
    r"""The error reason represented by type and enum.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        request_error (google.ads.googleads.v20.errors.types.RequestErrorEnum.RequestError):
            An error caused by the request

            This field is a member of `oneof`_ ``error_code``.
        bidding_strategy_error (google.ads.googleads.v20.errors.types.BiddingStrategyErrorEnum.BiddingStrategyError):
            An error with a Bidding Strategy mutate.

            This field is a member of `oneof`_ ``error_code``.
        url_field_error (google.ads.googleads.v20.errors.types.UrlFieldErrorEnum.UrlFieldError):
            An error with a URL field mutate.

            This field is a member of `oneof`_ ``error_code``.
        list_operation_error (google.ads.googleads.v20.errors.types.ListOperationErrorEnum.ListOperationError):
            An error with a list operation.

            This field is a member of `oneof`_ ``error_code``.
        query_error (google.ads.googleads.v20.errors.types.QueryErrorEnum.QueryError):
            An error with an AWQL query

            This field is a member of `oneof`_ ``error_code``.
        mutate_error (google.ads.googleads.v20.errors.types.MutateErrorEnum.MutateError):
            An error with a mutate

            This field is a member of `oneof`_ ``error_code``.
        field_mask_error (google.ads.googleads.v20.errors.types.FieldMaskErrorEnum.FieldMaskError):
            An error with a field mask

            This field is a member of `oneof`_ ``error_code``.
        authorization_error (google.ads.googleads.v20.errors.types.AuthorizationErrorEnum.AuthorizationError):
            An error encountered when trying to authorize
            a user.

            This field is a member of `oneof`_ ``error_code``.
        internal_error (google.ads.googleads.v20.errors.types.InternalErrorEnum.InternalError):
            An unexpected server-side error.

            This field is a member of `oneof`_ ``error_code``.
        quota_error (google.ads.googleads.v20.errors.types.QuotaErrorEnum.QuotaError):
            An error with the amount of quota remaining.

            This field is a member of `oneof`_ ``error_code``.
        ad_error (google.ads.googleads.v20.errors.types.AdErrorEnum.AdError):
            An error with an Ad Group Ad mutate.

            This field is a member of `oneof`_ ``error_code``.
        ad_group_error (google.ads.googleads.v20.errors.types.AdGroupErrorEnum.AdGroupError):
            An error with an Ad Group mutate.

            This field is a member of `oneof`_ ``error_code``.
        campaign_budget_error (google.ads.googleads.v20.errors.types.CampaignBudgetErrorEnum.CampaignBudgetError):
            An error with a Campaign Budget mutate.

            This field is a member of `oneof`_ ``error_code``.
        campaign_error (google.ads.googleads.v20.errors.types.CampaignErrorEnum.CampaignError):
            An error with a Campaign mutate.

            This field is a member of `oneof`_ ``error_code``.
        video_campaign_error (google.ads.googleads.v20.errors.types.VideoCampaignErrorEnum.VideoCampaignError):
            An error with a Video Campaign mutate.

            This field is a member of `oneof`_ ``error_code``.
        authentication_error (google.ads.googleads.v20.errors.types.AuthenticationErrorEnum.AuthenticationError):
            Indicates failure to properly authenticate
            user.

            This field is a member of `oneof`_ ``error_code``.
        ad_group_criterion_customizer_error (google.ads.googleads.v20.errors.types.AdGroupCriterionCustomizerErrorEnum.AdGroupCriterionCustomizerError):
            The reasons for the ad group criterion
            customizer error.

            This field is a member of `oneof`_ ``error_code``.
        ad_group_criterion_error (google.ads.googleads.v20.errors.types.AdGroupCriterionErrorEnum.AdGroupCriterionError):
            Indicates failure to properly authenticate
            user.

            This field is a member of `oneof`_ ``error_code``.
        ad_group_customizer_error (google.ads.googleads.v20.errors.types.AdGroupCustomizerErrorEnum.AdGroupCustomizerError):
            The reasons for the ad group customizer
            error.

            This field is a member of `oneof`_ ``error_code``.
        ad_customizer_error (google.ads.googleads.v20.errors.types.AdCustomizerErrorEnum.AdCustomizerError):
            The reasons for the ad customizer error

            This field is a member of `oneof`_ ``error_code``.
        ad_group_ad_error (google.ads.googleads.v20.errors.types.AdGroupAdErrorEnum.AdGroupAdError):
            The reasons for the ad group ad error

            This field is a member of `oneof`_ ``error_code``.
        ad_sharing_error (google.ads.googleads.v20.errors.types.AdSharingErrorEnum.AdSharingError):
            The reasons for the ad sharing error

            This field is a member of `oneof`_ ``error_code``.
        adx_error (google.ads.googleads.v20.errors.types.AdxErrorEnum.AdxError):
            The reasons for the adx error

            This field is a member of `oneof`_ ``error_code``.
        asset_error (google.ads.googleads.v20.errors.types.AssetErrorEnum.AssetError):
            The reasons for the asset error

            This field is a member of `oneof`_ ``error_code``.
        asset_group_asset_error (google.ads.googleads.v20.errors.types.AssetGroupAssetErrorEnum.AssetGroupAssetError):
            The reasons for the asset group asset error

            This field is a member of `oneof`_ ``error_code``.
        asset_group_listing_group_filter_error (google.ads.googleads.v20.errors.types.AssetGroupListingGroupFilterErrorEnum.AssetGroupListingGroupFilterError):
            The reasons for the asset group listing group
            filter error

            This field is a member of `oneof`_ ``error_code``.
        asset_group_error (google.ads.googleads.v20.errors.types.AssetGroupErrorEnum.AssetGroupError):
            The reasons for the asset group error

            This field is a member of `oneof`_ ``error_code``.
        asset_set_asset_error (google.ads.googleads.v20.errors.types.AssetSetAssetErrorEnum.AssetSetAssetError):
            The reasons for the asset set asset error

            This field is a member of `oneof`_ ``error_code``.
        asset_set_link_error (google.ads.googleads.v20.errors.types.AssetSetLinkErrorEnum.AssetSetLinkError):
            The reasons for the asset set link error

            This field is a member of `oneof`_ ``error_code``.
        asset_set_error (google.ads.googleads.v20.errors.types.AssetSetErrorEnum.AssetSetError):
            The reasons for the asset set error

            This field is a member of `oneof`_ ``error_code``.
        bidding_error (google.ads.googleads.v20.errors.types.BiddingErrorEnum.BiddingError):
            The reasons for the bidding errors

            This field is a member of `oneof`_ ``error_code``.
        campaign_criterion_error (google.ads.googleads.v20.errors.types.CampaignCriterionErrorEnum.CampaignCriterionError):
            The reasons for the campaign criterion error

            This field is a member of `oneof`_ ``error_code``.
        campaign_conversion_goal_error (google.ads.googleads.v20.errors.types.CampaignConversionGoalErrorEnum.CampaignConversionGoalError):
            The reasons for the campaign conversion goal
            error

            This field is a member of `oneof`_ ``error_code``.
        campaign_customizer_error (google.ads.googleads.v20.errors.types.CampaignCustomizerErrorEnum.CampaignCustomizerError):
            The reasons for the campaign customizer
            error.

            This field is a member of `oneof`_ ``error_code``.
        collection_size_error (google.ads.googleads.v20.errors.types.CollectionSizeErrorEnum.CollectionSizeError):
            The reasons for the collection size error

            This field is a member of `oneof`_ ``error_code``.
        conversion_goal_campaign_config_error (google.ads.googleads.v20.errors.types.ConversionGoalCampaignConfigErrorEnum.ConversionGoalCampaignConfigError):
            The reasons for the conversion goal campaign
            config error

            This field is a member of `oneof`_ ``error_code``.
        country_code_error (google.ads.googleads.v20.errors.types.CountryCodeErrorEnum.CountryCodeError):
            The reasons for the country code error

            This field is a member of `oneof`_ ``error_code``.
        criterion_error (google.ads.googleads.v20.errors.types.CriterionErrorEnum.CriterionError):
            The reasons for the criterion error

            This field is a member of `oneof`_ ``error_code``.
        custom_conversion_goal_error (google.ads.googleads.v20.errors.types.CustomConversionGoalErrorEnum.CustomConversionGoalError):
            The reasons for the custom conversion goal
            error

            This field is a member of `oneof`_ ``error_code``.
        customer_customizer_error (google.ads.googleads.v20.errors.types.CustomerCustomizerErrorEnum.CustomerCustomizerError):
            The reasons for the customer customizer
            error.

            This field is a member of `oneof`_ ``error_code``.
        customer_error (google.ads.googleads.v20.errors.types.CustomerErrorEnum.CustomerError):
            The reasons for the customer error

            This field is a member of `oneof`_ ``error_code``.
        customizer_attribute_error (google.ads.googleads.v20.errors.types.CustomizerAttributeErrorEnum.CustomizerAttributeError):
            The reasons for the customizer attribute
            error.

            This field is a member of `oneof`_ ``error_code``.
        date_error (google.ads.googleads.v20.errors.types.DateErrorEnum.DateError):
            The reasons for the date error

            This field is a member of `oneof`_ ``error_code``.
        date_range_error (google.ads.googleads.v20.errors.types.DateRangeErrorEnum.DateRangeError):
            The reasons for the date range error

            This field is a member of `oneof`_ ``error_code``.
        distinct_error (google.ads.googleads.v20.errors.types.DistinctErrorEnum.DistinctError):
            The reasons for the distinct error

            This field is a member of `oneof`_ ``error_code``.
        feed_attribute_reference_error (google.ads.googleads.v20.errors.types.FeedAttributeReferenceErrorEnum.FeedAttributeReferenceError):
            The reasons for the feed attribute reference
            error

            This field is a member of `oneof`_ ``error_code``.
        function_error (google.ads.googleads.v20.errors.types.FunctionErrorEnum.FunctionError):
            The reasons for the function error

            This field is a member of `oneof`_ ``error_code``.
        function_parsing_error (google.ads.googleads.v20.errors.types.FunctionParsingErrorEnum.FunctionParsingError):
            The reasons for the function parsing error

            This field is a member of `oneof`_ ``error_code``.
        id_error (google.ads.googleads.v20.errors.types.IdErrorEnum.IdError):
            The reasons for the id error

            This field is a member of `oneof`_ ``error_code``.
        image_error (google.ads.googleads.v20.errors.types.ImageErrorEnum.ImageError):
            The reasons for the image error

            This field is a member of `oneof`_ ``error_code``.
        language_code_error (google.ads.googleads.v20.errors.types.LanguageCodeErrorEnum.LanguageCodeError):
            The reasons for the language code error

            This field is a member of `oneof`_ ``error_code``.
        media_bundle_error (google.ads.googleads.v20.errors.types.MediaBundleErrorEnum.MediaBundleError):
            The reasons for the media bundle error

            This field is a member of `oneof`_ ``error_code``.
        media_upload_error (google.ads.googleads.v20.errors.types.MediaUploadErrorEnum.MediaUploadError):
            The reasons for media uploading errors.

            This field is a member of `oneof`_ ``error_code``.
        media_file_error (google.ads.googleads.v20.errors.types.MediaFileErrorEnum.MediaFileError):
            The reasons for the media file error

            This field is a member of `oneof`_ ``error_code``.
        merchant_center_error (google.ads.googleads.v20.errors.types.MerchantCenterErrorEnum.MerchantCenterError):
            Container for enum describing possible
            merchant center errors.

            This field is a member of `oneof`_ ``error_code``.
        multiplier_error (google.ads.googleads.v20.errors.types.MultiplierErrorEnum.MultiplierError):
            The reasons for the multiplier error

            This field is a member of `oneof`_ ``error_code``.
        new_resource_creation_error (google.ads.googleads.v20.errors.types.NewResourceCreationErrorEnum.NewResourceCreationError):
            The reasons for the new resource creation
            error

            This field is a member of `oneof`_ ``error_code``.
        not_empty_error (google.ads.googleads.v20.errors.types.NotEmptyErrorEnum.NotEmptyError):
            The reasons for the not empty error

            This field is a member of `oneof`_ ``error_code``.
        null_error (google.ads.googleads.v20.errors.types.NullErrorEnum.NullError):
            The reasons for the null error

            This field is a member of `oneof`_ ``error_code``.
        operator_error (google.ads.googleads.v20.errors.types.OperatorErrorEnum.OperatorError):
            The reasons for the operator error

            This field is a member of `oneof`_ ``error_code``.
        range_error (google.ads.googleads.v20.errors.types.RangeErrorEnum.RangeError):
            The reasons for the range error

            This field is a member of `oneof`_ ``error_code``.
        recommendation_error (google.ads.googleads.v20.errors.types.RecommendationErrorEnum.RecommendationError):
            The reasons for error in applying a
            recommendation

            This field is a member of `oneof`_ ``error_code``.
        recommendation_subscription_error (google.ads.googleads.v20.errors.types.RecommendationSubscriptionErrorEnum.RecommendationSubscriptionError):
            The reasons for the recommendation
            subscription error.

            This field is a member of `oneof`_ ``error_code``.
        region_code_error (google.ads.googleads.v20.errors.types.RegionCodeErrorEnum.RegionCodeError):
            The reasons for the region code error

            This field is a member of `oneof`_ ``error_code``.
        setting_error (google.ads.googleads.v20.errors.types.SettingErrorEnum.SettingError):
            The reasons for the setting error

            This field is a member of `oneof`_ ``error_code``.
        string_format_error (google.ads.googleads.v20.errors.types.StringFormatErrorEnum.StringFormatError):
            The reasons for the string format error

            This field is a member of `oneof`_ ``error_code``.
        string_length_error (google.ads.googleads.v20.errors.types.StringLengthErrorEnum.StringLengthError):
            The reasons for the string length error

            This field is a member of `oneof`_ ``error_code``.
        operation_access_denied_error (google.ads.googleads.v20.errors.types.OperationAccessDeniedErrorEnum.OperationAccessDeniedError):
            The reasons for the operation access denied
            error

            This field is a member of `oneof`_ ``error_code``.
        resource_access_denied_error (google.ads.googleads.v20.errors.types.ResourceAccessDeniedErrorEnum.ResourceAccessDeniedError):
            The reasons for the resource access denied
            error

            This field is a member of `oneof`_ ``error_code``.
        resource_count_limit_exceeded_error (google.ads.googleads.v20.errors.types.ResourceCountLimitExceededErrorEnum.ResourceCountLimitExceededError):
            The reasons for the resource count limit
            exceeded error

            This field is a member of `oneof`_ ``error_code``.
        youtube_video_registration_error (google.ads.googleads.v20.errors.types.YoutubeVideoRegistrationErrorEnum.YoutubeVideoRegistrationError):
            The reasons for YouTube video registration
            errors.

            This field is a member of `oneof`_ ``error_code``.
        ad_group_bid_modifier_error (google.ads.googleads.v20.errors.types.AdGroupBidModifierErrorEnum.AdGroupBidModifierError):
            The reasons for the ad group bid modifier
            error

            This field is a member of `oneof`_ ``error_code``.
        context_error (google.ads.googleads.v20.errors.types.ContextErrorEnum.ContextError):
            The reasons for the context error

            This field is a member of `oneof`_ ``error_code``.
        field_error (google.ads.googleads.v20.errors.types.FieldErrorEnum.FieldError):
            The reasons for the field error

            This field is a member of `oneof`_ ``error_code``.
        shared_set_error (google.ads.googleads.v20.errors.types.SharedSetErrorEnum.SharedSetError):
            The reasons for the shared set error

            This field is a member of `oneof`_ ``error_code``.
        shared_criterion_error (google.ads.googleads.v20.errors.types.SharedCriterionErrorEnum.SharedCriterionError):
            The reasons for the shared criterion error

            This field is a member of `oneof`_ ``error_code``.
        campaign_shared_set_error (google.ads.googleads.v20.errors.types.CampaignSharedSetErrorEnum.CampaignSharedSetError):
            The reasons for the campaign shared set error

            This field is a member of `oneof`_ ``error_code``.
        conversion_action_error (google.ads.googleads.v20.errors.types.ConversionActionErrorEnum.ConversionActionError):
            The reasons for the conversion action error

            This field is a member of `oneof`_ ``error_code``.
        conversion_adjustment_upload_error (google.ads.googleads.v20.errors.types.ConversionAdjustmentUploadErrorEnum.ConversionAdjustmentUploadError):
            The reasons for the conversion adjustment
            upload error

            This field is a member of `oneof`_ ``error_code``.
        conversion_custom_variable_error (google.ads.googleads.v20.errors.types.ConversionCustomVariableErrorEnum.ConversionCustomVariableError):
            The reasons for the conversion custom
            variable error

            This field is a member of `oneof`_ ``error_code``.
        conversion_upload_error (google.ads.googleads.v20.errors.types.ConversionUploadErrorEnum.ConversionUploadError):
            The reasons for the conversion upload error

            This field is a member of `oneof`_ ``error_code``.
        conversion_value_rule_error (google.ads.googleads.v20.errors.types.ConversionValueRuleErrorEnum.ConversionValueRuleError):
            The reasons for the conversion value rule
            error

            This field is a member of `oneof`_ ``error_code``.
        conversion_value_rule_set_error (google.ads.googleads.v20.errors.types.ConversionValueRuleSetErrorEnum.ConversionValueRuleSetError):
            The reasons for the conversion value rule set
            error

            This field is a member of `oneof`_ ``error_code``.
        header_error (google.ads.googleads.v20.errors.types.HeaderErrorEnum.HeaderError):
            The reasons for the header error.

            This field is a member of `oneof`_ ``error_code``.
        database_error (google.ads.googleads.v20.errors.types.DatabaseErrorEnum.DatabaseError):
            The reasons for the database error.

            This field is a member of `oneof`_ ``error_code``.
        policy_finding_error (google.ads.googleads.v20.errors.types.PolicyFindingErrorEnum.PolicyFindingError):
            The reasons for the policy finding error.

            This field is a member of `oneof`_ ``error_code``.
        enum_error (google.ads.googleads.v20.errors.types.EnumErrorEnum.EnumError):
            The reason for enum error.

            This field is a member of `oneof`_ ``error_code``.
        keyword_plan_error (google.ads.googleads.v20.errors.types.KeywordPlanErrorEnum.KeywordPlanError):
            The reason for keyword plan error.

            This field is a member of `oneof`_ ``error_code``.
        keyword_plan_campaign_error (google.ads.googleads.v20.errors.types.KeywordPlanCampaignErrorEnum.KeywordPlanCampaignError):
            The reason for keyword plan campaign error.

            This field is a member of `oneof`_ ``error_code``.
        keyword_plan_campaign_keyword_error (google.ads.googleads.v20.errors.types.KeywordPlanCampaignKeywordErrorEnum.KeywordPlanCampaignKeywordError):
            The reason for keyword plan campaign keyword
            error.

            This field is a member of `oneof`_ ``error_code``.
        keyword_plan_ad_group_error (google.ads.googleads.v20.errors.types.KeywordPlanAdGroupErrorEnum.KeywordPlanAdGroupError):
            The reason for keyword plan ad group error.

            This field is a member of `oneof`_ ``error_code``.
        keyword_plan_ad_group_keyword_error (google.ads.googleads.v20.errors.types.KeywordPlanAdGroupKeywordErrorEnum.KeywordPlanAdGroupKeywordError):
            The reason for keyword plan ad group keyword
            error.

            This field is a member of `oneof`_ ``error_code``.
        keyword_plan_idea_error (google.ads.googleads.v20.errors.types.KeywordPlanIdeaErrorEnum.KeywordPlanIdeaError):
            The reason for keyword idea error.

            This field is a member of `oneof`_ ``error_code``.
        account_budget_proposal_error (google.ads.googleads.v20.errors.types.AccountBudgetProposalErrorEnum.AccountBudgetProposalError):
            The reasons for account budget proposal
            errors.

            This field is a member of `oneof`_ ``error_code``.
        user_list_error (google.ads.googleads.v20.errors.types.UserListErrorEnum.UserListError):
            The reasons for the user list error

            This field is a member of `oneof`_ ``error_code``.
        change_event_error (google.ads.googleads.v20.errors.types.ChangeEventErrorEnum.ChangeEventError):
            The reasons for the change event error

            This field is a member of `oneof`_ ``error_code``.
        change_status_error (google.ads.googleads.v20.errors.types.ChangeStatusErrorEnum.ChangeStatusError):
            The reasons for the change status error

            This field is a member of `oneof`_ ``error_code``.
        feed_error (google.ads.googleads.v20.errors.types.FeedErrorEnum.FeedError):
            The reasons for the feed error

            This field is a member of `oneof`_ ``error_code``.
        geo_target_constant_suggestion_error (google.ads.googleads.v20.errors.types.GeoTargetConstantSuggestionErrorEnum.GeoTargetConstantSuggestionError):
            The reasons for the geo target constant
            suggestion error.

            This field is a member of `oneof`_ ``error_code``.
        campaign_draft_error (google.ads.googleads.v20.errors.types.CampaignDraftErrorEnum.CampaignDraftError):
            The reasons for the campaign draft error

            This field is a member of `oneof`_ ``error_code``.
        feed_item_error (google.ads.googleads.v20.errors.types.FeedItemErrorEnum.FeedItemError):
            The reasons for the feed item error

            This field is a member of `oneof`_ ``error_code``.
        label_error (google.ads.googleads.v20.errors.types.LabelErrorEnum.LabelError):
            The reason for the label error.

            This field is a member of `oneof`_ ``error_code``.
        billing_setup_error (google.ads.googleads.v20.errors.types.BillingSetupErrorEnum.BillingSetupError):
            The reasons for the billing setup error

            This field is a member of `oneof`_ ``error_code``.
        customer_client_link_error (google.ads.googleads.v20.errors.types.CustomerClientLinkErrorEnum.CustomerClientLinkError):
            The reasons for the customer client link
            error

            This field is a member of `oneof`_ ``error_code``.
        customer_manager_link_error (google.ads.googleads.v20.errors.types.CustomerManagerLinkErrorEnum.CustomerManagerLinkError):
            The reasons for the customer manager link
            error

            This field is a member of `oneof`_ ``error_code``.
        feed_mapping_error (google.ads.googleads.v20.errors.types.FeedMappingErrorEnum.FeedMappingError):
            The reasons for the feed mapping error

            This field is a member of `oneof`_ ``error_code``.
        customer_feed_error (google.ads.googleads.v20.errors.types.CustomerFeedErrorEnum.CustomerFeedError):
            The reasons for the customer feed error

            This field is a member of `oneof`_ ``error_code``.
        ad_group_feed_error (google.ads.googleads.v20.errors.types.AdGroupFeedErrorEnum.AdGroupFeedError):
            The reasons for the ad group feed error

            This field is a member of `oneof`_ ``error_code``.
        campaign_feed_error (google.ads.googleads.v20.errors.types.CampaignFeedErrorEnum.CampaignFeedError):
            The reasons for the campaign feed error

            This field is a member of `oneof`_ ``error_code``.
        custom_interest_error (google.ads.googleads.v20.errors.types.CustomInterestErrorEnum.CustomInterestError):
            The reasons for the custom interest error

            This field is a member of `oneof`_ ``error_code``.
        campaign_experiment_error (google.ads.googleads.v20.errors.types.CampaignExperimentErrorEnum.CampaignExperimentError):
            The reasons for the campaign experiment error

            This field is a member of `oneof`_ ``error_code``.
        extension_feed_item_error (google.ads.googleads.v20.errors.types.ExtensionFeedItemErrorEnum.ExtensionFeedItemError):
            The reasons for the extension feed item error

            This field is a member of `oneof`_ ``error_code``.
        ad_parameter_error (google.ads.googleads.v20.errors.types.AdParameterErrorEnum.AdParameterError):
            The reasons for the ad parameter error

            This field is a member of `oneof`_ ``error_code``.
        feed_item_validation_error (google.ads.googleads.v20.errors.types.FeedItemValidationErrorEnum.FeedItemValidationError):
            The reasons for the feed item validation
            error

            This field is a member of `oneof`_ ``error_code``.
        extension_setting_error (google.ads.googleads.v20.errors.types.ExtensionSettingErrorEnum.ExtensionSettingError):
            The reasons for the extension setting error

            This field is a member of `oneof`_ ``error_code``.
        feed_item_set_error (google.ads.googleads.v20.errors.types.FeedItemSetErrorEnum.FeedItemSetError):
            The reasons for the feed item set error

            This field is a member of `oneof`_ ``error_code``.
        feed_item_set_link_error (google.ads.googleads.v20.errors.types.FeedItemSetLinkErrorEnum.FeedItemSetLinkError):
            The reasons for the feed item set link error

            This field is a member of `oneof`_ ``error_code``.
        feed_item_target_error (google.ads.googleads.v20.errors.types.FeedItemTargetErrorEnum.FeedItemTargetError):
            The reasons for the feed item target error

            This field is a member of `oneof`_ ``error_code``.
        policy_violation_error (google.ads.googleads.v20.errors.types.PolicyViolationErrorEnum.PolicyViolationError):
            The reasons for the policy violation error

            This field is a member of `oneof`_ ``error_code``.
        partial_failure_error (google.ads.googleads.v20.errors.types.PartialFailureErrorEnum.PartialFailureError):
            The reasons for the mutate job error

            This field is a member of `oneof`_ ``error_code``.
        click_view_error (google.ads.googleads.v20.errors.types.ClickViewErrorEnum.ClickViewError):
            The reasons for the click view error

            This field is a member of `oneof`_ ``error_code``.
        policy_validation_parameter_error (google.ads.googleads.v20.errors.types.PolicyValidationParameterErrorEnum.PolicyValidationParameterError):
            The reasons for the policy validation
            parameter error

            This field is a member of `oneof`_ ``error_code``.
        size_limit_error (google.ads.googleads.v20.errors.types.SizeLimitErrorEnum.SizeLimitError):
            The reasons for the size limit error

            This field is a member of `oneof`_ ``error_code``.
        offline_user_data_job_error (google.ads.googleads.v20.errors.types.OfflineUserDataJobErrorEnum.OfflineUserDataJobError):
            The reasons for the offline user data job
            error.

            This field is a member of `oneof`_ ``error_code``.
        not_allowlisted_error (google.ads.googleads.v20.errors.types.NotAllowlistedErrorEnum.NotAllowlistedError):
            The reasons for the not allowlisted error

            This field is a member of `oneof`_ ``error_code``.
        manager_link_error (google.ads.googleads.v20.errors.types.ManagerLinkErrorEnum.ManagerLinkError):
            The reasons for the manager link error

            This field is a member of `oneof`_ ``error_code``.
        currency_code_error (google.ads.googleads.v20.errors.types.CurrencyCodeErrorEnum.CurrencyCodeError):
            The reasons for the currency code error

            This field is a member of `oneof`_ ``error_code``.
        experiment_error (google.ads.googleads.v20.errors.types.ExperimentErrorEnum.ExperimentError):
            The reasons for the experiment error

            This field is a member of `oneof`_ ``error_code``.
        access_invitation_error (google.ads.googleads.v20.errors.types.AccessInvitationErrorEnum.AccessInvitationError):
            The reasons for the access invitation error

            This field is a member of `oneof`_ ``error_code``.
        reach_plan_error (google.ads.googleads.v20.errors.types.ReachPlanErrorEnum.ReachPlanError):
            The reasons for the reach plan error

            This field is a member of `oneof`_ ``error_code``.
        invoice_error (google.ads.googleads.v20.errors.types.InvoiceErrorEnum.InvoiceError):
            The reasons for the invoice error

            This field is a member of `oneof`_ ``error_code``.
        payments_account_error (google.ads.googleads.v20.errors.types.PaymentsAccountErrorEnum.PaymentsAccountError):
            The reasons for errors in payments accounts
            service

            This field is a member of `oneof`_ ``error_code``.
        time_zone_error (google.ads.googleads.v20.errors.types.TimeZoneErrorEnum.TimeZoneError):
            The reasons for the time zone error

            This field is a member of `oneof`_ ``error_code``.
        asset_link_error (google.ads.googleads.v20.errors.types.AssetLinkErrorEnum.AssetLinkError):
            The reasons for the asset link error

            This field is a member of `oneof`_ ``error_code``.
        user_data_error (google.ads.googleads.v20.errors.types.UserDataErrorEnum.UserDataError):
            The reasons for the user data error.

            This field is a member of `oneof`_ ``error_code``.
        batch_job_error (google.ads.googleads.v20.errors.types.BatchJobErrorEnum.BatchJobError):
            The reasons for the batch job error

            This field is a member of `oneof`_ ``error_code``.
        account_link_error (google.ads.googleads.v20.errors.types.AccountLinkErrorEnum.AccountLinkError):
            The reasons for the account link status
            change error

            This field is a member of `oneof`_ ``error_code``.
        third_party_app_analytics_link_error (google.ads.googleads.v20.errors.types.ThirdPartyAppAnalyticsLinkErrorEnum.ThirdPartyAppAnalyticsLinkError):
            The reasons for the third party app analytics
            link mutate error

            This field is a member of `oneof`_ ``error_code``.
        customer_user_access_error (google.ads.googleads.v20.errors.types.CustomerUserAccessErrorEnum.CustomerUserAccessError):
            The reasons for the customer user access
            mutate error

            This field is a member of `oneof`_ ``error_code``.
        custom_audience_error (google.ads.googleads.v20.errors.types.CustomAudienceErrorEnum.CustomAudienceError):
            The reasons for the custom audience error

            This field is a member of `oneof`_ ``error_code``.
        audience_error (google.ads.googleads.v20.errors.types.AudienceErrorEnum.AudienceError):
            The reasons for the audience error

            This field is a member of `oneof`_ ``error_code``.
        search_term_insight_error (google.ads.googleads.v20.errors.types.SearchTermInsightErrorEnum.SearchTermInsightError):
            The reasons for the Search term insight error

            This field is a member of `oneof`_ ``error_code``.
        smart_campaign_error (google.ads.googleads.v20.errors.types.SmartCampaignErrorEnum.SmartCampaignError):
            The reasons for the Smart campaign error

            This field is a member of `oneof`_ ``error_code``.
        experiment_arm_error (google.ads.googleads.v20.errors.types.ExperimentArmErrorEnum.ExperimentArmError):
            The reasons for the experiment arm error

            This field is a member of `oneof`_ ``error_code``.
        audience_insights_error (google.ads.googleads.v20.errors.types.AudienceInsightsErrorEnum.AudienceInsightsError):
            The reasons for the Audience Insights error

            This field is a member of `oneof`_ ``error_code``.
        product_link_error (google.ads.googleads.v20.errors.types.ProductLinkErrorEnum.ProductLinkError):
            The reasons for the product link error

            This field is a member of `oneof`_ ``error_code``.
        data_link_error (google.ads.googleads.v20.errors.types.DataLinkErrorEnum.DataLinkError):
            The reasons for the data link error

            This field is a member of `oneof`_ ``error_code``.
        customer_sk_ad_network_conversion_value_schema_error (google.ads.googleads.v20.errors.types.CustomerSkAdNetworkConversionValueSchemaErrorEnum.CustomerSkAdNetworkConversionValueSchemaError):
            The reasons for the customer SK Ad network
            conversion value schema error

            This field is a member of `oneof`_ ``error_code``.
        currency_error (google.ads.googleads.v20.errors.types.CurrencyErrorEnum.CurrencyError):
            The reasons for the currency errors.

            This field is a member of `oneof`_ ``error_code``.
        asset_group_signal_error (google.ads.googleads.v20.errors.types.AssetGroupSignalErrorEnum.AssetGroupSignalError):
            The reasons for the asset group hint error

            This field is a member of `oneof`_ ``error_code``.
        product_link_invitation_error (google.ads.googleads.v20.errors.types.ProductLinkInvitationErrorEnum.ProductLinkInvitationError):
            The reasons for the product link invitation
            error

            This field is a member of `oneof`_ ``error_code``.
        customer_lifecycle_goal_error (google.ads.googleads.v20.errors.types.CustomerLifecycleGoalErrorEnum.CustomerLifecycleGoalError):
            The reasons for the customer lifecycle goal
            error

            This field is a member of `oneof`_ ``error_code``.
        campaign_lifecycle_goal_error (google.ads.googleads.v20.errors.types.CampaignLifecycleGoalErrorEnum.CampaignLifecycleGoalError):
            The reasons for the campaign lifecycle goal
            error

            This field is a member of `oneof`_ ``error_code``.
        identity_verification_error (google.ads.googleads.v20.errors.types.IdentityVerificationErrorEnum.IdentityVerificationError):
            The reasons for an identity verification
            error.

            This field is a member of `oneof`_ ``error_code``.
        user_list_customer_type_error (google.ads.googleads.v20.errors.types.UserListCustomerTypeErrorEnum.UserListCustomerTypeError):
            The reasons for a user list customer type
            error.

            This field is a member of `oneof`_ ``error_code``.
        shopping_product_error (google.ads.googleads.v20.errors.types.ShoppingProductErrorEnum.ShoppingProductError):
            The reasons for error in querying shopping
            product.

            This field is a member of `oneof`_ ``error_code``.
        automatically_created_asset_removal_error (google.ads.googleads.v20.errors.types.AutomaticallyCreatedAssetRemovalErrorEnum.AutomaticallyCreatedAssetRemovalError):
            The reasons for error in automatically
            created asset removal action.

            This field is a member of `oneof`_ ``error_code``.
        shareable_preview_error (google.ads.googleads.v20.errors.types.ShareablePreviewErrorEnum.ShareablePreviewError):
            The reasons for the shareable preview error.

            This field is a member of `oneof`_ ``error_code``.
        brand_guidelines_migration_error (google.ads.googleads.v20.errors.types.BrandGuidelinesMigrationErrorEnum.BrandGuidelinesMigrationError):
            The reasons for the brand guidelines
            migration error.

            This field is a member of `oneof`_ ``error_code``.
    """

    request_error: gage_request_error.RequestErrorEnum.RequestError = (
        proto.Field(
            proto.ENUM,
            number=1,
            oneof="error_code",
            enum=gage_request_error.RequestErrorEnum.RequestError,
        )
    )
    bidding_strategy_error: (
        gage_bidding_strategy_error.BiddingStrategyErrorEnum.BiddingStrategyError
    ) = proto.Field(
        proto.ENUM,
        number=2,
        oneof="error_code",
        enum=gage_bidding_strategy_error.BiddingStrategyErrorEnum.BiddingStrategyError,
    )
    url_field_error: gage_url_field_error.UrlFieldErrorEnum.UrlFieldError = (
        proto.Field(
            proto.ENUM,
            number=3,
            oneof="error_code",
            enum=gage_url_field_error.UrlFieldErrorEnum.UrlFieldError,
        )
    )
    list_operation_error: (
        gage_list_operation_error.ListOperationErrorEnum.ListOperationError
    ) = proto.Field(
        proto.ENUM,
        number=4,
        oneof="error_code",
        enum=gage_list_operation_error.ListOperationErrorEnum.ListOperationError,
    )
    query_error: gage_query_error.QueryErrorEnum.QueryError = proto.Field(
        proto.ENUM,
        number=5,
        oneof="error_code",
        enum=gage_query_error.QueryErrorEnum.QueryError,
    )
    mutate_error: gage_mutate_error.MutateErrorEnum.MutateError = proto.Field(
        proto.ENUM,
        number=7,
        oneof="error_code",
        enum=gage_mutate_error.MutateErrorEnum.MutateError,
    )
    field_mask_error: (
        gage_field_mask_error.FieldMaskErrorEnum.FieldMaskError
    ) = proto.Field(
        proto.ENUM,
        number=8,
        oneof="error_code",
        enum=gage_field_mask_error.FieldMaskErrorEnum.FieldMaskError,
    )
    authorization_error: (
        gage_authorization_error.AuthorizationErrorEnum.AuthorizationError
    ) = proto.Field(
        proto.ENUM,
        number=9,
        oneof="error_code",
        enum=gage_authorization_error.AuthorizationErrorEnum.AuthorizationError,
    )
    internal_error: gage_internal_error.InternalErrorEnum.InternalError = (
        proto.Field(
            proto.ENUM,
            number=10,
            oneof="error_code",
            enum=gage_internal_error.InternalErrorEnum.InternalError,
        )
    )
    quota_error: gage_quota_error.QuotaErrorEnum.QuotaError = proto.Field(
        proto.ENUM,
        number=11,
        oneof="error_code",
        enum=gage_quota_error.QuotaErrorEnum.QuotaError,
    )
    ad_error: gage_ad_error.AdErrorEnum.AdError = proto.Field(
        proto.ENUM,
        number=12,
        oneof="error_code",
        enum=gage_ad_error.AdErrorEnum.AdError,
    )
    ad_group_error: gage_ad_group_error.AdGroupErrorEnum.AdGroupError = (
        proto.Field(
            proto.ENUM,
            number=13,
            oneof="error_code",
            enum=gage_ad_group_error.AdGroupErrorEnum.AdGroupError,
        )
    )
    campaign_budget_error: (
        gage_campaign_budget_error.CampaignBudgetErrorEnum.CampaignBudgetError
    ) = proto.Field(
        proto.ENUM,
        number=14,
        oneof="error_code",
        enum=gage_campaign_budget_error.CampaignBudgetErrorEnum.CampaignBudgetError,
    )
    campaign_error: gage_campaign_error.CampaignErrorEnum.CampaignError = (
        proto.Field(
            proto.ENUM,
            number=15,
            oneof="error_code",
            enum=gage_campaign_error.CampaignErrorEnum.CampaignError,
        )
    )
    video_campaign_error: (
        gage_video_campaign_error.VideoCampaignErrorEnum.VideoCampaignError
    ) = proto.Field(
        proto.ENUM,
        number=182,
        oneof="error_code",
        enum=gage_video_campaign_error.VideoCampaignErrorEnum.VideoCampaignError,
    )
    authentication_error: (
        gage_authentication_error.AuthenticationErrorEnum.AuthenticationError
    ) = proto.Field(
        proto.ENUM,
        number=17,
        oneof="error_code",
        enum=gage_authentication_error.AuthenticationErrorEnum.AuthenticationError,
    )
    ad_group_criterion_customizer_error: (
        gage_ad_group_criterion_customizer_error.AdGroupCriterionCustomizerErrorEnum.AdGroupCriterionCustomizerError
    ) = proto.Field(
        proto.ENUM,
        number=161,
        oneof="error_code",
        enum=gage_ad_group_criterion_customizer_error.AdGroupCriterionCustomizerErrorEnum.AdGroupCriterionCustomizerError,
    )
    ad_group_criterion_error: (
        gage_ad_group_criterion_error.AdGroupCriterionErrorEnum.AdGroupCriterionError
    ) = proto.Field(
        proto.ENUM,
        number=18,
        oneof="error_code",
        enum=gage_ad_group_criterion_error.AdGroupCriterionErrorEnum.AdGroupCriterionError,
    )
    ad_group_customizer_error: (
        gage_ad_group_customizer_error.AdGroupCustomizerErrorEnum.AdGroupCustomizerError
    ) = proto.Field(
        proto.ENUM,
        number=159,
        oneof="error_code",
        enum=gage_ad_group_customizer_error.AdGroupCustomizerErrorEnum.AdGroupCustomizerError,
    )
    ad_customizer_error: (
        gage_ad_customizer_error.AdCustomizerErrorEnum.AdCustomizerError
    ) = proto.Field(
        proto.ENUM,
        number=19,
        oneof="error_code",
        enum=gage_ad_customizer_error.AdCustomizerErrorEnum.AdCustomizerError,
    )
    ad_group_ad_error: (
        gage_ad_group_ad_error.AdGroupAdErrorEnum.AdGroupAdError
    ) = proto.Field(
        proto.ENUM,
        number=21,
        oneof="error_code",
        enum=gage_ad_group_ad_error.AdGroupAdErrorEnum.AdGroupAdError,
    )
    ad_sharing_error: (
        gage_ad_sharing_error.AdSharingErrorEnum.AdSharingError
    ) = proto.Field(
        proto.ENUM,
        number=24,
        oneof="error_code",
        enum=gage_ad_sharing_error.AdSharingErrorEnum.AdSharingError,
    )
    adx_error: gage_adx_error.AdxErrorEnum.AdxError = proto.Field(
        proto.ENUM,
        number=25,
        oneof="error_code",
        enum=gage_adx_error.AdxErrorEnum.AdxError,
    )
    asset_error: gage_asset_error.AssetErrorEnum.AssetError = proto.Field(
        proto.ENUM,
        number=107,
        oneof="error_code",
        enum=gage_asset_error.AssetErrorEnum.AssetError,
    )
    asset_group_asset_error: (
        gage_asset_group_asset_error.AssetGroupAssetErrorEnum.AssetGroupAssetError
    ) = proto.Field(
        proto.ENUM,
        number=149,
        oneof="error_code",
        enum=gage_asset_group_asset_error.AssetGroupAssetErrorEnum.AssetGroupAssetError,
    )
    asset_group_listing_group_filter_error: (
        gage_asset_group_listing_group_filter_error.AssetGroupListingGroupFilterErrorEnum.AssetGroupListingGroupFilterError
    ) = proto.Field(
        proto.ENUM,
        number=155,
        oneof="error_code",
        enum=gage_asset_group_listing_group_filter_error.AssetGroupListingGroupFilterErrorEnum.AssetGroupListingGroupFilterError,
    )
    asset_group_error: (
        gage_asset_group_error.AssetGroupErrorEnum.AssetGroupError
    ) = proto.Field(
        proto.ENUM,
        number=148,
        oneof="error_code",
        enum=gage_asset_group_error.AssetGroupErrorEnum.AssetGroupError,
    )
    asset_set_asset_error: (
        gage_asset_set_asset_error.AssetSetAssetErrorEnum.AssetSetAssetError
    ) = proto.Field(
        proto.ENUM,
        number=153,
        oneof="error_code",
        enum=gage_asset_set_asset_error.AssetSetAssetErrorEnum.AssetSetAssetError,
    )
    asset_set_link_error: (
        gage_asset_set_link_error.AssetSetLinkErrorEnum.AssetSetLinkError
    ) = proto.Field(
        proto.ENUM,
        number=154,
        oneof="error_code",
        enum=gage_asset_set_link_error.AssetSetLinkErrorEnum.AssetSetLinkError,
    )
    asset_set_error: gage_asset_set_error.AssetSetErrorEnum.AssetSetError = (
        proto.Field(
            proto.ENUM,
            number=152,
            oneof="error_code",
            enum=gage_asset_set_error.AssetSetErrorEnum.AssetSetError,
        )
    )
    bidding_error: gage_bidding_error.BiddingErrorEnum.BiddingError = (
        proto.Field(
            proto.ENUM,
            number=26,
            oneof="error_code",
            enum=gage_bidding_error.BiddingErrorEnum.BiddingError,
        )
    )
    campaign_criterion_error: (
        gage_campaign_criterion_error.CampaignCriterionErrorEnum.CampaignCriterionError
    ) = proto.Field(
        proto.ENUM,
        number=29,
        oneof="error_code",
        enum=gage_campaign_criterion_error.CampaignCriterionErrorEnum.CampaignCriterionError,
    )
    campaign_conversion_goal_error: (
        gage_campaign_conversion_goal_error.CampaignConversionGoalErrorEnum.CampaignConversionGoalError
    ) = proto.Field(
        proto.ENUM,
        number=166,
        oneof="error_code",
        enum=gage_campaign_conversion_goal_error.CampaignConversionGoalErrorEnum.CampaignConversionGoalError,
    )
    campaign_customizer_error: (
        gage_campaign_customizer_error.CampaignCustomizerErrorEnum.CampaignCustomizerError
    ) = proto.Field(
        proto.ENUM,
        number=160,
        oneof="error_code",
        enum=gage_campaign_customizer_error.CampaignCustomizerErrorEnum.CampaignCustomizerError,
    )
    collection_size_error: (
        gage_collection_size_error.CollectionSizeErrorEnum.CollectionSizeError
    ) = proto.Field(
        proto.ENUM,
        number=31,
        oneof="error_code",
        enum=gage_collection_size_error.CollectionSizeErrorEnum.CollectionSizeError,
    )
    conversion_goal_campaign_config_error: (
        gage_conversion_goal_campaign_config_error.ConversionGoalCampaignConfigErrorEnum.ConversionGoalCampaignConfigError
    ) = proto.Field(
        proto.ENUM,
        number=165,
        oneof="error_code",
        enum=gage_conversion_goal_campaign_config_error.ConversionGoalCampaignConfigErrorEnum.ConversionGoalCampaignConfigError,
    )
    country_code_error: (
        gage_country_code_error.CountryCodeErrorEnum.CountryCodeError
    ) = proto.Field(
        proto.ENUM,
        number=109,
        oneof="error_code",
        enum=gage_country_code_error.CountryCodeErrorEnum.CountryCodeError,
    )
    criterion_error: gage_criterion_error.CriterionErrorEnum.CriterionError = (
        proto.Field(
            proto.ENUM,
            number=32,
            oneof="error_code",
            enum=gage_criterion_error.CriterionErrorEnum.CriterionError,
        )
    )
    custom_conversion_goal_error: (
        gage_custom_conversion_goal_error.CustomConversionGoalErrorEnum.CustomConversionGoalError
    ) = proto.Field(
        proto.ENUM,
        number=150,
        oneof="error_code",
        enum=gage_custom_conversion_goal_error.CustomConversionGoalErrorEnum.CustomConversionGoalError,
    )
    customer_customizer_error: (
        gage_customer_customizer_error.CustomerCustomizerErrorEnum.CustomerCustomizerError
    ) = proto.Field(
        proto.ENUM,
        number=158,
        oneof="error_code",
        enum=gage_customer_customizer_error.CustomerCustomizerErrorEnum.CustomerCustomizerError,
    )
    customer_error: gage_customer_error.CustomerErrorEnum.CustomerError = (
        proto.Field(
            proto.ENUM,
            number=90,
            oneof="error_code",
            enum=gage_customer_error.CustomerErrorEnum.CustomerError,
        )
    )
    customizer_attribute_error: (
        gage_customizer_attribute_error.CustomizerAttributeErrorEnum.CustomizerAttributeError
    ) = proto.Field(
        proto.ENUM,
        number=151,
        oneof="error_code",
        enum=gage_customizer_attribute_error.CustomizerAttributeErrorEnum.CustomizerAttributeError,
    )
    date_error: gage_date_error.DateErrorEnum.DateError = proto.Field(
        proto.ENUM,
        number=33,
        oneof="error_code",
        enum=gage_date_error.DateErrorEnum.DateError,
    )
    date_range_error: (
        gage_date_range_error.DateRangeErrorEnum.DateRangeError
    ) = proto.Field(
        proto.ENUM,
        number=34,
        oneof="error_code",
        enum=gage_date_range_error.DateRangeErrorEnum.DateRangeError,
    )
    distinct_error: gage_distinct_error.DistinctErrorEnum.DistinctError = (
        proto.Field(
            proto.ENUM,
            number=35,
            oneof="error_code",
            enum=gage_distinct_error.DistinctErrorEnum.DistinctError,
        )
    )
    feed_attribute_reference_error: (
        gage_feed_attribute_reference_error.FeedAttributeReferenceErrorEnum.FeedAttributeReferenceError
    ) = proto.Field(
        proto.ENUM,
        number=36,
        oneof="error_code",
        enum=gage_feed_attribute_reference_error.FeedAttributeReferenceErrorEnum.FeedAttributeReferenceError,
    )
    function_error: gage_function_error.FunctionErrorEnum.FunctionError = (
        proto.Field(
            proto.ENUM,
            number=37,
            oneof="error_code",
            enum=gage_function_error.FunctionErrorEnum.FunctionError,
        )
    )
    function_parsing_error: (
        gage_function_parsing_error.FunctionParsingErrorEnum.FunctionParsingError
    ) = proto.Field(
        proto.ENUM,
        number=38,
        oneof="error_code",
        enum=gage_function_parsing_error.FunctionParsingErrorEnum.FunctionParsingError,
    )
    id_error: gage_id_error.IdErrorEnum.IdError = proto.Field(
        proto.ENUM,
        number=39,
        oneof="error_code",
        enum=gage_id_error.IdErrorEnum.IdError,
    )
    image_error: gage_image_error.ImageErrorEnum.ImageError = proto.Field(
        proto.ENUM,
        number=40,
        oneof="error_code",
        enum=gage_image_error.ImageErrorEnum.ImageError,
    )
    language_code_error: (
        gage_language_code_error.LanguageCodeErrorEnum.LanguageCodeError
    ) = proto.Field(
        proto.ENUM,
        number=110,
        oneof="error_code",
        enum=gage_language_code_error.LanguageCodeErrorEnum.LanguageCodeError,
    )
    media_bundle_error: (
        gage_media_bundle_error.MediaBundleErrorEnum.MediaBundleError
    ) = proto.Field(
        proto.ENUM,
        number=42,
        oneof="error_code",
        enum=gage_media_bundle_error.MediaBundleErrorEnum.MediaBundleError,
    )
    media_upload_error: (
        gage_media_upload_error.MediaUploadErrorEnum.MediaUploadError
    ) = proto.Field(
        proto.ENUM,
        number=116,
        oneof="error_code",
        enum=gage_media_upload_error.MediaUploadErrorEnum.MediaUploadError,
    )
    media_file_error: (
        gage_media_file_error.MediaFileErrorEnum.MediaFileError
    ) = proto.Field(
        proto.ENUM,
        number=86,
        oneof="error_code",
        enum=gage_media_file_error.MediaFileErrorEnum.MediaFileError,
    )
    merchant_center_error: (
        gage_merchant_center_error.MerchantCenterErrorEnum.MerchantCenterError
    ) = proto.Field(
        proto.ENUM,
        number=162,
        oneof="error_code",
        enum=gage_merchant_center_error.MerchantCenterErrorEnum.MerchantCenterError,
    )
    multiplier_error: (
        gage_multiplier_error.MultiplierErrorEnum.MultiplierError
    ) = proto.Field(
        proto.ENUM,
        number=44,
        oneof="error_code",
        enum=gage_multiplier_error.MultiplierErrorEnum.MultiplierError,
    )
    new_resource_creation_error: (
        gage_new_resource_creation_error.NewResourceCreationErrorEnum.NewResourceCreationError
    ) = proto.Field(
        proto.ENUM,
        number=45,
        oneof="error_code",
        enum=gage_new_resource_creation_error.NewResourceCreationErrorEnum.NewResourceCreationError,
    )
    not_empty_error: gage_not_empty_error.NotEmptyErrorEnum.NotEmptyError = (
        proto.Field(
            proto.ENUM,
            number=46,
            oneof="error_code",
            enum=gage_not_empty_error.NotEmptyErrorEnum.NotEmptyError,
        )
    )
    null_error: gage_null_error.NullErrorEnum.NullError = proto.Field(
        proto.ENUM,
        number=47,
        oneof="error_code",
        enum=gage_null_error.NullErrorEnum.NullError,
    )
    operator_error: gage_operator_error.OperatorErrorEnum.OperatorError = (
        proto.Field(
            proto.ENUM,
            number=48,
            oneof="error_code",
            enum=gage_operator_error.OperatorErrorEnum.OperatorError,
        )
    )
    range_error: gage_range_error.RangeErrorEnum.RangeError = proto.Field(
        proto.ENUM,
        number=49,
        oneof="error_code",
        enum=gage_range_error.RangeErrorEnum.RangeError,
    )
    recommendation_error: (
        gage_recommendation_error.RecommendationErrorEnum.RecommendationError
    ) = proto.Field(
        proto.ENUM,
        number=58,
        oneof="error_code",
        enum=gage_recommendation_error.RecommendationErrorEnum.RecommendationError,
    )
    recommendation_subscription_error: (
        gage_recommendation_subscription_error.RecommendationSubscriptionErrorEnum.RecommendationSubscriptionError
    ) = proto.Field(
        proto.ENUM,
        number=180,
        oneof="error_code",
        enum=gage_recommendation_subscription_error.RecommendationSubscriptionErrorEnum.RecommendationSubscriptionError,
    )
    region_code_error: (
        gage_region_code_error.RegionCodeErrorEnum.RegionCodeError
    ) = proto.Field(
        proto.ENUM,
        number=51,
        oneof="error_code",
        enum=gage_region_code_error.RegionCodeErrorEnum.RegionCodeError,
    )
    setting_error: gage_setting_error.SettingErrorEnum.SettingError = (
        proto.Field(
            proto.ENUM,
            number=52,
            oneof="error_code",
            enum=gage_setting_error.SettingErrorEnum.SettingError,
        )
    )
    string_format_error: (
        gage_string_format_error.StringFormatErrorEnum.StringFormatError
    ) = proto.Field(
        proto.ENUM,
        number=53,
        oneof="error_code",
        enum=gage_string_format_error.StringFormatErrorEnum.StringFormatError,
    )
    string_length_error: (
        gage_string_length_error.StringLengthErrorEnum.StringLengthError
    ) = proto.Field(
        proto.ENUM,
        number=54,
        oneof="error_code",
        enum=gage_string_length_error.StringLengthErrorEnum.StringLengthError,
    )
    operation_access_denied_error: (
        gage_operation_access_denied_error.OperationAccessDeniedErrorEnum.OperationAccessDeniedError
    ) = proto.Field(
        proto.ENUM,
        number=55,
        oneof="error_code",
        enum=gage_operation_access_denied_error.OperationAccessDeniedErrorEnum.OperationAccessDeniedError,
    )
    resource_access_denied_error: (
        gage_resource_access_denied_error.ResourceAccessDeniedErrorEnum.ResourceAccessDeniedError
    ) = proto.Field(
        proto.ENUM,
        number=56,
        oneof="error_code",
        enum=gage_resource_access_denied_error.ResourceAccessDeniedErrorEnum.ResourceAccessDeniedError,
    )
    resource_count_limit_exceeded_error: (
        gage_resource_count_limit_exceeded_error.ResourceCountLimitExceededErrorEnum.ResourceCountLimitExceededError
    ) = proto.Field(
        proto.ENUM,
        number=57,
        oneof="error_code",
        enum=gage_resource_count_limit_exceeded_error.ResourceCountLimitExceededErrorEnum.ResourceCountLimitExceededError,
    )
    youtube_video_registration_error: (
        gage_youtube_video_registration_error.YoutubeVideoRegistrationErrorEnum.YoutubeVideoRegistrationError
    ) = proto.Field(
        proto.ENUM,
        number=117,
        oneof="error_code",
        enum=gage_youtube_video_registration_error.YoutubeVideoRegistrationErrorEnum.YoutubeVideoRegistrationError,
    )
    ad_group_bid_modifier_error: (
        gage_ad_group_bid_modifier_error.AdGroupBidModifierErrorEnum.AdGroupBidModifierError
    ) = proto.Field(
        proto.ENUM,
        number=59,
        oneof="error_code",
        enum=gage_ad_group_bid_modifier_error.AdGroupBidModifierErrorEnum.AdGroupBidModifierError,
    )
    context_error: gage_context_error.ContextErrorEnum.ContextError = (
        proto.Field(
            proto.ENUM,
            number=60,
            oneof="error_code",
            enum=gage_context_error.ContextErrorEnum.ContextError,
        )
    )
    field_error: gage_field_error.FieldErrorEnum.FieldError = proto.Field(
        proto.ENUM,
        number=61,
        oneof="error_code",
        enum=gage_field_error.FieldErrorEnum.FieldError,
    )
    shared_set_error: (
        gage_shared_set_error.SharedSetErrorEnum.SharedSetError
    ) = proto.Field(
        proto.ENUM,
        number=62,
        oneof="error_code",
        enum=gage_shared_set_error.SharedSetErrorEnum.SharedSetError,
    )
    shared_criterion_error: (
        gage_shared_criterion_error.SharedCriterionErrorEnum.SharedCriterionError
    ) = proto.Field(
        proto.ENUM,
        number=63,
        oneof="error_code",
        enum=gage_shared_criterion_error.SharedCriterionErrorEnum.SharedCriterionError,
    )
    campaign_shared_set_error: (
        gage_campaign_shared_set_error.CampaignSharedSetErrorEnum.CampaignSharedSetError
    ) = proto.Field(
        proto.ENUM,
        number=64,
        oneof="error_code",
        enum=gage_campaign_shared_set_error.CampaignSharedSetErrorEnum.CampaignSharedSetError,
    )
    conversion_action_error: (
        gage_conversion_action_error.ConversionActionErrorEnum.ConversionActionError
    ) = proto.Field(
        proto.ENUM,
        number=65,
        oneof="error_code",
        enum=gage_conversion_action_error.ConversionActionErrorEnum.ConversionActionError,
    )
    conversion_adjustment_upload_error: (
        gage_conversion_adjustment_upload_error.ConversionAdjustmentUploadErrorEnum.ConversionAdjustmentUploadError
    ) = proto.Field(
        proto.ENUM,
        number=115,
        oneof="error_code",
        enum=gage_conversion_adjustment_upload_error.ConversionAdjustmentUploadErrorEnum.ConversionAdjustmentUploadError,
    )
    conversion_custom_variable_error: (
        gage_conversion_custom_variable_error.ConversionCustomVariableErrorEnum.ConversionCustomVariableError
    ) = proto.Field(
        proto.ENUM,
        number=143,
        oneof="error_code",
        enum=gage_conversion_custom_variable_error.ConversionCustomVariableErrorEnum.ConversionCustomVariableError,
    )
    conversion_upload_error: (
        gage_conversion_upload_error.ConversionUploadErrorEnum.ConversionUploadError
    ) = proto.Field(
        proto.ENUM,
        number=111,
        oneof="error_code",
        enum=gage_conversion_upload_error.ConversionUploadErrorEnum.ConversionUploadError,
    )
    conversion_value_rule_error: (
        gage_conversion_value_rule_error.ConversionValueRuleErrorEnum.ConversionValueRuleError
    ) = proto.Field(
        proto.ENUM,
        number=145,
        oneof="error_code",
        enum=gage_conversion_value_rule_error.ConversionValueRuleErrorEnum.ConversionValueRuleError,
    )
    conversion_value_rule_set_error: (
        gage_conversion_value_rule_set_error.ConversionValueRuleSetErrorEnum.ConversionValueRuleSetError
    ) = proto.Field(
        proto.ENUM,
        number=146,
        oneof="error_code",
        enum=gage_conversion_value_rule_set_error.ConversionValueRuleSetErrorEnum.ConversionValueRuleSetError,
    )
    header_error: gage_header_error.HeaderErrorEnum.HeaderError = proto.Field(
        proto.ENUM,
        number=66,
        oneof="error_code",
        enum=gage_header_error.HeaderErrorEnum.HeaderError,
    )
    database_error: gage_database_error.DatabaseErrorEnum.DatabaseError = (
        proto.Field(
            proto.ENUM,
            number=67,
            oneof="error_code",
            enum=gage_database_error.DatabaseErrorEnum.DatabaseError,
        )
    )
    policy_finding_error: (
        gage_policy_finding_error.PolicyFindingErrorEnum.PolicyFindingError
    ) = proto.Field(
        proto.ENUM,
        number=68,
        oneof="error_code",
        enum=gage_policy_finding_error.PolicyFindingErrorEnum.PolicyFindingError,
    )
    enum_error: gage_enum_error.EnumErrorEnum.EnumError = proto.Field(
        proto.ENUM,
        number=70,
        oneof="error_code",
        enum=gage_enum_error.EnumErrorEnum.EnumError,
    )
    keyword_plan_error: (
        gage_keyword_plan_error.KeywordPlanErrorEnum.KeywordPlanError
    ) = proto.Field(
        proto.ENUM,
        number=71,
        oneof="error_code",
        enum=gage_keyword_plan_error.KeywordPlanErrorEnum.KeywordPlanError,
    )
    keyword_plan_campaign_error: (
        gage_keyword_plan_campaign_error.KeywordPlanCampaignErrorEnum.KeywordPlanCampaignError
    ) = proto.Field(
        proto.ENUM,
        number=72,
        oneof="error_code",
        enum=gage_keyword_plan_campaign_error.KeywordPlanCampaignErrorEnum.KeywordPlanCampaignError,
    )
    keyword_plan_campaign_keyword_error: (
        gage_keyword_plan_campaign_keyword_error.KeywordPlanCampaignKeywordErrorEnum.KeywordPlanCampaignKeywordError
    ) = proto.Field(
        proto.ENUM,
        number=132,
        oneof="error_code",
        enum=gage_keyword_plan_campaign_keyword_error.KeywordPlanCampaignKeywordErrorEnum.KeywordPlanCampaignKeywordError,
    )
    keyword_plan_ad_group_error: (
        gage_keyword_plan_ad_group_error.KeywordPlanAdGroupErrorEnum.KeywordPlanAdGroupError
    ) = proto.Field(
        proto.ENUM,
        number=74,
        oneof="error_code",
        enum=gage_keyword_plan_ad_group_error.KeywordPlanAdGroupErrorEnum.KeywordPlanAdGroupError,
    )
    keyword_plan_ad_group_keyword_error: (
        gage_keyword_plan_ad_group_keyword_error.KeywordPlanAdGroupKeywordErrorEnum.KeywordPlanAdGroupKeywordError
    ) = proto.Field(
        proto.ENUM,
        number=133,
        oneof="error_code",
        enum=gage_keyword_plan_ad_group_keyword_error.KeywordPlanAdGroupKeywordErrorEnum.KeywordPlanAdGroupKeywordError,
    )
    keyword_plan_idea_error: (
        gage_keyword_plan_idea_error.KeywordPlanIdeaErrorEnum.KeywordPlanIdeaError
    ) = proto.Field(
        proto.ENUM,
        number=76,
        oneof="error_code",
        enum=gage_keyword_plan_idea_error.KeywordPlanIdeaErrorEnum.KeywordPlanIdeaError,
    )
    account_budget_proposal_error: (
        gage_account_budget_proposal_error.AccountBudgetProposalErrorEnum.AccountBudgetProposalError
    ) = proto.Field(
        proto.ENUM,
        number=77,
        oneof="error_code",
        enum=gage_account_budget_proposal_error.AccountBudgetProposalErrorEnum.AccountBudgetProposalError,
    )
    user_list_error: gage_user_list_error.UserListErrorEnum.UserListError = (
        proto.Field(
            proto.ENUM,
            number=78,
            oneof="error_code",
            enum=gage_user_list_error.UserListErrorEnum.UserListError,
        )
    )
    change_event_error: (
        gage_change_event_error.ChangeEventErrorEnum.ChangeEventError
    ) = proto.Field(
        proto.ENUM,
        number=136,
        oneof="error_code",
        enum=gage_change_event_error.ChangeEventErrorEnum.ChangeEventError,
    )
    change_status_error: (
        gage_change_status_error.ChangeStatusErrorEnum.ChangeStatusError
    ) = proto.Field(
        proto.ENUM,
        number=79,
        oneof="error_code",
        enum=gage_change_status_error.ChangeStatusErrorEnum.ChangeStatusError,
    )
    feed_error: gage_feed_error.FeedErrorEnum.FeedError = proto.Field(
        proto.ENUM,
        number=80,
        oneof="error_code",
        enum=gage_feed_error.FeedErrorEnum.FeedError,
    )
    geo_target_constant_suggestion_error: (
        gage_geo_target_constant_suggestion_error.GeoTargetConstantSuggestionErrorEnum.GeoTargetConstantSuggestionError
    ) = proto.Field(
        proto.ENUM,
        number=81,
        oneof="error_code",
        enum=gage_geo_target_constant_suggestion_error.GeoTargetConstantSuggestionErrorEnum.GeoTargetConstantSuggestionError,
    )
    campaign_draft_error: (
        gage_campaign_draft_error.CampaignDraftErrorEnum.CampaignDraftError
    ) = proto.Field(
        proto.ENUM,
        number=82,
        oneof="error_code",
        enum=gage_campaign_draft_error.CampaignDraftErrorEnum.CampaignDraftError,
    )
    feed_item_error: gage_feed_item_error.FeedItemErrorEnum.FeedItemError = (
        proto.Field(
            proto.ENUM,
            number=83,
            oneof="error_code",
            enum=gage_feed_item_error.FeedItemErrorEnum.FeedItemError,
        )
    )
    label_error: gage_label_error.LabelErrorEnum.LabelError = proto.Field(
        proto.ENUM,
        number=84,
        oneof="error_code",
        enum=gage_label_error.LabelErrorEnum.LabelError,
    )
    billing_setup_error: (
        gage_billing_setup_error.BillingSetupErrorEnum.BillingSetupError
    ) = proto.Field(
        proto.ENUM,
        number=87,
        oneof="error_code",
        enum=gage_billing_setup_error.BillingSetupErrorEnum.BillingSetupError,
    )
    customer_client_link_error: (
        gage_customer_client_link_error.CustomerClientLinkErrorEnum.CustomerClientLinkError
    ) = proto.Field(
        proto.ENUM,
        number=88,
        oneof="error_code",
        enum=gage_customer_client_link_error.CustomerClientLinkErrorEnum.CustomerClientLinkError,
    )
    customer_manager_link_error: (
        gage_customer_manager_link_error.CustomerManagerLinkErrorEnum.CustomerManagerLinkError
    ) = proto.Field(
        proto.ENUM,
        number=91,
        oneof="error_code",
        enum=gage_customer_manager_link_error.CustomerManagerLinkErrorEnum.CustomerManagerLinkError,
    )
    feed_mapping_error: (
        gage_feed_mapping_error.FeedMappingErrorEnum.FeedMappingError
    ) = proto.Field(
        proto.ENUM,
        number=92,
        oneof="error_code",
        enum=gage_feed_mapping_error.FeedMappingErrorEnum.FeedMappingError,
    )
    customer_feed_error: (
        gage_customer_feed_error.CustomerFeedErrorEnum.CustomerFeedError
    ) = proto.Field(
        proto.ENUM,
        number=93,
        oneof="error_code",
        enum=gage_customer_feed_error.CustomerFeedErrorEnum.CustomerFeedError,
    )
    ad_group_feed_error: (
        gage_ad_group_feed_error.AdGroupFeedErrorEnum.AdGroupFeedError
    ) = proto.Field(
        proto.ENUM,
        number=94,
        oneof="error_code",
        enum=gage_ad_group_feed_error.AdGroupFeedErrorEnum.AdGroupFeedError,
    )
    campaign_feed_error: (
        gage_campaign_feed_error.CampaignFeedErrorEnum.CampaignFeedError
    ) = proto.Field(
        proto.ENUM,
        number=96,
        oneof="error_code",
        enum=gage_campaign_feed_error.CampaignFeedErrorEnum.CampaignFeedError,
    )
    custom_interest_error: (
        gage_custom_interest_error.CustomInterestErrorEnum.CustomInterestError
    ) = proto.Field(
        proto.ENUM,
        number=97,
        oneof="error_code",
        enum=gage_custom_interest_error.CustomInterestErrorEnum.CustomInterestError,
    )
    campaign_experiment_error: (
        gage_campaign_experiment_error.CampaignExperimentErrorEnum.CampaignExperimentError
    ) = proto.Field(
        proto.ENUM,
        number=98,
        oneof="error_code",
        enum=gage_campaign_experiment_error.CampaignExperimentErrorEnum.CampaignExperimentError,
    )
    extension_feed_item_error: (
        gage_extension_feed_item_error.ExtensionFeedItemErrorEnum.ExtensionFeedItemError
    ) = proto.Field(
        proto.ENUM,
        number=100,
        oneof="error_code",
        enum=gage_extension_feed_item_error.ExtensionFeedItemErrorEnum.ExtensionFeedItemError,
    )
    ad_parameter_error: (
        gage_ad_parameter_error.AdParameterErrorEnum.AdParameterError
    ) = proto.Field(
        proto.ENUM,
        number=101,
        oneof="error_code",
        enum=gage_ad_parameter_error.AdParameterErrorEnum.AdParameterError,
    )
    feed_item_validation_error: (
        gage_feed_item_validation_error.FeedItemValidationErrorEnum.FeedItemValidationError
    ) = proto.Field(
        proto.ENUM,
        number=102,
        oneof="error_code",
        enum=gage_feed_item_validation_error.FeedItemValidationErrorEnum.FeedItemValidationError,
    )
    extension_setting_error: (
        gage_extension_setting_error.ExtensionSettingErrorEnum.ExtensionSettingError
    ) = proto.Field(
        proto.ENUM,
        number=103,
        oneof="error_code",
        enum=gage_extension_setting_error.ExtensionSettingErrorEnum.ExtensionSettingError,
    )
    feed_item_set_error: (
        gage_feed_item_set_error.FeedItemSetErrorEnum.FeedItemSetError
    ) = proto.Field(
        proto.ENUM,
        number=140,
        oneof="error_code",
        enum=gage_feed_item_set_error.FeedItemSetErrorEnum.FeedItemSetError,
    )
    feed_item_set_link_error: (
        gage_feed_item_set_link_error.FeedItemSetLinkErrorEnum.FeedItemSetLinkError
    ) = proto.Field(
        proto.ENUM,
        number=141,
        oneof="error_code",
        enum=gage_feed_item_set_link_error.FeedItemSetLinkErrorEnum.FeedItemSetLinkError,
    )
    feed_item_target_error: (
        gage_feed_item_target_error.FeedItemTargetErrorEnum.FeedItemTargetError
    ) = proto.Field(
        proto.ENUM,
        number=104,
        oneof="error_code",
        enum=gage_feed_item_target_error.FeedItemTargetErrorEnum.FeedItemTargetError,
    )
    policy_violation_error: (
        gage_policy_violation_error.PolicyViolationErrorEnum.PolicyViolationError
    ) = proto.Field(
        proto.ENUM,
        number=105,
        oneof="error_code",
        enum=gage_policy_violation_error.PolicyViolationErrorEnum.PolicyViolationError,
    )
    partial_failure_error: (
        gage_partial_failure_error.PartialFailureErrorEnum.PartialFailureError
    ) = proto.Field(
        proto.ENUM,
        number=112,
        oneof="error_code",
        enum=gage_partial_failure_error.PartialFailureErrorEnum.PartialFailureError,
    )
    click_view_error: (
        gage_click_view_error.ClickViewErrorEnum.ClickViewError
    ) = proto.Field(
        proto.ENUM,
        number=113,
        oneof="error_code",
        enum=gage_click_view_error.ClickViewErrorEnum.ClickViewError,
    )
    policy_validation_parameter_error: (
        gage_policy_validation_parameter_error.PolicyValidationParameterErrorEnum.PolicyValidationParameterError
    ) = proto.Field(
        proto.ENUM,
        number=114,
        oneof="error_code",
        enum=gage_policy_validation_parameter_error.PolicyValidationParameterErrorEnum.PolicyValidationParameterError,
    )
    size_limit_error: (
        gage_size_limit_error.SizeLimitErrorEnum.SizeLimitError
    ) = proto.Field(
        proto.ENUM,
        number=118,
        oneof="error_code",
        enum=gage_size_limit_error.SizeLimitErrorEnum.SizeLimitError,
    )
    offline_user_data_job_error: (
        gage_offline_user_data_job_error.OfflineUserDataJobErrorEnum.OfflineUserDataJobError
    ) = proto.Field(
        proto.ENUM,
        number=119,
        oneof="error_code",
        enum=gage_offline_user_data_job_error.OfflineUserDataJobErrorEnum.OfflineUserDataJobError,
    )
    not_allowlisted_error: (
        gage_not_allowlisted_error.NotAllowlistedErrorEnum.NotAllowlistedError
    ) = proto.Field(
        proto.ENUM,
        number=137,
        oneof="error_code",
        enum=gage_not_allowlisted_error.NotAllowlistedErrorEnum.NotAllowlistedError,
    )
    manager_link_error: (
        gage_manager_link_error.ManagerLinkErrorEnum.ManagerLinkError
    ) = proto.Field(
        proto.ENUM,
        number=121,
        oneof="error_code",
        enum=gage_manager_link_error.ManagerLinkErrorEnum.ManagerLinkError,
    )
    currency_code_error: (
        gage_currency_code_error.CurrencyCodeErrorEnum.CurrencyCodeError
    ) = proto.Field(
        proto.ENUM,
        number=122,
        oneof="error_code",
        enum=gage_currency_code_error.CurrencyCodeErrorEnum.CurrencyCodeError,
    )
    experiment_error: (
        gage_experiment_error.ExperimentErrorEnum.ExperimentError
    ) = proto.Field(
        proto.ENUM,
        number=123,
        oneof="error_code",
        enum=gage_experiment_error.ExperimentErrorEnum.ExperimentError,
    )
    access_invitation_error: (
        gage_access_invitation_error.AccessInvitationErrorEnum.AccessInvitationError
    ) = proto.Field(
        proto.ENUM,
        number=124,
        oneof="error_code",
        enum=gage_access_invitation_error.AccessInvitationErrorEnum.AccessInvitationError,
    )
    reach_plan_error: (
        gage_reach_plan_error.ReachPlanErrorEnum.ReachPlanError
    ) = proto.Field(
        proto.ENUM,
        number=125,
        oneof="error_code",
        enum=gage_reach_plan_error.ReachPlanErrorEnum.ReachPlanError,
    )
    invoice_error: gage_invoice_error.InvoiceErrorEnum.InvoiceError = (
        proto.Field(
            proto.ENUM,
            number=126,
            oneof="error_code",
            enum=gage_invoice_error.InvoiceErrorEnum.InvoiceError,
        )
    )
    payments_account_error: (
        gage_payments_account_error.PaymentsAccountErrorEnum.PaymentsAccountError
    ) = proto.Field(
        proto.ENUM,
        number=127,
        oneof="error_code",
        enum=gage_payments_account_error.PaymentsAccountErrorEnum.PaymentsAccountError,
    )
    time_zone_error: gage_time_zone_error.TimeZoneErrorEnum.TimeZoneError = (
        proto.Field(
            proto.ENUM,
            number=128,
            oneof="error_code",
            enum=gage_time_zone_error.TimeZoneErrorEnum.TimeZoneError,
        )
    )
    asset_link_error: (
        gage_asset_link_error.AssetLinkErrorEnum.AssetLinkError
    ) = proto.Field(
        proto.ENUM,
        number=129,
        oneof="error_code",
        enum=gage_asset_link_error.AssetLinkErrorEnum.AssetLinkError,
    )
    user_data_error: gage_user_data_error.UserDataErrorEnum.UserDataError = (
        proto.Field(
            proto.ENUM,
            number=130,
            oneof="error_code",
            enum=gage_user_data_error.UserDataErrorEnum.UserDataError,
        )
    )
    batch_job_error: gage_batch_job_error.BatchJobErrorEnum.BatchJobError = (
        proto.Field(
            proto.ENUM,
            number=131,
            oneof="error_code",
            enum=gage_batch_job_error.BatchJobErrorEnum.BatchJobError,
        )
    )
    account_link_error: (
        gage_account_link_error.AccountLinkErrorEnum.AccountLinkError
    ) = proto.Field(
        proto.ENUM,
        number=134,
        oneof="error_code",
        enum=gage_account_link_error.AccountLinkErrorEnum.AccountLinkError,
    )
    third_party_app_analytics_link_error: (
        gage_third_party_app_analytics_link_error.ThirdPartyAppAnalyticsLinkErrorEnum.ThirdPartyAppAnalyticsLinkError
    ) = proto.Field(
        proto.ENUM,
        number=135,
        oneof="error_code",
        enum=gage_third_party_app_analytics_link_error.ThirdPartyAppAnalyticsLinkErrorEnum.ThirdPartyAppAnalyticsLinkError,
    )
    customer_user_access_error: (
        gage_customer_user_access_error.CustomerUserAccessErrorEnum.CustomerUserAccessError
    ) = proto.Field(
        proto.ENUM,
        number=138,
        oneof="error_code",
        enum=gage_customer_user_access_error.CustomerUserAccessErrorEnum.CustomerUserAccessError,
    )
    custom_audience_error: (
        gage_custom_audience_error.CustomAudienceErrorEnum.CustomAudienceError
    ) = proto.Field(
        proto.ENUM,
        number=139,
        oneof="error_code",
        enum=gage_custom_audience_error.CustomAudienceErrorEnum.CustomAudienceError,
    )
    audience_error: gage_audience_error.AudienceErrorEnum.AudienceError = (
        proto.Field(
            proto.ENUM,
            number=164,
            oneof="error_code",
            enum=gage_audience_error.AudienceErrorEnum.AudienceError,
        )
    )
    search_term_insight_error: (
        gage_search_term_insight_error.SearchTermInsightErrorEnum.SearchTermInsightError
    ) = proto.Field(
        proto.ENUM,
        number=174,
        oneof="error_code",
        enum=gage_search_term_insight_error.SearchTermInsightErrorEnum.SearchTermInsightError,
    )
    smart_campaign_error: (
        gage_smart_campaign_error.SmartCampaignErrorEnum.SmartCampaignError
    ) = proto.Field(
        proto.ENUM,
        number=147,
        oneof="error_code",
        enum=gage_smart_campaign_error.SmartCampaignErrorEnum.SmartCampaignError,
    )
    experiment_arm_error: (
        gage_experiment_arm_error.ExperimentArmErrorEnum.ExperimentArmError
    ) = proto.Field(
        proto.ENUM,
        number=156,
        oneof="error_code",
        enum=gage_experiment_arm_error.ExperimentArmErrorEnum.ExperimentArmError,
    )
    audience_insights_error: (
        gage_audience_insights_error.AudienceInsightsErrorEnum.AudienceInsightsError
    ) = proto.Field(
        proto.ENUM,
        number=167,
        oneof="error_code",
        enum=gage_audience_insights_error.AudienceInsightsErrorEnum.AudienceInsightsError,
    )
    product_link_error: (
        gage_product_link_error.ProductLinkErrorEnum.ProductLinkError
    ) = proto.Field(
        proto.ENUM,
        number=169,
        oneof="error_code",
        enum=gage_product_link_error.ProductLinkErrorEnum.ProductLinkError,
    )
    data_link_error: gage_data_link_error.DataLinkErrorEnum.DataLinkError = (
        proto.Field(
            proto.ENUM,
            number=187,
            oneof="error_code",
            enum=gage_data_link_error.DataLinkErrorEnum.DataLinkError,
        )
    )
    customer_sk_ad_network_conversion_value_schema_error: (
        gage_customer_sk_ad_network_conversion_value_schema_error.CustomerSkAdNetworkConversionValueSchemaErrorEnum.CustomerSkAdNetworkConversionValueSchemaError
    ) = proto.Field(
        proto.ENUM,
        number=170,
        oneof="error_code",
        enum=gage_customer_sk_ad_network_conversion_value_schema_error.CustomerSkAdNetworkConversionValueSchemaErrorEnum.CustomerSkAdNetworkConversionValueSchemaError,
    )
    currency_error: gage_currency_error.CurrencyErrorEnum.CurrencyError = (
        proto.Field(
            proto.ENUM,
            number=171,
            oneof="error_code",
            enum=gage_currency_error.CurrencyErrorEnum.CurrencyError,
        )
    )
    asset_group_signal_error: (
        gage_asset_group_signal_error.AssetGroupSignalErrorEnum.AssetGroupSignalError
    ) = proto.Field(
        proto.ENUM,
        number=176,
        oneof="error_code",
        enum=gage_asset_group_signal_error.AssetGroupSignalErrorEnum.AssetGroupSignalError,
    )
    product_link_invitation_error: (
        gage_product_link_invitation_error.ProductLinkInvitationErrorEnum.ProductLinkInvitationError
    ) = proto.Field(
        proto.ENUM,
        number=177,
        oneof="error_code",
        enum=gage_product_link_invitation_error.ProductLinkInvitationErrorEnum.ProductLinkInvitationError,
    )
    customer_lifecycle_goal_error: (
        gage_customer_lifecycle_goal_error.CustomerLifecycleGoalErrorEnum.CustomerLifecycleGoalError
    ) = proto.Field(
        proto.ENUM,
        number=178,
        oneof="error_code",
        enum=gage_customer_lifecycle_goal_error.CustomerLifecycleGoalErrorEnum.CustomerLifecycleGoalError,
    )
    campaign_lifecycle_goal_error: (
        gage_campaign_lifecycle_goal_error.CampaignLifecycleGoalErrorEnum.CampaignLifecycleGoalError
    ) = proto.Field(
        proto.ENUM,
        number=179,
        oneof="error_code",
        enum=gage_campaign_lifecycle_goal_error.CampaignLifecycleGoalErrorEnum.CampaignLifecycleGoalError,
    )
    identity_verification_error: (
        gage_identity_verification_error.IdentityVerificationErrorEnum.IdentityVerificationError
    ) = proto.Field(
        proto.ENUM,
        number=181,
        oneof="error_code",
        enum=gage_identity_verification_error.IdentityVerificationErrorEnum.IdentityVerificationError,
    )
    user_list_customer_type_error: (
        gage_user_list_customer_type_error.UserListCustomerTypeErrorEnum.UserListCustomerTypeError
    ) = proto.Field(
        proto.ENUM,
        number=183,
        oneof="error_code",
        enum=gage_user_list_customer_type_error.UserListCustomerTypeErrorEnum.UserListCustomerTypeError,
    )
    shopping_product_error: (
        gage_shopping_product_error.ShoppingProductErrorEnum.ShoppingProductError
    ) = proto.Field(
        proto.ENUM,
        number=184,
        oneof="error_code",
        enum=gage_shopping_product_error.ShoppingProductErrorEnum.ShoppingProductError,
    )
    automatically_created_asset_removal_error: (
        gage_automatically_created_asset_removal_error.AutomaticallyCreatedAssetRemovalErrorEnum.AutomaticallyCreatedAssetRemovalError
    ) = proto.Field(
        proto.ENUM,
        number=185,
        oneof="error_code",
        enum=gage_automatically_created_asset_removal_error.AutomaticallyCreatedAssetRemovalErrorEnum.AutomaticallyCreatedAssetRemovalError,
    )
    shareable_preview_error: (
        gage_shareable_preview_error.ShareablePreviewErrorEnum.ShareablePreviewError
    ) = proto.Field(
        proto.ENUM,
        number=186,
        oneof="error_code",
        enum=gage_shareable_preview_error.ShareablePreviewErrorEnum.ShareablePreviewError,
    )
    brand_guidelines_migration_error: (
        gage_brand_guidelines_migration_error.BrandGuidelinesMigrationErrorEnum.BrandGuidelinesMigrationError
    ) = proto.Field(
        proto.ENUM,
        number=191,
        oneof="error_code",
        enum=gage_brand_guidelines_migration_error.BrandGuidelinesMigrationErrorEnum.BrandGuidelinesMigrationError,
    )


class ErrorLocation(proto.Message):
    r"""Describes the part of the request proto that caused the
    error.

    Attributes:
        field_path_elements (MutableSequence[google.ads.googleads.v20.errors.types.ErrorLocation.FieldPathElement]):
            A field path that indicates which field was
            invalid in the request.
    """

    class FieldPathElement(proto.Message):
        r"""A part of a field path.

        .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

        Attributes:
            field_name (str):
                The name of a field or a oneof
            index (int):
                If field_name is a repeated field, this is the element that
                failed

                This field is a member of `oneof`_ ``_index``.
        """

        field_name: str = proto.Field(
            proto.STRING,
            number=1,
        )
        index: int = proto.Field(
            proto.INT32,
            number=3,
            optional=True,
        )

    field_path_elements: MutableSequence[FieldPathElement] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=2,
            message=FieldPathElement,
        )
    )


class ErrorDetails(proto.Message):
    r"""Additional error details.

    Attributes:
        unpublished_error_code (str):
            The error code that should have been
            returned, but wasn't. This is used when the
            error code is not published in the client
            specified version.
        policy_violation_details (google.ads.googleads.v20.errors.types.PolicyViolationDetails):
            Describes an ad policy violation.
        policy_finding_details (google.ads.googleads.v20.errors.types.PolicyFindingDetails):
            Describes policy violation findings.
        quota_error_details (google.ads.googleads.v20.errors.types.QuotaErrorDetails):
            Details on the quota error, including the
            scope (account or developer), the rate bucket
            name and the retry delay.
        resource_count_details (google.ads.googleads.v20.errors.types.ResourceCountDetails):
            Details for a resource count limit exceeded
            error.
    """

    unpublished_error_code: str = proto.Field(
        proto.STRING,
        number=1,
    )
    policy_violation_details: "PolicyViolationDetails" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="PolicyViolationDetails",
    )
    policy_finding_details: "PolicyFindingDetails" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="PolicyFindingDetails",
    )
    quota_error_details: "QuotaErrorDetails" = proto.Field(
        proto.MESSAGE,
        number=4,
        message="QuotaErrorDetails",
    )
    resource_count_details: "ResourceCountDetails" = proto.Field(
        proto.MESSAGE,
        number=5,
        message="ResourceCountDetails",
    )


class PolicyViolationDetails(proto.Message):
    r"""Error returned as part of a mutate response.
    This error indicates single policy violation by some text in one
    of the fields.

    Attributes:
        external_policy_description (str):
            Human readable description of policy
            violation.
        key (google.ads.googleads.v20.common.types.PolicyViolationKey):
            Unique identifier for this violation.
            If policy is exemptible, this key may be used to
            request exemption.
        external_policy_name (str):
            Human readable name of the policy.
        is_exemptible (bool):
            Whether user can file an exemption request
            for this violation.
    """

    external_policy_description: str = proto.Field(
        proto.STRING,
        number=2,
    )
    key: policy.PolicyViolationKey = proto.Field(
        proto.MESSAGE,
        number=4,
        message=policy.PolicyViolationKey,
    )
    external_policy_name: str = proto.Field(
        proto.STRING,
        number=5,
    )
    is_exemptible: bool = proto.Field(
        proto.BOOL,
        number=6,
    )


class PolicyFindingDetails(proto.Message):
    r"""Error returned as part of a mutate response.
    This error indicates one or more policy findings in the fields
    of a resource.

    Attributes:
        policy_topic_entries (MutableSequence[google.ads.googleads.v20.common.types.PolicyTopicEntry]):
            The list of policy topics for the resource. Contains the
            PROHIBITED or FULLY_LIMITED policy topic entries that
            prevented the resource from being saved (among any other
            entries the resource may also have).
    """

    policy_topic_entries: MutableSequence[policy.PolicyTopicEntry] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=1,
            message=policy.PolicyTopicEntry,
        )
    )


class QuotaErrorDetails(proto.Message):
    r"""Additional quota error details when there is QuotaError.

    Attributes:
        rate_scope (google.ads.googleads.v20.errors.types.QuotaErrorDetails.QuotaRateScope):
            The rate scope of the quota limit.
        rate_name (str):
            The high level description of the quota
            bucket. Examples are "Get requests for standard
            access" or "Requests per account".
        retry_delay (google.protobuf.duration_pb2.Duration):
            Backoff period that customers should wait
            before sending next request.
    """

    class QuotaRateScope(proto.Enum):
        r"""Enum of possible scopes that quota buckets belong to.

        Values:
            UNSPECIFIED (0):
                Unspecified enum
            UNKNOWN (1):
                Used for return value only. Represents value
                unknown in this version.
            ACCOUNT (2):
                Per customer account quota
            DEVELOPER (3):
                Per project or DevToken quota
        """

        UNSPECIFIED = 0
        UNKNOWN = 1
        ACCOUNT = 2
        DEVELOPER = 3

    rate_scope: QuotaRateScope = proto.Field(
        proto.ENUM,
        number=1,
        enum=QuotaRateScope,
    )
    rate_name: str = proto.Field(
        proto.STRING,
        number=2,
    )
    retry_delay: duration_pb2.Duration = proto.Field(
        proto.MESSAGE,
        number=3,
        message=duration_pb2.Duration,
    )


class ResourceCountDetails(proto.Message):
    r"""Error details returned when an resource count limit was
    exceeded.

    Attributes:
        enclosing_id (str):
            The ID of the resource whose limit was
            exceeded. External customer ID if the limit is
            for a customer.
        enclosing_resource (str):
            The name of the resource (Customer, Campaign
            etc.) whose limit was exceeded.
        limit (int):
            The limit which was exceeded.
        limit_type (google.ads.googleads.v20.enums.types.ResourceLimitTypeEnum.ResourceLimitType):
            The resource limit type which was exceeded.
        existing_count (int):
            The count of existing entities.
    """

    enclosing_id: str = proto.Field(
        proto.STRING,
        number=1,
    )
    enclosing_resource: str = proto.Field(
        proto.STRING,
        number=5,
    )
    limit: int = proto.Field(
        proto.INT32,
        number=2,
    )
    limit_type: resource_limit_type.ResourceLimitTypeEnum.ResourceLimitType = (
        proto.Field(
            proto.ENUM,
            number=3,
            enum=resource_limit_type.ResourceLimitTypeEnum.ResourceLimitType,
        )
    )
    existing_count: int = proto.Field(
        proto.INT32,
        number=4,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
