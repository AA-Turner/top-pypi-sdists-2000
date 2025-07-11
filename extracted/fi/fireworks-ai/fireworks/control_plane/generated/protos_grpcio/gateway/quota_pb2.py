# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: gateway/quota.proto
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
    'gateway/quota.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from . import options_pb2 as gateway_dot_options__pb2
from ..google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from ..google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from ..google.api import visibility_pb2 as google_dot_api_dot_visibility__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x13gateway/quota.proto\x12\x07gateway\x1a\x15gateway/options.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a\x1bgoogle/api/visibility.proto\x1a google/protobuf/field_mask.proto\x1a\x1fgoogle/protobuf/timestamp.proto\"\xa2\x02\n\x05Quota\x12\x13\n\x04name\x18\x01 \x01(\tB\x05\xe2\x41\x02\x03\x05\x12\r\n\x05value\x18\x02 \x01(\x03\x12\x11\n\tmax_value\x18\x03 \x01(\x03\x12\x35\n\x0bupdate_time\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.TimestampB\x04\xe2\x41\x01\x03\x12K\n\x0b\x63reate_time\x18\x05 \x01(\x0b\x32\x1a.google.protobuf.TimestampB\x1a\xe2\x41\x01\x03\xfa\xd2\xe4\x93\x02\x10\x12\x0eSUPERUSER_ONLY:^\xea\x41N\n\x16\x61pi.fireworks.ai/Quota\x12%accounts/{AccountId}/quotas/{QuotaId}*\x06quotas2\x05quota\x82\xf1\x04\t\n\x07\x41\x63\x63ount\"Z\n\x0fGetQuotaRequest\x12\x12\n\x04name\x18\x01 \x01(\tB\x04\xe2\x41\x01\x02\x12\x33\n\tread_mask\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.FieldMaskB\x04\xe2\x41\x01\x01\"\xbf\x01\n\x11ListQuotasRequest\x12\x14\n\x06parent\x18\x01 \x01(\tB\x04\xe2\x41\x01\x02\x12\x17\n\tpage_size\x18\x02 \x01(\x05\x42\x04\xe2\x41\x01\x01\x12\x18\n\npage_token\x18\x03 \x01(\tB\x04\xe2\x41\x01\x01\x12\x14\n\x06\x66ilter\x18\x04 \x01(\tB\x04\xe2\x41\x01\x01\x12\x16\n\x08order_by\x18\x05 \x01(\tB\x04\xe2\x41\x01\x01\x12\x33\n\tread_mask\x18\x06 \x01(\x0b\x32\x1a.google.protobuf.FieldMaskB\x04\xe2\x41\x01\x01\"\x8d\x01\n\x12UpdateQuotaRequest\x12#\n\x05quota\x18\x01 \x01(\x0b\x32\x0e.gateway.QuotaB\x04\xe2\x41\x01\x02\x12\x35\n\x0bupdate_mask\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.FieldMaskB\x04\xe2\x41\x01\x01\x12\x1b\n\rallow_missing\x18\x03 \x01(\x08\x42\x04\xe2\x41\x01\x01\"a\n\x12ListQuotasResponse\x12\x1e\n\x06quotas\x18\x01 \x03(\x0b\x32\x0e.gateway.Quota\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\x12\x12\n\ntotal_size\x18\x03 \x01(\x05\x42\x43ZAgithub.com/fw-ai/fireworks/control_plane/protos/generated/gatewayb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'gateway.quota_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'ZAgithub.com/fw-ai/fireworks/control_plane/protos/generated/gateway'
  _globals['_QUOTA'].fields_by_name['name']._loaded_options = None
  _globals['_QUOTA'].fields_by_name['name']._serialized_options = b'\342A\002\003\005'
  _globals['_QUOTA'].fields_by_name['update_time']._loaded_options = None
  _globals['_QUOTA'].fields_by_name['update_time']._serialized_options = b'\342A\001\003'
  _globals['_QUOTA'].fields_by_name['create_time']._loaded_options = None
  _globals['_QUOTA'].fields_by_name['create_time']._serialized_options = b'\342A\001\003\372\322\344\223\002\020\022\016SUPERUSER_ONLY'
  _globals['_QUOTA']._loaded_options = None
  _globals['_QUOTA']._serialized_options = b'\352AN\n\026api.fireworks.ai/Quota\022%accounts/{AccountId}/quotas/{QuotaId}*\006quotas2\005quota\202\361\004\t\n\007Account'
  _globals['_GETQUOTAREQUEST'].fields_by_name['name']._loaded_options = None
  _globals['_GETQUOTAREQUEST'].fields_by_name['name']._serialized_options = b'\342A\001\002'
  _globals['_GETQUOTAREQUEST'].fields_by_name['read_mask']._loaded_options = None
  _globals['_GETQUOTAREQUEST'].fields_by_name['read_mask']._serialized_options = b'\342A\001\001'
  _globals['_LISTQUOTASREQUEST'].fields_by_name['parent']._loaded_options = None
  _globals['_LISTQUOTASREQUEST'].fields_by_name['parent']._serialized_options = b'\342A\001\002'
  _globals['_LISTQUOTASREQUEST'].fields_by_name['page_size']._loaded_options = None
  _globals['_LISTQUOTASREQUEST'].fields_by_name['page_size']._serialized_options = b'\342A\001\001'
  _globals['_LISTQUOTASREQUEST'].fields_by_name['page_token']._loaded_options = None
  _globals['_LISTQUOTASREQUEST'].fields_by_name['page_token']._serialized_options = b'\342A\001\001'
  _globals['_LISTQUOTASREQUEST'].fields_by_name['filter']._loaded_options = None
  _globals['_LISTQUOTASREQUEST'].fields_by_name['filter']._serialized_options = b'\342A\001\001'
  _globals['_LISTQUOTASREQUEST'].fields_by_name['order_by']._loaded_options = None
  _globals['_LISTQUOTASREQUEST'].fields_by_name['order_by']._serialized_options = b'\342A\001\001'
  _globals['_LISTQUOTASREQUEST'].fields_by_name['read_mask']._loaded_options = None
  _globals['_LISTQUOTASREQUEST'].fields_by_name['read_mask']._serialized_options = b'\342A\001\001'
  _globals['_UPDATEQUOTAREQUEST'].fields_by_name['quota']._loaded_options = None
  _globals['_UPDATEQUOTAREQUEST'].fields_by_name['quota']._serialized_options = b'\342A\001\002'
  _globals['_UPDATEQUOTAREQUEST'].fields_by_name['update_mask']._loaded_options = None
  _globals['_UPDATEQUOTAREQUEST'].fields_by_name['update_mask']._serialized_options = b'\342A\001\001'
  _globals['_UPDATEQUOTAREQUEST'].fields_by_name['allow_missing']._loaded_options = None
  _globals['_UPDATEQUOTAREQUEST'].fields_by_name['allow_missing']._serialized_options = b'\342A\001\001'
  _globals['_QUOTA']._serialized_start=212
  _globals['_QUOTA']._serialized_end=502
  _globals['_GETQUOTAREQUEST']._serialized_start=504
  _globals['_GETQUOTAREQUEST']._serialized_end=594
  _globals['_LISTQUOTASREQUEST']._serialized_start=597
  _globals['_LISTQUOTASREQUEST']._serialized_end=788
  _globals['_UPDATEQUOTAREQUEST']._serialized_start=791
  _globals['_UPDATEQUOTAREQUEST']._serialized_end=932
  _globals['_LISTQUOTASRESPONSE']._serialized_start=934
  _globals['_LISTQUOTASRESPONSE']._serialized_end=1031
# @@protoc_insertion_point(module_scope)
