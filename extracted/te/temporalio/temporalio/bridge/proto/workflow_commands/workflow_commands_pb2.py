# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: temporal/sdk/core/workflow_commands/workflow_commands.proto
"""Generated protocol buffer code."""

from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import enum_type_wrapper

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2

from temporalio.api.common.v1 import (
    message_pb2 as temporal_dot_api_dot_common_dot_v1_dot_message__pb2,
)
from temporalio.api.enums.v1 import (
    workflow_pb2 as temporal_dot_api_dot_enums_dot_v1_dot_workflow__pb2,
)
from temporalio.api.failure.v1 import (
    message_pb2 as temporal_dot_api_dot_failure_dot_v1_dot_message__pb2,
)
from temporalio.api.sdk.v1 import (
    user_metadata_pb2 as temporal_dot_api_dot_sdk_dot_v1_dot_user__metadata__pb2,
)
from temporalio.bridge.proto.child_workflow import (
    child_workflow_pb2 as temporal_dot_sdk_dot_core_dot_child__workflow_dot_child__workflow__pb2,
)
from temporalio.bridge.proto.common import (
    common_pb2 as temporal_dot_sdk_dot_core_dot_common_dot_common__pb2,
)
from temporalio.bridge.proto.nexus import (
    nexus_pb2 as temporal_dot_sdk_dot_core_dot_nexus_dot_nexus__pb2,
)

DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n;temporal/sdk/core/workflow_commands/workflow_commands.proto\x12\x19\x63oresdk.workflow_commands\x1a\x1egoogle/protobuf/duration.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a$temporal/api/common/v1/message.proto\x1a$temporal/api/enums/v1/workflow.proto\x1a%temporal/api/failure/v1/message.proto\x1a\'temporal/api/sdk/v1/user_metadata.proto\x1a\x35temporal/sdk/core/child_workflow/child_workflow.proto\x1a#temporal/sdk/core/nexus/nexus.proto\x1a%temporal/sdk/core/common/common.proto"\xe5\x0f\n\x0fWorkflowCommand\x12\x38\n\ruser_metadata\x18\x64 \x01(\x0b\x32!.temporal.api.sdk.v1.UserMetadata\x12<\n\x0bstart_timer\x18\x01 \x01(\x0b\x32%.coresdk.workflow_commands.StartTimerH\x00\x12H\n\x11schedule_activity\x18\x02 \x01(\x0b\x32+.coresdk.workflow_commands.ScheduleActivityH\x00\x12\x42\n\x10respond_to_query\x18\x03 \x01(\x0b\x32&.coresdk.workflow_commands.QueryResultH\x00\x12S\n\x17request_cancel_activity\x18\x04 \x01(\x0b\x32\x30.coresdk.workflow_commands.RequestCancelActivityH\x00\x12>\n\x0c\x63\x61ncel_timer\x18\x05 \x01(\x0b\x32&.coresdk.workflow_commands.CancelTimerH\x00\x12[\n\x1b\x63omplete_workflow_execution\x18\x06 \x01(\x0b\x32\x34.coresdk.workflow_commands.CompleteWorkflowExecutionH\x00\x12S\n\x17\x66\x61il_workflow_execution\x18\x07 \x01(\x0b\x32\x30.coresdk.workflow_commands.FailWorkflowExecutionH\x00\x12g\n"continue_as_new_workflow_execution\x18\x08 \x01(\x0b\x32\x39.coresdk.workflow_commands.ContinueAsNewWorkflowExecutionH\x00\x12W\n\x19\x63\x61ncel_workflow_execution\x18\t \x01(\x0b\x32\x32.coresdk.workflow_commands.CancelWorkflowExecutionH\x00\x12\x45\n\x10set_patch_marker\x18\n \x01(\x0b\x32).coresdk.workflow_commands.SetPatchMarkerH\x00\x12`\n\x1estart_child_workflow_execution\x18\x0b \x01(\x0b\x32\x36.coresdk.workflow_commands.StartChildWorkflowExecutionH\x00\x12\x62\n\x1f\x63\x61ncel_child_workflow_execution\x18\x0c \x01(\x0b\x32\x37.coresdk.workflow_commands.CancelChildWorkflowExecutionH\x00\x12w\n*request_cancel_external_workflow_execution\x18\r \x01(\x0b\x32\x41.coresdk.workflow_commands.RequestCancelExternalWorkflowExecutionH\x00\x12h\n"signal_external_workflow_execution\x18\x0e \x01(\x0b\x32:.coresdk.workflow_commands.SignalExternalWorkflowExecutionH\x00\x12Q\n\x16\x63\x61ncel_signal_workflow\x18\x0f \x01(\x0b\x32/.coresdk.workflow_commands.CancelSignalWorkflowH\x00\x12S\n\x17schedule_local_activity\x18\x10 \x01(\x0b\x32\x30.coresdk.workflow_commands.ScheduleLocalActivityH\x00\x12^\n\x1drequest_cancel_local_activity\x18\x11 \x01(\x0b\x32\x35.coresdk.workflow_commands.RequestCancelLocalActivityH\x00\x12\x66\n!upsert_workflow_search_attributes\x18\x12 \x01(\x0b\x32\x39.coresdk.workflow_commands.UpsertWorkflowSearchAttributesH\x00\x12Y\n\x1amodify_workflow_properties\x18\x13 \x01(\x0b\x32\x33.coresdk.workflow_commands.ModifyWorkflowPropertiesH\x00\x12\x44\n\x0fupdate_response\x18\x14 \x01(\x0b\x32).coresdk.workflow_commands.UpdateResponseH\x00\x12U\n\x18schedule_nexus_operation\x18\x15 \x01(\x0b\x32\x31.coresdk.workflow_commands.ScheduleNexusOperationH\x00\x12`\n\x1erequest_cancel_nexus_operation\x18\x16 \x01(\x0b\x32\x36.coresdk.workflow_commands.RequestCancelNexusOperationH\x00\x42\t\n\x07variant"S\n\nStartTimer\x12\x0b\n\x03seq\x18\x01 \x01(\r\x12\x38\n\x15start_to_fire_timeout\x18\x02 \x01(\x0b\x32\x19.google.protobuf.Duration"\x1a\n\x0b\x43\x61ncelTimer\x12\x0b\n\x03seq\x18\x01 \x01(\r"\xb8\x06\n\x10ScheduleActivity\x12\x0b\n\x03seq\x18\x01 \x01(\r\x12\x13\n\x0b\x61\x63tivity_id\x18\x02 \x01(\t\x12\x15\n\ractivity_type\x18\x03 \x01(\t\x12\x12\n\ntask_queue\x18\x05 \x01(\t\x12I\n\x07headers\x18\x06 \x03(\x0b\x32\x38.coresdk.workflow_commands.ScheduleActivity.HeadersEntry\x12\x32\n\targuments\x18\x07 \x03(\x0b\x32\x1f.temporal.api.common.v1.Payload\x12<\n\x19schedule_to_close_timeout\x18\x08 \x01(\x0b\x32\x19.google.protobuf.Duration\x12<\n\x19schedule_to_start_timeout\x18\t \x01(\x0b\x32\x19.google.protobuf.Duration\x12\x39\n\x16start_to_close_timeout\x18\n \x01(\x0b\x32\x19.google.protobuf.Duration\x12\x34\n\x11heartbeat_timeout\x18\x0b \x01(\x0b\x32\x19.google.protobuf.Duration\x12\x39\n\x0cretry_policy\x18\x0c \x01(\x0b\x32#.temporal.api.common.v1.RetryPolicy\x12N\n\x11\x63\x61ncellation_type\x18\r \x01(\x0e\x32\x33.coresdk.workflow_commands.ActivityCancellationType\x12\x1e\n\x16\x64o_not_eagerly_execute\x18\x0e \x01(\x08\x12;\n\x11versioning_intent\x18\x0f \x01(\x0e\x32 .coresdk.common.VersioningIntent\x12\x32\n\x08priority\x18\x10 \x01(\x0b\x32 .temporal.api.common.v1.Priority\x1aO\n\x0cHeadersEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12.\n\x05value\x18\x02 \x01(\x0b\x32\x1f.temporal.api.common.v1.Payload:\x02\x38\x01"\xee\x05\n\x15ScheduleLocalActivity\x12\x0b\n\x03seq\x18\x01 \x01(\r\x12\x13\n\x0b\x61\x63tivity_id\x18\x02 \x01(\t\x12\x15\n\ractivity_type\x18\x03 \x01(\t\x12\x0f\n\x07\x61ttempt\x18\x04 \x01(\r\x12:\n\x16original_schedule_time\x18\x05 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12N\n\x07headers\x18\x06 \x03(\x0b\x32=.coresdk.workflow_commands.ScheduleLocalActivity.HeadersEntry\x12\x32\n\targuments\x18\x07 \x03(\x0b\x32\x1f.temporal.api.common.v1.Payload\x12<\n\x19schedule_to_close_timeout\x18\x08 \x01(\x0b\x32\x19.google.protobuf.Duration\x12<\n\x19schedule_to_start_timeout\x18\t \x01(\x0b\x32\x19.google.protobuf.Duration\x12\x39\n\x16start_to_close_timeout\x18\n \x01(\x0b\x32\x19.google.protobuf.Duration\x12\x39\n\x0cretry_policy\x18\x0b \x01(\x0b\x32#.temporal.api.common.v1.RetryPolicy\x12\x38\n\x15local_retry_threshold\x18\x0c \x01(\x0b\x32\x19.google.protobuf.Duration\x12N\n\x11\x63\x61ncellation_type\x18\r \x01(\x0e\x32\x33.coresdk.workflow_commands.ActivityCancellationType\x1aO\n\x0cHeadersEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12.\n\x05value\x18\x02 \x01(\x0b\x32\x1f.temporal.api.common.v1.Payload:\x02\x38\x01"$\n\x15RequestCancelActivity\x12\x0b\n\x03seq\x18\x01 \x01(\r")\n\x1aRequestCancelLocalActivity\x12\x0b\n\x03seq\x18\x01 \x01(\r"\x9c\x01\n\x0bQueryResult\x12\x10\n\x08query_id\x18\x01 \x01(\t\x12<\n\tsucceeded\x18\x02 \x01(\x0b\x32\'.coresdk.workflow_commands.QuerySuccessH\x00\x12\x32\n\x06\x66\x61iled\x18\x03 \x01(\x0b\x32 .temporal.api.failure.v1.FailureH\x00\x42\t\n\x07variant"A\n\x0cQuerySuccess\x12\x31\n\x08response\x18\x01 \x01(\x0b\x32\x1f.temporal.api.common.v1.Payload"L\n\x19\x43ompleteWorkflowExecution\x12/\n\x06result\x18\x01 \x01(\x0b\x32\x1f.temporal.api.common.v1.Payload"J\n\x15\x46\x61ilWorkflowExecution\x12\x31\n\x07\x66\x61ilure\x18\x01 \x01(\x0b\x32 .temporal.api.failure.v1.Failure"\xfb\x06\n\x1e\x43ontinueAsNewWorkflowExecution\x12\x15\n\rworkflow_type\x18\x01 \x01(\t\x12\x12\n\ntask_queue\x18\x02 \x01(\t\x12\x32\n\targuments\x18\x03 \x03(\x0b\x32\x1f.temporal.api.common.v1.Payload\x12\x37\n\x14workflow_run_timeout\x18\x04 \x01(\x0b\x32\x19.google.protobuf.Duration\x12\x38\n\x15workflow_task_timeout\x18\x05 \x01(\x0b\x32\x19.google.protobuf.Duration\x12Q\n\x04memo\x18\x06 \x03(\x0b\x32\x43.coresdk.workflow_commands.ContinueAsNewWorkflowExecution.MemoEntry\x12W\n\x07headers\x18\x07 \x03(\x0b\x32\x46.coresdk.workflow_commands.ContinueAsNewWorkflowExecution.HeadersEntry\x12j\n\x11search_attributes\x18\x08 \x03(\x0b\x32O.coresdk.workflow_commands.ContinueAsNewWorkflowExecution.SearchAttributesEntry\x12\x39\n\x0cretry_policy\x18\t \x01(\x0b\x32#.temporal.api.common.v1.RetryPolicy\x12;\n\x11versioning_intent\x18\n \x01(\x0e\x32 .coresdk.common.VersioningIntent\x1aL\n\tMemoEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12.\n\x05value\x18\x02 \x01(\x0b\x32\x1f.temporal.api.common.v1.Payload:\x02\x38\x01\x1aO\n\x0cHeadersEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12.\n\x05value\x18\x02 \x01(\x0b\x32\x1f.temporal.api.common.v1.Payload:\x02\x38\x01\x1aX\n\x15SearchAttributesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12.\n\x05value\x18\x02 \x01(\x0b\x32\x1f.temporal.api.common.v1.Payload:\x02\x38\x01"\x19\n\x17\x43\x61ncelWorkflowExecution"6\n\x0eSetPatchMarker\x12\x10\n\x08patch_id\x18\x01 \x01(\t\x12\x12\n\ndeprecated\x18\x02 \x01(\x08"\x94\n\n\x1bStartChildWorkflowExecution\x12\x0b\n\x03seq\x18\x01 \x01(\r\x12\x11\n\tnamespace\x18\x02 \x01(\t\x12\x13\n\x0bworkflow_id\x18\x03 \x01(\t\x12\x15\n\rworkflow_type\x18\x04 \x01(\t\x12\x12\n\ntask_queue\x18\x05 \x01(\t\x12.\n\x05input\x18\x06 \x03(\x0b\x32\x1f.temporal.api.common.v1.Payload\x12=\n\x1aworkflow_execution_timeout\x18\x07 \x01(\x0b\x32\x19.google.protobuf.Duration\x12\x37\n\x14workflow_run_timeout\x18\x08 \x01(\x0b\x32\x19.google.protobuf.Duration\x12\x38\n\x15workflow_task_timeout\x18\t \x01(\x0b\x32\x19.google.protobuf.Duration\x12\x46\n\x13parent_close_policy\x18\n \x01(\x0e\x32).coresdk.child_workflow.ParentClosePolicy\x12N\n\x18workflow_id_reuse_policy\x18\x0c \x01(\x0e\x32,.temporal.api.enums.v1.WorkflowIdReusePolicy\x12\x39\n\x0cretry_policy\x18\r \x01(\x0b\x32#.temporal.api.common.v1.RetryPolicy\x12\x15\n\rcron_schedule\x18\x0e \x01(\t\x12T\n\x07headers\x18\x0f \x03(\x0b\x32\x43.coresdk.workflow_commands.StartChildWorkflowExecution.HeadersEntry\x12N\n\x04memo\x18\x10 \x03(\x0b\x32@.coresdk.workflow_commands.StartChildWorkflowExecution.MemoEntry\x12g\n\x11search_attributes\x18\x11 \x03(\x0b\x32L.coresdk.workflow_commands.StartChildWorkflowExecution.SearchAttributesEntry\x12P\n\x11\x63\x61ncellation_type\x18\x12 \x01(\x0e\x32\x35.coresdk.child_workflow.ChildWorkflowCancellationType\x12;\n\x11versioning_intent\x18\x13 \x01(\x0e\x32 .coresdk.common.VersioningIntent\x12\x32\n\x08priority\x18\x14 \x01(\x0b\x32 .temporal.api.common.v1.Priority\x1aO\n\x0cHeadersEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12.\n\x05value\x18\x02 \x01(\x0b\x32\x1f.temporal.api.common.v1.Payload:\x02\x38\x01\x1aL\n\tMemoEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12.\n\x05value\x18\x02 \x01(\x0b\x32\x1f.temporal.api.common.v1.Payload:\x02\x38\x01\x1aX\n\x15SearchAttributesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12.\n\x05value\x18\x02 \x01(\x0b\x32\x1f.temporal.api.common.v1.Payload:\x02\x38\x01"J\n\x1c\x43\x61ncelChildWorkflowExecution\x12\x1a\n\x12\x63hild_workflow_seq\x18\x01 \x01(\r\x12\x0e\n\x06reason\x18\x02 \x01(\t"\x8e\x01\n&RequestCancelExternalWorkflowExecution\x12\x0b\n\x03seq\x18\x01 \x01(\r\x12G\n\x12workflow_execution\x18\x02 \x01(\x0b\x32+.coresdk.common.NamespacedWorkflowExecution\x12\x0e\n\x06reason\x18\x03 \x01(\t"\x8f\x03\n\x1fSignalExternalWorkflowExecution\x12\x0b\n\x03seq\x18\x01 \x01(\r\x12I\n\x12workflow_execution\x18\x02 \x01(\x0b\x32+.coresdk.common.NamespacedWorkflowExecutionH\x00\x12\x1b\n\x11\x63hild_workflow_id\x18\x03 \x01(\tH\x00\x12\x13\n\x0bsignal_name\x18\x04 \x01(\t\x12-\n\x04\x61rgs\x18\x05 \x03(\x0b\x32\x1f.temporal.api.common.v1.Payload\x12X\n\x07headers\x18\x06 \x03(\x0b\x32G.coresdk.workflow_commands.SignalExternalWorkflowExecution.HeadersEntry\x1aO\n\x0cHeadersEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12.\n\x05value\x18\x02 \x01(\x0b\x32\x1f.temporal.api.common.v1.Payload:\x02\x38\x01\x42\x08\n\x06target"#\n\x14\x43\x61ncelSignalWorkflow\x12\x0b\n\x03seq\x18\x01 \x01(\r"\xe6\x01\n\x1eUpsertWorkflowSearchAttributes\x12j\n\x11search_attributes\x18\x01 \x03(\x0b\x32O.coresdk.workflow_commands.UpsertWorkflowSearchAttributes.SearchAttributesEntry\x1aX\n\x15SearchAttributesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12.\n\x05value\x18\x02 \x01(\x0b\x32\x1f.temporal.api.common.v1.Payload:\x02\x38\x01"O\n\x18ModifyWorkflowProperties\x12\x33\n\rupserted_memo\x18\x01 \x01(\x0b\x32\x1c.temporal.api.common.v1.Memo"\xd2\x01\n\x0eUpdateResponse\x12\x1c\n\x14protocol_instance_id\x18\x01 \x01(\t\x12*\n\x08\x61\x63\x63\x65pted\x18\x02 \x01(\x0b\x32\x16.google.protobuf.EmptyH\x00\x12\x34\n\x08rejected\x18\x03 \x01(\x0b\x32 .temporal.api.failure.v1.FailureH\x00\x12\x34\n\tcompleted\x18\x04 \x01(\x0b\x32\x1f.temporal.api.common.v1.PayloadH\x00\x42\n\n\x08response"\xa1\x03\n\x16ScheduleNexusOperation\x12\x0b\n\x03seq\x18\x01 \x01(\r\x12\x10\n\x08\x65ndpoint\x18\x02 \x01(\t\x12\x0f\n\x07service\x18\x03 \x01(\t\x12\x11\n\toperation\x18\x04 \x01(\t\x12.\n\x05input\x18\x05 \x01(\x0b\x32\x1f.temporal.api.common.v1.Payload\x12<\n\x19schedule_to_close_timeout\x18\x06 \x01(\x0b\x32\x19.google.protobuf.Duration\x12X\n\x0cnexus_header\x18\x07 \x03(\x0b\x32\x42.coresdk.workflow_commands.ScheduleNexusOperation.NexusHeaderEntry\x12H\n\x11\x63\x61ncellation_type\x18\x08 \x01(\x0e\x32-.coresdk.nexus.NexusOperationCancellationType\x1a\x32\n\x10NexusHeaderEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01"*\n\x1bRequestCancelNexusOperation\x12\x0b\n\x03seq\x18\x01 \x01(\r*X\n\x18\x41\x63tivityCancellationType\x12\x0e\n\nTRY_CANCEL\x10\x00\x12\x1f\n\x1bWAIT_CANCELLATION_COMPLETED\x10\x01\x12\x0b\n\x07\x41\x42\x41NDON\x10\x02\x42\x36\xea\x02\x33Temporalio::Internal::Bridge::Api::WorkflowCommandsb\x06proto3'
)

