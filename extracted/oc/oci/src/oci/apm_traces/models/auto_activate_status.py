# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20200630


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class AutoActivateStatus(object):
    """
    Status of autoactivation for the given data key in the APM Domain.
    """

    #: A constant which can be used with the state property of a AutoActivateStatus.
    #: This constant has a value of "ON"
    STATE_ON = "ON"

    #: A constant which can be used with the state property of a AutoActivateStatus.
    #: This constant has a value of "OFF"
    STATE_OFF = "OFF"

    #: A constant which can be used with the data_key property of a AutoActivateStatus.
    #: This constant has a value of "PRIVATE_DATA_KEY"
    DATA_KEY_PRIVATE_DATA_KEY = "PRIVATE_DATA_KEY"

    #: A constant which can be used with the data_key property of a AutoActivateStatus.
    #: This constant has a value of "PUBLIC_DATA_KEY"
    DATA_KEY_PUBLIC_DATA_KEY = "PUBLIC_DATA_KEY"

    def __init__(self, **kwargs):
        """
        Initializes a new AutoActivateStatus object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param state:
            The value to assign to the state property of this AutoActivateStatus.
            Allowed values for this property are: "ON", "OFF", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type state: str

        :param data_key:
            The value to assign to the data_key property of this AutoActivateStatus.
            Allowed values for this property are: "PRIVATE_DATA_KEY", "PUBLIC_DATA_KEY", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type data_key: str

        """
        self.swagger_types = {
            'state': 'str',
            'data_key': 'str'
        }
        self.attribute_map = {
            'state': 'state',
            'data_key': 'dataKey'
        }
        self._state = None
        self._data_key = None

    @property
    def state(self):
        """
        **[Required]** Gets the state of this AutoActivateStatus.
        State of autoactivation in this APM Domain.  If \"ON\" auto-activate is set to true, if \"OFF\" auto-activate is set to false.

        Allowed values for this property are: "ON", "OFF", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The state of this AutoActivateStatus.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """
        Sets the state of this AutoActivateStatus.
        State of autoactivation in this APM Domain.  If \"ON\" auto-activate is set to true, if \"OFF\" auto-activate is set to false.


        :param state: The state of this AutoActivateStatus.
        :type: str
        """
        allowed_values = ["ON", "OFF"]
        if not value_allowed_none_or_none_sentinel(state, allowed_values):
            state = 'UNKNOWN_ENUM_VALUE'
        self._state = state

    @property
    def data_key(self):
        """
        **[Required]** Gets the data_key of this AutoActivateStatus.
        Data key type for which auto-activate needs needs to be turned on or off.

        Allowed values for this property are: "PRIVATE_DATA_KEY", "PUBLIC_DATA_KEY", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The data_key of this AutoActivateStatus.
        :rtype: str
        """
        return self._data_key

    @data_key.setter
    def data_key(self, data_key):
        """
        Sets the data_key of this AutoActivateStatus.
        Data key type for which auto-activate needs needs to be turned on or off.


        :param data_key: The data_key of this AutoActivateStatus.
        :type: str
        """
        allowed_values = ["PRIVATE_DATA_KEY", "PUBLIC_DATA_KEY"]
        if not value_allowed_none_or_none_sentinel(data_key, allowed_values):
            data_key = 'UNKNOWN_ENUM_VALUE'
        self._data_key = data_key

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
