# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20200630


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateDatabaseInsightDetails(object):
    """
    The information about database to be analyzed.
    """

    #: A constant which can be used with the entity_source property of a CreateDatabaseInsightDetails.
    #: This constant has a value of "EM_MANAGED_EXTERNAL_DATABASE"
    ENTITY_SOURCE_EM_MANAGED_EXTERNAL_DATABASE = "EM_MANAGED_EXTERNAL_DATABASE"

    #: A constant which can be used with the entity_source property of a CreateDatabaseInsightDetails.
    #: This constant has a value of "PE_COMANAGED_DATABASE"
    ENTITY_SOURCE_PE_COMANAGED_DATABASE = "PE_COMANAGED_DATABASE"

    #: A constant which can be used with the entity_source property of a CreateDatabaseInsightDetails.
    #: This constant has a value of "MDS_MYSQL_DATABASE_SYSTEM"
    ENTITY_SOURCE_MDS_MYSQL_DATABASE_SYSTEM = "MDS_MYSQL_DATABASE_SYSTEM"

    #: A constant which can be used with the entity_source property of a CreateDatabaseInsightDetails.
    #: This constant has a value of "EXTERNAL_MYSQL_DATABASE_SYSTEM"
    ENTITY_SOURCE_EXTERNAL_MYSQL_DATABASE_SYSTEM = "EXTERNAL_MYSQL_DATABASE_SYSTEM"

    #: A constant which can be used with the entity_source property of a CreateDatabaseInsightDetails.
    #: This constant has a value of "MACS_MANAGED_CLOUD_DATABASE"
    ENTITY_SOURCE_MACS_MANAGED_CLOUD_DATABASE = "MACS_MANAGED_CLOUD_DATABASE"

    #: A constant which can be used with the entity_source property of a CreateDatabaseInsightDetails.
    #: This constant has a value of "MACS_MANAGED_AUTONOMOUS_DATABASE"
    ENTITY_SOURCE_MACS_MANAGED_AUTONOMOUS_DATABASE = "MACS_MANAGED_AUTONOMOUS_DATABASE"

    def __init__(self, **kwargs):
        """
        Initializes a new CreateDatabaseInsightDetails object with values from keyword arguments. This class has the following subclasses and if you are using this class as input
        to a service operations then you should favor using a subclass over the base class:

        * :class:`~oci.opsi.models.CreateMacsManagedCloudDatabaseInsightDetails`
        * :class:`~oci.opsi.models.CreateExternalMysqlDatabaseInsightDetails`
        * :class:`~oci.opsi.models.CreateAutonomousDatabaseInsightDetails`
        * :class:`~oci.opsi.models.CreateMacsManagedAutonomousDatabaseInsightDetails`
        * :class:`~oci.opsi.models.CreateMdsMySqlDatabaseInsightDetails`
        * :class:`~oci.opsi.models.CreateEmManagedExternalDatabaseInsightDetails`
        * :class:`~oci.opsi.models.CreatePeComanagedDatabaseInsightDetails`

        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param entity_source:
            The value to assign to the entity_source property of this CreateDatabaseInsightDetails.
            Allowed values for this property are: "EM_MANAGED_EXTERNAL_DATABASE", "PE_COMANAGED_DATABASE", "MDS_MYSQL_DATABASE_SYSTEM", "EXTERNAL_MYSQL_DATABASE_SYSTEM", "MACS_MANAGED_CLOUD_DATABASE", "MACS_MANAGED_AUTONOMOUS_DATABASE"
        :type entity_source: str

        :param compartment_id:
            The value to assign to the compartment_id property of this CreateDatabaseInsightDetails.
        :type compartment_id: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this CreateDatabaseInsightDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this CreateDatabaseInsightDetails.
        :type defined_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'entity_source': 'str',
            'compartment_id': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))'
        }
        self.attribute_map = {
            'entity_source': 'entitySource',
            'compartment_id': 'compartmentId',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags'
        }
        self._entity_source = None
        self._compartment_id = None
        self._freeform_tags = None
        self._defined_tags = None

    @staticmethod
    def get_subtype(object_dictionary):
        """
        Given the hash representation of a subtype of this class,
        use the info in the hash to return the class of the subtype.
        """
        type = object_dictionary['entitySource']

        if type == 'MACS_MANAGED_CLOUD_DATABASE':
            return 'CreateMacsManagedCloudDatabaseInsightDetails'

        if type == 'EXTERNAL_MYSQL_DATABASE_SYSTEM':
            return 'CreateExternalMysqlDatabaseInsightDetails'

        if type == 'AUTONOMOUS_DATABASE':
            return 'CreateAutonomousDatabaseInsightDetails'

        if type == 'MACS_MANAGED_AUTONOMOUS_DATABASE':
            return 'CreateMacsManagedAutonomousDatabaseInsightDetails'

        if type == 'MDS_MYSQL_DATABASE_SYSTEM':
            return 'CreateMdsMySqlDatabaseInsightDetails'

        if type == 'EM_MANAGED_EXTERNAL_DATABASE':
            return 'CreateEmManagedExternalDatabaseInsightDetails'

        if type == 'PE_COMANAGED_DATABASE':
            return 'CreatePeComanagedDatabaseInsightDetails'
        else:
            return 'CreateDatabaseInsightDetails'

    @property
    def entity_source(self):
        """
        **[Required]** Gets the entity_source of this CreateDatabaseInsightDetails.
        Source of the database entity.

        Allowed values for this property are: "EM_MANAGED_EXTERNAL_DATABASE", "PE_COMANAGED_DATABASE", "MDS_MYSQL_DATABASE_SYSTEM", "EXTERNAL_MYSQL_DATABASE_SYSTEM", "MACS_MANAGED_CLOUD_DATABASE", "MACS_MANAGED_AUTONOMOUS_DATABASE"


        :return: The entity_source of this CreateDatabaseInsightDetails.
        :rtype: str
        """
        return self._entity_source

    @entity_source.setter
    def entity_source(self, entity_source):
        """
        Sets the entity_source of this CreateDatabaseInsightDetails.
        Source of the database entity.


        :param entity_source: The entity_source of this CreateDatabaseInsightDetails.
        :type: str
        """
        allowed_values = ["EM_MANAGED_EXTERNAL_DATABASE", "PE_COMANAGED_DATABASE", "MDS_MYSQL_DATABASE_SYSTEM", "EXTERNAL_MYSQL_DATABASE_SYSTEM", "MACS_MANAGED_CLOUD_DATABASE", "MACS_MANAGED_AUTONOMOUS_DATABASE"]
        if not value_allowed_none_or_none_sentinel(entity_source, allowed_values):
            raise ValueError(
                f"Invalid value for `entity_source`, must be None or one of {allowed_values}"
            )
        self._entity_source = entity_source

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this CreateDatabaseInsightDetails.
        Compartment Identifier of database


        :return: The compartment_id of this CreateDatabaseInsightDetails.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this CreateDatabaseInsightDetails.
        Compartment Identifier of database


        :param compartment_id: The compartment_id of this CreateDatabaseInsightDetails.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this CreateDatabaseInsightDetails.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :return: The freeform_tags of this CreateDatabaseInsightDetails.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this CreateDatabaseInsightDetails.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :param freeform_tags: The freeform_tags of this CreateDatabaseInsightDetails.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this CreateDatabaseInsightDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :return: The defined_tags of this CreateDatabaseInsightDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this CreateDatabaseInsightDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :param defined_tags: The defined_tags of this CreateDatabaseInsightDetails.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