_ACTIVITYCANCELLATIONTYPE = DESCRIPTOR.enum_types_by_name["ActivityCancellationType"]
ActivityCancellationType = enum_type_wrapper.EnumTypeWrapper(_ACTIVITYCANCELLATIONTYPE)
TRY_CANCEL = 0
WAIT_CANCELLATION_COMPLETED = 1
ABANDON = 2


_WORKFLOWCOMMAND = DESCRIPTOR.message_types_by_name["WorkflowCommand"]
_STARTTIMER = DESCRIPTOR.message_types_by_name["StartTimer"]
_CANCELTIMER = DESCRIPTOR.message_types_by_name["CancelTimer"]
_SCHEDULEACTIVITY = DESCRIPTOR.message_types_by_name["ScheduleActivity"]
_SCHEDULEACTIVITY_HEADERSENTRY = _SCHEDULEACTIVITY.nested_types_by_name["HeadersEntry"]
_SCHEDULELOCALACTIVITY = DESCRIPTOR.message_types_by_name["ScheduleLocalActivity"]
_SCHEDULELOCALACTIVITY_HEADERSENTRY = _SCHEDULELOCALACTIVITY.nested_types_by_name[
    "HeadersEntry"
]
_REQUESTCANCELACTIVITY = DESCRIPTOR.message_types_by_name["RequestCancelActivity"]
_REQUESTCANCELLOCALACTIVITY = DESCRIPTOR.message_types_by_name[
    "RequestCancelLocalActivity"
]
_QUERYRESULT = DESCRIPTOR.message_types_by_name["QueryResult"]
_QUERYSUCCESS = DESCRIPTOR.message_types_by_name["QuerySuccess"]
_COMPLETEWORKFLOWEXECUTION = DESCRIPTOR.message_types_by_name[
    "CompleteWorkflowExecution"
]
_FAILWORKFLOWEXECUTION = DESCRIPTOR.message_types_by_name["FailWorkflowExecution"]
_CONTINUEASNEWWORKFLOWEXECUTION = DESCRIPTOR.message_types_by_name[
    "ContinueAsNewWorkflowExecution"
]
_CONTINUEASNEWWORKFLOWEXECUTION_MEMOENTRY = (
    _CONTINUEASNEWWORKFLOWEXECUTION.nested_types_by_name["MemoEntry"]
)
_CONTINUEASNEWWORKFLOWEXECUTION_HEADERSENTRY = (
    _CONTINUEASNEWWORKFLOWEXECUTION.nested_types_by_name["HeadersEntry"]
)
_CONTINUEASNEWWORKFLOWEXECUTION_SEARCHATTRIBUTESENTRY = (
    _CONTINUEASNEWWORKFLOWEXECUTION.nested_types_by_name["SearchAttributesEntry"]
)
_CANCELWORKFLOWEXECUTION = DESCRIPTOR.message_types_by_name["CancelWorkflowExecution"]
_SETPATCHMARKER = DESCRIPTOR.message_types_by_name["SetPatchMarker"]
_STARTCHILDWORKFLOWEXECUTION = DESCRIPTOR.message_types_by_name[
    "StartChildWorkflowExecution"
]
_STARTCHILDWORKFLOWEXECUTION_HEADERSENTRY = (
    _STARTCHILDWORKFLOWEXECUTION.nested_types_by_name["HeadersEntry"]
)
_STARTCHILDWORKFLOWEXECUTION_MEMOENTRY = (
    _STARTCHILDWORKFLOWEXECUTION.nested_types_by_name["MemoEntry"]
)
_STARTCHILDWORKFLOWEXECUTION_SEARCHATTRIBUTESENTRY = (
    _STARTCHILDWORKFLOWEXECUTION.nested_types_by_name["SearchAttributesEntry"]
)
_CANCELCHILDWORKFLOWEXECUTION = DESCRIPTOR.message_types_by_name[
    "CancelChildWorkflowExecution"
]
_REQUESTCANCELEXTERNALWORKFLOWEXECUTION = DESCRIPTOR.message_types_by_name[
    "RequestCancelExternalWorkflowExecution"
]
_SIGNALEXTERNALWORKFLOWEXECUTION = DESCRIPTOR.message_types_by_name[
    "SignalExternalWorkflowExecution"
]
_SIGNALEXTERNALWORKFLOWEXECUTION_HEADERSENTRY = (
    _SIGNALEXTERNALWORKFLOWEXECUTION.nested_types_by_name["HeadersEntry"]
)
_CANCELSIGNALWORKFLOW = DESCRIPTOR.message_types_by_name["CancelSignalWorkflow"]
_UPSERTWORKFLOWSEARCHATTRIBUTES = DESCRIPTOR.message_types_by_name[
    "UpsertWorkflowSearchAttributes"
]
_UPSERTWORKFLOWSEARCHATTRIBUTES_SEARCHATTRIBUTESENTRY = (
    _UPSERTWORKFLOWSEARCHATTRIBUTES.nested_types_by_name["SearchAttributesEntry"]
)
_MODIFYWORKFLOWPROPERTIES = DESCRIPTOR.message_types_by_name["ModifyWorkflowProperties"]
_UPDATERESPONSE = DESCRIPTOR.message_types_by_name["UpdateResponse"]
_SCHEDULENEXUSOPERATION = DESCRIPTOR.message_types_by_name["ScheduleNexusOperation"]
_SCHEDULENEXUSOPERATION_NEXUSHEADERENTRY = _SCHEDULENEXUSOPERATION.nested_types_by_name[
    "NexusHeaderEntry"
]
_REQUESTCANCELNEXUSOPERATION = DESCRIPTOR.message_types_by_name[
    "RequestCancelNexusOperation"
]
WorkflowCommand = _reflection.GeneratedProtocolMessageType(
    "WorkflowCommand",
    (_message.Message,),
    {
        "DESCRIPTOR": _WORKFLOWCOMMAND,
        "__module__": "temporal.sdk.core.workflow_commands.workflow_commands_pb2",
        # @@protoc_insertion_point(class_scope:coresdk.workflow_commands.WorkflowCommand)
    },
)
_sym_db.RegisterMessage(WorkflowCommand)

