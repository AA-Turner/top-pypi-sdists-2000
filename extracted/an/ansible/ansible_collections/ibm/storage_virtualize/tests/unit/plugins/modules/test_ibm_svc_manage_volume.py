# Copyright (C) 2020 IBM CORPORATION
# Author(s): Sreshtant Bohidar <sreshtant.bohidar@ibm.com>
#
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

""" unit tests IBM Storage Virtualize Ansible module: ibm_svc_manage_volume """

from __future__ import (absolute_import, division, print_function)
__metaclass__ = type
import unittest
import pytest
import json
from mock import patch
from ansible.module_utils import basic
from ansible.module_utils._text import to_bytes
from ansible_collections.ibm.storage_virtualize.plugins.module_utils.ibm_svc_utils import IBMSVCRestApi
from ansible_collections.ibm.storage_virtualize.plugins.modules.ibm_svc_manage_volume import IBMSVCvolume


def set_module_args(args):
    """prepare arguments so that they will be picked up during module
    creation """
    args = json.dumps({'ANSIBLE_MODULE_ARGS': args})
    basic._ANSIBLE_ARGS = to_bytes(args)  # pylint: disable=protected-access


class AnsibleExitJson(Exception):
    """Exception class to be raised by module.exit_json and caught by the
    test case """
    pass


class AnsibleFailJson(Exception):
    """Exception class to be raised by module.fail_json and caught by the
    test case """
    pass


def exit_json(*args, **kwargs):  # pylint: disable=unused-argument
    """function to patch over exit_json; package return data into an
    exception """
    if 'changed' not in kwargs:
        kwargs['changed'] = False
    raise AnsibleExitJson(kwargs)


def fail_json(*args, **kwargs):  # pylint: disable=unused-argument
    """function to patch over fail_json; package return data into an
    exception """
    kwargs['failed'] = True
    raise AnsibleFailJson(kwargs)


