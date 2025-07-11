# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelComposed,
    cached_property,
)


class SecurityMonitoringRuleConvertPayload(ModelComposed):
    def __init__(self, **kwargs):
        """
        Convert a rule from JSON to Terraform.

        :param cases: Cases for generating signals.
        :type cases: [SecurityMonitoringRuleCaseCreate]

        :param custom_message: Custom/Overridden message for generated signals (used in case of Default rule update).
        :type custom_message: str, optional

        :param custom_name: Custom/Overridden name of the rule (used in case of Default rule update).
        :type custom_name: str, optional

        :param filters: Additional queries to filter matched events before they are processed. This field is deprecated for log detection, signal correlation, and workload security rules.
        :type filters: [SecurityMonitoringFilter], optional

        :param group_signals_by: Additional grouping to perform on top of the existing groups in the query section. Must be a subset of the existing groups.
        :type group_signals_by: [str], optional

        :param has_extended_title: Whether the notifications include the triggering group-by values in their title.
        :type has_extended_title: bool, optional

        :param is_enabled: Whether the rule is enabled.
        :type is_enabled: bool

        :param message: Message for generated signals.
        :type message: str

        :param name: The name of the rule.
        :type name: str

        :param options: Options.
        :type options: SecurityMonitoringRuleOptions

        :param queries: Queries for selecting logs which are part of the rule.
        :type queries: [SecurityMonitoringStandardRuleQuery]

        :param reference_tables: Reference tables for the rule.
        :type reference_tables: [SecurityMonitoringReferenceTable], optional

        :param tags: Tags for generated signals.
        :type tags: [str], optional

        :param third_party_cases: Cases for generating signals from third-party rules. Only available for third-party rules.
        :type third_party_cases: [SecurityMonitoringThirdPartyRuleCaseCreate], optional

        :param type: The rule type.
        :type type: SecurityMonitoringRuleTypeCreate, optional
        """
        super().__init__(kwargs)

    @cached_property
    def _composed_schemas(_):
        # we need this here to make our import statements work
        # we must store _composed_schemas in here so the code is only run
        # when we invoke this method. If we kept this at the class
        # level we would get an error because the class level
        # code would be run when this module is imported, and these composed
        # classes don't exist yet because their module has not finished
        # loading
        from datadog_api_client.v2.model.security_monitoring_standard_rule_payload import (
            SecurityMonitoringStandardRulePayload,
        )
        from datadog_api_client.v2.model.security_monitoring_signal_rule_payload import (
            SecurityMonitoringSignalRulePayload,
        )

        return {
            "oneOf": [
                SecurityMonitoringStandardRulePayload,
                SecurityMonitoringSignalRulePayload,
            ],
        }