StartTimer = _reflection.GeneratedProtocolMessageType(
    "StartTimer",
    (_message.Message,),
    {
        "DESCRIPTOR": _STARTTIMER,
        "__module__": "temporal.sdk.core.workflow_commands.workflow_commands_pb2",
        # @@protoc_insertion_point(class_scope:coresdk.workflow_commands.StartTimer)
    },
)
_sym_db.RegisterMessage(StartTimer)

CancelTimer = _reflection.GeneratedProtocolMessageType(
    "CancelTimer",
    (_message.Message,),
    {
        "DESCRIPTOR": _CANCELTIMER,
        "__module__": "temporal.sdk.core.workflow_commands.workflow_commands_pb2",
        # @@protoc_insertion_point(class_scope:coresdk.workflow_commands.CancelTimer)
    },
)
_sym_db.RegisterMessage(CancelTimer)

ScheduleActivity = _reflection.GeneratedProtocolMessageType(
    "ScheduleActivity",
    (_message.Message,),
    {
        "HeadersEntry": _reflection.GeneratedProtocolMessageType(
            "HeadersEntry",
            (_message.Message,),
            {
                "DESCRIPTOR": _SCHEDULEACTIVITY_HEADERSENTRY,
                "__module__": "temporal.sdk.core.workflow_commands.workflow_commands_pb2",
                # @@protoc_insertion_point(class_scope:coresdk.workflow_commands.ScheduleActivity.HeadersEntry)
            },
        ),
        "DESCRIPTOR": _SCHEDULEACTIVITY,
        "__module__": "temporal.sdk.core.workflow_commands.workflow_commands_pb2",
        # @@protoc_insertion_point(class_scope:coresdk.workflow_commands.ScheduleActivity)
    },
)
_sym_db.RegisterMessage(ScheduleActivity)
_sym_db.RegisterMessage(ScheduleActivity.HeadersEntry)

