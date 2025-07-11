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
    from . import MediaIceStatistics
    from . import MediaRtpStatistics
    from . import MediaStatisticsClientInfo
    from . import MediaStatisticsTrunkInfo
    from . import NamedEntity

class MediaEndpointStatistics(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self) -> None:
        """
        MediaEndpointStatistics - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'trunk': 'MediaStatisticsTrunkInfo',
            'station': 'NamedEntity',
            'user': 'NamedEntity',
            'ice': 'MediaIceStatistics',
            'rtp': 'MediaRtpStatistics',
            'reconnect_attempts': 'int',
            'source_type': 'str',
            'client_info': 'MediaStatisticsClientInfo'
        }

        self.attribute_map = {
            'trunk': 'trunk',
            'station': 'station',
            'user': 'user',
            'ice': 'ice',
            'rtp': 'rtp',
            'reconnect_attempts': 'reconnectAttempts',
            'source_type': 'sourceType',
            'client_info': 'clientInfo'
        }

        self._trunk = None
        self._station = None
        self._user = None
        self._ice = None
        self._rtp = None
        self._reconnect_attempts = None
        self._source_type = None
        self._client_info = None

    @property
    def trunk(self) -> 'MediaStatisticsTrunkInfo':
        """
        Gets the trunk of this MediaEndpointStatistics.
        Trunk information utilized when creating the media endpoint

        :return: The trunk of this MediaEndpointStatistics.
        :rtype: MediaStatisticsTrunkInfo
        """
        return self._trunk

    @trunk.setter
    def trunk(self, trunk: 'MediaStatisticsTrunkInfo') -> None:
        """
        Sets the trunk of this MediaEndpointStatistics.
        Trunk information utilized when creating the media endpoint

        :param trunk: The trunk of this MediaEndpointStatistics.
        :type: MediaStatisticsTrunkInfo
        """
        

        self._trunk = trunk

    @property
    def station(self) -> 'NamedEntity':
        """
        Gets the station of this MediaEndpointStatistics.
        Station information associated with media endpoint

        :return: The station of this MediaEndpointStatistics.
        :rtype: NamedEntity
        """
        return self._station

    @station.setter
    def station(self, station: 'NamedEntity') -> None:
        """
        Sets the station of this MediaEndpointStatistics.
        Station information associated with media endpoint

        :param station: The station of this MediaEndpointStatistics.
        :type: NamedEntity
        """
        

        self._station = station

    @property
    def user(self) -> 'NamedEntity':
        """
        Gets the user of this MediaEndpointStatistics.
        User information associated media endpoint

        :return: The user of this MediaEndpointStatistics.
        :rtype: NamedEntity
        """
        return self._user

    @user.setter
    def user(self, user: 'NamedEntity') -> None:
        """
        Sets the user of this MediaEndpointStatistics.
        User information associated media endpoint

        :param user: The user of this MediaEndpointStatistics.
        :type: NamedEntity
        """
        

        self._user = user

    @property
    def ice(self) -> 'MediaIceStatistics':
        """
        Gets the ice of this MediaEndpointStatistics.
        The ICE protocol statistics and details. Reference: https://www.rfc-editor.org/rfc/rfc5245

        :return: The ice of this MediaEndpointStatistics.
        :rtype: MediaIceStatistics
        """
        return self._ice

    @ice.setter
    def ice(self, ice: 'MediaIceStatistics') -> None:
        """
        Sets the ice of this MediaEndpointStatistics.
        The ICE protocol statistics and details. Reference: https://www.rfc-editor.org/rfc/rfc5245

        :param ice: The ice of this MediaEndpointStatistics.
        :type: MediaIceStatistics
        """
        

        self._ice = ice

    @property
    def rtp(self) -> 'MediaRtpStatistics':
        """
        Gets the rtp of this MediaEndpointStatistics.
        Statistics of sent and received RTP. Reference: https://www.rfc-editor.org/rfc/rfc3550

        :return: The rtp of this MediaEndpointStatistics.
        :rtype: MediaRtpStatistics
        """
        return self._rtp

    @rtp.setter
    def rtp(self, rtp: 'MediaRtpStatistics') -> None:
        """
        Sets the rtp of this MediaEndpointStatistics.
        Statistics of sent and received RTP. Reference: https://www.rfc-editor.org/rfc/rfc3550

        :param rtp: The rtp of this MediaEndpointStatistics.
        :type: MediaRtpStatistics
        """
        

        self._rtp = rtp

    @property
    def reconnect_attempts(self) -> int:
        """
        Gets the reconnect_attempts of this MediaEndpointStatistics.
        Media reconnect attempt count

        :return: The reconnect_attempts of this MediaEndpointStatistics.
        :rtype: int
        """
        return self._reconnect_attempts

    @reconnect_attempts.setter
    def reconnect_attempts(self, reconnect_attempts: int) -> None:
        """
        Sets the reconnect_attempts of this MediaEndpointStatistics.
        Media reconnect attempt count

        :param reconnect_attempts: The reconnect_attempts of this MediaEndpointStatistics.
        :type: int
        """
        

        self._reconnect_attempts = reconnect_attempts

    @property
    def source_type(self) -> str:
        """
        Gets the source_type of this MediaEndpointStatistics.
        Source type of media endpoint

        :return: The source_type of this MediaEndpointStatistics.
        :rtype: str
        """
        return self._source_type

    @source_type.setter
    def source_type(self, source_type: str) -> None:
        """
        Sets the source_type of this MediaEndpointStatistics.
        Source type of media endpoint

        :param source_type: The source_type of this MediaEndpointStatistics.
        :type: str
        """
        if isinstance(source_type, int):
            source_type = str(source_type)
        allowed_values = ["Client"]
        if source_type.lower() not in map(str.lower, allowed_values):
            # print("Invalid value for source_type -> " + source_type)
            self._source_type = "outdated_sdk_version"
        else:
            self._source_type = source_type

    @property
    def client_info(self) -> 'MediaStatisticsClientInfo':
        """
        Gets the client_info of this MediaEndpointStatistics.
        Client information associated with media endpoint

        :return: The client_info of this MediaEndpointStatistics.
        :rtype: MediaStatisticsClientInfo
        """
        return self._client_info

    @client_info.setter
    def client_info(self, client_info: 'MediaStatisticsClientInfo') -> None:
        """
        Sets the client_info of this MediaEndpointStatistics.
        Client information associated with media endpoint

        :param client_info: The client_info of this MediaEndpointStatistics.
        :type: MediaStatisticsClientInfo
        """
        

        self._client_info = client_info

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

