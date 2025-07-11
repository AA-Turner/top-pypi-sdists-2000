# coding: utf-8

"""
Copyright 2016 SmartBear Software

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.

    Ref: https://github.com/swagger-api/swagger-codegen
"""

from datetime import datetime
from datetime import date
from pprint import pformat
import re
import json

from ..utils import sanitize_for_serialization

# type hinting support
from typing import TYPE_CHECKING
from typing import List
from typing import Dict

if TYPE_CHECKING:
    from . import ContactColumnToDataActionFieldMapping
    from . import DataActionConditionPredicate
    from . import DomainEntityRef
    from . import TimeAndDateSubCondition

class Condition(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self) -> None:
        """
        Condition - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'type': 'str',
            'inverted': 'bool',
            'attribute_name': 'str',
            'value': 'str',
            'value_type': 'str',
            'operator': 'str',
            'codes': 'list[str]',
            'pcProperty': 'str',
            'property_type': 'str',
            'data_action': 'DomainEntityRef',
            'data_not_found_resolution': 'bool',
            'contact_id_field': 'str',
            'call_analysis_result_field': 'str',
            'agent_wrapup_field': 'str',
            'contact_column_to_data_action_field_mappings': 'list[ContactColumnToDataActionFieldMapping]',
            'predicates': 'list[DataActionConditionPredicate]',
            'sub_conditions': 'list[TimeAndDateSubCondition]',
            'match_any_conditions': 'bool',
            'time_zone_id': 'str'
        }

        self.attribute_map = {
            'type': 'type',
            'inverted': 'inverted',
            'attribute_name': 'attributeName',
            'value': 'value',
            'value_type': 'valueType',
            'operator': 'operator',
            'codes': 'codes',
            'pcProperty': 'property',
            'property_type': 'propertyType',
            'data_action': 'dataAction',
            'data_not_found_resolution': 'dataNotFoundResolution',
            'contact_id_field': 'contactIdField',
            'call_analysis_result_field': 'callAnalysisResultField',
            'agent_wrapup_field': 'agentWrapupField',
            'contact_column_to_data_action_field_mappings': 'contactColumnToDataActionFieldMappings',
            'predicates': 'predicates',
            'sub_conditions': 'subConditions',
            'match_any_conditions': 'matchAnyConditions',
            'time_zone_id': 'timeZoneId'
        }

        self._type = None
        self._inverted = None
        self._attribute_name = None
        self._value = None
        self._value_type = None
        self._operator = None
        self._codes = None
        self._pcProperty = None
        self._property_type = None
        self._data_action = None
        self._data_not_found_resolution = None
        self._contact_id_field = None
        self._call_analysis_result_field = None
        self._agent_wrapup_field = None
        self._contact_column_to_data_action_field_mappings = None
        self._predicates = None
        self._sub_conditions = None
        self._match_any_conditions = None
        self._time_zone_id = None

    @property
    def type(self) -> str:
        """
        Gets the type of this Condition.
        The type of the condition.

        :return: The type of this Condition.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type: str) -> None:
        """
        Sets the type of this Condition.
        The type of the condition.

        :param type: The type of this Condition.
        :type: str
        """
        if isinstance(type, int):
            type = str(type)
        allowed_values = ["wrapupCondition", "systemDispositionCondition", "contactAttributeCondition", "phoneNumberCondition", "phoneNumberTypeCondition", "callAnalysisCondition", "contactPropertyCondition", "dataActionCondition", "timeAndDateCondition"]
        if type.lower() not in map(str.lower, allowed_values):
            # print("Invalid value for type -> " + type)
            self._type = "outdated_sdk_version"
        else:
            self._type = type

    @property
    def inverted(self) -> bool:
        """
        Gets the inverted of this Condition.
        If true, inverts the result of evaluating this Condition. Default is false.

        :return: The inverted of this Condition.
        :rtype: bool
        """
        return self._inverted

    @inverted.setter
    def inverted(self, inverted: bool) -> None:
        """
        Sets the inverted of this Condition.
        If true, inverts the result of evaluating this Condition. Default is false.

        :param inverted: The inverted of this Condition.
        :type: bool
        """
        

        self._inverted = inverted

    @property
    def attribute_name(self) -> str:
        """
        Gets the attribute_name of this Condition.
        An attribute name associated with this Condition. Required for a contactAttributeCondition.

        :return: The attribute_name of this Condition.
        :rtype: str
        """
        return self._attribute_name

    @attribute_name.setter
    def attribute_name(self, attribute_name: str) -> None:
        """
        Sets the attribute_name of this Condition.
        An attribute name associated with this Condition. Required for a contactAttributeCondition.

        :param attribute_name: The attribute_name of this Condition.
        :type: str
        """
        

        self._attribute_name = attribute_name

    @property
    def value(self) -> str:
        """
        Gets the value of this Condition.
        A value associated with this Condition. This could be text, a number, or a relative time. Not used for a DataActionCondition.

        :return: The value of this Condition.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value: str) -> None:
        """
        Sets the value of this Condition.
        A value associated with this Condition. This could be text, a number, or a relative time. Not used for a DataActionCondition.

        :param value: The value of this Condition.
        :type: str
        """
        

        self._value = value

    @property
    def value_type(self) -> str:
        """
        Gets the value_type of this Condition.
        The type of the value associated with this Condition. Not used for a DataActionCondition.

        :return: The value_type of this Condition.
        :rtype: str
        """
        return self._value_type

    @value_type.setter
    def value_type(self, value_type: str) -> None:
        """
        Sets the value_type of this Condition.
        The type of the value associated with this Condition. Not used for a DataActionCondition.

        :param value_type: The value_type of this Condition.
        :type: str
        """
        if isinstance(value_type, int):
            value_type = str(value_type)
        allowed_values = ["STRING", "NUMERIC", "DATETIME", "PERIOD"]
        if value_type.lower() not in map(str.lower, allowed_values):
            # print("Invalid value for value_type -> " + value_type)
            self._value_type = "outdated_sdk_version"
        else:
            self._value_type = value_type

    @property
    def operator(self) -> str:
        """
        Gets the operator of this Condition.
        An operation with which to evaluate the Condition. Not used for a DataActionCondition.

        :return: The operator of this Condition.
        :rtype: str
        """
        return self._operator

    @operator.setter
    def operator(self, operator: str) -> None:
        """
        Sets the operator of this Condition.
        An operation with which to evaluate the Condition. Not used for a DataActionCondition.

        :param operator: The operator of this Condition.
        :type: str
        """
        if isinstance(operator, int):
            operator = str(operator)
        allowed_values = ["EQUALS", "LESS_THAN", "LESS_THAN_EQUALS", "GREATER_THAN", "GREATER_THAN_EQUALS", "CONTAINS", "BEGINS_WITH", "ENDS_WITH", "BEFORE", "AFTER", "IN", "BETWEEN"]
        if operator.lower() not in map(str.lower, allowed_values):
            # print("Invalid value for operator -> " + operator)
            self._operator = "outdated_sdk_version"
        else:
            self._operator = operator

    @property
    def codes(self) -> List[str]:
        """
        Gets the codes of this Condition.
        List of wrap-up code identifiers. Required for a wrapupCondition.

        :return: The codes of this Condition.
        :rtype: list[str]
        """
        return self._codes

    @codes.setter
    def codes(self, codes: List[str]) -> None:
        """
        Sets the codes of this Condition.
        List of wrap-up code identifiers. Required for a wrapupCondition.

        :param codes: The codes of this Condition.
        :type: list[str]
        """
        

        self._codes = codes

    @property
    def pcProperty(self) -> str:
        """
        Gets the pcProperty of this Condition.
        A value associated with the property type of this Condition. Required for a contactPropertyCondition.

        :return: The pcProperty of this Condition.
        :rtype: str
        """
        return self._pcProperty

    @pcProperty.setter
    def pcProperty(self, pcProperty: str) -> None:
        """
        Sets the pcProperty of this Condition.
        A value associated with the property type of this Condition. Required for a contactPropertyCondition.

        :param pcProperty: The pcProperty of this Condition.
        :type: str
        """
        

        self._pcProperty = pcProperty

    @property
    def property_type(self) -> str:
        """
        Gets the property_type of this Condition.
        The type of the property associated with this Condition. Required for a contactPropertyCondition.

        :return: The property_type of this Condition.
        :rtype: str
        """
        return self._property_type

    @property_type.setter
    def property_type(self, property_type: str) -> None:
        """
        Sets the property_type of this Condition.
        The type of the property associated with this Condition. Required for a contactPropertyCondition.

        :param property_type: The property_type of this Condition.
        :type: str
        """
        if isinstance(property_type, int):
            property_type = str(property_type)
        allowed_values = ["LAST_ATTEMPT_BY_COLUMN", "LAST_ATTEMPT_OVERALL", "LAST_WRAPUP_BY_COLUMN", "LAST_WRAPUP_OVERALL"]
        if property_type.lower() not in map(str.lower, allowed_values):
            # print("Invalid value for property_type -> " + property_type)
            self._property_type = "outdated_sdk_version"
        else:
            self._property_type = property_type

    @property
    def data_action(self) -> 'DomainEntityRef':
        """
        Gets the data_action of this Condition.
        The Data Action to use for this condition. Required for a dataActionCondition.

        :return: The data_action of this Condition.
        :rtype: DomainEntityRef
        """
        return self._data_action

    @data_action.setter
    def data_action(self, data_action: 'DomainEntityRef') -> None:
        """
        Sets the data_action of this Condition.
        The Data Action to use for this condition. Required for a dataActionCondition.

        :param data_action: The data_action of this Condition.
        :type: DomainEntityRef
        """
        

        self._data_action = data_action

    @property
    def data_not_found_resolution(self) -> bool:
        """
        Gets the data_not_found_resolution of this Condition.
        The result of this condition if the data action returns a result indicating there was no data. Required for a DataActionCondition.

        :return: The data_not_found_resolution of this Condition.
        :rtype: bool
        """
        return self._data_not_found_resolution

    @data_not_found_resolution.setter
    def data_not_found_resolution(self, data_not_found_resolution: bool) -> None:
        """
        Sets the data_not_found_resolution of this Condition.
        The result of this condition if the data action returns a result indicating there was no data. Required for a DataActionCondition.

        :param data_not_found_resolution: The data_not_found_resolution of this Condition.
        :type: bool
        """
        

        self._data_not_found_resolution = data_not_found_resolution

    @property
    def contact_id_field(self) -> str:
        """
        Gets the contact_id_field of this Condition.
        The input field from the data action that the contactId will be passed to for this condition. Valid for a dataActionCondition.

        :return: The contact_id_field of this Condition.
        :rtype: str
        """
        return self._contact_id_field

    @contact_id_field.setter
    def contact_id_field(self, contact_id_field: str) -> None:
        """
        Sets the contact_id_field of this Condition.
        The input field from the data action that the contactId will be passed to for this condition. Valid for a dataActionCondition.

        :param contact_id_field: The contact_id_field of this Condition.
        :type: str
        """
        

        self._contact_id_field = contact_id_field

    @property
    def call_analysis_result_field(self) -> str:
        """
        Gets the call_analysis_result_field of this Condition.
        The input field from the data action that the callAnalysisResult will be passed to for this condition. Valid for a wrapup dataActionCondition.

        :return: The call_analysis_result_field of this Condition.
        :rtype: str
        """
        return self._call_analysis_result_field

    @call_analysis_result_field.setter
    def call_analysis_result_field(self, call_analysis_result_field: str) -> None:
        """
        Sets the call_analysis_result_field of this Condition.
        The input field from the data action that the callAnalysisResult will be passed to for this condition. Valid for a wrapup dataActionCondition.

        :param call_analysis_result_field: The call_analysis_result_field of this Condition.
        :type: str
        """
        

        self._call_analysis_result_field = call_analysis_result_field

    @property
    def agent_wrapup_field(self) -> str:
        """
        Gets the agent_wrapup_field of this Condition.
        The input field from the data action that the agentWrapup will be passed to for this condition. Valid for a wrapup dataActionCondition.

        :return: The agent_wrapup_field of this Condition.
        :rtype: str
        """
        return self._agent_wrapup_field

    @agent_wrapup_field.setter
    def agent_wrapup_field(self, agent_wrapup_field: str) -> None:
        """
        Sets the agent_wrapup_field of this Condition.
        The input field from the data action that the agentWrapup will be passed to for this condition. Valid for a wrapup dataActionCondition.

        :param agent_wrapup_field: The agent_wrapup_field of this Condition.
        :type: str
        """
        

        self._agent_wrapup_field = agent_wrapup_field

    @property
    def contact_column_to_data_action_field_mappings(self) -> List['ContactColumnToDataActionFieldMapping']:
        """
        Gets the contact_column_to_data_action_field_mappings of this Condition.
        A list of mappings defining which contact data fields will be passed to which data action input fields for this condition. Valid for a dataActionCondition.

        :return: The contact_column_to_data_action_field_mappings of this Condition.
        :rtype: list[ContactColumnToDataActionFieldMapping]
        """
        return self._contact_column_to_data_action_field_mappings

    @contact_column_to_data_action_field_mappings.setter
    def contact_column_to_data_action_field_mappings(self, contact_column_to_data_action_field_mappings: List['ContactColumnToDataActionFieldMapping']) -> None:
        """
        Sets the contact_column_to_data_action_field_mappings of this Condition.
        A list of mappings defining which contact data fields will be passed to which data action input fields for this condition. Valid for a dataActionCondition.

        :param contact_column_to_data_action_field_mappings: The contact_column_to_data_action_field_mappings of this Condition.
        :type: list[ContactColumnToDataActionFieldMapping]
        """
        

        self._contact_column_to_data_action_field_mappings = contact_column_to_data_action_field_mappings

    @property
    def predicates(self) -> List['DataActionConditionPredicate']:
        """
        Gets the predicates of this Condition.
        A list of predicates defining the comparisons to use for this condition. Required for a dataActionCondition.

        :return: The predicates of this Condition.
        :rtype: list[DataActionConditionPredicate]
        """
        return self._predicates

    @predicates.setter
    def predicates(self, predicates: List['DataActionConditionPredicate']) -> None:
        """
        Sets the predicates of this Condition.
        A list of predicates defining the comparisons to use for this condition. Required for a dataActionCondition.

        :param predicates: The predicates of this Condition.
        :type: list[DataActionConditionPredicate]
        """
        

        self._predicates = predicates

    @property
    def sub_conditions(self) -> List['TimeAndDateSubCondition']:
        """
        Gets the sub_conditions of this Condition.
        A list of sub-conditions to evaluate. Required for a timeAndDateCondition.

        :return: The sub_conditions of this Condition.
        :rtype: list[TimeAndDateSubCondition]
        """
        return self._sub_conditions

    @sub_conditions.setter
    def sub_conditions(self, sub_conditions: List['TimeAndDateSubCondition']) -> None:
        """
        Sets the sub_conditions of this Condition.
        A list of sub-conditions to evaluate. Required for a timeAndDateCondition.

        :param sub_conditions: The sub_conditions of this Condition.
        :type: list[TimeAndDateSubCondition]
        """
        

        self._sub_conditions = sub_conditions

    @property
    def match_any_conditions(self) -> bool:
        """
        Gets the match_any_conditions of this Condition.
        If true, only one sub-condition must match for the condition to be true. If false, all sub-conditions must match. Default is false. Required for a timeAndDateCondition.

        :return: The match_any_conditions of this Condition.
        :rtype: bool
        """
        return self._match_any_conditions

    @match_any_conditions.setter
    def match_any_conditions(self, match_any_conditions: bool) -> None:
        """
        Sets the match_any_conditions of this Condition.
        If true, only one sub-condition must match for the condition to be true. If false, all sub-conditions must match. Default is false. Required for a timeAndDateCondition.

        :param match_any_conditions: The match_any_conditions of this Condition.
        :type: bool
        """
        

        self._match_any_conditions = match_any_conditions

    @property
    def time_zone_id(self) -> str:
        """
        Gets the time_zone_id of this Condition.
        The time zone to use for this condition. Required for a timeAndDateCondition.

        :return: The time_zone_id of this Condition.
        :rtype: str
        """
        return self._time_zone_id

    @time_zone_id.setter
    def time_zone_id(self, time_zone_id: str) -> None:
        """
        Sets the time_zone_id of this Condition.
        The time zone to use for this condition. Required for a timeAndDateCondition.

        :param time_zone_id: The time_zone_id of this Condition.
        :type: str
        """
        

        self._time_zone_id = time_zone_id

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in self.swagger_types.items():
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_json(self):
        """
        Returns the model as raw JSON
        """
        return json.dumps(sanitize_for_serialization(self.to_dict()))

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other