ScheduleLocalActivity = _reflection.GeneratedProtocolMessageType(
    "ScheduleLocalActivity",
    (_message.Message,),
    {
        "HeadersEntry": _reflection.GeneratedProtocolMessageType(
            "HeadersEntry",
            (_message.Message,),
            {
                "DESCRIPTOR": _SCHEDULELOCALACTIVITY_HEADERSENTRY,
                "__module__": "temporal.sdk.core.workflow_commands.workflow_commands_pb2",
                # @@protoc_insertion_point(class_scope:coresdk.workflow_commands.ScheduleLocalActivity.HeadersEntry)
            },
        ),
        "DESCRIPTOR": _SCHEDULELOCALACTIVITY,
        "__module__": "temporal.sdk.core.workflow_commands.workflow_commands_pb2",
        # @@protoc_insertion_point(class_scope:coresdk.workflow_commands.ScheduleLocalActivity)
    },
)
_sym_db.RegisterMessage(ScheduleLocalActivity)
_sym_db.RegisterMessage(ScheduleLocalActivity.HeadersEntry)

RequestCancelActivity = _reflection.GeneratedProtocolMessageType(
    "RequestCancelActivity",
    (_message.Message,),
    {
        "DESCRIPTOR": _REQUESTCANCELACTIVITY,
        "__module__": "temporal.sdk.core.workflow_commands.workflow_commands_pb2",
        # @@protoc_insertion_point(class_scope:coresdk.workflow_commands.RequestCancelActivity)
    },
)
_sym_db.RegisterMessage(RequestCancelActivity)

RequestCancelLocalActivity = _reflection.GeneratedProtocolMessageType(
    "RequestCancelLocalActivity",
    (_message.Message,),
    {
        "DESCRIPTOR": _REQUESTCANCELLOCALACTIVITY,
        "__module__": "temporal.sdk.core.workflow_commands.workflow_commands_pb2",
        # @@protoc_insertion_point(class_scope:coresdk.workflow_commands.RequestCancelLocalActivity)
    },
)
_sym_db.RegisterMessage(RequestCancelLocalActivity)

QueryResult = _reflection.GeneratedProtocolMessageType(
    "QueryResult",
    (_message.Message,),
    {
        "DESCRIPTOR": _QUERYRESULT,
        "__module__": "temporal.sdk.core.workflow_commands.workflow_commands_pb2",
        # @@protoc_insertion_point(class_scope:coresdk.workflow_commands.QueryResult)
    },
)
_sym_db.RegisterMessage(QueryResult)

QuerySuccess = _reflection.GeneratedProtocolMessageType(
    "QuerySuccess",
    (_message.Message,),
    {
        "DESCRIPTOR": _QUERYSUCCESS,
        "__module__": "temporal.sdk.core.workflow_commands.workflow_commands_pb2",
        # @@protoc_insertion_point(class_scope:coresdk.workflow_commands.QuerySuccess)
    },
)
_sym_db.RegisterMessage(QuerySuccess)

CompleteWorkflowExecution = _reflection.GeneratedProtocolMessageType(
    "CompleteWorkflowExecution",
    (_message.Message,),
    {
        "DESCRIPTOR": _COMPLETEWORKFLOWEXECUTION,
        "__module__": "temporal.sdk.core.workflow_commands.workflow_commands_pb2",
        # @@protoc_insertion_point(class_scope:coresdk.workflow_commands.CompleteWorkflowExecution)
    },
)
_sym_db.RegisterMessage(CompleteWorkflowExecution)

FailWorkflowExecution = _reflection.GeneratedProtocolMessageType(
    "FailWorkflowExecution",
    (_message.Message,),
    {
        "DESCRIPTOR": _FAILWORKFLOWEXECUTION,
        "__module__": "temporal.sdk.core.workflow_commands.workflow_commands_pb2",
        # @@protoc_insertion_point(class_scope:coresdk.workflow_commands.FailWorkflowExecution)
    },
)
_sym_db.RegisterMessage(FailWorkflowExecution)