class TestIBMSVCvolume(unittest.TestCase):
    """ a group of related Unit Tests"""

    @patch('ansible_collections.ibm.storage_virtualize.plugins.module_utils.'
           'ibm_svc_utils.IBMSVCRestApi._svc_authorize')
    def setUp(self, connect):
        self.mock_module_helper = patch.multiple(basic.AnsibleModule,
                                                 exit_json=exit_json,
                                                 fail_json=fail_json)
        self.mock_module_helper.start()
        self.addCleanup(self.mock_module_helper.stop)
        self.restapi = IBMSVCRestApi(self.mock_module_helper, '1.2.3.4',
                                     'domain.ibm.com', 'username', 'password',
                                     False, 'test.log', '')

    def set_default_args(self):
        return dict({
            'name': 'test',
            'state': 'present'
        })

    def test_module_fail_when_required_args_missing(self):
        """ required arguments are reported as errors """
        with pytest.raises(AnsibleFailJson) as exc:
            set_module_args({})
            IBMSVCvolume()
        print('Info: %s' % exc.value.args[0]['msg'])

    @patch('ansible_collections.ibm.storage_virtualize.plugins.module_utils.'
           'ibm_svc_utils.IBMSVCRestApi.svc_obj_info')
    @patch('ansible_collections.ibm.storage_virtualize.plugins.module_utils.'
           'ibm_svc_utils.IBMSVCRestApi._svc_authorize')
    def test_assemble_iogrp(self, svc_authorize_mock, svc_obj_info_mock):
        set_module_args({
            'clustername': 'clustername',
            'domain': 'domain',
            'state': 'present',
            'username': 'username',
            'password': 'password',
            'name': 'test_volume',
            'pool': 'test_pool',
            'size': '1',
            'unit': 'gb',
            'iogrp': 'io_grp0, io_grp1'
        })
        svc_obj_info_mock.return_value = [
            {
                "id": "0", "name": "io_grp0", "node_count": "2", "vdisk_count": "4",
                "host_count": "1", "site_id": "1", "site_name": "site1"
            }, {
                "id": "1", "name": "io_grp1", "node_count": "2", "vdisk_count": "0",
                "host_count": "1", "site_id": "2", "site_name": "site2"
            }, {
                "id": "2", "name": "io_grp2", "node_count": "0", "vdisk_count": "0",
                "host_count": "1", "site_id": "", "site_name": ""
            }, {
                "id": "3", "name": "io_grp3", "node_count": "0", "vdisk_count": "0",
                "host_count": "1", "site_id": "", "site_name": ""
            }, {
                "id": "4", "name": "recovery_io_grp", "node_count": "0", "vdisk_count": "0",
                "host_count": "0", "site_id": "", "site_name": ""
            }
        ]
        v = IBMSVCvolume()
        v.assemble_iogrp()
        self.assertTrue(isinstance(v.iogrp, list))

    @patch('ansible_collections.ibm.storage_virtualize.plugins.module_utils.'
           'ibm_svc_utils.IBMSVCRestApi.svc_obj_info')
    @patch('ansible_collections.ibm.storage_virtualize.plugins.module_utils.'
           'ibm_svc_utils.IBMSVCRestApi._svc_authorize')
    def test_failure_with_empty_or_nonexisting_iogrp(self, svc_authorize_mock, svc_obj_info_mock):
        set_module_args({
            'clustername': 'clustername',
            'domain': 'domain',
            'state': 'present',
            'username': 'username',
            'password': 'password',
            'name': 'test_volume',
            'pool': 'test_pool',
            'size': '1',
            'unit': 'gb',
            'iogrp': 'io_grp0, io_grp1, io_grp2, io_grp10'
        })
        svc_obj_info_mock.return_value = [
            {
                "id": "0", "name": "io_grp0", "node_count": "2", "vdisk_count": "4",
                "host_count": "1", "site_id": "1", "site_name": "site1"
            }, {
                "id": "1", "name": "io_grp1", "node_count": "2", "vdisk_count": "0",
                "host_count": "1", "site_id": "2", "site_name": "site2"
            }, {
                "id": "2", "name": "io_grp2", "node_count": "0", "vdisk_count": "0",
                "host_count": "1", "site_id": "", "site_name": ""
            }, {
                "id": "3", "name": "io_grp3", "node_count": "0", "vdisk_count": "0",
                "host_count": "1", "site_id": "", "site_name": ""
            }, {
                "id": "4", "name": "recovery_io_grp", "node_count": "0", "vdisk_count": "0",
                "host_count": "0", "site_id": "", "site_name": ""
            }
        ]
        v = IBMSVCvolume()
        with pytest.raises(AnsibleFailJson) as exc:
            v.assemble_iogrp()
            self.assertTrue(exc.value.args[0]['failed'])

    @patch('ansible_collections.ibm.storage_virtualize.plugins.module_utils.'
           'ibm_svc_utils.IBMSVCRestApi._svc_authorize')
    def test_mandatory_parameter_validation(self, svc_authorize_mock):
        set_module_args({
            'clustername': 'clustername',
            'domain': 'domain',
            'state': 'present',
            'username': 'username',
            'password': 'password',
            'name': 'test_volume',
            'pool': 'test_pool',
            'size': '1',
            'unit': 'gb',
            'iogrp': 'io_grp0, io_grp1'
        })
        v = IBMSVCvolume()
        v.mandatory_parameter_validation()

    @patch('ansible_collections.ibm.storage_virtualize.plugins.module_utils.'
           'ibm_svc_utils.IBMSVCRestApi._svc_authorize')
    def test_failure_when_mandatory_parameter_are_missing(self, svc_authorize_mock):
        set_module_args({
            'clustername': 'clustername',
            'domain': 'domain',
            'state': 'present',
            'username': 'username',
            'password': 'password',
            'pool': 'test_pool',
            'size': '1',
            'unit': 'gb',
            'iogrp': 'io_grp0, io_grp1'
        })
        with pytest.raises(AnsibleFailJson) as exc:
            v = IBMSVCvolume()
            v.mandatory_parameter_validation()
        self.assertTrue(exc.value.args[0]['failed'])

    @patch('ansible_collections.ibm.storage_virtualize.plugins.module_utils.'
           'ibm_svc_utils.IBMSVCRestApi._svc_authorize')
    def test_failure_when_both_parameter_volumegroup_and_novolumegroup_are_used(self, svc_authorize_mock):
        set_module_args({
            'clustername': 'clustername',
            'domain': 'domain',
            'state': 'present',
            'username': 'username',
            'password': 'password',
            'name': 'test_volume',
            'pool': 'test_pool',
            'size': '1',
            'unit': 'gb',
            'iogrp': 'io_grp0, io_grp1',
            'volumegroup': 'test_volumegroup',
            'novolumegroup': True
        })
        with pytest.raises(AnsibleFailJson) as exc:
            v = IBMSVCvolume()
            v.mandatory_parameter_validation()
        self.assertTrue(exc.value.args[0]['failed'])
        self.assertEqual(exc.value.args[0]['msg'], 'Mutually exclusive parameters detected: [volumegroup] and [novolumegroup]')

    @patch('ansible_collections.ibm.storage_virtualize.plugins.module_utils.'
           'ibm_svc_utils.IBMSVCRestApi._svc_authorize')
    def test_volume_creation_parameter_validation(self, svc_authorize_mock):
        set_module_args({
            'clustername': 'clustername',
            'domain': 'domain',
            'state': 'present',
            'username': 'username',
            'password': 'password',
            'name': 'test_volume',
            'pool': 'test_pool',
            'size': '1',
            'unit': 'gb',
            'iogrp': 'io_grp0, io_grp1',
            'volumegroup': 'test_volumegroup'
        })
        v = IBMSVCvolume()
        v.volume_creation_parameter_validation()

    @patch('ansible_collections.ibm.storage_virtualize.plugins.module_utils.'
           'ibm_svc_utils.IBMSVCRestApi._svc_authorize')
    def test_failure_when_volume_creation_parameter_are_missing(self, svc_authorize_mock):
        set_module_args({
            'clustername': 'clustername',
            'domain': 'domain',
            'state': 'present',
            'username': 'username',
            'password': 'password',
            'name': 'test_volume',
            'iogrp': 'io_grp0, io_grp1',
            'volumegroup': 'test_volumegroup'
        })
        with pytest.raises(AnsibleFailJson) as exc:
            v = IBMSVCvolume()
            v.volume_creation_parameter_validation()
        self.assertTrue(exc.value.args[0]['failed'])

    @patch('ansible_collections.ibm.storage_virtualize.plugins.module_utils.'
           'ibm_svc_utils.IBMSVCRestApi._svc_authorize')
    def test_validate_volume_type(self, svc_authorize_mock):
        set_module_args({
            'clustername': 'clustername',
            'domain': 'domain',
            'state': 'present',
            'username': 'username',
            'password': 'password',
            'name': 'test_volume',
            'pool': 'test_pool',
            'size': '1',
            'unit': 'gb',
            'iogrp': 'io_grp0, io_grp1',
            'volumegroup': 'test_volumegroup'
        })
        data = [
            {
                "id": "24", "name": "test_volume", "IO_group_id": "0", "IO_group_name": "io_grp0", "status": "online",
                "mdisk_grp_id": "2", "mdisk_grp_name": "site1pool1", "capacity": "1073741824", "type": "striped",
                "formatted": "yes", "formatting": "no", "mdisk_id": "", "mdisk_name": "", "FC_id": "", "FC_name": "",
                "RC_id": "", "RC_name": "", "vdisk_UID": "60050768108180ED700000000000002E", "preferred_node_id": "1",
                "fast_write_state": "empty", "cache": "readwrite", "udid": "", "fc_map_count": "0", "sync_rate": "50",
                "copy_count": "1", "se_copy_count": "0", "filesystem": "", "mirror_write_priority": "latency",
                "RC_change": "no", "compressed_copy_count": "0", "access_IO_group_count": "2", "last_access_time": "",
                "parent_mdisk_grp_id": "2", "parent_mdisk_grp_name": "site1pool1", "owner_type": "none", "owner_id": "",
                "owner_name": "", "encrypt": "no", "volume_id": "24", "volume_name": "test_volume", "function": "", "throttle_id": "",
                "throttle_name": "", "IOPs_limit": "", "bandwidth_limit_MB": "", "volume_group_id": "0",
                "volume_group_name": "test_volumegroup", "cloud_backup_enabled": "no", "cloud_account_id": "",
                "cloud_account_name": "", "backup_status": "off", "last_backup_time": "", "restore_status": "none",
                "backup_grain_size": "", "deduplicated_copy_count": "0", "protocol": "", "preferred_node_name": "node1",
                "safeguarded_expiration_time": "", "safeguarded_backup_count": "0"
            }, {
                "copy_id": "0", "status": "online",
                "sync": "yes", "auto_delete": "no", "primary": "yes", "mdisk_grp_id": "2", "mdisk_grp_name": "site1pool1",
                "type": "striped", "mdisk_id": "", "mdisk_name": "", "fast_write_state": "empty", "used_capacity": "1073741824",
                "real_capacity": "1073741824", "free_capacity": "0", "overallocation": "100", "autoexpand": "", "warning": "",
                "grainsize": "", "se_copy": "no", "easy_tier": "on", "easy_tier_status": "balanced", "tiers": [
                    {"tier": "tier_scm", "tier_capacity": "0"},
                    {"tier": "tier0_flash", "tier_capacity": "1073741824"},
                    {"tier": "tier1_flash", "tier_capacity": "0"},
                    {"tier": "tier_enterprise", "tier_capacity": "0"},
                    {"tier": "tier_nearline", "tier_capacity": "0"}
                ], "compressed_copy": "no", "uncompressed_used_capacity": "1073741824", "parent_mdisk_grp_id": "2",
                "parent_mdisk_grp_name": "site1pool1", "encrypt": "no", "deduplicated_copy": "no",
                "used_capacity_before_reduction": "", "safeguarded_mdisk_grp_id": "", "safeguarded_mdisk_grp_name": ""
            }
        ]
        v = IBMSVCvolume()
        v.validate_volume_type(data)

    @patch('ansible_collections.ibm.storage_virtualize.plugins.module_utils.'
           'ibm_svc_utils.IBMSVCRestApi._svc_authorize')
    def test_failure_for_unsupported_volume_type(self, svc_authorize_mock):
        set_module_args({
            'clustername': 'clustername',
            'domain': 'domain',
            'state': 'present',
            'username': 'username',
            'password': 'password',
            'name': 'test_volume',
            'pool': 'test_pool',
            'size': '1',
            'unit': 'gb',
            'iogrp': 'io_grp0, io_grp1',
            'volumegroup': 'test_volumegroup'
        })
        data = [
            {
                "id": "26", "name": "abc", "IO_group_id": "0", "IO_group_name": "io_grp0", "status": "online",
                "mdisk_grp_id": "2", "mdisk_grp_name": "site1pool1", "capacity": "1073741824", "type": "striped",
                "formatted": "yes", "formatting": "no", "mdisk_id": "", "mdisk_name": "", "FC_id": "", "FC_name": "",
                "RC_id": "26", "RC_name": "rcrel7", "vdisk_UID": "60050768108180ED700000000000002D",
                "preferred_node_id": "2", "fast_write_state": "empty", "cache": "readwrite", "udid": "",
                "fc_map_count": "0", "sync_rate": "50", "copy_count": "1", "se_copy_count": "0", "filesystem": "",
                "mirror_write_priority": "latency", "RC_change": "no", "compressed_copy_count": "0",
                "access_IO_group_count": "2", "last_access_time": "", "parent_mdisk_grp_id": "2",
                "parent_mdisk_grp_name": "site1pool1", "owner_type": "none", "owner_id": "", "owner_name": "", "encrypt": "no",
                "volume_id": "26", "volume_name": "abc", "function": "master", "throttle_id": "", "throttle_name": "",
                "IOPs_limit": "", "bandwidth_limit_MB": "", "volume_group_id": "0", "volume_group_name": "test_volumegroup",
                "cloud_backup_enabled": "no", "cloud_account_id": "", "cloud_account_name": "", "backup_status": "off",
                "last_backup_time": "", "restore_status": "none", "backup_grain_size": "", "deduplicated_copy_count": "0",
                "protocol": "", "preferred_node_name": "node2", "safeguarded_expiration_time": "",
                "safeguarded_backup_count": "0"
            },
            {
                "copy_id": "0", "status": "online", "sync": "yes", "auto_delete": "no",
                "primary": "yes", "mdisk_grp_id": "2", "mdisk_grp_name": "site1pool1", "type": "striped", "mdisk_id": "",
                "mdisk_name": "", "fast_write_state": "empty", "used_capacity": "1073741824", "real_capacity": "1073741824",
                "free_capacity": "0", "overallocation": "100", "autoexpand": "", "warning": "", "grainsize": "", "se_copy": "no",
                "easy_tier": "on", "easy_tier_status": "balanced", "tiers": [
                    {"tier": "tier_scm", "tier_capacity": "0"},
                    {"tier": "tier0_flash", "tier_capacity": "1073741824"},
                    {"tier": "tier1_flash", "tier_capacity": "0"},
                    {"tier": "tier_enterprise", "tier_capacity": "0"},
                    {"tier": "tier_nearline", "tier_capacity": "0"}
                ], "compressed_copy": "no", "uncompressed_used_capacity": "1073741824", "parent_mdisk_grp_id": "2",
                "parent_mdisk_grp_name": "site1pool1", "encrypt": "no", "deduplicated_copy": "no",
                "used_capacity_before_reduction": "", "safeguarded_mdisk_grp_id": "", "safeguarded_mdisk_grp_name": ""
            }
        ]
        with pytest.raises(AnsibleFailJson) as exc:
            v = IBMSVCvolume()
            v.validate_volume_type(data)
        self.assertTrue(exc.value.args[0]['failed'])

    @patch('ansible_collections.ibm.storage_virtualize.plugins.module_utils.'
           'ibm_svc_utils.IBMSVCRestApi.svc_obj_info')
    @patch('ansible_collections.ibm.storage_virtualize.plugins.module_utils.'
           'ibm_svc_utils.IBMSVCRestApi._svc_authorize')
    def test_get_existing_volume(self, svc_authorize_mock, svc_obj_info_mock):
        set_module_args({
            'clustername': 'clustername',
            'domain': 'domain',
            'state': 'present',
            'username': 'username',
            'password': 'password',
            'name': 'test_volume',
            'pool': 'test_pool',
            'size': '1',
            'unit': 'gb',
            'iogrp': 'io_grp0, io_grp1',
            'volumegroup': 'test_volumegroup'
        })
        svc_obj_info_mock.return_value = [
            {
                "id": "24", "name": "test_volume", "IO_group_id": "0", "IO_group_name": "io_grp0", "status": "online",
                "mdisk_grp_id": "2", "mdisk_grp_name": "site1pool1", "capacity": "1073741824", "type": "striped",
                "formatted": "yes", "formatting": "no", "mdisk_id": "", "mdisk_name": "", "FC_id": "", "FC_name": "",
                "RC_id": "", "RC_name": "", "vdisk_UID": "60050768108180ED700000000000002E", "preferred_node_id": "1",
                "fast_write_state": "empty", "cache": "readwrite", "udid": "", "fc_map_count": "0", "sync_rate": "50",
                "copy_count": "1", "se_copy_count": "0", "filesystem": "", "mirror_write_priority": "latency",
                "RC_change": "no", "compressed_copy_count": "0", "access_IO_group_count": "2", "last_access_time": "",
                "parent_mdisk_grp_id": "2", "parent_mdisk_grp_name": "site1pool1", "owner_type": "none", "owner_id": "",
                "owner_name": "", "encrypt": "no", "volume_id": "24", "volume_name": "test_volume", "function": "", "throttle_id": "",
                "throttle_name": "", "IOPs_limit": "", "bandwidth_limit_MB": "", "volume_group_id": "0",
                "volume_group_name": "test_volumegroup", "cloud_backup_enabled": "no", "cloud_account_id": "",
                "cloud_account_name": "", "backup_status": "off", "last_backup_time": "", "restore_status": "none",
                "backup_grain_size": "", "deduplicated_copy_count": "0", "protocol": "", "preferred_node_name": "node1",
                "safeguarded_expiration_time": "", "safeguarded_backup_count": "0"
            }, {
                "copy_id": "0", "status": "online",
                "sync": "yes", "auto_delete": "no", "primary": "yes", "mdisk_grp_id": "2", "mdisk_grp_name": "site1pool1",
                "type": "striped", "mdisk_id": "", "mdisk_name": "", "fast_write_state": "empty", "used_capacity": "1073741824",
                "real_capacity": "1073741824", "free_capacity": "0", "overallocation": "100", "autoexpand": "", "warning": "",
                "grainsize": "", "se_copy": "no", "easy_tier": "on", "easy_tier_status": "balanced", "tiers": [
                    {"tier": "tier_scm", "tier_capacity": "0"},
                    {"tier": "tier0_flash", "tier_capacity": "1073741824"},
                    {"tier": "tier1_flash", "tier_capacity": "0"},
                    {"tier": "tier_enterprise", "tier_capacity": "0"},
                    {"tier": "tier_nearline", "tier_capacity": "0"}
                ], "compressed_copy": "no", "uncompressed_used_capacity": "1073741824", "parent_mdisk_grp_id": "2",
                "parent_mdisk_grp_name": "site1pool1", "encrypt": "no", "deduplicated_copy": "no",
                "used_capacity_before_reduction": "", "safeguarded_mdisk_grp_id": "", "safeguarded_mdisk_grp_name": ""
            }
        ]
        v = IBMSVCvolume()
        data = v.get_existing_volume('test_volume')
        self.assertEqual(data[0]['name'], 'test_volume')

    @patch('ansible_collections.ibm.storage_virtualize.plugins.module_utils.'
           'ibm_svc_utils.IBMSVCRestApi.svc_obj_info')
    @patch('ansible_collections.ibm.storage_virtualize.plugins.module_utils.'
           'ibm_svc_utils.IBMSVCRestApi._svc_authorize')
    def test_get_existing_iogrp(self, svc_authorize_mock, svc_obj_info_mock):
        set_module_args({
            'clustername': 'clustername',
            'domain': 'domain',
            'state': 'present',
            'username': 'username',
            'password': 'password',
            'name': 'test_volume',
            'pool': 'test_pool',
            'size': '1',
            'unit': 'gb',
            'iogrp': 'io_grp0, io_grp1',
            'volumegroup': 'test_volumegroup'
        })
        svc_obj_info_mock.return_value = [
            {
                "vdisk_id": "24",
                "vdisk_name": "test_volume",
                "IO_group_id": "0",
                "IO_group_name": "io_grp0"
            },
            {
                "vdisk_id": "24",
                "vdisk_name": "test_volume",
                "IO_group_id": "1",
                "IO_group_name": "io_grp1"
            }
        ]
        v = IBMSVCvolume()
        data = v.get_existing_iogrp()
        self.assertTrue('io_grp0' in data)
        self.assertTrue('io_grp1' in data)

    @patch('ansible_collections.ibm.storage_virtualize.plugins.module_utils.'
           'ibm_svc_utils.IBMSVCRestApi.svc_run_command')
    @patch('ansible_collections.ibm.storage_virtualize.plugins.module_utils.'
           'ibm_svc_utils.IBMSVCRestApi._svc_authorize')
    def test_create_volume(self, svc_authorize_mock, svc_run_command_mock):
        set_module_args({
            'clustername': 'clustername',
            'domain': 'domain',
            'state': 'present',
            'username': 'username',
            'password': 'password',
            'name': 'test_volume',
            'pool': 'test_pool',
            'size': '1',
            'unit': 'gb',
            'iogrp': 'io_grp0, io_grp1',
            'volumegroup': 'test_volumegroup'
        })
        svc_run_command_mock.return_value = {
            'id': '25',
            'message': 'Volume, id [25], successfully created'
        }
        v = IBMSVCvolume()
        v.create_volume()

    @patch('ansible_collections.ibm.storage_virtualize.plugins.module_utils.'
           'ibm_svc_utils.IBMSVCRestApi._svc_authorize')
    def test_failure_volume_state_present_with_unmap(self, svc_authorize_mock):
        """
        Parameter [unmap] cannot be specified when creating or updating a volume.
        """
        set_module_args({
            'clustername': 'clustername',
            'domain': 'domain',
            'username': 'username',
            'password': 'password',
            'name': 'test_volume',
            'novolumegroup': True,
            'state': 'present',
            'unmap': ['host_mappings']
        })

        with pytest.raises(AnsibleFailJson) as exc:
            v = IBMSVCvolume()
            v.apply()
        self.assertTrue(exc.value.args[0]['failed'])
        self.assertEqual(exc.value.args[0]['msg'], 'Parameter [unmap] cannot be specified when creating or updating a volume.')

    @patch('ansible_collections.ibm.storage_virtualize.plugins.module_utils.'
           'ibm_svc_utils.IBMSVCRestApi.svc_run_command')
    @patch('ansible_collections.ibm.storage_virtualize.plugins.module_utils.'
           'ibm_svc_utils.IBMSVCRestApi._svc_authorize')
    def test_remove_volume(self, svc_authorize_mock, svc_run_command_mock):
        set_module_args({
            'clustername': 'clustername',
            'domain': 'domain',
            'state': 'absent',
            'username': 'username',
            'password': 'password',
            'name': 'test_volume'
        })
        svc_run_command_mock.return_value = None
        v = IBMSVCvolume()
        v.remove_volume()

    @patch('ansible_collections.ibm.storage_virtualize.plugins.module_utils.'
           'ibm_svc_utils.IBMSVCRestApi.svc_run_command')
    @patch('ansible_collections.ibm.storage_virtualize.plugins.module_utils.'
           'ibm_svc_utils.IBMSVCRestApi.svc_obj_info')
    @patch('ansible_collections.ibm.storage_virtualize.plugins.module_utils.'
           'ibm_svc_utils.IBMSVCRestApi._svc_authorize')
    def test_remove_volume_with_unmap(self,
                                      svc_authorize_mock,
                                      svc_obj_info_mock,
                                      svc_run_command_mock):
        """
        Remove a volume and unmap it from host mappings, remote copy relationships, and flashcopy mappings.
        """
        set_module_args({
            'clustername': 'clustername',
            'domain': 'domain',
            'username': 'username',
            'password': 'password',
            'name': 'test_volume',
            'state': 'absent',
            'unmap': ['host_mappings', 'remotecopy_relationships', 'flashcopy_mappings']
        })
        svc_obj_info_mock.return_value = [  # lsvdisk detailed mock object
            {
                "name:": "test_volume",
                "type": "striped",
                "RC_name": ""
            },
            {}
        ]
        with pytest.raises(AnsibleExitJson) as exc:
            v = IBMSVCvolume()
            v.apply()
        self.assertTrue(exc.value.args[0]['changed'])
        self.assertEqual(exc.value.args[0]['msg'], 'volume [test_volume] has been deleted.')

    @patch('ansible_collections.ibm.storage_virtualize.plugins.module_utils.'
           'ibm_svc_utils.IBMSVCRestApi._svc_authorize')
    def test_failure_remove_volume_with_invalid_params(self, svc_authorize_mock):
        set_module_args({
            'clustername': 'clustername',
            'domain': 'domain',
            'username': 'username',
            'password': 'password',
            'name': 'test_volume',
            'pool': 'test_pool',
            'size': '1',
            'unit': 'gb',
            'iogrp': 'io_grp0, io_grp1',
            'volumegroup': 'test_volumegroup',
            'state': 'absent'
        })
        with pytest.raises(AnsibleFailJson) as exc:
            v = IBMSVCvolume()
            v.apply()
        self.assertTrue(exc.value.args[0]['failed'])

    @patch('ansible_collections.ibm.storage_virtualize.plugins.module_utils.'
           'ibm_svc_utils.IBMSVCRestApi._svc_authorize')
    def test_convert_to_bytes(self, svc_authorize_mock):
        set_module_args({
            'clustername': 'clustername',
            'domain': 'domain',
            'state': 'absent',
            'username': 'username',
            'password': 'password',
            'name': 'test_volume',
            'pool': 'test_pool',
            'size': '1',
            'unit': 'gb',
            'iogrp': 'io_grp0, io_grp1',
            'volumegroup': 'test_volumegroup'
        })

        v = IBMSVCvolume()
        size_in_bytes = v.convert_to_bytes()
        self.assertEqual(size_in_bytes, 1073741824)

    @patch('ansible_collections.ibm.storage_virtualize.plugins.module_utils.'
           'ibm_svc_utils.IBMSVCRestApi.svc_obj_info')
    @patch('ansible_collections.ibm.storage_virtualize.plugins.module_utils.'
           'ibm_svc_utils.IBMSVCRestApi._svc_authorize')
    def test_probe_volume(self, svc_authorize_mock, svc_obj_info_mock):
        set_module_args({
            'clustername': 'clustername',
            'domain': 'domain',
            'state': 'absent',
            'username': 'username',
            'password': 'password',
            'name': 'test_volume',
            'pool': 'test_pool',
            'size': '1',
            'unit': 'gb',
            'iogrp': 'io_grp0',
            'volumegroup': 'test_volumegroup'
        })
        svc_obj_info_mock.return_value = [
            {
                "vdisk_id": "24",
                "vdisk_name": "test_volume",
                "IO_group_id": "0",
                "IO_group_name": "io_grp0"
            },
            {
                "vdisk_id": "24",
                "vdisk_name": "test_volume",
                "IO_group_id": "1",
                "IO_group_name": "io_grp1"
            }
        ]
        data = [
            {
                "id": "24", "name": "test_volume", "IO_group_id": "0", "IO_group_name": "io_grp0", "status": "online",
                "mdisk_grp_id": "2", "mdisk_grp_name": "site1pool1", "capacity": "100000000", "type": "striped",
                "formatted": "yes", "formatting": "no", "mdisk_id": "", "mdisk_name": "", "FC_id": "", "FC_name": "",
                "RC_id": "", "RC_name": "", "vdisk_UID": "60050768108180ED700000000000002E", "preferred_node_id": "1",
                "fast_write_state": "empty", "cache": "readwrite", "udid": "", "fc_map_count": "0", "sync_rate": "50",
                "copy_count": "1", "se_copy_count": "0", "filesystem": "", "mirror_write_priority": "latency",
                "RC_change": "no", "compressed_copy_count": "0", "access_IO_group_count": "2", "last_access_time": "",
                "parent_mdisk_grp_id": "2", "parent_mdisk_grp_name": "site1pool1", "owner_type": "none", "owner_id": "",
                "owner_name": "", "encrypt": "no", "volume_id": "24", "volume_name": "test_volume", "function": "", "throttle_id": "",
                "throttle_name": "", "IOPs_limit": "", "bandwidth_limit_MB": "", "volume_group_id": "0",
                "volume_group_name": "test_volumegroup2", "cloud_backup_enabled": "no", "cloud_account_id": "",
                "cloud_account_name": "", "backup_status": "off", "last_backup_time": "", "restore_status": "none",
                "backup_grain_size": "", "deduplicated_copy_count": "0", "protocol": "", "preferred_node_name": "node1",
                "safeguarded_expiration_time": "", "safeguarded_backup_count": "0"
            }, {
                "copy_id": "0", "status": "online",
                "sync": "yes", "auto_delete": "no", "primary": "yes", "mdisk_grp_id": "2", "mdisk_grp_name": "site1pool1",
                "type": "striped", "mdisk_id": "", "mdisk_name": "", "fast_write_state": "empty", "used_capacity": "1073741824",
                "real_capacity": "1073741824", "free_capacity": "0", "overallocation": "100", "autoexpand": "", "warning": "",
                "grainsize": "", "se_copy": "no", "easy_tier": "on", "easy_tier_status": "balanced", "tiers": [
                    {"tier": "tier_scm", "tier_capacity": "0"},
                    {"tier": "tier0_flash", "tier_capacity": "1073741824"},
                    {"tier": "tier1_flash", "tier_capacity": "0"},
                    {"tier": "tier_enterprise", "tier_capacity": "0"},
                    {"tier": "tier_nearline", "tier_capacity": "0"}
                ], "compressed_copy": "no", "uncompressed_used_capacity": "1073741824", "parent_mdisk_grp_id": "2",
                "parent_mdisk_grp_name": "site1pool1", "encrypt": "no", "deduplicated_copy": "no",
                "used_capacity_before_reduction": "", "safeguarded_mdisk_grp_id": "", "safeguarded_mdisk_grp_name": ""
            }
        ]
        v = IBMSVCvolume()
        probe_data = v.probe_volume(data)
        self.assertTrue('size' in probe_data)
        self.assertTrue('iogrp' in probe_data)
        self.assertTrue('volumegroup' in probe_data)

    @patch('ansible_collections.ibm.storage_virtualize.plugins.module_utils.'
           'ibm_svc_utils.IBMSVCRestApi.svc_run_command')
    @patch('ansible_collections.ibm.storage_virtualize.plugins.module_utils.'
           'ibm_svc_utils.IBMSVCRestApi._svc_authorize')
    def test_expand_volume(self, svc_authorize_mock, svc_run_command_mock):
        set_module_args({
            'clustername': 'clustername',
            'domain': 'domain',
            'state': 'absent',
            'username': 'username',
            'password': 'password',
            'name': 'test_volume',
            'pool': 'test_pool',
            'size': '1',
            'unit': 'gb',
            'iogrp': 'io_grp0, io_grp1',
            'volumegroup': 'test_volumegroup'
        })
        svc_run_command_mock.return_value = None
        v = IBMSVCvolume()
        v.expand_volume(973741824)

    @patch('ansible_collections.ibm.storage_virtualize.plugins.module_utils.'
           'ibm_svc_utils.IBMSVCRestApi.svc_run_command')
    @patch('ansible_collections.ibm.storage_virtualize.plugins.module_utils.'
           'ibm_svc_utils.IBMSVCRestApi._svc_authorize')
    def test_shrink_volume(self, svc_authorize_mock, svc_run_command_mock):
        set_module_args({
            'clustername': 'clustername',
            'domain': 'domain',
            'state': 'absent',
            'username': 'username',
            'password': 'password',
            'name': 'test_volume',
            'pool': 'test_pool',
            'size': '1',
            'unit': 'gb',
            'iogrp': 'io_grp0, io_grp1',
            'volumegroup': 'test_volumegroup'
        })
        svc_run_command_mock.return_value = None
        v = IBMSVCvolume()
        v.shrink_volume(973790)

    @patch('ansible_collections.ibm.storage_virtualize.plugins.module_utils.'
           'ibm_svc_utils.IBMSVCRestApi.svc_run_command')
    @patch('ansible_collections.ibm.storage_virtualize.plugins.module_utils.'
           'ibm_svc_utils.IBMSVCRestApi._svc_authorize')
    def test_add_iogrp(self, svc_authorize_mock, svc_run_command_mock):
        set_module_args({
            'clustername': 'clustername',
            'domain': 'domain',
            'state': 'absent',
            'username': 'username',
            'password': 'password',
            'name': 'test_volume',
            'pool': 'test_pool',
            'size': '1',
            'unit': 'gb',
            'iogrp': 'io_grp0',
            'volumegroup': 'test_volumegroup'
        })
        svc_run_command_mock.return_value = None
        v = IBMSVCvolume()
        v.add_iogrp(['io_grp1', 'io_grp2'])

    @patch('ansible_collections.ibm.storage_virtualize.plugins.module_utils.'
           'ibm_svc_utils.IBMSVCRestApi.svc_run_command')
    @patch('ansible_collections.ibm.storage_virtualize.plugins.module_utils.'
           'ibm_svc_utils.IBMSVCRestApi._svc_authorize')
    def test_remove_iogrp(self, svc_authorize_mock, svc_run_command_mock):
        set_module_args({
            'clustername': 'clustername',
            'domain': 'domain',
            'state': 'absent',
            'username': 'username',
            'password': 'password',
            'name': 'test_volume',
            'pool': 'test_pool',
            'size': '1',
            'unit': 'gb',
            'iogrp': 'io_grp0',
            'volumegroup': 'test_volumegroup'
        })
        svc_run_command_mock.return_value = None
        v = IBMSVCvolume()
        v.remove_iogrp(['io_grp1'])

    @patch('ansible_collections.ibm.storage_virtualize.plugins.module_utils.'
           'ibm_svc_utils.IBMSVCRestApi.svc_run_command')
    @patch('ansible_collections.ibm.storage_virtualize.plugins.module_utils.'
           'ibm_svc_utils.IBMSVCRestApi.svc_run_command')
    @patch('ansible_collections.ibm.storage_virtualize.plugins.module_utils.'
           'ibm_svc_utils.IBMSVCRestApi.svc_run_command')
    @patch('ansible_collections.ibm.storage_virtualize.plugins.module_utils.'
           'ibm_svc_utils.IBMSVCRestApi._svc_authorize')
    def test_update_volume(self, svc_authorize_mock, srcm1, srcm2, srcm3):
        set_module_args({
            'clustername': 'clustername',
            'domain': 'domain',
            'state': 'absent',
            'username': 'username',
            'password': 'password',
            'name': 'test_volume',
            'pool': 'test_pool',
            'size': '1',
            'unit': 'gb',
            'iogrp': 'io_grp0',
            'volumegroup': 'test_volumegroup2'
        })
        modify = {
            "iogrp": {
                "remove": [
                    "io_grp1",
                    "io_grp0"
                ]
            },
            "size": {
                "expand": 973741824
            },
            "volumegroup": {
                "name": "test_volumegroup2"
            }
        }
        srcm1.return_value = None
        srcm2.return_value = None
        srcm3.return_value = None
        v = IBMSVCvolume()
        v.update_volume(modify)

    @patch('ansible_collections.ibm.storage_virtualize.plugins.module_utils.'
           'ibm_svc_utils.IBMSVCRestApi._svc_authorize')
    def test_module_with_for_missing_name_parameter(self, svc_authorize_mock):
        set_module_args({
            'clustername': 'clustername',
            'domain': 'domain',
            'state': 'absent',
            'username': 'username',
            'password': 'password',
            'pool': 'test_pool',
            'size': '1',
            'unit': 'gb',
            'iogrp': 'io_grp0',
            'volumegroup': 'test_volumegroup'
        })
        with pytest.raises(AnsibleFailJson) as exc:
            v = IBMSVCvolume()
            v.apply()
        self.assertTrue(exc.value.args[0]['failed'])

    @patch('ansible_collections.ibm.storage_virtualize.plugins.module_utils.'
           'ibm_svc_utils.IBMSVCRestApi._svc_authorize')
    def test_module_with_missing_pool_parameter_while_creating_volume(self, svc_authorize_mock):
        set_module_args({
            'clustername': 'clustername',
            'domain': 'domain',
            'state': 'absent',
            'username': 'username',
            'password': 'password',
            'name': 'test_volume',
            'size': '1',
            'unit': 'gb',
            'iogrp': 'io_grp0',
            'volumegroup': 'test_volumegroup'
        })
        with pytest.raises(AnsibleFailJson) as exc:
            v = IBMSVCvolume()
            v.apply()
        self.assertTrue(exc.value.args[0]['failed'])

    @patch('ansible_collections.ibm.storage_virtualize.plugins.module_utils.'
           'ibm_svc_utils.IBMSVCRestApi.svc_run_command')
    @patch('ansible_collections.ibm.storage_virtualize.plugins.modules.'
           'ibm_svc_manage_volume.IBMSVCvolume.get_existing_volume')
    @patch('ansible_collections.ibm.storage_virtualize.plugins.modules.'
           'ibm_svc_manage_volume.IBMSVCvolume.assemble_iogrp')
    @patch('ansible_collections.ibm.storage_virtualize.plugins.modules.'
           'ibm_svc_manage_volume.IBMSVCvolume.mandatory_parameter_validation')
    @patch('ansible_collections.ibm.storage_virtualize.plugins.module_utils.'
           'ibm_svc_utils.IBMSVCRestApi._svc_authorize')
    def test_module_for_creating_new_volume(self, auth_mock, c1, c2, c3, c4):
        set_module_args({
            'clustername': 'clustername',
            'domain': 'domain',
            'username': 'username',
            'password': 'password',
            'name': 'test_volume',
            'state': 'present',
            'size': '1',
            'unit': 'gb',
            'pool': 'test_pool',
            'iogrp': 'io_grp0, io_grp1',
        })
        c3.return_value = []
        c4.return_value = {
            'id': '25',
            'message': 'Volume, id [25], successfully created'
        }
        with pytest.raises(AnsibleExitJson) as exc:
            v = IBMSVCvolume()
            v.apply()
        self.assertTrue(exc.value.args[0]['changed'])

    @patch('ansible_collections.ibm.storage_virtualize.plugins.module_utils.'
           'ibm_svc_utils.IBMSVCRestApi.svc_run_command')
    @patch('ansible_collections.ibm.storage_virtualize.plugins.modules.'
           'ibm_svc_manage_volume.IBMSVCvolume.get_existing_volume')
    @patch('ansible_collections.ibm.storage_virtualize.plugins.modules.'
           'ibm_svc_manage_volume.IBMSVCvolume.assemble_iogrp')
    @patch('ansible_collections.ibm.storage_virtualize.plugins.modules.'
           'ibm_svc_manage_volume.IBMSVCvolume.mandatory_parameter_validation')
    @patch('ansible_collections.ibm.storage_virtualize.plugins.module_utils.'
           'ibm_svc_utils.IBMSVCRestApi._svc_authorize')
    def test_module_for_creating_an_existing_volume(self, auth_mock, c1, c2, c3, c4):
        set_module_args({
            'clustername': 'clustername',
            'domain': 'domain',
            'username': 'username',
            'password': 'password',
            'name': 'test_volume',
            'state': 'present',
            'size': '1',
            'unit': 'gb',
            'pool': 'site1pool1',
        })
        c3.return_value = [
            {
                "id": "24", "name": "test_volume", "IO_group_id": "0", "IO_group_name": "io_grp0", "status": "online",
                "mdisk_grp_id": "2", "mdisk_grp_name": "site1pool1", "capacity": "1073741824", "type": "striped",
                "formatted": "yes", "formatting": "no", "mdisk_id": "", "mdisk_name": "", "FC_id": "", "FC_name": "",
                "RC_id": "", "RC_name": "", "vdisk_UID": "60050768108180ED700000000000002E", "preferred_node_id": "1",
                "fast_write_state": "empty", "cache": "readwrite", "udid": "", "fc_map_count": "0", "sync_rate": "50",
                "copy_count": "1", "se_copy_count": "0", "filesystem": "", "mirror_write_priority": "latency",
                "RC_change": "no", "compressed_copy_count": "0", "access_IO_group_count": "2", "last_access_time": "",
                "parent_mdisk_grp_id": "2", "parent_mdisk_grp_name": "site1pool1", "owner_type": "none", "owner_id": "",
                "owner_name": "", "encrypt": "no", "volume_id": "24", "volume_name": "test_volume", "function": "", "throttle_id": "",
                "throttle_name": "", "IOPs_limit": "", "bandwidth_limit_MB": "", "volume_group_id": "0",
                "volume_group_name": "test_volumegroup", "cloud_backup_enabled": "no", "cloud_account_id": "",
                "cloud_account_name": "", "backup_status": "off", "last_backup_time": "", "restore_status": "none",
                "backup_grain_size": "", "deduplicated_copy_count": "0", "protocol": "", "preferred_node_name": "node1",
                "safeguarded_expiration_time": "", "safeguarded_backup_count": "0"
            }, {
                "copy_id": "0", "status": "online",
                "sync": "yes", "auto_delete": "no", "primary": "yes", "mdisk_grp_id": "2", "mdisk_grp_name": "site1pool1",
                "type": "striped", "mdisk_id": "", "mdisk_name": "", "fast_write_state": "empty", "used_capacity": "1073741824",
                "real_capacity": "1073741824", "free_capacity": "0", "overallocation": "100", "autoexpand": "", "warning": "",
                "grainsize": "", "se_copy": "no", "easy_tier": "on", "easy_tier_status": "balanced", "tiers": [
                    {"tier": "tier_scm", "tier_capacity": "0"},
                    {"tier": "tier0_flash", "tier_capacity": "1073741824"},
                    {"tier": "tier1_flash", "tier_capacity": "0"},
                    {"tier": "tier_enterprise", "tier_capacity": "0"},
                    {"tier": "tier_nearline", "tier_capacity": "0"}
                ], "compressed_copy": "no", "uncompressed_used_capacity": "1073741824", "parent_mdisk_grp_id": "2",
                "parent_mdisk_grp_name": "site1pool1", "encrypt": "no", "deduplicated_copy": "no",
                "used_capacity_before_reduction": "", "safeguarded_mdisk_grp_id": "", "safeguarded_mdisk_grp_name": ""
            }
        ]
        c4.return_value = {
            'id': '25',
            'message': 'Volume, id [25], successfully created'
        }
        with pytest.raises(AnsibleExitJson) as exc:
            v = IBMSVCvolume()
            v.apply()
        self.assertFalse(exc.value.args[0]['changed'])

    @patch('ansible_collections.ibm.storage_virtualize.plugins.module_utils.'
           'ibm_svc_utils.IBMSVCRestApi.svc_run_command')
    @patch('ansible_collections.ibm.storage_virtualize.plugins.modules.'
           'ibm_svc_manage_volume.IBMSVCvolume.get_existing_volume')
    @patch('ansible_collections.ibm.storage_virtualize.plugins.modules.'
           'ibm_svc_manage_volume.IBMSVCvolume.assemble_iogrp')
    @patch('ansible_collections.ibm.storage_virtualize.plugins.modules.'
           'ibm_svc_manage_volume.IBMSVCvolume.mandatory_parameter_validation')
    @patch('ansible_collections.ibm.storage_virtualize.plugins.module_utils.'
           'ibm_svc_utils.IBMSVCRestApi._svc_authorize')
    def test_module_for_deleting_an_existing_volume(self, auth_mock, c1, c2, c3, c4):
        set_module_args({
            'clustername': 'clustername',
            'domain': 'domain',
            'username': 'username',
            'password': 'password',
            'name': 'test_volume',
            'state': 'absent'
        })
        c3.return_value = [
            {
                "id": "24", "name": "test_volume", "IO_group_id": "0", "IO_group_name": "io_grp0", "status": "online",
                "mdisk_grp_id": "2", "mdisk_grp_name": "site1pool1", "capacity": "1073741824", "type": "striped",
                "formatted": "yes", "formatting": "no", "mdisk_id": "", "mdisk_name": "", "FC_id": "", "FC_name": "",
                "RC_id": "", "RC_name": "", "vdisk_UID": "60050768108180ED700000000000002E", "preferred_node_id": "1",
                "fast_write_state": "empty", "cache": "readwrite", "udid": "", "fc_map_count": "0", "sync_rate": "50",
                "copy_count": "1", "se_copy_count": "0", "filesystem": "", "mirror_write_priority": "latency",
                "RC_change": "no", "compressed_copy_count": "0", "access_IO_group_count": "2", "last_access_time": "",
                "parent_mdisk_grp_id": "2", "parent_mdisk_grp_name": "site1pool1", "owner_type": "none", "owner_id": "",
                "owner_name": "", "encrypt": "no", "volume_id": "24", "volume_name": "test_volume", "function": "", "throttle_id": "",
                "throttle_name": "", "IOPs_limit": "", "bandwidth_limit_MB": "", "volume_group_id": "0",
                "volume_group_name": "test_volumegroup", "cloud_backup_enabled": "no", "cloud_account_id": "",
                "cloud_account_name": "", "backup_status": "off", "last_backup_time": "", "restore_status": "none",
                "backup_grain_size": "", "deduplicated_copy_count": "0", "protocol": "", "preferred_node_name": "node1",
                "safeguarded_expiration_time": "", "safeguarded_backup_count": "0"
            }, {
                "copy_id": "0", "status": "online",
                "sync": "yes", "auto_delete": "no", "primary": "yes", "mdisk_grp_id": "2", "mdisk_grp_name": "site1pool1",
                "type": "striped", "mdisk_id": "", "mdisk_name": "", "fast_write_state": "empty", "used_capacity": "1073741824",
                "real_capacity": "1073741824", "free_capacity": "0", "overallocation": "100", "autoexpand": "", "warning": "",
                "grainsize": "", "se_copy": "no", "easy_tier": "on", "easy_tier_status": "balanced", "tiers": [
                    {"tier": "tier_scm", "tier_capacity": "0"},
                    {"tier": "tier0_flash", "tier_capacity": "1073741824"},
                    {"tier": "tier1_flash", "tier_capacity": "0"},
                    {"tier": "tier_enterprise", "tier_capacity": "0"},
                    {"tier": "tier_nearline", "tier_capacity": "0"}
                ], "compressed_copy": "no", "uncompressed_used_capacity": "1073741824", "parent_mdisk_grp_id": "2",
                "parent_mdisk_grp_name": "site1pool1", "encrypt": "no", "deduplicated_copy": "no",
                "used_capacity_before_reduction": "", "safeguarded_mdisk_grp_id": "", "safeguarded_mdisk_grp_name": ""
            }
        ]
        c4.return_value = None
        with pytest.raises(AnsibleExitJson) as exc:
            v = IBMSVCvolume()
            v.apply()
        self.assertTrue(exc.value.args[0]['changed'])

    @patch('ansible_collections.ibm.storage_virtualize.plugins.module_utils.'
           'ibm_svc_utils.IBMSVCRestApi.svc_run_command')
    @patch('ansible_collections.ibm.storage_virtualize.plugins.modules.'
           'ibm_svc_manage_volume.IBMSVCvolume.get_existing_volume')
    @patch('ansible_collections.ibm.storage_virtualize.plugins.modules.'
           'ibm_svc_manage_volume.IBMSVCvolume.assemble_iogrp')
    @patch('ansible_collections.ibm.storage_virtualize.plugins.modules.'
           'ibm_svc_manage_volume.IBMSVCvolume.mandatory_parameter_validation')
    @patch('ansible_collections.ibm.storage_virtualize.plugins.module_utils.'
           'ibm_svc_utils.IBMSVCRestApi._svc_authorize')
    def test_module_for_deleting_non_existing_volume(self, auth_mock, c1, c2, c3, c4):
        set_module_args({
            'clustername': 'clustername',
            'domain': 'domain',
            'username': 'username',
            'password': 'password',
            'name': 'test_volume',
            'state': 'absent',
            'size': '1',
            'unit': 'gb',
            'pool': 'test_pool',
        })
        c3.return_value = []
        with pytest.raises(AnsibleExitJson) as exc:
            v = IBMSVCvolume()
            v.apply()
        self.assertFalse(exc.value.args[0]['changed'])

    @patch('ansible_collections.ibm.storage_virtualize.plugins.module_utils.'
           'ibm_svc_utils.IBMSVCRestApi.svc_run_command')
    @patch('ansible_collections.ibm.storage_virtualize.plugins.modules.'
           'ibm_svc_manage_volume.IBMSVCvolume.get_existing_volume')
    @patch('ansible_collections.ibm.storage_virtualize.plugins.modules.'
           'ibm_svc_manage_volume.IBMSVCvolume.assemble_iogrp')
    @patch('ansible_collections.ibm.storage_virtualize.plugins.modules.'
           'ibm_svc_manage_volume.IBMSVCvolume.mandatory_parameter_validation')
    @patch('ansible_collections.ibm.storage_virtualize.plugins.module_utils.'
           'ibm_svc_utils.IBMSVCRestApi._svc_authorize')
    def test_module_for_creating_thin_volume(self, auth_mock, c1, c2, c3, c4):
        set_module_args({
            'clustername': 'clustername',
            'domain': 'domain',
            'username': 'username',
            'password': 'password',
            'name': 'test_volume',
            'state': 'present',
            'size': '1',
            'unit': 'gb',
            'pool': 'test_pool',
            'iogrp': 'io_grp0, io_grp1',
            'thin': True,
            'buffersize': '10%'
        })
        c3.return_value = []
        c4.return_value = {
            'id': '25',
            'message': 'Volume, id [25], successfully created'
        }
        with pytest.raises(AnsibleExitJson) as exc:
            v = IBMSVCvolume()
            v.apply()
        self.assertTrue(exc.value.args[0]['changed'])

    @patch('ansible_collections.ibm.storage_virtualize.plugins.module_utils.'
           'ibm_svc_utils.IBMSVCRestApi.svc_run_command')
    @patch('ansible_collections.ibm.storage_virtualize.plugins.modules.'
           'ibm_svc_manage_volume.IBMSVCvolume.get_existing_volume')
    @patch('ansible_collections.ibm.storage_virtualize.plugins.modules.'
           'ibm_svc_manage_volume.IBMSVCvolume.assemble_iogrp')
    @patch('ansible_collections.ibm.storage_virtualize.plugins.modules.'
           'ibm_svc_manage_volume.IBMSVCvolume.mandatory_parameter_validation')
    @patch('ansible_collections.ibm.storage_virtualize.plugins.module_utils.'
           'ibm_svc_utils.IBMSVCRestApi._svc_authorize')
    def test_module_for_creating_compressed_volume(self, auth_mock, c1, c2, c3, c4):
        set_module_args({
            'clustername': 'clustername',
            'domain': 'domain',
            'username': 'username',
            'password': 'password',
            'name': 'test_volume',
            'state': 'present',
            'size': '1',
            'unit': 'gb',
            'pool': 'test_pool',
            'iogrp': 'io_grp0, io_grp1',
            'compressed': True,
            'buffersize': '10%'
        })
        c3.return_value = []
        c4.return_value = {
            'id': '25',
            'message': 'Volume, id [25], successfully created'
        }
        with pytest.raises(AnsibleExitJson) as exc:
            v = IBMSVCvolume()
            v.apply()
        self.assertTrue(exc.value.args[0]['changed'])

    @patch('ansible_collections.ibm.storage_virtualize.plugins.module_utils.'
           'ibm_svc_utils.IBMSVCRestApi.svc_run_command')
    @patch('ansible_collections.ibm.storage_virtualize.plugins.modules.'
           'ibm_svc_manage_volume.IBMSVCvolume.get_existing_volume')
    @patch('ansible_collections.ibm.storage_virtualize.plugins.modules.'
           'ibm_svc_manage_volume.IBMSVCvolume.assemble_iogrp')
    @patch('ansible_collections.ibm.storage_virtualize.plugins.modules.'
           'ibm_svc_manage_volume.IBMSVCvolume.mandatory_parameter_validation')
    @patch('ansible_collections.ibm.storage_virtualize.plugins.module_utils.'
           'ibm_svc_utils.IBMSVCRestApi._svc_authorize')
    def test_module_for_creating_deduplicated_volume(self, auth_mock, c1, c2, c3, c4):
        set_module_args({
            'clustername': 'clustername',
            'domain': 'domain',
            'username': 'username',
            'password': 'password',
            'name': 'test_volume',
            'state': 'present',
            'size': '1',
            'unit': 'gb',
            'pool': 'test_pool',
            'iogrp': 'io_grp0, io_grp1',
            'deduplicated': True,
        })
        c3.return_value = []
        c4.return_value = {
            'id': '25',
            'message': 'Volume, id [25], successfully created'
        }
        with pytest.raises(AnsibleExitJson) as exc:
            v = IBMSVCvolume()
            v.apply()
        self.assertTrue(exc.value.args[0]['changed'])

    @patch('ansible_collections.ibm.storage_virtualize.plugins.modules.'
           'ibm_svc_manage_volume.IBMSVCvolume.get_existing_volume')
    @patch('ansible_collections.ibm.storage_virtualize.plugins.modules.'
           'ibm_svc_manage_volume.IBMSVCvolume.assemble_iogrp')
    @patch('ansible_collections.ibm.storage_virtualize.plugins.modules.'
           'ibm_svc_manage_volume.IBMSVCvolume.mandatory_parameter_validation')
    @patch('ansible_collections.ibm.storage_virtualize.plugins.module_utils.'
           'ibm_svc_utils.IBMSVCRestApi._svc_authorize')
    def test_failure_while_updating_pool_parameter(self, auth_mock, c1, c2, c3):
        set_module_args({
            'clustername': 'clustername',
            'domain': 'domain',
            'username': 'username',
            'password': 'password',
            'name': 'test_thin',
            'state': 'present',
            'size': '1',
            'unit': 'gb',
            'pool': 'new_pool_name',
            'thin': True,
            'buffersize': '2%'
        })
        c3.return_value = [
            {
                "id": "77", "name": "test_thin", "IO_group_id": "0", "IO_group_name": "io_grp0", "status": "online",
                "mdisk_grp_id": "0", "mdisk_grp_name": "site2pool1", "capacity": "1073741824", "type": "striped",
                "formatted": "no", "formatting": "no", "mdisk_id": "", "mdisk_name": "", "FC_id": "", "FC_name": "",
                "RC_id": "", "RC_name": "", "vdisk_UID": "60050764008881864800000000000471", "preferred_node_id": "1",
                "fast_write_state": "empty", "cache": "readwrite", "udid": "", "fc_map_count": "0", "sync_rate": "50",
                "copy_count": "1", "se_copy_count": "1", "filesystem": "", "mirror_write_priority": "latency",
                "RC_change": "no", "compressed_copy_count": "0", "access_IO_group_count": "1", "last_access_time": "",
                "parent_mdisk_grp_id": "0", "parent_mdisk_grp_name": "site2pool1", "owner_type": "none", "owner_id": "",
                "owner_name": "", "encrypt": "no", "volume_id": "77", "volume_name": "test_thin", "function": "",
                "throttle_id": "", "throttle_name": "", "IOPs_limit": "", "bandwidth_limit_MB": "", "volume_group_id": "",
                "volume_group_name": "", "cloud_backup_enabled": "no", "cloud_account_id": "", "cloud_account_name": "",
                "backup_status": "off", "last_backup_time": "", "restore_status": "none", "backup_grain_size": "",
                "deduplicated_copy_count": "0", "protocol": "", "preferred_node_name": "node1",
                "safeguarded_expiration_time": "", "safeguarded_backup_count": "0"
            },
            {
                "copy_id": "0", "status": "online", "sync": "yes", "auto_delete": "no", "primary": "yes", "mdisk_grp_id": "0",
                "mdisk_grp_name": "site2pool1", "type": "striped", "mdisk_id": "", "mdisk_name": "",
                "fast_write_state": "empty", "used_capacity": "786432", "real_capacity": "38252032",
                "free_capacity": "37465600", "overallocation": "2807", "autoexpand": "on", "warning": "80",
                "grainsize": "256", "se_copy": "yes", "easy_tier": "on", "easy_tier_status": "balanced",
                "tiers": [
                    {"tier": "tier_scm", "tier_capacity": "0"},
                    {"tier": "tier0_flash", "tier_capacity": "38252032"},
                    {"tier": "tier1_flash", "tier_capacity": "0"},
                    {"tier": "tier_enterprise", "tier_capacity": "0"},
                    {"tier": "tier_nearline", "tier_capacity": "0"}
                ], "compressed_copy": "no", "uncompressed_used_capacity": "786432", "parent_mdisk_grp_id": "0",
                "parent_mdisk_grp_name": "site2pool1", "encrypt": "no", "deduplicated_copy": "no",
                "used_capacity_before_reduction": "", "safeguarded_mdisk_grp_id": "", "safeguarded_mdisk_grp_name": ""
            }
        ]
        with pytest.raises(AnsibleFailJson) as exc:
            v = IBMSVCvolume()
            v.apply()
        self.assertTrue(exc.value.args[0]['failed'])

    @patch('ansible_collections.ibm.storage_virtualize.plugins.modules.'
           'ibm_svc_manage_volume.IBMSVCvolume.get_existing_volume')
    @patch('ansible_collections.ibm.storage_virtualize.plugins.modules.'
           'ibm_svc_manage_volume.IBMSVCvolume.assemble_iogrp')
    @patch('ansible_collections.ibm.storage_virtualize.plugins.modules.'
           'ibm_svc_manage_volume.IBMSVCvolume.mandatory_parameter_validation')
    @patch('ansible_collections.ibm.storage_virtualize.plugins.module_utils.'
           'ibm_svc_utils.IBMSVCRestApi._svc_authorize')
    def test_failure_while_updating_thin_parameter(self, auth_mock, c1, c2, c3):
        set_module_args({
            'clustername': 'clustername',
            'domain': 'domain',
            'username': 'username',
            'password': 'password',
            'name': 'test_volume',
            'state': 'present',
            'size': '1',
            'unit': 'gb',
            'pool': 'site2pool1',
            'thin': True,
            'buffersize': '2%'
        })
        c3.return_value = [
            {
                "id": "24", "name": "test_volume", "IO_group_id": "0", "IO_group_name": "io_grp0", "status": "online",
                "mdisk_grp_id": "2", "mdisk_grp_name": "site1pool1", "capacity": "1073741824", "type": "striped",
                "formatted": "yes", "formatting": "no", "mdisk_id": "", "mdisk_name": "", "FC_id": "", "FC_name": "",
                "RC_id": "", "RC_name": "", "vdisk_UID": "60050768108180ED700000000000002E", "preferred_node_id": "1",
                "fast_write_state": "empty", "cache": "readwrite", "udid": "", "fc_map_count": "0", "sync_rate": "50",
                "copy_count": "1", "se_copy_count": "0", "filesystem": "", "mirror_write_priority": "latency",
                "RC_change": "no", "compressed_copy_count": "0", "access_IO_group_count": "2", "last_access_time": "",
                "parent_mdisk_grp_id": "2", "parent_mdisk_grp_name": "site1pool1", "owner_type": "none", "owner_id": "",
                "owner_name": "", "encrypt": "no", "volume_id": "24", "volume_name": "test_volume", "function": "", "throttle_id": "",
                "throttle_name": "", "IOPs_limit": "", "bandwidth_limit_MB": "", "volume_group_id": "0",
                "volume_group_name": "test_volumegroup", "cloud_backup_enabled": "no", "cloud_account_id": "",
                "cloud_account_name": "", "backup_status": "off", "last_backup_time": "", "restore_status": "none",
                "backup_grain_size": "", "deduplicated_copy_count": "0", "protocol": "", "preferred_node_name": "node1",
                "safeguarded_expiration_time": "", "safeguarded_backup_count": "0"
            }, {
                "copy_id": "0", "status": "online",
                "sync": "yes", "auto_delete": "no", "primary": "yes", "mdisk_grp_id": "2", "mdisk_grp_name": "site1pool1",
                "type": "striped", "mdisk_id": "", "mdisk_name": "", "fast_write_state": "empty", "used_capacity": "1073741824",
                "real_capacity": "1073741824", "free_capacity": "0", "overallocation": "100", "autoexpand": "", "warning": "",
                "grainsize": "", "se_copy": "no", "easy_tier": "on", "easy_tier_status": "balanced", "tiers": [
                    {"tier": "tier_scm", "tier_capacity": "0"},
                    {"tier": "tier0_flash", "tier_capacity": "1073741824"},
                    {"tier": "tier1_flash", "tier_capacity": "0"},
                    {"tier": "tier_enterprise", "tier_capacity": "0"},
                    {"tier": "tier_nearline", "tier_capacity": "0"}
                ], "compressed_copy": "no", "uncompressed_used_capacity": "1073741824", "parent_mdisk_grp_id": "2",
                "parent_mdisk_grp_name": "site1pool1", "encrypt": "no", "deduplicated_copy": "no",
                "used_capacity_before_reduction": "", "safeguarded_mdisk_grp_id": "", "safeguarded_mdisk_grp_name": ""
            }
        ]
        with pytest.raises(AnsibleFailJson) as exc:
            v = IBMSVCvolume()
            v.apply()
        self.assertTrue(exc.value.args[0]['failed'])

    @patch('ansible_collections.ibm.storage_virtualize.plugins.modules.'
           'ibm_svc_manage_volume.IBMSVCvolume.get_existing_volume')
    @patch('ansible_collections.ibm.storage_virtualize.plugins.modules.'
           'ibm_svc_manage_volume.IBMSVCvolume.assemble_iogrp')
    @patch('ansible_collections.ibm.storage_virtualize.plugins.modules.'
           'ibm_svc_manage_volume.IBMSVCvolume.mandatory_parameter_validation')
    @patch('ansible_collections.ibm.storage_virtualize.plugins.module_utils.'
           'ibm_svc_utils.IBMSVCRestApi._svc_authorize')
    def test_failure_while_updating_compressed_parameter(self, auth_mock, c1, c2, c3):
        set_module_args({
            'clustername': 'clustername',
            'domain': 'domain',
            'username': 'username',
            'password': 'password',
            'name': 'test_volume',
            'state': 'present',
            'size': '1',
            'unit': 'gb',
            'pool': 'site2pool1',
            'compressed': True,
            'buffersize': '2%'
        })
        c3.return_value = [
            {
                "id": "24", "name": "test_volume", "IO_group_id": "0", "IO_group_name": "io_grp0", "status": "online",
                "mdisk_grp_id": "2", "mdisk_grp_name": "site1pool1", "capacity": "1073741824", "type": "striped",
                "formatted": "yes", "formatting": "no", "mdisk_id": "", "mdisk_name": "", "FC_id": "", "FC_name": "",
                "RC_id": "", "RC_name": "", "vdisk_UID": "60050768108180ED700000000000002E", "preferred_node_id": "1",
                "fast_write_state": "empty", "cache": "readwrite", "udid": "", "fc_map_count": "0", "sync_rate": "50",
                "copy_count": "1", "se_copy_count": "0", "filesystem": "", "mirror_write_priority": "latency",
                "RC_change": "no", "compressed_copy_count": "0", "access_IO_group_count": "2", "last_access_time": "",
                "parent_mdisk_grp_id": "2", "parent_mdisk_grp_name": "site1pool1", "owner_type": "none", "owner_id": "",
                "owner_name": "", "encrypt": "no", "volume_id": "24", "volume_name": "test_volume", "function": "", "throttle_id": "",
                "throttle_name": "", "IOPs_limit": "", "bandwidth_limit_MB": "", "volume_group_id": "0",
                "volume_group_name": "test_volumegroup", "cloud_backup_enabled": "no", "cloud_account_id": "",
                "cloud_account_name": "", "backup_status": "off", "last_backup_time": "", "restore_status": "none",
                "backup_grain_size": "", "deduplicated_copy_count": "0", "protocol": "", "preferred_node_name": "node1",
                "safeguarded_expiration_time": "", "safeguarded_backup_count": "0"
            }, {
                "copy_id": "0", "status": "online",
                "sync": "yes", "auto_delete": "no", "primary": "yes", "mdisk_grp_id": "2", "mdisk_grp_name": "site1pool1",
                "type": "striped", "mdisk_id": "", "mdisk_name": "", "fast_write_state": "empty", "used_capacity": "1073741824",
                "real_capacity": "1073741824", "free_capacity": "0", "overallocation": "100", "autoexpand": "", "warning": "",
                "grainsize": "", "se_copy": "no", "easy_tier": "on", "easy_tier_status": "balanced", "tiers": [
                    {"tier": "tier_scm", "tier_capacity": "0"},
                    {"tier": "tier0_flash", "tier_capacity": "1073741824"},
                    {"tier": "tier1_flash", "tier_capacity": "0"},
                    {"tier": "tier_enterprise", "tier_capacity": "0"},
                    {"tier": "tier_nearline", "tier_capacity": "0"}
                ], "compressed_copy": "no", "uncompressed_used_capacity": "1073741824", "parent_mdisk_grp_id": "2",
                "parent_mdisk_grp_name": "site1pool1", "encrypt": "no", "deduplicated_copy": "no",
                "used_capacity_before_reduction": "", "safeguarded_mdisk_grp_id": "", "safeguarded_mdisk_grp_name": ""
            }
        ]
        with pytest.raises(AnsibleFailJson) as exc:
            v = IBMSVCvolume()
            v.apply()
        self.assertTrue(exc.value.args[0]['failed'])

    @patch('ansible_collections.ibm.storage_virtualize.plugins.modules.'
           'ibm_svc_manage_volume.IBMSVCvolume.get_existing_volume')
    @patch('ansible_collections.ibm.storage_virtualize.plugins.modules.'
           'ibm_svc_manage_volume.IBMSVCvolume.assemble_iogrp')
    @patch('ansible_collections.ibm.storage_virtualize.plugins.modules.'
           'ibm_svc_manage_volume.IBMSVCvolume.mandatory_parameter_validation')
    @patch('ansible_collections.ibm.storage_virtualize.plugins.module_utils.'
           'ibm_svc_utils.IBMSVCRestApi._svc_authorize')
    def test_failure_while_updating_deduplicated_parameter(self, auth_mock, c1, c2, c3):
        set_module_args({
            'clustername': 'clustername',
            'domain': 'domain',
            'username': 'username',
            'password': 'password',
            'name': 'test_volume',
            'state': 'present',
            'size': '1',
            'unit': 'gb',
            'pool': 'site2pool1',
            'compressed': True,
            'deduplicated': True,
            'buffersize': '2%'
        })
        c3.return_value = [
            {
                "id": "24", "name": "test_volume", "IO_group_id": "0", "IO_group_name": "io_grp0", "status": "online",
                "mdisk_grp_id": "2", "mdisk_grp_name": "site1pool1", "capacity": "1073741824", "type": "striped",
                "formatted": "yes", "formatting": "no", "mdisk_id": "", "mdisk_name": "", "FC_id": "", "FC_name": "",
                "RC_id": "", "RC_name": "", "vdisk_UID": "60050768108180ED700000000000002E", "preferred_node_id": "1",
                "fast_write_state": "empty", "cache": "readwrite", "udid": "", "fc_map_count": "0", "sync_rate": "50",
                "copy_count": "1", "se_copy_count": "0", "filesystem": "", "mirror_write_priority": "latency",
                "RC_change": "no", "compressed_copy_count": "0", "access_IO_group_count": "2", "last_access_time": "",
                "parent_mdisk_grp_id": "2", "parent_mdisk_grp_name": "site1pool1", "owner_type": "none", "owner_id": "",
                "owner_name": "", "encrypt": "no", "volume_id": "24", "volume_name": "test_volume", "function": "", "throttle_id": "",
                "throttle_name": "", "IOPs_limit": "", "bandwidth_limit_MB": "", "volume_group_id": "0",
                "volume_group_name": "test_volumegroup", "cloud_backup_enabled": "no", "cloud_account_id": "",
                "cloud_account_name": "", "backup_status": "off", "last_backup_time": "", "restore_status": "none",
                "backup_grain_size": "", "deduplicated_copy_count": "0", "protocol": "", "preferred_node_name": "node1",
                "safeguarded_expiration_time": "", "safeguarded_backup_count": "0"
            }, {
                "copy_id": "0", "status": "online",
                "sync": "yes", "auto_delete": "no", "primary": "yes", "mdisk_grp_id": "2", "mdisk_grp_name": "site1pool1",
                "type": "striped", "mdisk_id": "", "mdisk_name": "", "fast_write_state": "empty", "used_capacity": "1073741824",
                "real_capacity": "1073741824", "free_capacity": "0", "overallocation": "100", "autoexpand": "", "warning": "",
                "grainsize": "", "se_copy": "no", "easy_tier": "on", "easy_tier_status": "balanced", "tiers": [
                    {"tier": "tier_scm", "tier_capacity": "0"},
                    {"tier": "tier0_flash", "tier_capacity": "1073741824"},
                    {"tier": "tier1_flash", "tier_capacity": "0"},
                    {"tier": "tier_enterprise", "tier_capacity": "0"},
                    {"tier": "tier_nearline", "tier_capacity": "0"}
                ], "compressed_copy": "no", "uncompressed_used_capacity": "1073741824", "parent_mdisk_grp_id": "2",
                "parent_mdisk_grp_name": "site1pool1", "encrypt": "no", "deduplicated_copy": "no",
                "used_capacity_before_reduction": "", "safeguarded_mdisk_grp_id": "", "safeguarded_mdisk_grp_name": ""
            }
        ]
        with pytest.raises(AnsibleFailJson) as exc:
            v = IBMSVCvolume()
            v.apply()
        self.assertTrue(exc.value.args[0]['failed'])

    @patch('ansible_collections.ibm.storage_virtualize.plugins.modules.'
           'ibm_svc_manage_volume.IBMSVCvolume.get_existing_volume')
    @patch('ansible_collections.ibm.storage_virtualize.plugins.modules.'
           'ibm_svc_manage_volume.IBMSVCvolume.assemble_iogrp')
    @patch('ansible_collections.ibm.storage_virtualize.plugins.modules.'
           'ibm_svc_manage_volume.IBMSVCvolume.mandatory_parameter_validation')
    @patch('ansible_collections.ibm.storage_virtualize.plugins.module_utils.'
           'ibm_svc_utils.IBMSVCRestApi._svc_authorize')
    def test_failure_while_managing_mirrored_volume(self, auth_mock, c1, c2, c3):
        set_module_args({
            'clustername': 'clustername',
            'domain': 'domain',
            'username': 'username',
            'password': 'password',
            'name': 'test_compress',
            'state': 'present',
            'size': '2',
            'unit': 'gb',
            'pool': 'site2pool1',
            'compressed': True,
            'deduplicated': True,
            'buffersize': '2%'
        })
        c3.return_value = [
            {
                "id": "78", "name": "test_compress", "IO_group_id": "0", "IO_group_name": "io_grp0",
                "status": "online", "mdisk_grp_id": "0", "mdisk_grp_name": "site2pool1", "capacity": "1073741824",
                "type": "many", "formatted": "no", "formatting": "no", "mdisk_id": "", "mdisk_name": "",
                "FC_id": "", "FC_name": "", "RC_id": "", "RC_name": "", "vdisk_UID": "60050764008881864800000000000472",
                "preferred_node_id": "5", "fast_write_state": "empty", "cache": "readwrite", "udid": "",
                "fc_map_count": "0", "sync_rate": "50", "copy_count": "1", "se_copy_count": "0", "filesystem": "",
                "mirror_write_priority": "latency", "RC_change": "no", "compressed_copy_count": "1",
                "access_IO_group_count": "1", "last_access_time": "", "parent_mdisk_grp_id": "0",
                "parent_mdisk_grp_name": "site2pool1", "owner_type": "none", "owner_id": "", "owner_name": "",
                "encrypt": "no", "volume_id": "78", "volume_name": "test_compress", "function": "",
                "throttle_id": "", "throttle_name": "", "IOPs_limit": "", "bandwidth_limit_MB": "",
                "volume_group_id": "", "volume_group_name": "", "cloud_backup_enabled": "no", "cloud_account_id": "",
                "cloud_account_name": "", "backup_status": "off", "last_backup_time": "", "restore_status": "none",
                "backup_grain_size": "", "deduplicated_copy_count": "0", "protocol": "", "preferred_node_name": "node2",
                "safeguarded_expiration_time": "", "safeguarded_backup_count": "0"
            },
            {
                "copy_id": "0", "status": "online", "sync": "yes", "auto_delete": "no", "primary": "yes",
                "mdisk_grp_id": "0", "mdisk_grp_name": "site2pool1", "type": "striped", "mdisk_id": "",
                "mdisk_name": "", "fast_write_state": "empty", "used_capacity": "163840",
                "real_capacity": "38252032", "free_capacity": "38088192", "overallocation": "2807",
                "autoexpand": "on", "warning": "80", "grainsize": "", "se_copy": "no", "easy_tier": "on",
                "easy_tier_status": "balanced", "tiers": [
                    {"tier": "tier_scm", "tier_capacity": "0"},
                    {"tier": "tier0_flash", "tier_capacity": "38252032"},
                    {"tier": "tier1_flash", "tier_capacity": "0"},
                    {"tier": "tier_enterprise", "tier_capacity": "0"},
                    {"tier": "tier_nearline", "tier_capacity": "0"}
                ], "compressed_copy": "yes", "uncompressed_used_capacity": "0", "parent_mdisk_grp_id": "0",
                "parent_mdisk_grp_name": "site2pool1", "encrypt": "no", "deduplicated_copy": "yes",
                "used_capacity_before_reduction": "", "safeguarded_mdisk_grp_id": "",
                "safeguarded_mdisk_grp_name": ""
            }
        ]
        with pytest.raises(AnsibleFailJson) as exc:
            v = IBMSVCvolume()
            v.apply()
        self.assertTrue(exc.value.args[0]['failed'])

    @patch('ansible_collections.ibm.storage_virtualize.plugins.module_utils.'
           'ibm_svc_utils.IBMSVCRestApi.svc_run_command')
    @patch('ansible_collections.ibm.storage_virtualize.plugins.module_utils.'
           'ibm_svc_utils.IBMSVCRestApi.svc_obj_info')
    @patch('ansible_collections.ibm.storage_virtualize.plugins.module_utils.'
           'ibm_svc_utils.IBMSVCRestApi._svc_authorize')
    def test_volume_rename(self, auth, mock_old, src):
        set_module_args({
            'clustername': 'clustername',
            'domain': 'domain',
            'username': 'username',
            'password': 'password',
            'old_name': 'name',
            'name': 'new_name',
            'state': 'present',
        })
        arg_data = []
        mock_old.return_value = [
            {
                "id": "24", "name": "test_volume", "IO_group_id": "0", "IO_group_name": "io_grp0", "status": "online",
                "mdisk_grp_id": "2", "mdisk_grp_name": "site1pool1", "capacity": "1073741824", "type": "striped",
                "formatted": "yes", "formatting": "no", "mdisk_id": "", "mdisk_name": "", "FC_id": "", "FC_name": "",
                "RC_id": "", "RC_name": "", "vdisk_UID": "60050768108180ED700000000000002E", "preferred_node_id": "1",
                "fast_write_state": "empty", "cache": "readwrite", "udid": "", "fc_map_count": "0", "sync_rate": "50",
                "copy_count": "1", "se_copy_count": "0", "filesystem": "", "mirror_write_priority": "latency",
                "RC_change": "no", "compressed_copy_count": "0", "access_IO_group_count": "2", "last_access_time": "",
                "parent_mdisk_grp_id": "2", "parent_mdisk_grp_name": "site1pool1", "owner_type": "none", "owner_id": "",
                "owner_name": "", "encrypt": "no", "volume_id": "24", "volume_name": "test_volume", "function": "", "throttle_id": "",
                "throttle_name": "", "IOPs_limit": "", "bandwidth_limit_MB": "", "volume_group_id": "0",
                "volume_group_name": "test_volumegroup", "cloud_backup_enabled": "no", "cloud_account_id": "",
                "cloud_account_name": "", "backup_status": "off", "last_backup_time": "", "restore_status": "none",
                "backup_grain_size": "", "deduplicated_copy_count": "0", "protocol": "", "preferred_node_name": "node1",
                "safeguarded_expiration_time": "", "safeguarded_backup_count": "0"
            }, {
                "copy_id": "0", "status": "online",
                "sync": "yes", "auto_delete": "no", "primary": "yes", "mdisk_grp_id": "2", "mdisk_grp_name": "site1pool1",
                "type": "striped", "mdisk_id": "", "mdisk_name": "", "fast_write_state": "empty", "used_capacity": "1073741824",
                "real_capacity": "1073741824", "free_capacity": "0", "overallocation": "100", "autoexpand": "", "warning": "",
                "grainsize": "", "se_copy": "no", "easy_tier": "on", "easy_tier_status": "balanced", "tiers": [
                    {"tier": "tier_scm", "tier_capacity": "0"},
                    {"tier": "tier0_flash", "tier_capacity": "1073741824"},
                    {"tier": "tier1_flash", "tier_capacity": "0"},
                    {"tier": "tier_enterprise", "tier_capacity": "0"},
                    {"tier": "tier_nearline", "tier_capacity": "0"}
                ], "compressed_copy": "no", "uncompressed_used_capacity": "1073741824", "parent_mdisk_grp_id": "2",
                "parent_mdisk_grp_name": "site1pool1", "encrypt": "no", "deduplicated_copy": "no",
                "used_capacity_before_reduction": "", "safeguarded_mdisk_grp_id": "", "safeguarded_mdisk_grp_name": ""
            }
        ]
        src.return_value = None
        v = IBMSVCvolume()
        data = v.volume_rename(arg_data)
        self.assertEqual(data, 'Volume [name] has been successfully rename to [new_name]')

    @patch('ansible_collections.ibm.storage_virtualize.plugins.module_utils.'
           'ibm_svc_utils.IBMSVCRestApi._svc_authorize')
    def test_volume_rename_failure_for_unsupported_param(self, am):
        set_module_args({
            'clustername': 'clustername',
            'domain': 'domain',
            'username': 'username',
            'password': 'password',
            'old_name': 'name',
            'name': 'new_name',
            'state': 'present',
            'thin': True
        })
        with pytest.raises(AnsibleFailJson) as exc:
            v = IBMSVCvolume()
            v.apply()
        self.assertTrue(exc.value.args[0]['failed'])

    @patch('ansible_collections.ibm.storage_virtualize.plugins.module_utils.'
           'ibm_svc_utils.IBMSVCRestApi.svc_run_command')
    @patch('ansible_collections.ibm.storage_virtualize.plugins.module_utils.'
           'ibm_svc_utils.IBMSVCRestApi.svc_obj_info')
    @patch('ansible_collections.ibm.storage_virtualize.plugins.module_utils.'
           'ibm_svc_utils.IBMSVCRestApi._svc_authorize')
    def test_failure_volume_creation_cloud_backup_validation(self, auth, obj_mock, src):

        set_module_args({
            'clustername': 'clustername',
            'domain': 'domain',
            'username': 'username',
            'password': 'password',
            'name': 'name',
            'enable_cloud_snapshot': True,
            'cloud_account_name': 'aws_acc',
            'state': 'present',
        })

        obj_mock.return_value = {}
        with pytest.raises(AnsibleFailJson) as exc:
            v = IBMSVCvolume()
            v.apply()
        self.assertTrue(exc.value.args[0]['failed'])
        self.assertEqual(exc.value.args[0]['msg'], "Following parameter not applicable for creation: enable_cloud_snapshot")

    @patch('ansible_collections.ibm.storage_virtualize.plugins.module_utils.'
           'ibm_svc_utils.IBMSVCRestApi.svc_obj_info')
    @patch('ansible_collections.ibm.storage_virtualize.plugins.module_utils.'
           'ibm_svc_utils.IBMSVCRestApi._svc_authorize')
    def test_failure_volume_creation_invalid_params_cloud_account(self,
                                                                  svc_authorize_mock,
                                                                  svc_obj_info_mock):
        """
        Following parameter not applicable for creation: cloud_account_name
        """
        set_module_args({
            'clustername': 'clustername',
            'domain': 'domain',
            'state': 'present',
            'username': 'username',
            'password': 'password',
            'name': 'test_volume',
            'pool': 'test_pool',
            'size': '1',
            'unit': 'gb',
            'volumegroup': 'test_volumegroup',
            'cloud_account_name': 'test'
        })
        svc_obj_info_mock.side_effect = [{}, {}]
        with pytest.raises(AnsibleFailJson) as exc:
            v = IBMSVCvolume()
            v.apply()
        self.assertTrue(exc.value.args[0]['failed'])
        self.assertEqual(exc.value.args[0]['msg'], "Following parameter not applicable for creation: cloud_account_name")

    @patch('ansible_collections.ibm.storage_virtualize.plugins.module_utils.'
           'ibm_svc_utils.IBMSVCRestApi.svc_run_command')
    @patch('ansible_collections.ibm.storage_virtualize.plugins.module_utils.'
           'ibm_svc_utils.IBMSVCRestApi.svc_obj_info')
    @patch('ansible_collections.ibm.storage_virtualize.plugins.module_utils.'
           'ibm_svc_utils.IBMSVCRestApi._svc_authorize')
    def test_enable_cloud_backup(self, auth, obj_mock, src):
        set_module_args({
            'clustername': 'clustername',
            'domain': 'domain',
            'username': 'username',
            'password': 'password',
            'name': 'name',
            'enable_cloud_snapshot': True,
            'cloud_account_name': 'aws_acc',
            'state': 'present',
        })

        obj_mock.return_value = [{'name': 'name', 'cloud_backup_enabled': 'no', 'type': 'striped', 'RC_name': ''}, {}]
        with pytest.raises(AnsibleExitJson) as exc:
            v = IBMSVCvolume()
            v.apply()
        self.assertTrue(exc.value.args[0]['changed'])

    @patch('ansible_collections.ibm.storage_virtualize.plugins.module_utils.'
           'ibm_svc_utils.IBMSVCRestApi.svc_run_command')
    @patch('ansible_collections.ibm.storage_virtualize.plugins.module_utils.'
           'ibm_svc_utils.IBMSVCRestApi.svc_obj_info')
    @patch('ansible_collections.ibm.storage_virtualize.plugins.module_utils.'
           'ibm_svc_utils.IBMSVCRestApi._svc_authorize')
    def test_enable_cloud_backup_idempotency(self, auth, obj_mock, src):
        set_module_args({
            'clustername': 'clustername',
            'domain': 'domain',
            'username': 'username',
            'password': 'password',
            'name': 'name',
            'enable_cloud_snapshot': True,
            'cloud_account_name': 'aws_acc',
            'state': 'present',
        })

        obj_mock.return_value = [{'name': 'name', 'cloud_backup_enabled': 'yes', 'cloud_account_name': 'aws_acc', 'type': 'striped', 'RC_name': ''}, {}]
        with pytest.raises(AnsibleExitJson) as exc:
            v = IBMSVCvolume()
            v.apply()
        self.assertFalse(exc.value.args[0]['changed'])

    @patch('ansible_collections.ibm.storage_virtualize.plugins.module_utils.'
           'ibm_svc_utils.IBMSVCRestApi.svc_run_command')
    @patch('ansible_collections.ibm.storage_virtualize.plugins.module_utils.'
           'ibm_svc_utils.IBMSVCRestApi.svc_obj_info')
    @patch('ansible_collections.ibm.storage_virtualize.plugins.module_utils.'
           'ibm_svc_utils.IBMSVCRestApi._svc_authorize')
    def test_disable_cloud_backup(self, auth, obj_mock, src):
        set_module_args({
            'clustername': 'clustername',
            'domain': 'domain',
            'username': 'username',
            'password': 'password',
            'name': 'name',
            'enable_cloud_snapshot': False,
            'state': 'present',
        })

        obj_mock.return_value = [{'name': 'name', 'cloud_backup_enabled': 'yes', 'type': 'striped', 'RC_name': ''}, {}]
        with pytest.raises(AnsibleExitJson) as exc:
            v = IBMSVCvolume()
            v.apply()
        self.assertTrue(exc.value.args[0]['changed'])

    @patch('ansible_collections.ibm.storage_virtualize.plugins.module_utils.'
           'ibm_svc_utils.IBMSVCRestApi.svc_run_command')
    @patch('ansible_collections.ibm.storage_virtualize.plugins.module_utils.'
           'ibm_svc_utils.IBMSVCRestApi.svc_obj_info')
    @patch('ansible_collections.ibm.storage_virtualize.plugins.module_utils.'
           'ibm_svc_utils.IBMSVCRestApi._svc_authorize')
    def test_disable_cloud_backup_idempotency(self, auth, obj_mock, src):
        set_module_args({
            'clustername': 'clustername',
            'domain': 'domain',
            'username': 'username',
            'password': 'password',
            'name': 'name',
            'enable_cloud_snapshot': False,
            'state': 'present',
        })

        obj_mock.return_value = [{'name': 'name', 'cloud_backup_enabled': 'no', 'type': 'striped', 'RC_name': ''}, {}]
        with pytest.raises(AnsibleExitJson) as exc:
            v = IBMSVCvolume()
            v.apply()
        self.assertFalse(exc.value.args[0]['changed'])

    # Create thinclone from volume
    @patch('ansible_collections.ibm.storage_virtualize.plugins.modules.'
           'ibm_svc_manage_volume.IBMSVCvolume.create_transient_snapshot')
    @patch('ansible_collections.ibm.storage_virtualize.plugins.module_utils.'
           'ibm_svc_utils.IBMSVCRestApi.svc_run_command')
    @patch('ansible_collections.ibm.storage_virtualize.plugins.module_utils.'
           'ibm_svc_utils.IBMSVCRestApi._svc_authorize')
    def test_create_volume_thinclone(self, svc_authorize_mock, svc_run_command_mock, create_transient_snapshot_mock):
        set_module_args({
            'clustername': 'clustername',
            'domain': 'domain',
            'state': 'present',
            'username': 'username',
            'password': 'password',
            'name': 'test_volume',
            'pool': 'test_pool',
            'type': 'thinclone',
            'fromsourcevolume': 'vol1'
        })

        svc_run_command_mock.return_value = {
            'id': '25',
            'message': 'Volume, id [25], successfully created'
        }
        create_transient_snapshot_mock.return_value = 10
        v = IBMSVCvolume()
        v.create_volume()

    # Create clone from volume
    @patch('ansible_collections.ibm.storage_virtualize.plugins.modules.'
           'ibm_svc_manage_volume.IBMSVCvolume.create_transient_snapshot')
    @patch('ansible_collections.ibm.storage_virtualize.plugins.module_utils.'
           'ibm_svc_utils.IBMSVCRestApi.svc_run_command')
    @patch('ansible_collections.ibm.storage_virtualize.plugins.module_utils.'
           'ibm_svc_utils.IBMSVCRestApi._svc_authorize')
    def test_create_volume_clone(self, svc_authorize_mock, svc_run_command_mock, create_transient_snapshot_mock):
        set_module_args({
            'clustername': 'clustername',
            'domain': 'domain',
            'state': 'present',
            'username': 'username',
            'password': 'password',
            'name': 'test_volume',
            'pool': 'test_pool',
            'type': 'clone',
            'fromsourcevolume': 'vol1'
        })

        svc_run_command_mock.return_value = {
            'id': '25',
            'message': 'Volume, id [25], successfully created'
        }
        create_transient_snapshot_mock.return_value = 10
        v = IBMSVCvolume()
        v.create_volume()

    @patch('ansible_collections.ibm.storage_virtualize.plugins.module_utils.'
           'ibm_svc_utils.IBMSVCRestApi._svc_authorize')
    def test_failure_when_thinclone_creation_parameter_type_missing(self, svc_authorize_mock):
        set_module_args({
            'clustername': 'clustername',
            'domain': 'domain',
            'state': 'present',
            'username': 'username',
            'password': 'password',
            'name': 'test_volume',
            'fromsourcevolume': 'src_volume1',
            'pool': 'pool1'
        })
        with pytest.raises(AnsibleFailJson) as exc:
            v = IBMSVCvolume()
            v.volume_creation_parameter_validation()
        self.assertTrue(exc.value.args[0]['failed'])

    @patch('ansible_collections.ibm.storage_virtualize.plugins.module_utils.'
           'ibm_svc_utils.IBMSVCRestApi._svc_authorize')
    def test_failure_when_thinclone_creation_parameter_fromsourcevolume_missing(self, svc_authorize_mock):
        set_module_args({
            'clustername': 'clustername',
            'domain': 'domain',
            'state': 'present',
            'username': 'username',
            'password': 'password',
            'name': 'test_volume',
            'type': 'thinclone',
            'pool': 'pool1'
        })
        with pytest.raises(AnsibleFailJson) as exc:
            v = IBMSVCvolume()
            v.volume_creation_parameter_validation()
        self.assertTrue(exc.value.args[0]['failed'])

    @patch('ansible_collections.ibm.storage_virtualize.plugins.module_utils.'
           'ibm_svc_utils.IBMSVCRestApi._svc_authorize')
    def test_failure_when_thinclone_creation_parameter_pool_missing(self, svc_authorize_mock):
        set_module_args({
            'clustername': 'clustername',
            'domain': 'domain',
            'state': 'present',
            'username': 'username',
            'password': 'password',
            'name': 'test_volume',
            'type': 'thinclone',
            'fromsourcevolume': 'src_volume1',
        })
        with pytest.raises(AnsibleFailJson) as exc:
            v = IBMSVCvolume()
            v.volume_creation_parameter_validation()
        self.assertTrue(exc.value.args[0]['failed'])

    @patch('ansible_collections.ibm.storage_virtualize.plugins.module_utils.'
           'ibm_svc_utils.IBMSVCRestApi._svc_authorize')
    def test_failure_when_size_provided_in_thinclone_creation(self, svc_authorize_mock):
        set_module_args({
            'clustername': 'clustername',
            'domain': 'domain',
            'state': 'present',
            'username': 'username',
            'password': 'password',
            'name': 'test_volume',
            'type': 'thinclone',
            'fromsourcevolume': 'src_volume1',
            'size': '2048',
            'pool': 'pool1'
        })
        with pytest.raises(AnsibleFailJson) as exc:
            v = IBMSVCvolume()
            v.volume_creation_parameter_validation()
        self.assertTrue(exc.value.args[0]['failed'])

    @patch('ansible_collections.ibm.storage_virtualize.plugins.module_utils.'
           'ibm_svc_utils.IBMSVCRestApi._svc_authorize')
    def test_volume_rename_failure_for_unsupported_param_type(self, am):
        set_module_args({
            'clustername': 'clustername',
            'domain': 'domain',
            'username': 'username',
            'password': 'password',
            'old_name': 'name',
            'name': 'new_name',
            'state': 'present',
            'type': 'thinclone'
        })
        with pytest.raises(AnsibleFailJson) as exc:
            v = IBMSVCvolume()
            v.apply()
        self.assertTrue(exc.value.args[0]['failed'])

    # Test create_transient_snapshot
    @patch('ansible_collections.ibm.storage_virtualize.plugins.module_utils.'
           'ibm_svc_utils.IBMSVCRestApi.svc_run_command')
    @patch('ansible_collections.ibm.storage_virtualize.plugins.module_utils.'
           'ibm_svc_utils.IBMSVCRestApi._svc_authorize')
    def test_create_transient_snapshot(self, svc_authorize_mock, svc_run_cmd_mock):
        set_module_args({
            'clustername': 'clustername',
            'domain': 'domain',
            'username': 'username',
            'password': 'password',
            'name': 'new_name',
            'state': 'present',
            'type': 'thinclone',
            'fromsourcevolume': 'vol1'
        })
        svc_run_cmd_mock.return_value = {
            "id": "3",
            "message": "Snapshot, id [3], successfully created or triggered"
        }
        v = IBMSVCvolume()
        snapshot_id = v.create_transient_snapshot()
        self.assertEqual(snapshot_id, '3')

    # converttoclone implementation UTs: SKG:DBG
    # Convert thinclone volume to clone
    @patch('ansible_collections.ibm.storage_virtualize.plugins.module_utils.'
           'ibm_svc_utils.IBMSVCRestApi.svc_obj_info')
    @patch('ansible_collections.ibm.storage_virtualize.plugins.module_utils.'
           'ibm_svc_utils.IBMSVCRestApi.svc_run_command')
    @patch('ansible_collections.ibm.storage_virtualize.plugins.module_utils.'
           'ibm_svc_utils.IBMSVCRestApi._svc_authorize')
    def test_convert_thinclone_volume_to_clone(self, svc_authorize_mock, svc_run_command_mock, svc_obj_info_mock):
        set_module_args({
            'clustername': 'clustername',
            'domain': 'domain',
            'state': 'present',
            'username': 'username',
            'password': 'password',
            'name': 'vol0',
            'type': 'clone'
        })

        # 3 volumes are enough for all converttoclone scenarios.
        # One currently thinclone, one clone and with blank volume_type

        svc_obj_info_mock.return_value = [
            {"id": "0", "name": "vol0", "volume_type": "thinclone"},
            {"id": "1", "name": "vol1", "volume_type": "clone"},
            {"id": "2", "name": "vol2", "volume_type": ""}
        ]

        svc_run_command_mock.return_value = ""

        with pytest.raises(AnsibleExitJson) as exc:
            v = IBMSVCvolume()
            v.apply()
        self.assertTrue(exc.value.args[0]['changed'])

    # Try converting such volume to clone which is in copying state (i.e. volume_type=clone currently)
    @patch('ansible_collections.ibm.storage_virtualize.plugins.module_utils.'
           'ibm_svc_utils.IBMSVCRestApi.svc_obj_info')
    @patch('ansible_collections.ibm.storage_virtualize.plugins.module_utils.'
           'ibm_svc_utils.IBMSVCRestApi.svc_run_command')
    @patch('ansible_collections.ibm.storage_virtualize.plugins.module_utils.'
           'ibm_svc_utils.IBMSVCRestApi._svc_authorize')
    def test_convert_thinclone_volume_to_clone_idempotency_when_copy_in_progress(self,
                                                                                 svc_authorize_mock,
                                                                                 svc_run_command_mock,
                                                                                 svc_obj_info_mock):
        set_module_args({
            'clustername': 'clustername',
            'domain': 'domain',
            'state': 'present',
            'username': 'username',
            'password': 'password',
            'name': 'vol1',
            'type': 'clone'
        })

        svc_obj_info_mock.return_value = [
            {"id": "0", "name": "vol0", "volume_type": "thinclone"},
            {"id": "1", "name": "vol1", "volume_type": "clone"},
            {"id": "2", "name": "vol2", "volume_type": ""}
        ]

        svc_run_command_mock.return_value = ""

        with pytest.raises(AnsibleExitJson) as exc:
            v = IBMSVCvolume()
            v.apply()
        self.assertFalse(exc.value.args[0]['changed'])
        self.assertEqual(exc.value.args[0]['msg'], 'Volume vol1 is not a thinclone.')

    # Try converting an already cloned volume to clone (for which volume_type is clone
    # currently, becaue copy is still in progress); should pass.
    @patch('ansible_collections.ibm.storage_virtualize.plugins.module_utils.'
           'ibm_svc_utils.IBMSVCRestApi.svc_obj_info')
    @patch('ansible_collections.ibm.storage_virtualize.plugins.module_utils.'
           'ibm_svc_utils.IBMSVCRestApi.svc_run_command')
    @patch('ansible_collections.ibm.storage_virtualize.plugins.module_utils.'
           'ibm_svc_utils.IBMSVCRestApi._svc_authorize')
    def test_convert_thinclone_volume_to_clone_idempotency(self,
                                                           svc_authorize_mock,
                                                           svc_run_command_mock,
                                                           svc_obj_info_mock):
        set_module_args({
            'clustername': 'clustername',
            'domain': 'domain',
            'state': 'present',
            'username': 'username',
            'password': 'password',
            'name': 'vol1',
            'type': 'clone'
        })

        svc_obj_info_mock.return_value = [
            {"id": "0", "name": "vol0", "volume_type": "thinclone"},
            {"id": "1", "name": "vol1", "volume_type": "clone"},
            {"id": "2", "name": "vol2", "volume_type": ""}
        ]

        svc_run_command_mock.return_value = ""

        with pytest.raises(AnsibleExitJson) as exc:
            v = IBMSVCvolume()
            v.apply()
        self.assertFalse(exc.value.args[0]['changed'])
        self.assertEqual(exc.value.args[0]['msg'], 'Volume vol2 is not a thinclone.')

    # Convert thinclone volume to clone
    @patch('ansible_collections.ibm.storage_virtualize.plugins.module_utils.'
           'ibm_svc_utils.IBMSVCRestApi.svc_obj_info')
    @patch('ansible_collections.ibm.storage_virtualize.plugins.module_utils.'
           'ibm_svc_utils.IBMSVCRestApi.svc_run_command')
    @patch('ansible_collections.ibm.storage_virtualize.plugins.module_utils.'
           'ibm_svc_utils.IBMSVCRestApi._svc_authorize')
    def test_convert_thinclone_volume_to_clone(self,
                                               svc_authorize_mock,
                                               svc_run_command_mock,
                                               svc_obj_info_mock):
        set_module_args({
            'clustername': 'clustername',
            'domain': 'domain',
            'state': 'present',
            'username': 'username',
            'password': 'password',
            'name': 'vol0',
            'type': 'clone'
        })

        # 3 volumes are enough for all converttoclone scenarios.
        # One currently thinclone, one clone and with blank volume_type

        svc_obj_info_mock.return_value = [
            {"id": "0", "name": "vol0", "volume_type": "thinclone"}
        ]

        svc_run_command_mock.return_value = ""

        with pytest.raises(AnsibleExitJson) as exc:
            v = IBMSVCvolume()
            v.apply()
        self.assertTrue(exc.value.args[0]['changed'])

    # Try converting such volume to clone which is in copying state (i.e. volume_type=clone currently)
    @patch('ansible_collections.ibm.storage_virtualize.plugins.module_utils.'
           'ibm_svc_utils.IBMSVCRestApi.svc_obj_info')
    @patch('ansible_collections.ibm.storage_virtualize.plugins.module_utils.'
           'ibm_svc_utils.IBMSVCRestApi.svc_run_command')
    @patch('ansible_collections.ibm.storage_virtualize.plugins.module_utils.'
           'ibm_svc_utils.IBMSVCRestApi._svc_authorize')
    def test_convert_thinclone_volume_to_clone_idempotency_when_copy_in_progress(self,
                                                                                 svc_authorize_mock,
                                                                                 svc_run_command_mock,
                                                                                 svc_obj_info_mock):
        set_module_args({
            'clustername': 'clustername',
            'domain': 'domain',
            'state': 'present',
            'username': 'username',
            'password': 'password',
            'name': 'vol1',
            'type': 'clone'
        })

        svc_obj_info_mock.return_value = [
            {"id": "1", "name": "vol1", "volume_type": "clone"}
        ]

        svc_run_command_mock.return_value = ""

        with pytest.raises(AnsibleExitJson) as exc:
            v = IBMSVCvolume()
            v.apply()
        self.assertFalse(exc.value.args[0]['changed'])
        self.assertEqual(exc.value.args[0]['msg'], 'Volume vol1 is not a thinclone.')

    # Try converting a normal volume to clone; should pass without any change because
    # volume might have converted to clone previously and copy might have been completed.
    # Once copy completes, a cloned volume's volume_type changes to blank.
    @patch('ansible_collections.ibm.storage_virtualize.plugins.module_utils.'
           'ibm_svc_utils.IBMSVCRestApi.svc_obj_info')
    @patch('ansible_collections.ibm.storage_virtualize.plugins.module_utils.'
           'ibm_svc_utils.IBMSVCRestApi.svc_run_command')
    @patch('ansible_collections.ibm.storage_virtualize.plugins.module_utils.'
           'ibm_svc_utils.IBMSVCRestApi._svc_authorize')
    def test_convert_thinclone_volume_to_clone_idempotency(self,
                                                           svc_authorize_mock,
                                                           svc_run_command_mock,
                                                           svc_obj_info_mock):
        set_module_args({
            'clustername': 'clustername',
            'domain': 'domain',
            'state': 'present',
            'username': 'username',
            'password': 'password',
            'name': 'vol2',
            'type': 'clone'
        })

        svc_obj_info_mock.return_value = [
            {"id": "2", "name": "vol2", "volume_type": ""}
        ]

        svc_run_command_mock.return_value = ""

        with pytest.raises(AnsibleExitJson) as exc:
            v = IBMSVCvolume()
            v.apply()
        self.assertFalse(exc.value.args[0]['changed'])
        self.assertEqual(exc.value.args[0]['msg'], 'Volume vol2 is not a thinclone.')

    @patch('ansible_collections.ibm.storage_virtualize.plugins.module_utils.'
           'ibm_svc_utils.IBMSVCRestApi.svc_obj_info')
    @patch('ansible_collections.ibm.storage_virtualize.plugins.module_utils.'
           'ibm_svc_utils.IBMSVCRestApi.svc_run_command')
    @patch('ansible_collections.ibm.storage_virtualize.plugins.module_utils.'
           'ibm_svc_utils.IBMSVCRestApi._svc_authorize')
    def test_convert_thinclone_volume_list_to_clone(self,
                                                    svc_authorize_mock,
                                                    svc_run_command_mock,
                                                    svc_obj_info_mock):
        # Test converting a list of volumes to clone when all of them are thinclone
        set_module_args({
            'clustername': 'clustername',
            'domain': 'domain',
            'state': 'present',
            'username': 'username',
            'password': 'password',
            'name': 'vol0:vol1:vol2',
            'type': 'clone'
        })

        svc_obj_info_mock.return_value = [
            {"id": "0", "name": "vol0", "volume_type": "thinclone"},
            {"id": "1", "name": "vol1", "volume_type": "thinclone"},
            {"id": "2", "name": "vol2", "volume_type": "thinclone"}
        ]

        svc_run_command_mock.return_value = ""

        with pytest.raises(AnsibleExitJson) as exc:
            v = IBMSVCvolume()
            v.apply()
        self.assertTrue(exc.value.args[0]['changed'])
        self.assertEqual(exc.value.args[0]['msg'], 'Volume(s) [vol0:vol1:vol2] converted to clone.')

    @patch('ansible_collections.ibm.storage_virtualize.plugins.module_utils.'
           'ibm_svc_utils.IBMSVCRestApi.svc_obj_info')
    @patch('ansible_collections.ibm.storage_virtualize.plugins.module_utils.'
           'ibm_svc_utils.IBMSVCRestApi.svc_run_command')
    @patch('ansible_collections.ibm.storage_virtualize.plugins.module_utils.'
           'ibm_svc_utils.IBMSVCRestApi._svc_authorize')
    def test_convert_mixed_type_volume_list_to_clone(self,
                                                     svc_authorize_mock,
                                                     svc_run_command_mock,
                                                     svc_obj_info_mock):
        # Test converting a list of volumes to clone when some of them are thinclone
        # and others are in copying state (i.e. volume_type=clone currently)
        # Idempotency case where a subset of volumes has been cloned
        set_module_args({
            'clustername': 'clustername',
            'domain': 'domain',
            'state': 'present',
            'username': 'username',
            'password': 'password',
            'name': 'vol0:vol1:vol2',
            'type': 'clone'
        })

        svc_obj_info_mock.return_value = [
            {"id": "0", "name": "vol0", "volume_type": "thinclone"},
            {"id": "1", "name": "vol1", "volume_type": "clone"},
            {"id": "2", "name": "vol2", "volume_type": "thinclone"}
        ]

        svc_run_command_mock.return_value = ""

        with pytest.raises(AnsibleExitJson) as exc:
            v = IBMSVCvolume()
            v.apply()
        self.assertTrue(exc.value.args[0]['changed'])
        self.assertEqual(exc.value.args[0]['msg'], 'Volume(s) [vol0:vol1:vol2] converted to clone.')

    @patch('ansible_collections.ibm.storage_virtualize.plugins.module_utils.'
           'ibm_svc_utils.IBMSVCRestApi.svc_obj_info')
    @patch('ansible_collections.ibm.storage_virtualize.plugins.module_utils.'
           'ibm_svc_utils.IBMSVCRestApi.svc_run_command')
    @patch('ansible_collections.ibm.storage_virtualize.plugins.module_utils.'
           'ibm_svc_utils.IBMSVCRestApi._svc_authorize')
    def test_convert_thinclone_volume_list_to_clone_idempotency(self,
                                                                svc_authorize_mock,
                                                                svc_run_command_mock,
                                                                svc_obj_info_mock):
        # Test converting a list of volumes to clone when none of them are thinclone
        # Idempotency case where a all volumes have either been cloned or were not
        # thinclone originally (but ansible does not know which case is true, so pass it)
        set_module_args({
            'clustername': 'clustername',
            'domain': 'domain',
            'state': 'present',
            'username': 'username',
            'password': 'password',
            'name': 'vol0:vol1:vol2',
            'type': 'clone'
        })

        svc_obj_info_mock.return_value = [
            {"id": "0", "name": "vol0", "volume_type": ""},
            {"id": "1", "name": "vol1", "volume_type": ""},
            {"id": "2", "name": "vol2", "volume_type": ""}
        ]

        svc_run_command_mock.return_value = ""

        with pytest.raises(AnsibleExitJson) as exc:
            v = IBMSVCvolume()
            v.apply()
        self.assertFalse(exc.value.args[0]['changed'])
        self.assertEqual(exc.value.args[0]['msg'], 'Volume(s) [vol0:vol1:vol2] are not thinclone!!')

    @patch('ansible_collections.ibm.storage_virtualize.plugins.module_utils.'
           'ibm_svc_utils.IBMSVCRestApi.svc_obj_info')
    @patch('ansible_collections.ibm.storage_virtualize.plugins.module_utils.'
           'ibm_svc_utils.IBMSVCRestApi.svc_run_command')
    @patch('ansible_collections.ibm.storage_virtualize.plugins.module_utils.'
           'ibm_svc_utils.IBMSVCRestApi._svc_authorize')
    def test_failure_convert_invalid_volumes_in_list_to_clone(self,
                                                              svc_authorize_mock,
                                                              svc_run_command_mock,
                                                              svc_obj_info_mock):
        # Test converting a list of volumes to clone when some of them are invalid,
        # meaning they don't exist on the cluster (vol1 and vol4 in this example)
        set_module_args({
            'clustername': 'clustername',
            'domain': 'domain',
            'state': 'present',
            'username': 'username',
            'password': 'password',
            'name': 'vol0:vol1:vol2:vol4',
            'type': 'clone'
        })

        svc_obj_info_mock.return_value = [
            {"id": "0", "name": "vol0", "volume_type": "thinclone"},
            {"id": "2", "name": "vol2", "volume_type": ""},
            {"id": "3", "name": "vol3", "volume_type": ""},
        ]

        svc_run_command_mock.return_value = ""

        with pytest.raises(AnsibleFailJson) as exc:
            v = IBMSVCvolume()
            v.apply()
        self.assertEqual(exc.value.args[0]['msg'], 'CMMVC9855E The command failed because one or more of'
                         ' the specified volumes does not exist.')

    @patch('ansible_collections.ibm.storage_virtualize.plugins.module_utils.'
           'ibm_svc_utils.IBMSVCRestApi.svc_obj_info')
    @patch('ansible_collections.ibm.storage_virtualize.plugins.module_utils.'
           'ibm_svc_utils.IBMSVCRestApi._svc_authorize')
    def test_failure_volume_creation_warning_invalid_params(self,
                                                            svc_authorize_mock,
                                                            svc_obj_info_mock):
        """
        Parameter [warning] is invalid without [thin] or [compressed]
        """
        set_module_args({
            'clustername': 'clustername',
            'domain': 'domain',
            'state': 'present',
            'username': 'username',
            'password': 'password',
            'name': 'test_volume',
            'pool': 'test_pool',
            'size': '1',
            'unit': 'gb',
            'volumegroup': 'test_volumegroup',
            'warning': '70'
        })
        svc_obj_info_mock.side_effect = [{}]  # lsvdisk [name]
        with pytest.raises(AnsibleFailJson) as exc:
            v = IBMSVCvolume()
            v.apply()
        self.assertTrue(exc.value.args[0]['failed'])
        self.assertEqual(exc.value.args[0]['msg'], "Parameter [warning] is invalid without [thin] or [compressed]")

    @patch('ansible_collections.ibm.storage_virtualize.plugins.module_utils.'
           'ibm_svc_utils.IBMSVCRestApi.svc_run_command')
    @patch('ansible_collections.ibm.storage_virtualize.plugins.module_utils.'
           'ibm_svc_utils.IBMSVCRestApi.svc_obj_info')
    @patch('ansible_collections.ibm.storage_virtualize.plugins.module_utils.'
           'ibm_svc_utils.IBMSVCRestApi._svc_authorize')
    def test_volume_creation_thin_with_warning(self,
                                               svc_authorize_mock,
                                               svc_obj_info_mock,
                                               svc_run_command_mock):
        """
        Create a thin-provisioned volume with warning.
        """
        set_module_args({
            'clustername': 'clustername',
            'domain': 'domain',
            'state': 'present',
            'username': 'username',
            'password': 'password',
            'name': 'test_volume',
            'pool': 'test_pool',
            'size': '1',
            'unit': 'gb',
            'volumegroup': 'test_volumegroup',
            'thin': True,
            'warning': '70'
        })
        svc_obj_info_mock.side_effect = [{}]  # lsvdisk [name]
        svc_run_command_mock.return_value = {
            'id': '25',
            'message': 'Volume, id [25], successfully created'
        }
        with pytest.raises(AnsibleExitJson) as exc:
            v = IBMSVCvolume()
            v.apply()
        self.assertTrue(exc.value.args[0]['changed'])

    @patch('ansible_collections.ibm.storage_virtualize.plugins.module_utils.'
           'ibm_svc_utils.IBMSVCRestApi.svc_run_command')
    @patch('ansible_collections.ibm.storage_virtualize.plugins.module_utils.'
           'ibm_svc_utils.IBMSVCRestApi.svc_obj_info')
    @patch('ansible_collections.ibm.storage_virtualize.plugins.module_utils.'
           'ibm_svc_utils.IBMSVCRestApi._svc_authorize')
    def test_volume_creation_compressed_with_warning(self,
                                                     svc_authorize_mock,
                                                     svc_obj_info_mock,
                                                     svc_run_command_mock):
        """
        Create a compressed volume with warning.
        """
        set_module_args({
            'clustername': 'clustername',
            'domain': 'domain',
            'state': 'present',
            'username': 'username',
            'password': 'password',
            'name': 'test_volume',
            'pool': 'test_pool',
            'size': '1',
            'unit': 'gb',
            'volumegroup': 'test_volumegroup',
            'compressed': True,
            'warning': '70'
        })
        svc_obj_info_mock.side_effect = [{}]  # lsvdisk [name]
        svc_run_command_mock.return_value = {
            'id': '25',
            'message': 'Volume, id [25], successfully created'
        }
        with pytest.raises(AnsibleExitJson) as exc:
            v = IBMSVCvolume()
            v.apply()
        self.assertTrue(exc.value.args[0]['changed'])

    @patch('ansible_collections.ibm.storage_virtualize.plugins.module_utils.'
           'ibm_svc_utils.IBMSVCRestApi.svc_run_command')
    @patch('ansible_collections.ibm.storage_virtualize.plugins.module_utils.'
           'ibm_svc_utils.IBMSVCRestApi.svc_obj_info')
    @patch('ansible_collections.ibm.storage_virtualize.plugins.module_utils.'
           'ibm_svc_utils.IBMSVCRestApi._svc_authorize')
    def test_failure_volume_warning_update_invalid_vol_type(self,
                                                            svc_authorize_mock,
                                                            svc_obj_info_mock,
                                                            svc_run_command_mock):
        """
        Parameter [warning] is applicable only for thin-provisioned and compressed volumes.
        """
        set_module_args({
            'clustername': 'clustername',
            'domain': 'domain',
            'state': 'present',
            'username': 'username',
            'password': 'password',
            'name': 'test_volume',
            'size': '1',
            'unit': 'gb',
            'warning': '70'
        })
        svc_obj_info_mock.side_effect = [
            [
                {"capacity": "1073741824", "type": "striped", "RC_name": ""},
                {"real_capacity": "1073741824", "warning": "80", "compressed_copy": "no"}
            ]  # lsvdisk [name]
        ]
        with pytest.raises(AnsibleFailJson) as exc:
            v = IBMSVCvolume()
            v.apply()
        self.assertTrue(exc.value.args[0]['failed'])
        self.assertEqual(exc.value.args[0]['msg'], 'Parameter [warning] is applicable only for thin-provisioned and compressed volumes.')

    @patch('ansible_collections.ibm.storage_virtualize.plugins.module_utils.'
           'ibm_svc_utils.IBMSVCRestApi.svc_run_command')
    @patch('ansible_collections.ibm.storage_virtualize.plugins.module_utils.'
           'ibm_svc_utils.IBMSVCRestApi.svc_obj_info')
    @patch('ansible_collections.ibm.storage_virtualize.plugins.module_utils.'
           'ibm_svc_utils.IBMSVCRestApi._svc_authorize')
    def test_volume_warning_update_thin(self,
                                        svc_authorize_mock,
                                        svc_obj_info_mock,
                                        svc_run_command_mock):
        """
        Update the warning parameter when volume is of type thin-provisioned
        """
        set_module_args({
            'clustername': 'clustername',
            'domain': 'domain',
            'state': 'present',
            'username': 'username',
            'password': 'password',
            'name': 'test_volume',
            'size': '1',
            'unit': 'gb',
            'warning': '70'
        })
        svc_obj_info_mock.side_effect = [
            [
                {"capacity": "1073741824", "RC_name": "", "type": "striped"},
                {"real_capacity": "1073741820", "compressed_copy": "no", "warning": "80"}
            ]  # lsvdisk [name]
        ]
        with pytest.raises(AnsibleExitJson) as exc:
            v = IBMSVCvolume()
            v.apply()
        self.assertTrue(exc.value.args[0]['changed'])

    @patch('ansible_collections.ibm.storage_virtualize.plugins.module_utils.'
           'ibm_svc_utils.IBMSVCRestApi.svc_run_command')
    @patch('ansible_collections.ibm.storage_virtualize.plugins.module_utils.'
           'ibm_svc_utils.IBMSVCRestApi.svc_obj_info')
    @patch('ansible_collections.ibm.storage_virtualize.plugins.module_utils.'
           'ibm_svc_utils.IBMSVCRestApi._svc_authorize')
    def test_volume_warning_thin_idempotency(self,
                                             svc_authorize_mock,
                                             svc_obj_info_mock,
                                             svc_run_command_mock):
        """
        Update the warning parameter when volume is of type thin-provisioned
        """
        set_module_args({
            'clustername': 'clustername',
            'domain': 'domain',
            'state': 'present',
            'username': 'username',
            'password': 'password',
            'name': 'test_volume',
            'size': '1',
            'unit': 'gb',
            'warning': '70'
        })
        svc_obj_info_mock.side_effect = [
            [
                {"capacity": "1073741824", "RC_name": "", "type": "striped"},
                {"real_capacity": "1073741820", "compressed_copy": "no", "warning": "70"}
            ]  # lsvdisk [name]
        ]
        with pytest.raises(AnsibleExitJson) as exc:
            v = IBMSVCvolume()
            v.apply()
        self.assertFalse(exc.value.args[0]['changed'])

    @patch('ansible_collections.ibm.storage_virtualize.plugins.module_utils.'
           'ibm_svc_utils.IBMSVCRestApi.svc_run_command')
    @patch('ansible_collections.ibm.storage_virtualize.plugins.module_utils.'
           'ibm_svc_utils.IBMSVCRestApi.svc_obj_info')
    @patch('ansible_collections.ibm.storage_virtualize.plugins.module_utils.'
           'ibm_svc_utils.IBMSVCRestApi._svc_authorize')
    def test_volume_warning_update_compressed(self,
                                              svc_authorize_mock,
                                              svc_obj_info_mock,
                                              svc_run_command_mock):
        """
        Update the warning parameter when volume is of type compressed.
        """
        set_module_args({
            'clustername': 'clustername',
            'domain': 'domain',
            'state': 'present',
            'username': 'username',
            'password': 'password',
            'name': 'test_volume',
            'size': '1',
            'unit': 'gb',
            'warning': '70'
        })
        svc_obj_info_mock.side_effect = [
            [
                {"capacity": "1073741824", "RC_name": "", "type": "striped"},
                {"real_capacity": "1073741824", "compressed_copy": "yes", "warning": "80"}
            ]  # lsvdisk [name]
        ]
        with pytest.raises(AnsibleExitJson) as exc:
            v = IBMSVCvolume()
            v.apply()
        self.assertTrue(exc.value.args[0]['changed'])

    @patch('ansible_collections.ibm.storage_virtualize.plugins.module_utils.'
           'ibm_svc_utils.IBMSVCRestApi.svc_run_command')
    @patch('ansible_collections.ibm.storage_virtualize.plugins.module_utils.'
           'ibm_svc_utils.IBMSVCRestApi.svc_obj_info')
    @patch('ansible_collections.ibm.storage_virtualize.plugins.module_utils.'
           'ibm_svc_utils.IBMSVCRestApi._svc_authorize')
    def test_volume_warning_compressed_idempotency(self,
                                                   svc_authorize_mock,
                                                   svc_obj_info_mock,
                                                   svc_run_command_mock):
        """
        Update the warning parameter when volume is of type compressed.
        """
        set_module_args({
            'clustername': 'clustername',
            'domain': 'domain',
            'state': 'present',
            'username': 'username',
            'password': 'password',
            'name': 'test_volume',
            'size': '1',
            'unit': 'gb',
            'warning': '70'
        })
        svc_obj_info_mock.side_effect = [
            [
                {"capacity": "1073741824", "RC_name": "", "type": "striped"},
                {"real_capacity": "1073741824", "compressed_copy": "yes", "warning": "70"}
            ]  # lsvdisk [name]
        ]
        with pytest.raises(AnsibleExitJson) as exc:
            v = IBMSVCvolume()
            v.apply()
        self.assertFalse(exc.value.args[0]['changed'])

    @patch('ansible_collections.ibm.storage_virtualize.plugins.module_utils.'
           'ibm_svc_utils.IBMSVCRestApi.svc_obj_info')
    @patch('ansible_collections.ibm.storage_virtualize.plugins.module_utils.'
           'ibm_svc_utils.IBMSVCRestApi._svc_authorize')
    def test_failure_volume_delete_with_invalid_params(self,
                                                       svc_authorize_mock,
                                                       svc_obj_info_mock):
        """
        Following parameter(s) are invalid while deletion of volume: warning
        """
        set_module_args({
            'clustername': 'clustername',
            'domain': 'domain',
            'state': 'absent',
            'username': 'username',
            'password': 'password',
            'name': 'test_volume',
            'warning': '70'
        })
        svc_obj_info_mock.side_effect = [
            [
                {"capacity": "1073741824", "RC_name": "", "type": "striped"},
                {"real_capacity": "1073741824", "compressed_copy": "yes", "warning": "70"}
            ]  # lsvdisk [name]
        ]
        with pytest.raises(AnsibleFailJson) as exc:
            v = IBMSVCvolume()
            v.apply()
        self.assertTrue(exc.value.args[0]['failed'])
        self.assertEqual(exc.value.args[0]['msg'], "Following parameter(s) are invalid while deletion of volume: warning")


if __name__ == '__main__':
    unittest.main()
