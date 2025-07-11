# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: gateway/batch_inference_job.proto
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
    'gateway/batch_inference_job.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from . import deployment_pb2 as gateway_dot_deployment__pb2
from . import job_progress_pb2 as gateway_dot_job__progress__pb2
from . import options_pb2 as gateway_dot_options__pb2
from . import status_pb2 as gateway_dot_status__pb2
from ..google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from ..google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from ..google.api import visibility_pb2 as google_dot_api_dot_visibility__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n!gateway/batch_inference_job.proto\x12\x07gateway\x1a\x18gateway/deployment.proto\x1a\x1agateway/job_progress.proto\x1a\x15gateway/options.proto\x1a\x14gateway/status.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a\x1bgoogle/api/visibility.proto\x1a google/protobuf/field_mask.proto\x1a\x1fgoogle/protobuf/timestamp.proto\"\x8d\n\n\x11\x42\x61tchInferenceJob\x12\x13\n\x04name\x18\x01 \x01(\tB\x05\xe2\x41\x02\x03\x05\x12\x1a\n\x0c\x64isplay_name\x18\x02 \x01(\tB\x04\xe2\x41\x01\x01\x12\x36\n\x0b\x63reate_time\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.TimestampB\x05\xe2\x41\x02\x03\x05\x12\x35\n\x0b\x65xpire_time\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.TimestampB\x04\xe2\x41\x01\x03\x12\x19\n\ncreated_by\x18\x05 \x01(\tB\x05\xe2\x41\x02\x03\x05\x12\'\n\x05state\x18\x06 \x01(\x0e\x32\x11.gateway.JobStateB\x05\xe2\x41\x02\x03\x05\x12&\n\x06status\x18\x07 \x01(\x0b\x32\x0f.gateway.StatusB\x05\xe2\x41\x02\x03\x05\x12\x13\n\x05model\x18\x08 \x01(\tB\x04\xe2\x41\x01\x02\x12\x1e\n\x10input_dataset_id\x18\t \x01(\tB\x04\xe2\x41\x01\x02\x12\x1f\n\x11output_dataset_id\x18\n \x01(\tB\x04\xe2\x41\x01\x02\x12=\n\x12\x61ppend_to_messages\x18\x0b \x01(\x0b\x32\x19.gateway.AppendToMessagesB\x04\xe2\x41\x01\x01H\x00\x12@\n\x14inference_parameters\x18\x0c \x01(\x0b\x32\x1c.gateway.InferenceParametersB\x04\xe2\x41\x01\x01\x12\x35\n\x0bupdate_time\x18\r \x01(\x0b\x32\x1a.google.protobuf.TimestampB\x04\xe2\x41\x01\x03\x12\'\n\x19\x65nding_assistant_messages\x18\x0e \x01(\tB\x04\xe2\x41\x01\x01\x12%\n\x06region\x18\x0f \x01(\x0e\x32\x0f.gateway.RegionB\x04\xe2\x41\x01\x01\x12$\n\x11max_replica_count\x18\x10 \x01(\x05\x42\x04\xe2\x41\x01\x01H\x01\x88\x01\x01\x12\x38\n\x10\x61\x63\x63\x65lerator_type\x18\x11 \x01(\x0e\x32\x18.gateway.AcceleratorTypeB\x04\xe2\x41\x01\x01\x12$\n\x11\x61\x63\x63\x65lerator_count\x18\x12 \x01(\x05\x42\x04\xe2\x41\x01\x01H\x02\x88\x01\x01\x12\x36\n\tprecision\x18\x13 \x01(\x0e\x32\x1d.gateway.Deployment.PrecisionB\x04\xe2\x41\x01\x01\x12\x46\n\"reinforcement_fine_tuning_epoch_id\x18\x14 \x01(\tB\x1a\xe2\x41\x01\x01\xfa\xd2\xe4\x93\x02\x10\x12\x0eSUPERUSER_ONLY\x12;\n\x17skip_dataset_validation\x18\x15 \x01(\x08\x42\x1a\xe2\x41\x01\x01\xfa\xd2\xe4\x93\x02\x10\x12\x0eSUPERUSER_ONLY\x12G\n\x0cjob_progress\x18\x16 \x01(\x0b\x32\x14.gateway.JobProgressB\x1b\xe2\x41\x02\x03\x05\xfa\xd2\xe4\x93\x02\x10\x12\x0eSUPERUSER_ONLY\x12,\n\x08priority\x18\x17 \x01(\x05\x42\x1a\xe2\x41\x01\x01\xfa\xd2\xe4\x93\x02\x10\x12\x0eSUPERUSER_ONLY:\x9d\x01\xea\x41\x8a\x01\n\"api.fireworks.ai/BatchInferenceJob\x12=accounts/{AccountId}/batchInferenceJobs/{BatchInferenceJobId}*\x12\x62\x61tchInferenceJobs2\x11\x62\x61tchInferenceJob\x82\xf1\x04\x0b\n\x07\x41\x63\x63ount\x18\x01\x42\x08\n\x06\x66ormatB\x14\n\x12_max_replica_countB\x14\n\x12_accelerator_count\"\x87\x01\n\x13InferenceParameters\x12\x12\n\nmax_tokens\x18\x01 \x01(\x05\x12\x13\n\x0btemperature\x18\x02 \x01(\x02\x12\r\n\x05top_p\x18\x03 \x01(\x02\x12\t\n\x01n\x18\x04 \x01(\x05\x12\x18\n\nextra_body\x18\x05 \x01(\tB\x04\xe2\x41\x01\x01\x12\x13\n\x05top_k\x18\x06 \x01(\x05\x42\x04\xe2\x41\x01\x01\"5\n\x10\x41ppendToMessages\x12!\n\x19unroll_multiple_responses\x18\x01 \x01(\x08\"f\n\x1bGetBatchInferenceJobRequest\x12\x12\n\x04name\x18\x01 \x01(\tB\x04\xe2\x41\x01\x02\x12\x33\n\tread_mask\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.FieldMaskB\x04\xe2\x41\x01\x01\"\x9b\x01\n\x1e\x43reateBatchInferenceJobRequest\x12\x14\n\x06parent\x18\x01 \x01(\tB\x04\xe2\x41\x01\x02\x12=\n\x13\x62\x61tch_inference_job\x18\x02 \x01(\x0b\x32\x1a.gateway.BatchInferenceJobB\x04\xe2\x41\x01\x02\x12$\n\x16\x62\x61tch_inference_job_id\x18\x03 \x01(\tB\x04\xe2\x41\x01\x01\"\xfe\x01\n\x1dListBatchInferenceJobsRequest\x12\x14\n\x06parent\x18\x01 \x01(\tB\x04\xe2\x41\x01\x02\x12\x17\n\tpage_size\x18\x02 \x01(\x05\x42\x04\xe2\x41\x01\x01\x12\x18\n\npage_token\x18\x03 \x01(\tB\x04\xe2\x41\x01\x01\x12\x14\n\x06\x66ilter\x18\x04 \x01(\tB\x04\xe2\x41\x01\x01\x12\x16\n\x08order_by\x18\x05 \x01(\tB\x04\xe2\x41\x01\x01\x12\x31\n\rshow_internal\x18\x06 \x01(\x08\x42\x1a\xe2\x41\x01\x01\xfa\xd2\xe4\x93\x02\x10\x12\x0eSUPERUSER_ONLY\x12\x33\n\tread_mask\x18\x07 \x01(\x0b\x32\x1a.google.protobuf.FieldMaskB\x04\xe2\x41\x01\x01\"\x87\x01\n\x1eListBatchInferenceJobsResponse\x12\x38\n\x14\x62\x61tch_inference_jobs\x18\x01 \x03(\x0b\x32\x1a.gateway.BatchInferenceJob\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\x12\x12\n\ntotal_size\x18\x03 \x01(\x05\"\x96\x01\n\x1eUpdateBatchInferenceJobRequest\x12=\n\x13\x62\x61tch_inference_job\x18\x01 \x01(\x0b\x32\x1a.gateway.BatchInferenceJobB\x04\xe2\x41\x01\x02\x12\x35\n\x0bupdate_mask\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.FieldMaskB\x04\xe2\x41\x01\x01\"4\n\x1e\x44\x65leteBatchInferenceJobRequest\x12\x12\n\x04name\x18\x01 \x01(\tB\x04\xe2\x41\x01\x02\"\xe8\x01\n.GetBatchInferenceJobInputUploadEndpointRequest\x12\x12\n\x04name\x18\x01 \x01(\tB\x04\xe2\x41\x01\x02\x12k\n\x10\x66ilename_to_size\x18\x02 \x03(\x0b\x32K.gateway.GetBatchInferenceJobInputUploadEndpointRequest.FilenameToSizeEntryB\x04\xe2\x41\x01\x02\x1a\x35\n\x13\x46ilenameToSizeEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x03:\x02\x38\x01\"\xe3\x01\n/GetBatchInferenceJobInputUploadEndpointResponse\x12s\n\x17\x66ilename_to_signed_urls\x18\x01 \x03(\x0b\x32R.gateway.GetBatchInferenceJobInputUploadEndpointResponse.FilenameToSignedUrlsEntry\x1a;\n\x19\x46ilenameToSignedUrlsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"A\n+ValidateBatchInferenceJobInputUploadRequest\x12\x12\n\x04name\x18\x01 \x01(\tB\x04\xe2\x41\x01\x02\"G\n1GetBatchInferenceJobOutputDownloadEndpointRequest\x12\x12\n\x04name\x18\x01 \x01(\tB\x04\xe2\x41\x01\x02\"\xe9\x01\n2GetBatchInferenceJobOutputDownloadEndpointResponse\x12v\n\x17\x66ilename_to_signed_urls\x18\x01 \x03(\x0b\x32U.gateway.GetBatchInferenceJobOutputDownloadEndpointResponse.FilenameToSignedUrlsEntry\x1a;\n\x19\x46ilenameToSignedUrlsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x42\x43ZAgithub.com/fw-ai/fireworks/control_plane/protos/generated/gatewayb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'gateway.batch_inference_job_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'ZAgithub.com/fw-ai/fireworks/control_plane/protos/generated/gateway'
  _globals['_BATCHINFERENCEJOB'].fields_by_name['name']._loaded_options = None
  _globals['_BATCHINFERENCEJOB'].fields_by_name['name']._serialized_options = b'\342A\002\003\005'
  _globals['_BATCHINFERENCEJOB'].fields_by_name['display_name']._loaded_options = None
  _globals['_BATCHINFERENCEJOB'].fields_by_name['display_name']._serialized_options = b'\342A\001\001'
  _globals['_BATCHINFERENCEJOB'].fields_by_name['create_time']._loaded_options = None
  _globals['_BATCHINFERENCEJOB'].fields_by_name['create_time']._serialized_options = b'\342A\002\003\005'
  _globals['_BATCHINFERENCEJOB'].fields_by_name['expire_time']._loaded_options = None
  _globals['_BATCHINFERENCEJOB'].fields_by_name['expire_time']._serialized_options = b'\342A\001\003'
  _globals['_BATCHINFERENCEJOB'].fields_by_name['created_by']._loaded_options = None
  _globals['_BATCHINFERENCEJOB'].fields_by_name['created_by']._serialized_options = b'\342A\002\003\005'
  _globals['_BATCHINFERENCEJOB'].fields_by_name['state']._loaded_options = None
  _globals['_BATCHINFERENCEJOB'].fields_by_name['state']._serialized_options = b'\342A\002\003\005'
  _globals['_BATCHINFERENCEJOB'].fields_by_name['status']._loaded_options = None
  _globals['_BATCHINFERENCEJOB'].fields_by_name['status']._serialized_options = b'\342A\002\003\005'
  _globals['_BATCHINFERENCEJOB'].fields_by_name['model']._loaded_options = None
  _globals['_BATCHINFERENCEJOB'].fields_by_name['model']._serialized_options = b'\342A\001\002'
  _globals['_BATCHINFERENCEJOB'].fields_by_name['input_dataset_id']._loaded_options = None
  _globals['_BATCHINFERENCEJOB'].fields_by_name['input_dataset_id']._serialized_options = b'\342A\001\002'
  _globals['_BATCHINFERENCEJOB'].fields_by_name['output_dataset_id']._loaded_options = None
  _globals['_BATCHINFERENCEJOB'].fields_by_name['output_dataset_id']._serialized_options = b'\342A\001\002'
  _globals['_BATCHINFERENCEJOB'].fields_by_name['append_to_messages']._loaded_options = None
  _globals['_BATCHINFERENCEJOB'].fields_by_name['append_to_messages']._serialized_options = b'\342A\001\001'
  _globals['_BATCHINFERENCEJOB'].fields_by_name['inference_parameters']._loaded_options = None
  _globals['_BATCHINFERENCEJOB'].fields_by_name['inference_parameters']._serialized_options = b'\342A\001\001'
  _globals['_BATCHINFERENCEJOB'].fields_by_name['update_time']._loaded_options = None
  _globals['_BATCHINFERENCEJOB'].fields_by_name['update_time']._serialized_options = b'\342A\001\003'
  _globals['_BATCHINFERENCEJOB'].fields_by_name['ending_assistant_messages']._loaded_options = None
  _globals['_BATCHINFERENCEJOB'].fields_by_name['ending_assistant_messages']._serialized_options = b'\342A\001\001'
  _globals['_BATCHINFERENCEJOB'].fields_by_name['region']._loaded_options = None
  _globals['_BATCHINFERENCEJOB'].fields_by_name['region']._serialized_options = b'\342A\001\001'
  _globals['_BATCHINFERENCEJOB'].fields_by_name['max_replica_count']._loaded_options = None
  _globals['_BATCHINFERENCEJOB'].fields_by_name['max_replica_count']._serialized_options = b'\342A\001\001'
  _globals['_BATCHINFERENCEJOB'].fields_by_name['accelerator_type']._loaded_options = None
  _globals['_BATCHINFERENCEJOB'].fields_by_name['accelerator_type']._serialized_options = b'\342A\001\001'
  _globals['_BATCHINFERENCEJOB'].fields_by_name['accelerator_count']._loaded_options = None
  _globals['_BATCHINFERENCEJOB'].fields_by_name['accelerator_count']._serialized_options = b'\342A\001\001'
  _globals['_BATCHINFERENCEJOB'].fields_by_name['precision']._loaded_options = None
  _globals['_BATCHINFERENCEJOB'].fields_by_name['precision']._serialized_options = b'\342A\001\001'
  _globals['_BATCHINFERENCEJOB'].fields_by_name['reinforcement_fine_tuning_epoch_id']._loaded_options = None
  _globals['_BATCHINFERENCEJOB'].fields_by_name['reinforcement_fine_tuning_epoch_id']._serialized_options = b'\342A\001\001\372\322\344\223\002\020\022\016SUPERUSER_ONLY'
  _globals['_BATCHINFERENCEJOB'].fields_by_name['skip_dataset_validation']._loaded_options = None
  _globals['_BATCHINFERENCEJOB'].fields_by_name['skip_dataset_validation']._serialized_options = b'\342A\001\001\372\322\344\223\002\020\022\016SUPERUSER_ONLY'
  _globals['_BATCHINFERENCEJOB'].fields_by_name['job_progress']._loaded_options = None
  _globals['_BATCHINFERENCEJOB'].fields_by_name['job_progress']._serialized_options = b'\342A\002\003\005\372\322\344\223\002\020\022\016SUPERUSER_ONLY'
  _globals['_BATCHINFERENCEJOB'].fields_by_name['priority']._loaded_options = None
  _globals['_BATCHINFERENCEJOB'].fields_by_name['priority']._serialized_options = b'\342A\001\001\372\322\344\223\002\020\022\016SUPERUSER_ONLY'
  _globals['_BATCHINFERENCEJOB']._loaded_options = None
  _globals['_BATCHINFERENCEJOB']._serialized_options = b'\352A\212\001\n\"api.fireworks.ai/BatchInferenceJob\022=accounts/{AccountId}/batchInferenceJobs/{BatchInferenceJobId}*\022batchInferenceJobs2\021batchInferenceJob\202\361\004\013\n\007Account\030\001'
  _globals['_INFERENCEPARAMETERS'].fields_by_name['extra_body']._loaded_options = None
  _globals['_INFERENCEPARAMETERS'].fields_by_name['extra_body']._serialized_options = b'\342A\001\001'
  _globals['_INFERENCEPARAMETERS'].fields_by_name['top_k']._loaded_options = None
  _globals['_INFERENCEPARAMETERS'].fields_by_name['top_k']._serialized_options = b'\342A\001\001'
  _globals['_GETBATCHINFERENCEJOBREQUEST'].fields_by_name['name']._loaded_options = None
  _globals['_GETBATCHINFERENCEJOBREQUEST'].fields_by_name['name']._serialized_options = b'\342A\001\002'
  _globals['_GETBATCHINFERENCEJOBREQUEST'].fields_by_name['read_mask']._loaded_options = None
  _globals['_GETBATCHINFERENCEJOBREQUEST'].fields_by_name['read_mask']._serialized_options = b'\342A\001\001'
  _globals['_CREATEBATCHINFERENCEJOBREQUEST'].fields_by_name['parent']._loaded_options = None
  _globals['_CREATEBATCHINFERENCEJOBREQUEST'].fields_by_name['parent']._serialized_options = b'\342A\001\002'
  _globals['_CREATEBATCHINFERENCEJOBREQUEST'].fields_by_name['batch_inference_job']._loaded_options = None
  _globals['_CREATEBATCHINFERENCEJOBREQUEST'].fields_by_name['batch_inference_job']._serialized_options = b'\342A\001\002'
  _globals['_CREATEBATCHINFERENCEJOBREQUEST'].fields_by_name['batch_inference_job_id']._loaded_options = None
  _globals['_CREATEBATCHINFERENCEJOBREQUEST'].fields_by_name['batch_inference_job_id']._serialized_options = b'\342A\001\001'
  _globals['_LISTBATCHINFERENCEJOBSREQUEST'].fields_by_name['parent']._loaded_options = None
  _globals['_LISTBATCHINFERENCEJOBSREQUEST'].fields_by_name['parent']._serialized_options = b'\342A\001\002'
  _globals['_LISTBATCHINFERENCEJOBSREQUEST'].fields_by_name['page_size']._loaded_options = None
  _globals['_LISTBATCHINFERENCEJOBSREQUEST'].fields_by_name['page_size']._serialized_options = b'\342A\001\001'
  _globals['_LISTBATCHINFERENCEJOBSREQUEST'].fields_by_name['page_token']._loaded_options = None
  _globals['_LISTBATCHINFERENCEJOBSREQUEST'].fields_by_name['page_token']._serialized_options = b'\342A\001\001'
  _globals['_LISTBATCHINFERENCEJOBSREQUEST'].fields_by_name['filter']._loaded_options = None
  _globals['_LISTBATCHINFERENCEJOBSREQUEST'].fields_by_name['filter']._serialized_options = b'\342A\001\001'
  _globals['_LISTBATCHINFERENCEJOBSREQUEST'].fields_by_name['order_by']._loaded_options = None
  _globals['_LISTBATCHINFERENCEJOBSREQUEST'].fields_by_name['order_by']._serialized_options = b'\342A\001\001'
  _globals['_LISTBATCHINFERENCEJOBSREQUEST'].fields_by_name['show_internal']._loaded_options = None
  _globals['_LISTBATCHINFERENCEJOBSREQUEST'].fields_by_name['show_internal']._serialized_options = b'\342A\001\001\372\322\344\223\002\020\022\016SUPERUSER_ONLY'
  _globals['_LISTBATCHINFERENCEJOBSREQUEST'].fields_by_name['read_mask']._loaded_options = None
  _globals['_LISTBATCHINFERENCEJOBSREQUEST'].fields_by_name['read_mask']._serialized_options = b'\342A\001\001'
  _globals['_UPDATEBATCHINFERENCEJOBREQUEST'].fields_by_name['batch_inference_job']._loaded_options = None
  _globals['_UPDATEBATCHINFERENCEJOBREQUEST'].fields_by_name['batch_inference_job']._serialized_options = b'\342A\001\002'
  _globals['_UPDATEBATCHINFERENCEJOBREQUEST'].fields_by_name['update_mask']._loaded_options = None
  _globals['_UPDATEBATCHINFERENCEJOBREQUEST'].fields_by_name['update_mask']._serialized_options = b'\342A\001\001'
  _globals['_DELETEBATCHINFERENCEJOBREQUEST'].fields_by_name['name']._loaded_options = None
  _globals['_DELETEBATCHINFERENCEJOBREQUEST'].fields_by_name['name']._serialized_options = b'\342A\001\002'
  _globals['_GETBATCHINFERENCEJOBINPUTUPLOADENDPOINTREQUEST_FILENAMETOSIZEENTRY']._loaded_options = None
  _globals['_GETBATCHINFERENCEJOBINPUTUPLOADENDPOINTREQUEST_FILENAMETOSIZEENTRY']._serialized_options = b'8\001'
  _globals['_GETBATCHINFERENCEJOBINPUTUPLOADENDPOINTREQUEST'].fields_by_name['name']._loaded_options = None
  _globals['_GETBATCHINFERENCEJOBINPUTUPLOADENDPOINTREQUEST'].fields_by_name['name']._serialized_options = b'\342A\001\002'
  _globals['_GETBATCHINFERENCEJOBINPUTUPLOADENDPOINTREQUEST'].fields_by_name['filename_to_size']._loaded_options = None
  _globals['_GETBATCHINFERENCEJOBINPUTUPLOADENDPOINTREQUEST'].fields_by_name['filename_to_size']._serialized_options = b'\342A\001\002'
  _globals['_GETBATCHINFERENCEJOBINPUTUPLOADENDPOINTRESPONSE_FILENAMETOSIGNEDURLSENTRY']._loaded_options = None
  _globals['_GETBATCHINFERENCEJOBINPUTUPLOADENDPOINTRESPONSE_FILENAMETOSIGNEDURLSENTRY']._serialized_options = b'8\001'
  _globals['_VALIDATEBATCHINFERENCEJOBINPUTUPLOADREQUEST'].fields_by_name['name']._loaded_options = None
  _globals['_VALIDATEBATCHINFERENCEJOBINPUTUPLOADREQUEST'].fields_by_name['name']._serialized_options = b'\342A\001\002'
  _globals['_GETBATCHINFERENCEJOBOUTPUTDOWNLOADENDPOINTREQUEST'].fields_by_name['name']._loaded_options = None
  _globals['_GETBATCHINFERENCEJOBOUTPUTDOWNLOADENDPOINTREQUEST'].fields_by_name['name']._serialized_options = b'\342A\001\002'
  _globals['_GETBATCHINFERENCEJOBOUTPUTDOWNLOADENDPOINTRESPONSE_FILENAMETOSIGNEDURLSENTRY']._loaded_options = None
  _globals['_GETBATCHINFERENCEJOBOUTPUTDOWNLOADENDPOINTRESPONSE_FILENAMETOSIGNEDURLSENTRY']._serialized_options = b'8\001'
  _globals['_BATCHINFERENCEJOB']._serialized_start=302
  _globals['_BATCHINFERENCEJOB']._serialized_end=1595
  _globals['_INFERENCEPARAMETERS']._serialized_start=1598
  _globals['_INFERENCEPARAMETERS']._serialized_end=1733
  _globals['_APPENDTOMESSAGES']._serialized_start=1735
  _globals['_APPENDTOMESSAGES']._serialized_end=1788
  _globals['_GETBATCHINFERENCEJOBREQUEST']._serialized_start=1790
  _globals['_GETBATCHINFERENCEJOBREQUEST']._serialized_end=1892
  _globals['_CREATEBATCHINFERENCEJOBREQUEST']._serialized_start=1895
  _globals['_CREATEBATCHINFERENCEJOBREQUEST']._serialized_end=2050
  _globals['_LISTBATCHINFERENCEJOBSREQUEST']._serialized_start=2053
  _globals['_LISTBATCHINFERENCEJOBSREQUEST']._serialized_end=2307
  _globals['_LISTBATCHINFERENCEJOBSRESPONSE']._serialized_start=2310
  _globals['_LISTBATCHINFERENCEJOBSRESPONSE']._serialized_end=2445
  _globals['_UPDATEBATCHINFERENCEJOBREQUEST']._serialized_start=2448
  _globals['_UPDATEBATCHINFERENCEJOBREQUEST']._serialized_end=2598
  _globals['_DELETEBATCHINFERENCEJOBREQUEST']._serialized_start=2600
  _globals['_DELETEBATCHINFERENCEJOBREQUEST']._serialized_end=2652
  _globals['_GETBATCHINFERENCEJOBINPUTUPLOADENDPOINTREQUEST']._serialized_start=2655
  _globals['_GETBATCHINFERENCEJOBINPUTUPLOADENDPOINTREQUEST']._serialized_end=2887
  _globals['_GETBATCHINFERENCEJOBINPUTUPLOADENDPOINTREQUEST_FILENAMETOSIZEENTRY']._serialized_start=2834
  _globals['_GETBATCHINFERENCEJOBINPUTUPLOADENDPOINTREQUEST_FILENAMETOSIZEENTRY']._serialized_end=2887
  _globals['_GETBATCHINFERENCEJOBINPUTUPLOADENDPOINTRESPONSE']._serialized_start=2890
  _globals['_GETBATCHINFERENCEJOBINPUTUPLOADENDPOINTRESPONSE']._serialized_end=3117
  _globals['_GETBATCHINFERENCEJOBINPUTUPLOADENDPOINTRESPONSE_FILENAMETOSIGNEDURLSENTRY']._serialized_start=3058
  _globals['_GETBATCHINFERENCEJOBINPUTUPLOADENDPOINTRESPONSE_FILENAMETOSIGNEDURLSENTRY']._serialized_end=3117
  _globals['_VALIDATEBATCHINFERENCEJOBINPUTUPLOADREQUEST']._serialized_start=3119
  _globals['_VALIDATEBATCHINFERENCEJOBINPUTUPLOADREQUEST']._serialized_end=3184
  _globals['_GETBATCHINFERENCEJOBOUTPUTDOWNLOADENDPOINTREQUEST']._serialized_start=3186
  _globals['_GETBATCHINFERENCEJOBOUTPUTDOWNLOADENDPOINTREQUEST']._serialized_end=3257
  _globals['_GETBATCHINFERENCEJOBOUTPUTDOWNLOADENDPOINTRESPONSE']._serialized_start=3260
  _globals['_GETBATCHINFERENCEJOBOUTPUTDOWNLOADENDPOINTRESPONSE']._serialized_end=3493
  _globals['_GETBATCHINFERENCEJOBOUTPUTDOWNLOADENDPOINTRESPONSE_FILENAMETOSIGNEDURLSENTRY']._serialized_start=3058
  _globals['_GETBATCHINFERENCEJOBOUTPUTDOWNLOADENDPOINTRESPONSE_FILENAMETOSIGNEDURLSENTRY']._serialized_end=3117
# @@protoc_insertion_point(module_scope)