ContinueAsNewWorkflowExecution = _reflection.GeneratedProtocolMessageType(
    "ContinueAsNewWorkflowExecution",
    (_message.Message,),
    {
        "MemoEntry": _reflection.GeneratedProtocolMessageType(
            "MemoEntry",
            (_message.Message,),
            {
                "DESCRIPTOR": _CONTINUEASNEWWORKFLOWEXECUTION_MEMOENTRY,
                "__module__": "temporal.sdk.core.workflow_commands.workflow_commands_pb2",
                # @@protoc_insertion_point(class_scope:coresdk.workflow_commands.ContinueAsNewWorkflowExecution.MemoEntry)
            },
        ),
        "HeadersEntry": _reflection.GeneratedProtocolMessageType(
            "HeadersEntry",
            (_message.Message,),
            {
                "DESCRIPTOR": _CONTINUEASNEWWORKFLOWEXECUTION_HEADERSENTRY,
                "__module__": "temporal.sdk.core.workflow_commands.workflow_commands_pb2",
                # @@protoc_insertion_point(class_scope:coresdk.workflow_commands.ContinueAsNewWorkflowExecution.HeadersEntry)
            },
        ),
        "SearchAttributesEntry": _reflection.GeneratedProtocolMessageType(
            "SearchAttributesEntry",
            (_message.Message,),
            {
                "DESCRIPTOR": _CONTINUEASNEWWORKFLOWEXECUTION_SEARCHATTRIBUTESENTRY,
                "__module__": "temporal.sdk.core.workflow_commands.workflow_commands_pb2",
                # @@protoc_insertion_point(class_scope:coresdk.workflow_commands.ContinueAsNewWorkflowExecution.SearchAttributesEntry)
            },
        ),
        "DESCRIPTOR": _CONTINUEASNEWWORKFLOWEXECUTION,
        "__module__": "temporal.sdk.core.workflow_commands.workflow_commands_pb2",
        # @@protoc_insertion_point(class_scope:coresdk.workflow_commands.ContinueAsNewWorkflowExecution)
    },
)
_sym_db.RegisterMessage(ContinueAsNewWorkflowExecution)
_sym_db.RegisterMessage(ContinueAsNewWorkflowExecution.MemoEntry)
_sym_db.RegisterMessage(ContinueAsNewWorkflowExecution.HeadersEntry)
_sym_db.RegisterMessage(ContinueAsNewWorkflowExecution.SearchAttributesEntry)

CancelWorkflowExecution = _reflection.GeneratedProtocolMessageType(
    "CancelWorkflowExecution",
    (_message.Message,),
    {
        "DESCRIPTOR": _CANCELWORKFLOWEXECUTION,
        "__module__": "temporal.sdk.core.workflow_commands.workflow_commands_pb2",
        # @@protoc_insertion_point(class_scope:coresdk.workflow_commands.CancelWorkflowExecution)
    },
)
_sym_db.RegisterMessage(CancelWorkflowExecution)

SetPatchMarker = _reflection.GeneratedProtocolMessageType(
    "SetPatchMarker",
    (_message.Message,),
    {
        "DESCRIPTOR": _SETPATCHMARKER,
        "__module__": "temporal.sdk.core.workflow_commands.workflow_commands_pb2",
        # @@protoc_insertion_point(class_scope:coresdk.workflow_commands.SetPatchMarker)
    },
)
_sym_db.RegisterMessage(SetPatchMarker)

StartChildWorkflowExecution = _reflection.GeneratedProtocolMessageType(
    "StartChildWorkflowExecution",
    (_message.Message,),
    {
        "HeadersEntry": _reflection.GeneratedProtocolMessageType(
            "HeadersEntry",
            (_message.Message,),
            {
                "DESCRIPTOR": _STARTCHILDWORKFLOWEXECUTION_HEADERSENTRY,
                "__module__": "temporal.sdk.core.workflow_commands.workflow_commands_pb2",
                # @@protoc_insertion_point(class_scope:coresdk.workflow_commands.StartChildWorkflowExecution.HeadersEntry)
            },
        ),
        "MemoEntry": _reflection.GeneratedProtocolMessageType(
            "MemoEntry",
            (_message.Message,),
            {
                "DESCRIPTOR": _STARTCHILDWORKFLOWEXECUTION_MEMOENTRY,
                "__module__": "temporal.sdk.core.workflow_commands.workflow_commands_pb2",
                # @@protoc_insertion_point(class_scope:coresdk.workflow_commands.StartChildWorkflowExecution.MemoEntry)
            },
        ),
        "SearchAttributesEntry": _reflection.GeneratedProtocolMessageType(
            "SearchAttributesEntry",
            (_message.Message,),
            {
                "DESCRIPTOR": _STARTCHILDWORKFLOWEXECUTION_SEARCHATTRIBUTESENTRY,
                "__module__": "temporal.sdk.core.workflow_commands.workflow_commands_pb2",
                # @@protoc_insertion_point(class_scope:coresdk.workflow_commands.StartChildWorkflowExecution.SearchAttributesEntry)
            },
        ),
        "DESCRIPTOR": _STARTCHILDWORKFLOWEXECUTION,
        "__module__": "temporal.sdk.core.workflow_commands.workflow_commands_pb2",
        # @@protoc_insertion_point(class_scope:coresdk.workflow_commands.StartChildWorkflowExecution)
    },
)
_sym_db.RegisterMessage(StartChildWorkflowExecution)
_sym_db.RegisterMessage(StartChildWorkflowExecution.HeadersEntry)
_sym_db.RegisterMessage(StartChildWorkflowExecution.MemoEntry)
_sym_db.RegisterMessage(StartChildWorkflowExecution.SearchAttributesEntry)

CancelChildWorkflowExecution = _reflection.GeneratedProtocolMessageType(
    "CancelChildWorkflowExecution",
    (_message.Message,),
    {
        "DESCRIPTOR": _CANCELCHILDWORKFLOWEXECUTION,
        "__module__": "temporal.sdk.core.workflow_commands.workflow_commands_pb2",
        # @@protoc_insertion_point(class_scope:coresdk.workflow_commands.CancelChildWorkflowExecution)
    },
)
_sym_db.RegisterMessage(CancelChildWorkflowExecution)

RequestCancelExternalWorkflowExecution = _reflection.GeneratedProtocolMessageType(
    "RequestCancelExternalWorkflowExecution",
    (_message.Message,),
    {
        "DESCRIPTOR": _REQUESTCANCELEXTERNALWORKFLOWEXECUTION,
        "__module__": "temporal.sdk.core.workflow_commands.workflow_commands_pb2",
        # @@protoc_insertion_point(class_scope:coresdk.workflow_commands.RequestCancelExternalWorkflowExecution)
    },
)
_sym_db.RegisterMessage(RequestCancelExternalWorkflowExecution)

SignalExternalWorkflowExecution = _reflection.GeneratedProtocolMessageType(
    "SignalExternalWorkflowExecution",
    (_message.Message,),
    {
        "HeadersEntry": _reflection.GeneratedProtocolMessageType(
            "HeadersEntry",
            (_message.Message,),
            {
                "DESCRIPTOR": _SIGNALEXTERNALWORKFLOWEXECUTION_HEADERSENTRY,
                "__module__": "temporal.sdk.core.workflow_commands.workflow_commands_pb2",
                # @@protoc_insertion_point(class_scope:coresdk.workflow_commands.SignalExternalWorkflowExecution.HeadersEntry)
            },
        ),
        "DESCRIPTOR": _SIGNALEXTERNALWORKFLOWEXECUTION,
        "__module__": "temporal.sdk.core.workflow_commands.workflow_commands_pb2",
        # @@protoc_insertion_point(class_scope:coresdk.workflow_commands.SignalExternalWorkflowExecution)
    },
)
_sym_db.RegisterMessage(SignalExternalWorkflowExecution)
_sym_db.RegisterMessage(SignalExternalWorkflowExecution.HeadersEntry)

