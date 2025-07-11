# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20241101


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class MiddlewareBinaryBackupContent(object):
    """
    The content of the middleware binaries included in a backup.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new MiddlewareBinaryBackupContent object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param version:
            The value to assign to the version property of this MiddlewareBinaryBackupContent.
        :type version: str

        :param patches:
            The value to assign to the patches property of this MiddlewareBinaryBackupContent.
        :type patches: list[oci.wlms.models.MiddlewareBackupPatch]

        """
        self.swagger_types = {
            'version': 'str',
            'patches': 'list[MiddlewareBackupPatch]'
        }
        self.attribute_map = {
            'version': 'version',
            'patches': 'patches'
        }
        self._version = None
        self._patches = None

    @property
    def version(self):
        """
        Gets the version of this MiddlewareBinaryBackupContent.
        The version of the middleware binaries included in the backup.


        :return: The version of this MiddlewareBinaryBackupContent.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """
        Sets the version of this MiddlewareBinaryBackupContent.
        The version of the middleware binaries included in the backup.


        :param version: The version of this MiddlewareBinaryBackupContent.
        :type: str
        """
        self._version = version

    @property
    def patches(self):
        """
        Gets the patches of this MiddlewareBinaryBackupContent.
        The list of patches installed in the middleware included in the backup.


        :return: The patches of this MiddlewareBinaryBackupContent.
        :rtype: list[oci.wlms.models.MiddlewareBackupPatch]
        """
        return self._patches

    @patches.setter
    def patches(self, patches):
        """
        Sets the patches of this MiddlewareBinaryBackupContent.
        The list of patches installed in the middleware included in the backup.


        :param patches: The patches of this MiddlewareBinaryBackupContent.
        :type: list[oci.wlms.models.MiddlewareBackupPatch]
        """
        self._patches = patches

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
