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
    from datadog_api_client.v2.model.security_monitoring_rule_case_create import SecurityMonitoringRuleCaseCreate
    from datadog_api_client.v2.model.security_monitoring_filter import SecurityMonitoringFilter
    from datadog_api_client.v2.model.security_monitoring_rule_options import SecurityMonitoringRuleOptions
    from datadog_api_client.v2.model.security_monitoring_standard_rule_query import SecurityMonitoringStandardRuleQuery
    from datadog_api_client.v2.model.security_monitoring_reference_table import SecurityMonitoringReferenceTable
    from datadog_api_client.v2.model.security_monitoring_third_party_rule_case_create import (
        SecurityMonitoringThirdPartyRuleCaseCreate,
    )
    from datadog_api_client.v2.model.security_monitoring_rule_type_create import SecurityMonitoringRuleTypeCreate


class SecurityMonitoringStandardRulePayload(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.security_monitoring_rule_case_create import SecurityMonitoringRuleCaseCreate
        from datadog_api_client.v2.model.security_monitoring_filter import SecurityMonitoringFilter
        from datadog_api_client.v2.model.security_monitoring_rule_options import SecurityMonitoringRuleOptions
        from datadog_api_client.v2.model.security_monitoring_standard_rule_query import (
            SecurityMonitoringStandardRuleQuery,
        )
        from datadog_api_client.v2.model.security_monitoring_reference_table import SecurityMonitoringReferenceTable
        from datadog_api_client.v2.model.security_monitoring_third_party_rule_case_create import (
            SecurityMonitoringThirdPartyRuleCaseCreate,
        )
        from datadog_api_client.v2.model.security_monitoring_rule_type_create import SecurityMonitoringRuleTypeCreate

        return {
            "cases": ([SecurityMonitoringRuleCaseCreate],),
            "custom_message": (str,),
            "custom_name": (str,),
            "filters": ([SecurityMonitoringFilter],),
            "group_signals_by": ([str],),
            "has_extended_title": (bool,),
            "is_enabled": (bool,),
            "message": (str,),
            "name": (str,),
            "options": (SecurityMonitoringRuleOptions,),
            "queries": ([SecurityMonitoringStandardRuleQuery],),
            "reference_tables": ([SecurityMonitoringReferenceTable],),
            "tags": ([str],),
            "third_party_cases": ([SecurityMonitoringThirdPartyRuleCaseCreate],),
            "type": (SecurityMonitoringRuleTypeCreate,),
        }

    attribute_map = {
        "cases": "cases",
        "custom_message": "customMessage",
        "custom_name": "customName",
        "filters": "filters",
        "group_signals_by": "groupSignalsBy",
        "has_extended_title": "hasExtendedTitle",
        "is_enabled": "isEnabled",
        "message": "message",
        "name": "name",
        "options": "options",
        "queries": "queries",
        "reference_tables": "referenceTables",
        "tags": "tags",
        "third_party_cases": "thirdPartyCases",
        "type": "type",
    }

    def __init__(
        self_,
        cases: List[SecurityMonitoringRuleCaseCreate],
        is_enabled: bool,
        message: str,
        name: str,
        options: SecurityMonitoringRuleOptions,
        queries: List[SecurityMonitoringStandardRuleQuery],
        custom_message: Union[str, UnsetType] = unset,
        custom_name: Union[str, UnsetType] = unset,
        filters: Union[List[SecurityMonitoringFilter], UnsetType] = unset,
        group_signals_by: Union[List[str], UnsetType] = unset,
        has_extended_title: Union[bool, UnsetType] = unset,
        reference_tables: Union[List[SecurityMonitoringReferenceTable], UnsetType] = unset,
        tags: Union[List[str], UnsetType] = unset,
        third_party_cases: Union[List[SecurityMonitoringThirdPartyRuleCaseCreate], UnsetType] = unset,
        type: Union[SecurityMonitoringRuleTypeCreate, UnsetType] = unset,
        **kwargs,
    ):
        """
        The payload of a rule.

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
        if custom_message is not unset:
            kwargs["custom_message"] = custom_message
        if custom_name is not unset:
            kwargs["custom_name"] = custom_name
        if filters is not unset:
            kwargs["filters"] = filters
        if group_signals_by is not unset:
            kwargs["group_signals_by"] = group_signals_by
        if has_extended_title is not unset:
            kwargs["has_extended_title"] = has_extended_title
        if reference_tables is not unset:
            kwargs["reference_tables"] = reference_tables
        if tags is not unset:
            kwargs["tags"] = tags
        if third_party_cases is not unset:
            kwargs["third_party_cases"] = third_party_cases
        if type is not unset:
            kwargs["type"] = type
        super().__init__(kwargs)

        self_.cases = cases
        self_.is_enabled = is_enabled
        self_.message = message
        self_.name = name
        self_.options = options
        self_.queries = queries