CancelSignalWorkflow = _reflection.GeneratedProtocolMessageType(
    "CancelSignalWorkflow",
    (_message.Message,),
    {
        "DESCRIPTOR": _CANCELSIGNALWORKFLOW,
        "__module__": "temporal.sdk.core.workflow_commands.workflow_commands_pb2",
        # @@protoc_insertion_point(class_scope:coresdk.workflow_commands.CancelSignalWorkflow)
    },
)
_sym_db.RegisterMessage(CancelSignalWorkflow)

UpsertWorkflowSearchAttributes = _reflection.GeneratedProtocolMessageType(
    "UpsertWorkflowSearchAttributes",
    (_message.Message,),
    {
        "SearchAttributesEntry": _reflection.GeneratedProtocolMessageType(
            "SearchAttributesEntry",
            (_message.Message,),
            {
                "DESCRIPTOR": _UPSERTWORKFLOWSEARCHATTRIBUTES_SEARCHATTRIBUTESENTRY,
                "__module__": "temporal.sdk.core.workflow_commands.workflow_commands_pb2",
                # @@protoc_insertion_point(class_scope:coresdk.workflow_commands.UpsertWorkflowSearchAttributes.SearchAttributesEntry)
            },
        ),
        "DESCRIPTOR": _UPSERTWORKFLOWSEARCHATTRIBUTES,
        "__module__": "temporal.sdk.core.workflow_commands.workflow_commands_pb2",
        # @@protoc_insertion_point(class_scope:coresdk.workflow_commands.UpsertWorkflowSearchAttributes)
    },
)
_sym_db.RegisterMessage(UpsertWorkflowSearchAttributes)
_sym_db.RegisterMessage(UpsertWorkflowSearchAttributes.SearchAttributesEntry)

ModifyWorkflowProperties = _reflection.GeneratedProtocolMessageType(
    "ModifyWorkflowProperties",
    (_message.Message,),
    {
        "DESCRIPTOR": _MODIFYWORKFLOWPROPERTIES,
        "__module__": "temporal.sdk.core.workflow_commands.workflow_commands_pb2",
        # @@protoc_insertion_point(class_scope:coresdk.workflow_commands.ModifyWorkflowProperties)
    },
)
_sym_db.RegisterMessage(ModifyWorkflowProperties)

UpdateResponse = _reflection.GeneratedProtocolMessageType(
    "UpdateResponse",
    (_message.Message,),
    {
        "DESCRIPTOR": _UPDATERESPONSE,
        "__module__": "temporal.sdk.core.workflow_commands.workflow_commands_pb2",
        # @@protoc_insertion_point(class_scope:coresdk.workflow_commands.UpdateResponse)
    },
)
_sym_db.RegisterMessage(UpdateResponse)

ScheduleNexusOperation = _reflection.GeneratedProtocolMessageType(
    "ScheduleNexusOperation",
    (_message.Message,),
    {
        "NexusHeaderEntry": _reflection.GeneratedProtocolMessageType(
            "NexusHeaderEntry",
            (_message.Message,),
            {
                "DESCRIPTOR": _SCHEDULENEXUSOPERATION_NEXUSHEADERENTRY,
                "__module__": "temporal.sdk.core.workflow_commands.workflow_commands_pb2",
                # @@protoc_insertion_point(class_scope:coresdk.workflow_commands.ScheduleNexusOperation.NexusHeaderEntry)
            },
        ),
        "DESCRIPTOR": _SCHEDULENEXUSOPERATION,
        "__module__": "temporal.sdk.core.workflow_commands.workflow_commands_pb2",
        # @@protoc_insertion_point(class_scope:coresdk.workflow_commands.ScheduleNexusOperation)
    },
)
_sym_db.RegisterMessage(ScheduleNexusOperation)
_sym_db.RegisterMessage(ScheduleNexusOperation.NexusHeaderEntry)

RequestCancelNexusOperation = _reflection.GeneratedProtocolMessageType(
    "RequestCancelNexusOperation",
    (_message.Message,),
    {
        "DESCRIPTOR": _REQUESTCANCELNEXUSOPERATION,
        "__module__": "temporal.sdk.core.workflow_commands.workflow_commands_pb2",
        # @@protoc_insertion_point(class_scope:coresdk.workflow_commands.RequestCancelNexusOperation)
    },
)
_sym_db.RegisterMessage(RequestCancelNexusOperation)

