# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: gateway/status.proto
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
    'gateway/status.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x14gateway/status.proto\x12\x07gateway\"6\n\x06Status\x12\x1b\n\x04\x63ode\x18\x01 \x01(\x0e\x32\r.gateway.Code\x12\x0f\n\x07message\x18\x02 \x01(\t*\xb7\x02\n\x04\x43ode\x12\x06\n\x02OK\x10\x00\x12\r\n\tCANCELLED\x10\x01\x12\x0b\n\x07UNKNOWN\x10\x02\x12\x14\n\x10INVALID_ARGUMENT\x10\x03\x12\x15\n\x11\x44\x45\x41\x44LINE_EXCEEDED\x10\x04\x12\r\n\tNOT_FOUND\x10\x05\x12\x12\n\x0e\x41LREADY_EXISTS\x10\x06\x12\x15\n\x11PERMISSION_DENIED\x10\x07\x12\x13\n\x0fUNAUTHENTICATED\x10\x10\x12\x16\n\x12RESOURCE_EXHAUSTED\x10\x08\x12\x17\n\x13\x46\x41ILED_PRECONDITION\x10\t\x12\x0b\n\x07\x41\x42ORTED\x10\n\x12\x10\n\x0cOUT_OF_RANGE\x10\x0b\x12\x11\n\rUNIMPLEMENTED\x10\x0c\x12\x0c\n\x08INTERNAL\x10\r\x12\x0f\n\x0bUNAVAILABLE\x10\x0e\x12\r\n\tDATA_LOSS\x10\x0f*\x98\x03\n\x08JobState\x12\x19\n\x15JOB_STATE_UNSPECIFIED\x10\x00\x12\x16\n\x12JOB_STATE_CREATING\x10\x01\x12\x15\n\x11JOB_STATE_RUNNING\x10\x02\x12\x17\n\x13JOB_STATE_COMPLETED\x10\x03\x12\x14\n\x10JOB_STATE_FAILED\x10\x04\x12\x17\n\x13JOB_STATE_CANCELLED\x10\x05\x12\x16\n\x12JOB_STATE_DELETING\x10\x06\x12\x1d\n\x19JOB_STATE_WRITING_RESULTS\x10\x07\x12\x18\n\x14JOB_STATE_VALIDATING\x10\x08\x12\x15\n\x11JOB_STATE_ROLLOUT\x10\t\x12\x18\n\x14JOB_STATE_EVALUATION\x10\n\x12 \n\x1cJOB_STATE_FAILED_CLEANING_UP\x10\x0b\x12\"\n\x1eJOB_STATE_DELETING_CLEANING_UP\x10\x0c\x12\x1b\n\x17JOB_STATE_POLICY_UPDATE\x10\r\x12\x15\n\x11JOB_STATE_PENDING\x10\x0e\x42\x43ZAgithub.com/fw-ai/fireworks/control_plane/protos/generated/gatewayb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'gateway.status_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'ZAgithub.com/fw-ai/fireworks/control_plane/protos/generated/gateway'
  _globals['_CODE']._serialized_start=90
  _globals['_CODE']._serialized_end=401
  _globals['_JOBSTATE']._serialized_start=404
  _globals['_JOBSTATE']._serialized_end=812
  _globals['_STATUS']._serialized_start=33
  _globals['_STATUS']._serialized_end=87
# @@protoc_insertion_point(module_scope)
