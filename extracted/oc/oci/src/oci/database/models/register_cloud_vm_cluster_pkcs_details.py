# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20160918


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class RegisterCloudVmClusterPkcsDetails(object):
    """
    Details of registering PKCS11 driver.
    """

    #: A constant which can be used with the tde_key_store_type property of a RegisterCloudVmClusterPkcsDetails.
    #: This constant has a value of "AZURE"
    TDE_KEY_STORE_TYPE_AZURE = "AZURE"

    #: A constant which can be used with the tde_key_store_type property of a RegisterCloudVmClusterPkcsDetails.
    #: This constant has a value of "OCI"
    TDE_KEY_STORE_TYPE_OCI = "OCI"

    def __init__(self, **kwargs):
        """
        Initializes a new RegisterCloudVmClusterPkcsDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param tde_key_store_type:
            The value to assign to the tde_key_store_type property of this RegisterCloudVmClusterPkcsDetails.
            Allowed values for this property are: "AZURE", "OCI"
        :type tde_key_store_type: str

        """
        self.swagger_types = {
            'tde_key_store_type': 'str'
        }
        self.attribute_map = {
            'tde_key_store_type': 'tdeKeyStoreType'
        }
        self._tde_key_store_type = None

    @property
    def tde_key_store_type(self):
        """
        **[Required]** Gets the tde_key_store_type of this RegisterCloudVmClusterPkcsDetails.
        TDE keystore type

        Allowed values for this property are: "AZURE", "OCI"


        :return: The tde_key_store_type of this RegisterCloudVmClusterPkcsDetails.
        :rtype: str
        """
        return self._tde_key_store_type

    @tde_key_store_type.setter
    def tde_key_store_type(self, tde_key_store_type):
        """
        Sets the tde_key_store_type of this RegisterCloudVmClusterPkcsDetails.
        TDE keystore type


        :param tde_key_store_type: The tde_key_store_type of this RegisterCloudVmClusterPkcsDetails.
        :type: str
        """
        allowed_values = ["AZURE", "OCI"]
        if not value_allowed_none_or_none_sentinel(tde_key_store_type, allowed_values):
            raise ValueError(
                f"Invalid value for `tde_key_store_type`, must be None or one of {allowed_values}"
            )
        self._tde_key_store_type = tde_key_store_type

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
