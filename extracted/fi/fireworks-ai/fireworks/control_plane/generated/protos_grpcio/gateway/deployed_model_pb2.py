# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: gateway/deployed_model.proto
# Protobuf Python Version: 5.29.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    29,
    0,
    '',
    'gateway/deployed_model.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from . import options_pb2 as gateway_dot_options__pb2
from . import status_pb2 as gateway_dot_status__pb2
from ..google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from ..google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from ..google.api import visibility_pb2 as google_dot_api_dot_visibility__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1cgateway/deployed_model.proto\x12\x07gateway\x1a\x15gateway/options.proto\x1a\x14gateway/status.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a\x1bgoogle/api/visibility.proto\x1a google/protobuf/field_mask.proto\x1a\x1fgoogle/protobuf/timestamp.proto\"\x98\x05\n\rDeployedModel\x12\x13\n\x04name\x18\x01 \x01(\tB\x05\xe2\x41\x02\x03\x05\x12\x1a\n\x0c\x64isplay_name\x18\x02 \x01(\tB\x04\xe2\x41\x01\x01\x12\x19\n\x0b\x64\x65scription\x18\x03 \x01(\tB\x04\xe2\x41\x01\x01\x12\x36\n\x0b\x63reate_time\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.TimestampB\x05\xe2\x41\x02\x03\x05\x12+\n\ncreated_by\x18\x05 \x01(\tB\x17\xe2\x41\x02\x03\x05\xfa\xd2\xe4\x93\x02\x0c\x12\nOWNER_ONLY\x12\r\n\x05model\x18\x06 \x01(\t\x12\x12\n\ndeployment\x18\x07 \x01(\t\x12\x0f\n\x07\x64\x65\x66\x61ult\x18\x08 \x01(\x08\x12\x32\n\x05state\x18\t \x01(\x0e\x32\x1c.gateway.DeployedModel.StateB\x05\xe2\x41\x02\x03\x05\x12\x12\n\nserverless\x18\n \x01(\x08\x12&\n\x06status\x18\x0b \x01(\x0b\x32\x0f.gateway.StatusB\x05\xe2\x41\x02\x03\x05\x12\x0e\n\x06public\x18\x0c \x01(\x08\x12\x35\n\x0bupdate_time\x18\r \x01(\x0b\x32\x1a.google.protobuf.TimestampB\x04\xe2\x41\x01\x03\"`\n\x05State\x12\x15\n\x11STATE_UNSPECIFIED\x10\x00\x12\x0f\n\x0bUNDEPLOYING\x10\x01\x12\r\n\tDEPLOYING\x10\x02\x12\x0c\n\x08\x44\x45PLOYED\x10\x03\x12\x0c\n\x08UPDATING\x10\x04\"\x04\x08\x05\x10\x05:\x88\x01\xea\x41v\n\x1e\x61pi.fireworks.ai/DeployedModel\x12\x35\x61\x63\x63ounts/{AccountId}/deployedModels/{DeployedModelId}*\x0e\x64\x65ployedModels2\rdeployedModel\x82\xf1\x04\x0b\n\x07\x41\x63\x63ount\x18\x01\"\xa1\x01\n\x10\x44\x65ployedModelRef\x12\x13\n\x04name\x18\x01 \x01(\tB\x05\xe2\x41\x02\x03\x05\x12\x18\n\ndeployment\x18\x02 \x01(\tB\x04\xe2\x41\x01\x03\x12\x31\n\x05state\x18\x03 \x01(\x0e\x32\x1c.gateway.DeployedModel.StateB\x04\xe2\x41\x01\x03\x12\x15\n\x07\x64\x65\x66\x61ult\x18\x04 \x01(\x08\x42\x04\xe2\x41\x01\x03\x12\x14\n\x06public\x18\x05 \x01(\x08\x42\x04\xe2\x41\x01\x03\"h\n\x1a\x43reateDeployedModelRequest\x12\x14\n\x06parent\x18\x01 \x01(\tB\x04\xe2\x41\x01\x02\x12\x34\n\x0e\x64\x65ployed_model\x18\x02 \x01(\x0b\x32\x16.gateway.DeployedModelB\x04\xe2\x41\x01\x02\"0\n\x1a\x44\x65leteDeployedModelRequest\x12\x12\n\x04name\x18\x01 \x01(\tB\x04\xe2\x41\x01\x02\"b\n\x17GetDeployedModelRequest\x12\x12\n\x04name\x18\x01 \x01(\tB\x04\xe2\x41\x01\x02\x12\x33\n\tread_mask\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.FieldMaskB\x04\xe2\x41\x01\x01\"\xfa\x01\n\x19ListDeployedModelsRequest\x12\x14\n\x06parent\x18\x01 \x01(\tB\x04\xe2\x41\x01\x02\x12\x17\n\tpage_size\x18\x02 \x01(\x05\x42\x04\xe2\x41\x01\x01\x12\x18\n\npage_token\x18\x03 \x01(\tB\x04\xe2\x41\x01\x01\x12\x14\n\x06\x66ilter\x18\x04 \x01(\tB\x04\xe2\x41\x01\x01\x12\x16\n\x08order_by\x18\x05 \x01(\tB\x04\xe2\x41\x01\x01\x12\x33\n\tread_mask\x18\x06 \x01(\x0b\x32\x1a.google.protobuf.FieldMaskB\x04\xe2\x41\x01\x01\x12\x31\n\rshow_internal\x18\x07 \x01(\x08\x42\x1a\xe2\x41\x01\x01\xfa\xd2\xe4\x93\x02\x10\x12\x0eSUPERUSER_ONLY\"z\n\x1aListDeployedModelsResponse\x12/\n\x0f\x64\x65ployed_models\x18\x01 \x03(\x0b\x32\x16.gateway.DeployedModel\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\x12\x12\n\ntotal_size\x18\x03 \x01(\x05\"\x89\x01\n\x1aUpdateDeployedModelRequest\x12\x34\n\x0e\x64\x65ployed_model\x18\x01 \x01(\x0b\x32\x16.gateway.DeployedModelB\x04\xe2\x41\x01\x02\x12\x35\n\x0bupdate_mask\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.FieldMaskB\x04\xe2\x41\x01\x01\x42\x43ZAgithub.com/fw-ai/fireworks/control_plane/protos/generated/gatewayb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'gateway.deployed_model_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'ZAgithub.com/fw-ai/fireworks/control_plane/protos/generated/gateway'
  _globals['_DEPLOYEDMODEL'].fields_by_name['name']._loaded_options = None
  _globals['_DEPLOYEDMODEL'].fields_by_name['name']._serialized_options = b'\342A\002\003\005'
  _globals['_DEPLOYEDMODEL'].fields_by_name['display_name']._loaded_options = None
  _globals['_DEPLOYEDMODEL'].fields_by_name['display_name']._serialized_options = b'\342A\001\001'
  _globals['_DEPLOYEDMODEL'].fields_by_name['description']._loaded_options = None
  _globals['_DEPLOYEDMODEL'].fields_by_name['description']._serialized_options = b'\342A\001\001'
  _globals['_DEPLOYEDMODEL'].fields_by_name['create_time']._loaded_options = None
  _globals['_DEPLOYEDMODEL'].fields_by_name['create_time']._serialized_options = b'\342A\002\003\005'
  _globals['_DEPLOYEDMODEL'].fields_by_name['created_by']._loaded_options = None
  _globals['_DEPLOYEDMODEL'].fields_by_name['created_by']._serialized_options = b'\342A\002\003\005\372\322\344\223\002\014\022\nOWNER_ONLY'
  _globals['_DEPLOYEDMODEL'].fields_by_name['state']._loaded_options = None
  _globals['_DEPLOYEDMODEL'].fields_by_name['state']._serialized_options = b'\342A\002\003\005'
  _globals['_DEPLOYEDMODEL'].fields_by_name['status']._loaded_options = None
  _globals['_DEPLOYEDMODEL'].fields_by_name['status']._serialized_options = b'\342A\002\003\005'
  _globals['_DEPLOYEDMODEL'].fields_by_name['update_time']._loaded_options = None
  _globals['_DEPLOYEDMODEL'].fields_by_name['update_time']._serialized_options = b'\342A\001\003'
  _globals['_DEPLOYEDMODEL']._loaded_options = None
  _globals['_DEPLOYEDMODEL']._serialized_options = b'\352Av\n\036api.fireworks.ai/DeployedModel\0225accounts/{AccountId}/deployedModels/{DeployedModelId}*\016deployedModels2\rdeployedModel\202\361\004\013\n\007Account\030\001'
  _globals['_DEPLOYEDMODELREF'].fields_by_name['name']._loaded_options = None
  _globals['_DEPLOYEDMODELREF'].fields_by_name['name']._serialized_options = b'\342A\002\003\005'
  _globals['_DEPLOYEDMODELREF'].fields_by_name['deployment']._loaded_options = None
  _globals['_DEPLOYEDMODELREF'].fields_by_name['deployment']._serialized_options = b'\342A\001\003'
  _globals['_DEPLOYEDMODELREF'].fields_by_name['state']._loaded_options = None
  _globals['_DEPLOYEDMODELREF'].fields_by_name['state']._serialized_options = b'\342A\001\003'
  _globals['_DEPLOYEDMODELREF'].fields_by_name['default']._loaded_options = None
  _globals['_DEPLOYEDMODELREF'].fields_by_name['default']._serialized_options = b'\342A\001\003'
  _globals['_DEPLOYEDMODELREF'].fields_by_name['public']._loaded_options = None
  _globals['_DEPLOYEDMODELREF'].fields_by_name['public']._serialized_options = b'\342A\001\003'
  _globals['_CREATEDEPLOYEDMODELREQUEST'].fields_by_name['parent']._loaded_options = None
  _globals['_CREATEDEPLOYEDMODELREQUEST'].fields_by_name['parent']._serialized_options = b'\342A\001\002'
  _globals['_CREATEDEPLOYEDMODELREQUEST'].fields_by_name['deployed_model']._loaded_options = None
  _globals['_CREATEDEPLOYEDMODELREQUEST'].fields_by_name['deployed_model']._serialized_options = b'\342A\001\002'
  _globals['_DELETEDEPLOYEDMODELREQUEST'].fields_by_name['name']._loaded_options = None
  _globals['_DELETEDEPLOYEDMODELREQUEST'].fields_by_name['name']._serialized_options = b'\342A\001\002'
  _globals['_GETDEPLOYEDMODELREQUEST'].fields_by_name['name']._loaded_options = None
  _globals['_GETDEPLOYEDMODELREQUEST'].fields_by_name['name']._serialized_options = b'\342A\001\002'
  _globals['_GETDEPLOYEDMODELREQUEST'].fields_by_name['read_mask']._loaded_options = None
  _globals['_GETDEPLOYEDMODELREQUEST'].fields_by_name['read_mask']._serialized_options = b'\342A\001\001'
  _globals['_LISTDEPLOYEDMODELSREQUEST'].fields_by_name['parent']._loaded_options = None
  _globals['_LISTDEPLOYEDMODELSREQUEST'].fields_by_name['parent']._serialized_options = b'\342A\001\002'
  _globals['_LISTDEPLOYEDMODELSREQUEST'].fields_by_name['page_size']._loaded_options = None
  _globals['_LISTDEPLOYEDMODELSREQUEST'].fields_by_name['page_size']._serialized_options = b'\342A\001\001'
  _globals['_LISTDEPLOYEDMODELSREQUEST'].fields_by_name['page_token']._loaded_options = None
  _globals['_LISTDEPLOYEDMODELSREQUEST'].fields_by_name['page_token']._serialized_options = b'\342A\001\001'
  _globals['_LISTDEPLOYEDMODELSREQUEST'].fields_by_name['filter']._loaded_options = None
  _globals['_LISTDEPLOYEDMODELSREQUEST'].fields_by_name['filter']._serialized_options = b'\342A\001\001'
  _globals['_LISTDEPLOYEDMODELSREQUEST'].fields_by_name['order_by']._loaded_options = None
  _globals['_LISTDEPLOYEDMODELSREQUEST'].fields_by_name['order_by']._serialized_options = b'\342A\001\001'
  _globals['_LISTDEPLOYEDMODELSREQUEST'].fields_by_name['read_mask']._loaded_options = None
  _globals['_LISTDEPLOYEDMODELSREQUEST'].fields_by_name['read_mask']._serialized_options = b'\342A\001\001'
  _globals['_LISTDEPLOYEDMODELSREQUEST'].fields_by_name['show_internal']._loaded_options = None
  _globals['_LISTDEPLOYEDMODELSREQUEST'].fields_by_name['show_internal']._serialized_options = b'\342A\001\001\372\322\344\223\002\020\022\016SUPERUSER_ONLY'
  _globals['_UPDATEDEPLOYEDMODELREQUEST'].fields_by_name['deployed_model']._loaded_options = None
  _globals['_UPDATEDEPLOYEDMODELREQUEST'].fields_by_name['deployed_model']._serialized_options = b'\342A\001\002'
  _globals['_UPDATEDEPLOYEDMODELREQUEST'].fields_by_name['update_mask']._loaded_options = None
  _globals['_UPDATEDEPLOYEDMODELREQUEST'].fields_by_name['update_mask']._serialized_options = b'\342A\001\001'
  _globals['_DEPLOYEDMODEL']._serialized_start=243
  _globals['_DEPLOYEDMODEL']._serialized_end=907
  _globals['_DEPLOYEDMODEL_STATE']._serialized_start=672
  _globals['_DEPLOYEDMODEL_STATE']._serialized_end=768
  _globals['_DEPLOYEDMODELREF']._serialized_start=910
  _globals['_DEPLOYEDMODELREF']._serialized_end=1071
  _globals['_CREATEDEPLOYEDMODELREQUEST']._serialized_start=1073
  _globals['_CREATEDEPLOYEDMODELREQUEST']._serialized_end=1177
  _globals['_DELETEDEPLOYEDMODELREQUEST']._serialized_start=1179
  _globals['_DELETEDEPLOYEDMODELREQUEST']._serialized_end=1227
  _globals['_GETDEPLOYEDMODELREQUEST']._serialized_start=1229
  _globals['_GETDEPLOYEDMODELREQUEST']._serialized_end=1327
  _globals['_LISTDEPLOYEDMODELSREQUEST']._serialized_start=1330
  _globals['_LISTDEPLOYEDMODELSREQUEST']._serialized_end=1580
  _globals['_LISTDEPLOYEDMODELSRESPONSE']._serialized_start=1582
  _globals['_LISTDEPLOYEDMODELSRESPONSE']._serialized_end=1704
  _globals['_UPDATEDEPLOYEDMODELREQUEST']._serialized_start=1707
  _globals['_UPDATEDEPLOYEDMODELREQUEST']._serialized_end=1844
# @@protoc_insertion_point(module_scope)