if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = (
        b"\352\0023Temporalio::Internal::Bridge::Api::WorkflowCommands"
    )
    _SCHEDULEACTIVITY_HEADERSENTRY._options = None
    _SCHEDULEACTIVITY_HEADERSENTRY._serialized_options = b"8\001"
    _SCHEDULELOCALACTIVITY_HEADERSENTRY._options = None
    _SCHEDULELOCALACTIVITY_HEADERSENTRY._serialized_options = b"8\001"
    _CONTINUEASNEWWORKFLOWEXECUTION_MEMOENTRY._options = None
    _CONTINUEASNEWWORKFLOWEXECUTION_MEMOENTRY._serialized_options = b"8\001"
    _CONTINUEASNEWWORKFLOWEXECUTION_HEADERSENTRY._options = None
    _CONTINUEASNEWWORKFLOWEXECUTION_HEADERSENTRY._serialized_options = b"8\001"
    _CONTINUEASNEWWORKFLOWEXECUTION_SEARCHATTRIBUTESENTRY._options = None
    _CONTINUEASNEWWORKFLOWEXECUTION_SEARCHATTRIBUTESENTRY._serialized_options = b"8\001"
    _STARTCHILDWORKFLOWEXECUTION_HEADERSENTRY._options = None
    _STARTCHILDWORKFLOWEXECUTION_HEADERSENTRY._serialized_options = b"8\001"
    _STARTCHILDWORKFLOWEXECUTION_MEMOENTRY._options = None
    _STARTCHILDWORKFLOWEXECUTION_MEMOENTRY._serialized_options = b"8\001"
    _STARTCHILDWORKFLOWEXECUTION_SEARCHATTRIBUTESENTRY._options = None
    _STARTCHILDWORKFLOWEXECUTION_SEARCHATTRIBUTESENTRY._serialized_options = b"8\001"
    _SIGNALEXTERNALWORKFLOWEXECUTION_HEADERSENTRY._options = None
    _SIGNALEXTERNALWORKFLOWEXECUTION_HEADERSENTRY._serialized_options = b"8\001"
    _UPSERTWORKFLOWSEARCHATTRIBUTES_SEARCHATTRIBUTESENTRY._options = None
    _UPSERTWORKFLOWSEARCHATTRIBUTES_SEARCHATTRIBUTESENTRY._serialized_options = b"8\001"
    _SCHEDULENEXUSOPERATION_NEXUSHEADERENTRY._options = None
    _SCHEDULENEXUSOPERATION_NEXUSHEADERENTRY._serialized_options = b"8\001"
    _ACTIVITYCANCELLATIONTYPE._serialized_start = 8580
    _ACTIVITYCANCELLATIONTYPE._serialized_end = 8668
    _WORKFLOWCOMMAND._serialized_start = 472
    _WORKFLOWCOMMAND._serialized_end = 2493
    _STARTTIMER._serialized_start = 2495
    _STARTTIMER._serialized_end = 2578
    _CANCELTIMER._serialized_start = 2580
    _CANCELTIMER._serialized_end = 2606
    _SCHEDULEACTIVITY._serialized_start = 2609
    _SCHEDULEACTIVITY._serialized_end = 3433
    _SCHEDULEACTIVITY_HEADERSENTRY._serialized_start = 3354
    _SCHEDULEACTIVITY_HEADERSENTRY._serialized_end = 3433
    _SCHEDULELOCALACTIVITY._serialized_start = 3436
    _SCHEDULELOCALACTIVITY._serialized_end = 4186
    _SCHEDULELOCALACTIVITY_HEADERSENTRY._serialized_start = 3354
    _SCHEDULELOCALACTIVITY_HEADERSENTRY._serialized_end = 3433
    _REQUESTCANCELACTIVITY._serialized_start = 4188
    _REQUESTCANCELACTIVITY._serialized_end = 4224
    _REQUESTCANCELLOCALACTIVITY._serialized_start = 4226
    _REQUESTCANCELLOCALACTIVITY._serialized_end = 4267
    _QUERYRESULT._serialized_start = 4270
    _QUERYRESULT._serialized_end = 4426
    _QUERYSUCCESS._serialized_start = 4428
    _QUERYSUCCESS._serialized_end = 4493
    _COMPLETEWORKFLOWEXECUTION._serialized_start = 4495
    _COMPLETEWORKFLOWEXECUTION._serialized_end = 4571
    _FAILWORKFLOWEXECUTION._serialized_start = 4573
    _FAILWORKFLOWEXECUTION._serialized_end = 4647
    _CONTINUEASNEWWORKFLOWEXECUTION._serialized_start = 4650
    _CONTINUEASNEWWORKFLOWEXECUTION._serialized_end = 5541
    _CONTINUEASNEWWORKFLOWEXECUTION_MEMOENTRY._serialized_start = 5294
    _CONTINUEASNEWWORKFLOWEXECUTION_MEMOENTRY._serialized_end = 5370
    _CONTINUEASNEWWORKFLOWEXECUTION_HEADERSENTRY._serialized_start = 3354
    _CONTINUEASNEWWORKFLOWEXECUTION_HEADERSENTRY._serialized_end = 3433
    _CONTINUEASNEWWORKFLOWEXECUTION_SEARCHATTRIBUTESENTRY._serialized_start = 5453
    _CONTINUEASNEWWORKFLOWEXECUTION_SEARCHATTRIBUTESENTRY._serialized_end = 5541
    _CANCELWORKFLOWEXECUTION._serialized_start = 5543
    _CANCELWORKFLOWEXECUTION._serialized_end = 5568
    _SETPATCHMARKER._serialized_start = 5570
    _SETPATCHMARKER._serialized_end = 5624
    _STARTCHILDWORKFLOWEXECUTION._serialized_start = 5627
    _STARTCHILDWORKFLOWEXECUTION._serialized_end = 6927
    _STARTCHILDWORKFLOWEXECUTION_HEADERSENTRY._serialized_start = 3354
    _STARTCHILDWORKFLOWEXECUTION_HEADERSENTRY._serialized_end = 3433
    _STARTCHILDWORKFLOWEXECUTION_MEMOENTRY._serialized_start = 5294
    _STARTCHILDWORKFLOWEXECUTION_MEMOENTRY._serialized_end = 5370
    _STARTCHILDWORKFLOWEXECUTION_SEARCHATTRIBUTESENTRY._serialized_start = 5453
    _STARTCHILDWORKFLOWEXECUTION_SEARCHATTRIBUTESENTRY._serialized_end = 5541
    _CANCELCHILDWORKFLOWEXECUTION._serialized_start = 6929
    _CANCELCHILDWORKFLOWEXECUTION._serialized_end = 7003
    _REQUESTCANCELEXTERNALWORKFLOWEXECUTION._serialized_start = 7006
    _REQUESTCANCELEXTERNALWORKFLOWEXECUTION._serialized_end = 7148
    _SIGNALEXTERNALWORKFLOWEXECUTION._serialized_start = 7151
    _SIGNALEXTERNALWORKFLOWEXECUTION._serialized_end = 7550
    _SIGNALEXTERNALWORKFLOWEXECUTION_HEADERSENTRY._serialized_start = 3354
    _SIGNALEXTERNALWORKFLOWEXECUTION_HEADERSENTRY._serialized_end = 3433
    _CANCELSIGNALWORKFLOW._serialized_start = 7552
    _CANCELSIGNALWORKFLOW._serialized_end = 7587
    _UPSERTWORKFLOWSEARCHATTRIBUTES._serialized_start = 7590
    _UPSERTWORKFLOWSEARCHATTRIBUTES._serialized_end = 7820
    _UPSERTWORKFLOWSEARCHATTRIBUTES_SEARCHATTRIBUTESENTRY._serialized_start = 5453
    _UPSERTWORKFLOWSEARCHATTRIBUTES_SEARCHATTRIBUTESENTRY._serialized_end = 5541
    _MODIFYWORKFLOWPROPERTIES._serialized_start = 7822
    _MODIFYWORKFLOWPROPERTIES._serialized_end = 7901
    _UPDATERESPONSE._serialized_start = 7904
    _UPDATERESPONSE._serialized_end = 8114
    _SCHEDULENEXUSOPERATION._serialized_start = 8117
    _SCHEDULENEXUSOPERATION._serialized_end = 8534
    _SCHEDULENEXUSOPERATION_NEXUSHEADERENTRY._serialized_start = 8484
    _SCHEDULENEXUSOPERATION_NEXUSHEADERENTRY._serialized_end = 8534
    _REQUESTCANCELNEXUSOPERATION._serialized_start = 8536
    _REQUESTCANCELNEXUSOPERATION._serialized_end = 8578
# @@protoc_insertion_point(module_scope)
