# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.cloud_configuration_rule_case_create import CloudConfigurationRuleCaseCreate
    from datadog_api_client.v2.model.cloud_configuration_rule_compliance_signal_options import (
        CloudConfigurationRuleComplianceSignalOptions,
    )
    from datadog_api_client.v2.model.security_monitoring_filter import SecurityMonitoringFilter
    from datadog_api_client.v2.model.cloud_configuration_rule_options import CloudConfigurationRuleOptions
    from datadog_api_client.v2.model.cloud_configuration_rule_type import CloudConfigurationRuleType


class CloudConfigurationRulePayload(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.cloud_configuration_rule_case_create import CloudConfigurationRuleCaseCreate
        from datadog_api_client.v2.model.cloud_configuration_rule_compliance_signal_options import (
            CloudConfigurationRuleComplianceSignalOptions,
        )
        from datadog_api_client.v2.model.security_monitoring_filter import SecurityMonitoringFilter
        from datadog_api_client.v2.model.cloud_configuration_rule_options import CloudConfigurationRuleOptions
        from datadog_api_client.v2.model.cloud_configuration_rule_type import CloudConfigurationRuleType

        return {
            "cases": ([CloudConfigurationRuleCaseCreate],),
            "compliance_signal_options": (CloudConfigurationRuleComplianceSignalOptions,),
            "custom_message": (str,),
            "custom_name": (str,),
            "filters": ([SecurityMonitoringFilter],),
            "is_enabled": (bool,),
            "message": (str,),
            "name": (str,),
            "options": (CloudConfigurationRuleOptions,),
            "tags": ([str],),
            "type": (CloudConfigurationRuleType,),
        }

    attribute_map = {
        "cases": "cases",
        "compliance_signal_options": "complianceSignalOptions",
        "custom_message": "customMessage",
        "custom_name": "customName",
        "filters": "filters",
        "is_enabled": "isEnabled",
        "message": "message",
        "name": "name",
        "options": "options",
        "tags": "tags",
        "type": "type",
    }

    def __init__(
        self_,
        cases: List[CloudConfigurationRuleCaseCreate],
        compliance_signal_options: CloudConfigurationRuleComplianceSignalOptions,
        is_enabled: bool,
        message: str,
        name: str,
        options: CloudConfigurationRuleOptions,
        custom_message: Union[str, UnsetType] = unset,
        custom_name: Union[str, UnsetType] = unset,
        filters: Union[List[SecurityMonitoringFilter], UnsetType] = unset,
        tags: Union[List[str], UnsetType] = unset,
        type: Union[CloudConfigurationRuleType, UnsetType] = unset,
        **kwargs,
    ):
        """
        The payload of a cloud configuration rule.

        :param cases: Description of generated findings and signals (severity and channels to be notified in case of a signal). Must contain exactly one item.
        :type cases: [CloudConfigurationRuleCaseCreate]

        :param compliance_signal_options: How to generate compliance signals. Useful for cloud_configuration rules only.
        :type compliance_signal_options: CloudConfigurationRuleComplianceSignalOptions

        :param custom_message: Custom/Overridden message for generated signals (used in case of Default rule update).
        :type custom_message: str, optional

        :param custom_name: Custom/Overridden name of the rule (used in case of Default rule update).
        :type custom_name: str, optional

        :param filters: Additional queries to filter matched events before they are processed.
        :type filters: [SecurityMonitoringFilter], optional

        :param is_enabled: Whether the rule is enabled.
        :type is_enabled: bool

        :param message: Message in markdown format for generated findings and signals.
        :type message: str

        :param name: The name of the rule.
        :type name: str

        :param options: Options on cloud configuration rules.
        :type options: CloudConfigurationRuleOptions

        :param tags: Tags for generated findings and signals.
        :type tags: [str], optional

        :param type: The rule type.
        :type type: CloudConfigurationRuleType, optional
        """
        if custom_message is not unset:
            kwargs["custom_message"] = custom_message
        if custom_name is not unset:
            kwargs["custom_name"] = custom_name
        if filters is not unset:
            kwargs["filters"] = filters
        if tags is not unset:
            kwargs["tags"] = tags
        if type is not unset:
            kwargs["type"] = type
        super().__init__(kwargs)

        self_.cases = cases
        self_.compliance_signal_options = compliance_signal_options
        self_.is_enabled = is_enabled
        self_.message = message
        self_.name = name
        self_.options = options
