"""
Type annotations for ssm service literal definitions.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm/literals/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from mypy_boto3_ssm.literals import AccessRequestStatusType

    data: AccessRequestStatusType = "Approved"
    ```
"""

import sys

if sys.version_info >= (3, 12):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = (
    "AccessRequestStatusType",
    "AccessTypeType",
    "AssociationComplianceSeverityType",
    "AssociationExecutionFilterKeyType",
    "AssociationExecutionTargetsFilterKeyType",
    "AssociationFilterKeyType",
    "AssociationFilterOperatorTypeType",
    "AssociationStatusNameType",
    "AssociationSyncComplianceType",
    "AttachmentHashTypeType",
    "AttachmentsSourceKeyType",
    "AutomationExecutionFilterKeyType",
    "AutomationExecutionStatusType",
    "AutomationSubtypeType",
    "AutomationTypeType",
    "CalendarStateType",
    "CommandExecutedWaiterName",
    "CommandFilterKeyType",
    "CommandInvocationStatusType",
    "CommandPluginStatusType",
    "CommandStatusType",
    "ComplianceQueryOperatorTypeType",
    "ComplianceSeverityType",
    "ComplianceStatusType",
    "ComplianceUploadTypeType",
    "ConnectionStatusType",
    "DescribeActivationsFilterKeysType",
    "DescribeActivationsPaginatorName",
    "DescribeAssociationExecutionTargetsPaginatorName",
    "DescribeAssociationExecutionsPaginatorName",
    "DescribeAutomationExecutionsPaginatorName",
    "DescribeAutomationStepExecutionsPaginatorName",
    "DescribeAvailablePatchesPaginatorName",
    "DescribeEffectiveInstanceAssociationsPaginatorName",
    "DescribeEffectivePatchesForPatchBaselinePaginatorName",
    "DescribeInstanceAssociationsStatusPaginatorName",
    "DescribeInstanceInformationPaginatorName",
    "DescribeInstancePatchStatesForPatchGroupPaginatorName",
    "DescribeInstancePatchStatesPaginatorName",
    "DescribeInstancePatchesPaginatorName",
    "DescribeInstancePropertiesPaginatorName",
    "DescribeInventoryDeletionsPaginatorName",
    "DescribeMaintenanceWindowExecutionTaskInvocationsPaginatorName",
    "DescribeMaintenanceWindowExecutionTasksPaginatorName",
    "DescribeMaintenanceWindowExecutionsPaginatorName",
    "DescribeMaintenanceWindowSchedulePaginatorName",
    "DescribeMaintenanceWindowTargetsPaginatorName",
    "DescribeMaintenanceWindowTasksPaginatorName",
    "DescribeMaintenanceWindowsForTargetPaginatorName",
    "DescribeMaintenanceWindowsPaginatorName",
    "DescribeOpsItemsPaginatorName",
    "DescribeParametersPaginatorName",
    "DescribePatchBaselinesPaginatorName",
    "DescribePatchGroupsPaginatorName",
    "DescribePatchPropertiesPaginatorName",
    "DescribeSessionsPaginatorName",
    "DocumentFilterKeyType",
    "DocumentFormatType",
    "DocumentHashTypeType",
    "DocumentMetadataEnumType",
    "DocumentParameterTypeType",
    "DocumentPermissionTypeType",
    "DocumentReviewActionType",
    "DocumentReviewCommentTypeType",
    "DocumentStatusType",
    "DocumentTypeType",
    "ExecutionModeType",
    "ExecutionPreviewStatusType",
    "ExternalAlarmStateType",
    "FaultType",
    "GetInventoryPaginatorName",
    "GetInventorySchemaPaginatorName",
    "GetOpsSummaryPaginatorName",
    "GetParameterHistoryPaginatorName",
    "GetParametersByPathPaginatorName",
    "GetResourcePoliciesPaginatorName",
    "ImpactTypeType",
    "InstanceInformationFilterKeyType",
    "InstancePatchStateOperatorTypeType",
    "InstancePropertyFilterKeyType",
    "InstancePropertyFilterOperatorType",
    "InventoryAttributeDataTypeType",
    "InventoryDeletionStatusType",
    "InventoryQueryOperatorTypeType",
    "InventorySchemaDeleteOptionType",
    "LastResourceDataSyncStatusType",
    "ListAssociationVersionsPaginatorName",
    "ListAssociationsPaginatorName",
    "ListCommandInvocationsPaginatorName",
    "ListCommandsPaginatorName",
    "ListComplianceItemsPaginatorName",
    "ListComplianceSummariesPaginatorName",
    "ListDocumentVersionsPaginatorName",
    "ListDocumentsPaginatorName",
    "ListNodesPaginatorName",
    "ListNodesSummaryPaginatorName",
    "ListOpsItemEventsPaginatorName",
    "ListOpsItemRelatedItemsPaginatorName",
    "ListOpsMetadataPaginatorName",
    "ListResourceComplianceSummariesPaginatorName",
    "ListResourceDataSyncPaginatorName",
    "MaintenanceWindowExecutionStatusType",
    "MaintenanceWindowResourceTypeType",
    "MaintenanceWindowTaskCutoffBehaviorType",
    "MaintenanceWindowTaskTypeType",
    "ManagedStatusType",
    "NodeAggregatorTypeType",
    "NodeAttributeNameType",
    "NodeFilterKeyType",
    "NodeFilterOperatorTypeType",
    "NodeTypeNameType",
    "NotificationEventType",
    "NotificationTypeType",
    "OperatingSystemType",
    "OpsFilterOperatorTypeType",
    "OpsItemDataTypeType",
    "OpsItemEventFilterKeyType",
    "OpsItemEventFilterOperatorType",
    "OpsItemFilterKeyType",
    "OpsItemFilterOperatorType",
    "OpsItemRelatedItemsFilterKeyType",
    "OpsItemRelatedItemsFilterOperatorType",
    "OpsItemStatusType",
    "PaginatorName",
    "ParameterTierType",
    "ParameterTypeType",
    "ParametersFilterKeyType",
    "PatchActionType",
    "PatchComplianceDataStateType",
    "PatchComplianceLevelType",
    "PatchComplianceStatusType",
    "PatchDeploymentStatusType",
    "PatchFilterKeyType",
    "PatchOperationTypeType",
    "PatchPropertyType",
    "PatchSetType",
    "PingStatusType",
    "PlatformTypeType",
    "RebootOptionType",
    "RegionName",
    "ResourceDataSyncS3FormatType",
    "ResourceServiceName",
    "ResourceTypeForTaggingType",
    "ResourceTypeType",
    "ReviewStatusType",
    "SSMServiceName",
    "ServiceName",
    "SessionFilterKeyType",
    "SessionStateType",
    "SessionStatusType",
    "SignalTypeType",
    "SourceTypeType",
    "StepExecutionFilterKeyType",
    "StopTypeType",
    "WaiterName",
)

AccessRequestStatusType = Literal["Approved", "Expired", "Pending", "Rejected", "Revoked"]
AccessTypeType = Literal["JustInTime", "Standard"]
AssociationComplianceSeverityType = Literal["CRITICAL", "HIGH", "LOW", "MEDIUM", "UNSPECIFIED"]
AssociationExecutionFilterKeyType = Literal["CreatedTime", "ExecutionId", "Status"]
AssociationExecutionTargetsFilterKeyType = Literal["ResourceId", "ResourceType", "Status"]
AssociationFilterKeyType = Literal[
    "AssociationId",
    "AssociationName",
    "AssociationStatusName",
    "InstanceId",
    "LastExecutedAfter",
    "LastExecutedBefore",
    "Name",
    "ResourceGroupName",
]
AssociationFilterOperatorTypeType = Literal["EQUAL", "GREATER_THAN", "LESS_THAN"]
AssociationStatusNameType = Literal["Failed", "Pending", "Success"]
AssociationSyncComplianceType = Literal["AUTO", "MANUAL"]
AttachmentHashTypeType = Literal["Sha256"]
AttachmentsSourceKeyType = Literal["AttachmentReference", "S3FileUrl", "SourceUrl"]
AutomationExecutionFilterKeyType = Literal[
    "AutomationSubtype",
    "AutomationType",
    "CurrentAction",
    "DocumentNamePrefix",
    "ExecutionId",
    "ExecutionStatus",
    "OpsItemId",
    "ParentExecutionId",
    "StartTimeAfter",
    "StartTimeBefore",
    "TagKey",
    "TargetResourceGroup",
]
AutomationExecutionStatusType = Literal[
    "Approved",
    "Cancelled",
    "Cancelling",
    "ChangeCalendarOverrideApproved",
    "ChangeCalendarOverrideRejected",
    "CompletedWithFailure",
    "CompletedWithSuccess",
    "Exited",
    "Failed",
    "InProgress",
    "Pending",
    "PendingApproval",
    "PendingChangeCalendarOverride",
    "Rejected",
    "RunbookInProgress",
    "Scheduled",
    "Success",
    "TimedOut",
    "Waiting",
]
AutomationSubtypeType = Literal["AccessRequest", "ChangeRequest"]
AutomationTypeType = Literal["CrossAccount", "Local"]
CalendarStateType = Literal["CLOSED", "OPEN"]
CommandExecutedWaiterName = Literal["command_executed"]
CommandFilterKeyType = Literal[
    "DocumentName", "ExecutionStage", "InvokedAfter", "InvokedBefore", "Status"
]
CommandInvocationStatusType = Literal[
    "Cancelled", "Cancelling", "Delayed", "Failed", "InProgress", "Pending", "Success", "TimedOut"
]
CommandPluginStatusType = Literal[
    "Cancelled", "Failed", "InProgress", "Pending", "Success", "TimedOut"
]
CommandStatusType = Literal[
    "Cancelled", "Cancelling", "Failed", "InProgress", "Pending", "Success", "TimedOut"
]
ComplianceQueryOperatorTypeType = Literal[
    "BEGIN_WITH", "EQUAL", "GREATER_THAN", "LESS_THAN", "NOT_EQUAL"
]
ComplianceSeverityType = Literal[
    "CRITICAL", "HIGH", "INFORMATIONAL", "LOW", "MEDIUM", "UNSPECIFIED"
]
ComplianceStatusType = Literal["COMPLIANT", "NON_COMPLIANT"]
ComplianceUploadTypeType = Literal["COMPLETE", "PARTIAL"]
ConnectionStatusType = Literal["connected", "notconnected"]
DescribeActivationsFilterKeysType = Literal["ActivationIds", "DefaultInstanceName", "IamRole"]
DescribeActivationsPaginatorName = Literal["describe_activations"]
DescribeAssociationExecutionTargetsPaginatorName = Literal["describe_association_execution_targets"]
DescribeAssociationExecutionsPaginatorName = Literal["describe_association_executions"]
DescribeAutomationExecutionsPaginatorName = Literal["describe_automation_executions"]
DescribeAutomationStepExecutionsPaginatorName = Literal["describe_automation_step_executions"]
DescribeAvailablePatchesPaginatorName = Literal["describe_available_patches"]
DescribeEffectiveInstanceAssociationsPaginatorName = Literal[
    "describe_effective_instance_associations"
]
DescribeEffectivePatchesForPatchBaselinePaginatorName = Literal[
    "describe_effective_patches_for_patch_baseline"
]
DescribeInstanceAssociationsStatusPaginatorName = Literal["describe_instance_associations_status"]
DescribeInstanceInformationPaginatorName = Literal["describe_instance_information"]
DescribeInstancePatchStatesForPatchGroupPaginatorName = Literal[
    "describe_instance_patch_states_for_patch_group"
]
DescribeInstancePatchStatesPaginatorName = Literal["describe_instance_patch_states"]
DescribeInstancePatchesPaginatorName = Literal["describe_instance_patches"]
DescribeInstancePropertiesPaginatorName = Literal["describe_instance_properties"]
DescribeInventoryDeletionsPaginatorName = Literal["describe_inventory_deletions"]
DescribeMaintenanceWindowExecutionTaskInvocationsPaginatorName = Literal[
    "describe_maintenance_window_execution_task_invocations"
]
DescribeMaintenanceWindowExecutionTasksPaginatorName = Literal[
    "describe_maintenance_window_execution_tasks"
]
DescribeMaintenanceWindowExecutionsPaginatorName = Literal["describe_maintenance_window_executions"]
DescribeMaintenanceWindowSchedulePaginatorName = Literal["describe_maintenance_window_schedule"]
DescribeMaintenanceWindowTargetsPaginatorName = Literal["describe_maintenance_window_targets"]
DescribeMaintenanceWindowTasksPaginatorName = Literal["describe_maintenance_window_tasks"]
DescribeMaintenanceWindowsForTargetPaginatorName = Literal[
    "describe_maintenance_windows_for_target"
]
DescribeMaintenanceWindowsPaginatorName = Literal["describe_maintenance_windows"]
DescribeOpsItemsPaginatorName = Literal["describe_ops_items"]
DescribeParametersPaginatorName = Literal["describe_parameters"]
DescribePatchBaselinesPaginatorName = Literal["describe_patch_baselines"]
DescribePatchGroupsPaginatorName = Literal["describe_patch_groups"]
DescribePatchPropertiesPaginatorName = Literal["describe_patch_properties"]
DescribeSessionsPaginatorName = Literal["describe_sessions"]
DocumentFilterKeyType = Literal["DocumentType", "Name", "Owner", "PlatformTypes"]
DocumentFormatType = Literal["JSON", "TEXT", "YAML"]
DocumentHashTypeType = Literal["Sha1", "Sha256"]
DocumentMetadataEnumType = Literal["DocumentReviews"]
DocumentParameterTypeType = Literal["String", "StringList"]
DocumentPermissionTypeType = Literal["Share"]
DocumentReviewActionType = Literal["Approve", "Reject", "SendForReview", "UpdateReview"]
DocumentReviewCommentTypeType = Literal["Comment"]
DocumentStatusType = Literal["Active", "Creating", "Deleting", "Failed", "Updating"]
DocumentTypeType = Literal[
    "ApplicationConfiguration",
    "ApplicationConfigurationSchema",
    "AutoApprovalPolicy",
    "Automation",
    "Automation.ChangeTemplate",
    "ChangeCalendar",
    "CloudFormation",
    "Command",
    "ConformancePackTemplate",
    "DeploymentStrategy",
    "ManualApprovalPolicy",
    "Package",
    "Policy",
    "ProblemAnalysis",
    "ProblemAnalysisTemplate",
    "QuickSetup",
    "Session",
]
ExecutionModeType = Literal["Auto", "Interactive"]
ExecutionPreviewStatusType = Literal["Failed", "InProgress", "Pending", "Success"]
ExternalAlarmStateType = Literal["ALARM", "UNKNOWN"]
FaultType = Literal["Client", "Server", "Unknown"]
GetInventoryPaginatorName = Literal["get_inventory"]
GetInventorySchemaPaginatorName = Literal["get_inventory_schema"]
GetOpsSummaryPaginatorName = Literal["get_ops_summary"]
GetParameterHistoryPaginatorName = Literal["get_parameter_history"]
GetParametersByPathPaginatorName = Literal["get_parameters_by_path"]
GetResourcePoliciesPaginatorName = Literal["get_resource_policies"]
ImpactTypeType = Literal["Mutating", "NonMutating", "Undetermined"]
InstanceInformationFilterKeyType = Literal[
    "ActivationIds",
    "AgentVersion",
    "AssociationStatus",
    "IamRole",
    "InstanceIds",
    "PingStatus",
    "PlatformTypes",
    "ResourceType",
]
InstancePatchStateOperatorTypeType = Literal["Equal", "GreaterThan", "LessThan", "NotEqual"]
InstancePropertyFilterKeyType = Literal[
    "ActivationIds",
    "AgentVersion",
    "AssociationStatus",
    "DocumentName",
    "IamRole",
    "InstanceIds",
    "PingStatus",
    "PlatformTypes",
    "ResourceType",
]
InstancePropertyFilterOperatorType = Literal[
    "BeginWith", "Equal", "GreaterThan", "LessThan", "NotEqual"
]
InventoryAttributeDataTypeType = Literal["number", "string"]
InventoryDeletionStatusType = Literal["Complete", "InProgress"]
InventoryQueryOperatorTypeType = Literal[
    "BeginWith", "Equal", "Exists", "GreaterThan", "LessThan", "NotEqual"
]
InventorySchemaDeleteOptionType = Literal["DeleteSchema", "DisableSchema"]
LastResourceDataSyncStatusType = Literal["Failed", "InProgress", "Successful"]
ListAssociationVersionsPaginatorName = Literal["list_association_versions"]
ListAssociationsPaginatorName = Literal["list_associations"]
ListCommandInvocationsPaginatorName = Literal["list_command_invocations"]
ListCommandsPaginatorName = Literal["list_commands"]
ListComplianceItemsPaginatorName = Literal["list_compliance_items"]
ListComplianceSummariesPaginatorName = Literal["list_compliance_summaries"]
ListDocumentVersionsPaginatorName = Literal["list_document_versions"]
ListDocumentsPaginatorName = Literal["list_documents"]
ListNodesPaginatorName = Literal["list_nodes"]
ListNodesSummaryPaginatorName = Literal["list_nodes_summary"]
ListOpsItemEventsPaginatorName = Literal["list_ops_item_events"]
ListOpsItemRelatedItemsPaginatorName = Literal["list_ops_item_related_items"]
ListOpsMetadataPaginatorName = Literal["list_ops_metadata"]
ListResourceComplianceSummariesPaginatorName = Literal["list_resource_compliance_summaries"]
ListResourceDataSyncPaginatorName = Literal["list_resource_data_sync"]
MaintenanceWindowExecutionStatusType = Literal[
    "CANCELLED",
    "CANCELLING",
    "FAILED",
    "IN_PROGRESS",
    "PENDING",
    "SKIPPED_OVERLAPPING",
    "SUCCESS",
    "TIMED_OUT",
]
MaintenanceWindowResourceTypeType = Literal["INSTANCE", "RESOURCE_GROUP"]
MaintenanceWindowTaskCutoffBehaviorType = Literal["CANCEL_TASK", "CONTINUE_TASK"]
MaintenanceWindowTaskTypeType = Literal["AUTOMATION", "LAMBDA", "RUN_COMMAND", "STEP_FUNCTIONS"]
ManagedStatusType = Literal["All", "Managed", "Unmanaged"]
NodeAggregatorTypeType = Literal["Count"]
NodeAttributeNameType = Literal[
    "AgentVersion", "PlatformName", "PlatformType", "PlatformVersion", "Region", "ResourceType"
]
NodeFilterKeyType = Literal[
    "AccountId",
    "AgentType",
    "AgentVersion",
    "ComputerName",
    "InstanceId",
    "InstanceStatus",
    "IpAddress",
    "ManagedStatus",
    "OrganizationalUnitId",
    "OrganizationalUnitPath",
    "PlatformName",
    "PlatformType",
    "PlatformVersion",
    "Region",
    "ResourceType",
]
NodeFilterOperatorTypeType = Literal["BeginWith", "Equal", "NotEqual"]
NodeTypeNameType = Literal["Instance"]
NotificationEventType = Literal["All", "Cancelled", "Failed", "InProgress", "Success", "TimedOut"]
NotificationTypeType = Literal["Command", "Invocation"]
OperatingSystemType = Literal[
    "ALMA_LINUX",
    "AMAZON_LINUX",
    "AMAZON_LINUX_2",
    "AMAZON_LINUX_2022",
    "AMAZON_LINUX_2023",
    "CENTOS",
    "DEBIAN",
    "MACOS",
    "ORACLE_LINUX",
    "RASPBIAN",
    "REDHAT_ENTERPRISE_LINUX",
    "ROCKY_LINUX",
    "SUSE",
    "UBUNTU",
    "WINDOWS",
]
OpsFilterOperatorTypeType = Literal[
    "BeginWith", "Equal", "Exists", "GreaterThan", "LessThan", "NotEqual"
]
OpsItemDataTypeType = Literal["SearchableString", "String"]
OpsItemEventFilterKeyType = Literal["OpsItemId"]
OpsItemEventFilterOperatorType = Literal["Equal"]
OpsItemFilterKeyType = Literal[
    "AccessRequestByApproverArn",
    "AccessRequestByApproverId",
    "AccessRequestByIsReplica",
    "AccessRequestByRequesterArn",
    "AccessRequestByRequesterId",
    "AccessRequestBySourceAccountId",
    "AccessRequestBySourceOpsItemId",
    "AccessRequestBySourceRegion",
    "AccessRequestByTargetResourceId",
    "AccountId",
    "ActualEndTime",
    "ActualStartTime",
    "AutomationId",
    "Category",
    "ChangeRequestByApproverArn",
    "ChangeRequestByApproverName",
    "ChangeRequestByRequesterArn",
    "ChangeRequestByRequesterName",
    "ChangeRequestByTargetsResourceGroup",
    "ChangeRequestByTemplate",
    "CreatedBy",
    "CreatedTime",
    "InsightByType",
    "LastModifiedTime",
    "OperationalData",
    "OperationalDataKey",
    "OperationalDataValue",
    "OpsItemId",
    "OpsItemType",
    "PlannedEndTime",
    "PlannedStartTime",
    "Priority",
    "ResourceId",
    "Severity",
    "Source",
    "Status",
    "Title",
]
OpsItemFilterOperatorType = Literal["Contains", "Equal", "GreaterThan", "LessThan"]
OpsItemRelatedItemsFilterKeyType = Literal["AssociationId", "ResourceType", "ResourceUri"]
OpsItemRelatedItemsFilterOperatorType = Literal["Equal"]
OpsItemStatusType = Literal[
    "Approved",
    "Cancelled",
    "Cancelling",
    "ChangeCalendarOverrideApproved",
    "ChangeCalendarOverrideRejected",
    "Closed",
    "CompletedWithFailure",
    "CompletedWithSuccess",
    "Failed",
    "InProgress",
    "Open",
    "Pending",
    "PendingApproval",
    "PendingChangeCalendarOverride",
    "Rejected",
    "Resolved",
    "Revoked",
    "RunbookInProgress",
    "Scheduled",
    "TimedOut",
]
ParameterTierType = Literal["Advanced", "Intelligent-Tiering", "Standard"]
ParameterTypeType = Literal["SecureString", "String", "StringList"]
ParametersFilterKeyType = Literal["KeyId", "Name", "Type"]
PatchActionType = Literal["ALLOW_AS_DEPENDENCY", "BLOCK"]
PatchComplianceDataStateType = Literal[
    "AVAILABLE_SECURITY_UPDATE",
    "FAILED",
    "INSTALLED",
    "INSTALLED_OTHER",
    "INSTALLED_PENDING_REBOOT",
    "INSTALLED_REJECTED",
    "MISSING",
    "NOT_APPLICABLE",
]
PatchComplianceLevelType = Literal[
    "CRITICAL", "HIGH", "INFORMATIONAL", "LOW", "MEDIUM", "UNSPECIFIED"
]
PatchComplianceStatusType = Literal["COMPLIANT", "NON_COMPLIANT"]
PatchDeploymentStatusType = Literal[
    "APPROVED", "EXPLICIT_APPROVED", "EXPLICIT_REJECTED", "PENDING_APPROVAL"
]
PatchFilterKeyType = Literal[
    "ADVISORY_ID",
    "ARCH",
    "BUGZILLA_ID",
    "CLASSIFICATION",
    "CVE_ID",
    "EPOCH",
    "MSRC_SEVERITY",
    "NAME",
    "PATCH_ID",
    "PATCH_SET",
    "PRIORITY",
    "PRODUCT",
    "PRODUCT_FAMILY",
    "RELEASE",
    "REPOSITORY",
    "SECTION",
    "SECURITY",
    "SEVERITY",
    "VERSION",
]
PatchOperationTypeType = Literal["Install", "Scan"]
PatchPropertyType = Literal[
    "CLASSIFICATION", "MSRC_SEVERITY", "PRIORITY", "PRODUCT", "PRODUCT_FAMILY", "SEVERITY"
]
PatchSetType = Literal["APPLICATION", "OS"]
PingStatusType = Literal["ConnectionLost", "Inactive", "Online"]
PlatformTypeType = Literal["Linux", "MacOS", "Windows"]
RebootOptionType = Literal["NoReboot", "RebootIfNeeded"]
ResourceDataSyncS3FormatType = Literal["JsonSerDe"]
ResourceTypeForTaggingType = Literal[
    "Association",
    "Automation",
    "Document",
    "MaintenanceWindow",
    "ManagedInstance",
    "OpsItem",
    "OpsMetadata",
    "Parameter",
    "PatchBaseline",
]
ResourceTypeType = Literal["EC2Instance", "ManagedInstance"]
ReviewStatusType = Literal["APPROVED", "NOT_REVIEWED", "PENDING", "REJECTED"]
SessionFilterKeyType = Literal[
    "AccessType", "InvokedAfter", "InvokedBefore", "Owner", "SessionId", "Status", "Target"
]
SessionStateType = Literal["Active", "History"]
SessionStatusType = Literal[
    "Connected", "Connecting", "Disconnected", "Failed", "Terminated", "Terminating"
]
SignalTypeType = Literal["Approve", "Reject", "Resume", "Revoke", "StartStep", "StopStep"]
SourceTypeType = Literal["AWS::EC2::Instance", "AWS::IoT::Thing", "AWS::SSM::ManagedInstance"]
StepExecutionFilterKeyType = Literal[
    "Action",
    "ParentStepExecutionId",
    "ParentStepIteration",
    "ParentStepIteratorValue",
    "StartTimeAfter",
    "StartTimeBefore",
    "StepExecutionId",
    "StepExecutionStatus",
    "StepName",
]
StopTypeType = Literal["Cancel", "Complete"]
SSMServiceName = Literal["ssm"]
ServiceName = Literal[
    "accessanalyzer",
    "account",
    "acm",
    "acm-pca",
    "aiops",
    "amp",
    "amplify",
    "amplifybackend",
    "amplifyuibuilder",
    "apigateway",
    "apigatewaymanagementapi",
    "apigatewayv2",
    "appconfig",
    "appconfigdata",
    "appfabric",
    "appflow",
    "appintegrations",
    "application-autoscaling",
    "application-insights",
    "application-signals",
    "applicationcostprofiler",
    "appmesh",
    "apprunner",
    "appstream",
    "appsync",
    "apptest",
    "arc-zonal-shift",
    "artifact",
    "athena",
    "auditmanager",
    "autoscaling",
    "autoscaling-plans",
    "b2bi",
    "backup",
    "backup-gateway",
    "backupsearch",
    "batch",
    "bcm-data-exports",
    "bcm-pricing-calculator",
    "bedrock",
    "bedrock-agent",
    "bedrock-agent-runtime",
    "bedrock-data-automation",
    "bedrock-data-automation-runtime",
    "bedrock-runtime",
    "billing",
    "billingconductor",
    "braket",
    "budgets",
    "ce",
    "chatbot",
    "chime",
    "chime-sdk-identity",
    "chime-sdk-media-pipelines",
    "chime-sdk-meetings",
    "chime-sdk-messaging",
    "chime-sdk-voice",
    "cleanrooms",
    "cleanroomsml",
    "cloud9",
    "cloudcontrol",
    "clouddirectory",
    "cloudformation",
    "cloudfront",
    "cloudfront-keyvaluestore",
    "cloudhsm",
    "cloudhsmv2",
    "cloudsearch",
    "cloudsearchdomain",
    "cloudtrail",
    "cloudtrail-data",
    "cloudwatch",
    "codeartifact",
    "codebuild",
    "codecatalyst",
    "codecommit",
    "codeconnections",
    "codedeploy",
    "codeguru-reviewer",
    "codeguru-security",
    "codeguruprofiler",
    "codepipeline",
    "codestar-connections",
    "codestar-notifications",
    "cognito-identity",
    "cognito-idp",
    "cognito-sync",
    "comprehend",
    "comprehendmedical",
    "compute-optimizer",
    "config",
    "connect",
    "connect-contact-lens",
    "connectcampaigns",
    "connectcampaignsv2",
    "connectcases",
    "connectparticipant",
    "controlcatalog",
    "controltower",
    "cost-optimization-hub",
    "cur",
    "customer-profiles",
    "databrew",
    "dataexchange",
    "datapipeline",
    "datasync",
    "datazone",
    "dax",
    "deadline",
    "detective",
    "devicefarm",
    "devops-guru",
    "directconnect",
    "discovery",
    "dlm",
    "dms",
    "docdb",
    "docdb-elastic",
    "drs",
    "ds",
    "ds-data",
    "dsql",
    "dynamodb",
    "dynamodbstreams",
    "ebs",
    "ec2",
    "ec2-instance-connect",
    "ecr",
    "ecr-public",
    "ecs",
    "efs",
    "eks",
    "eks-auth",
    "elasticache",
    "elasticbeanstalk",
    "elastictranscoder",
    "elb",
    "elbv2",
    "emr",
    "emr-containers",
    "emr-serverless",
    "entityresolution",
    "es",
    "events",
    "evidently",
    "evs",
    "finspace",
    "finspace-data",
    "firehose",
    "fis",
    "fms",
    "forecast",
    "forecastquery",
    "frauddetector",
    "freetier",
    "fsx",
    "gamelift",
    "gameliftstreams",
    "geo-maps",
    "geo-places",
    "geo-routes",
    "glacier",
    "globalaccelerator",
    "glue",
    "grafana",
    "greengrass",
    "greengrassv2",
    "groundstation",
    "guardduty",
    "health",
    "healthlake",
    "iam",
    "identitystore",
    "imagebuilder",
    "importexport",
    "inspector",
    "inspector-scan",
    "inspector2",
    "internetmonitor",
    "invoicing",
    "iot",
    "iot-data",
    "iot-jobs-data",
    "iot-managed-integrations",
    "iotanalytics",
    "iotdeviceadvisor",
    "iotevents",
    "iotevents-data",
    "iotfleethub",
    "iotfleetwise",
    "iotsecuretunneling",
    "iotsitewise",
    "iotthingsgraph",
    "iottwinmaker",
    "iotwireless",
    "ivs",
    "ivs-realtime",
    "ivschat",
    "kafka",
    "kafkaconnect",
    "kendra",
    "kendra-ranking",
    "keyspaces",
    "keyspacesstreams",
    "kinesis",
    "kinesis-video-archived-media",
    "kinesis-video-media",
    "kinesis-video-signaling",
    "kinesis-video-webrtc-storage",
    "kinesisanalytics",
    "kinesisanalyticsv2",
    "kinesisvideo",
    "kms",
    "lakeformation",
    "lambda",
    "launch-wizard",
    "lex-models",
    "lex-runtime",
    "lexv2-models",
    "lexv2-runtime",
    "license-manager",
    "license-manager-linux-subscriptions",
    "license-manager-user-subscriptions",
    "lightsail",
    "location",
    "logs",
    "lookoutequipment",
    "lookoutmetrics",
    "lookoutvision",
    "m2",
    "machinelearning",
    "macie2",
    "mailmanager",
    "managedblockchain",
    "managedblockchain-query",
    "marketplace-agreement",
    "marketplace-catalog",
    "marketplace-deployment",
    "marketplace-entitlement",
    "marketplace-reporting",
    "marketplacecommerceanalytics",
    "mediaconnect",
    "mediaconvert",
    "medialive",
    "mediapackage",
    "mediapackage-vod",
    "mediapackagev2",
    "mediastore",
    "mediastore-data",
    "mediatailor",
    "medical-imaging",
    "memorydb",
    "meteringmarketplace",
    "mgh",
    "mgn",
    "migration-hub-refactor-spaces",
    "migrationhub-config",
    "migrationhuborchestrator",
    "migrationhubstrategy",
    "mpa",
    "mq",
    "mturk",
    "mwaa",
    "neptune",
    "neptune-graph",
    "neptunedata",
    "network-firewall",
    "networkflowmonitor",
    "networkmanager",
    "networkmonitor",
    "notifications",
    "notificationscontacts",
    "oam",
    "observabilityadmin",
    "omics",
    "opensearch",
    "opensearchserverless",
    "opsworks",
    "opsworkscm",
    "organizations",
    "osis",
    "outposts",
    "panorama",
    "partnercentral-selling",
    "payment-cryptography",
    "payment-cryptography-data",
    "pca-connector-ad",
    "pca-connector-scep",
    "pcs",
    "personalize",
    "personalize-events",
    "personalize-runtime",
    "pi",
    "pinpoint",
    "pinpoint-email",
    "pinpoint-sms-voice",
    "pinpoint-sms-voice-v2",
    "pipes",
    "polly",
    "pricing",
    "proton",
    "qapps",
    "qbusiness",
    "qconnect",
    "qldb",
    "qldb-session",
    "quicksight",
    "ram",
    "rbin",
    "rds",
    "rds-data",
    "redshift",
    "redshift-data",
    "redshift-serverless",
    "rekognition",
    "repostspace",
    "resiliencehub",
    "resource-explorer-2",
    "resource-groups",
    "resourcegroupstaggingapi",
    "robomaker",
    "rolesanywhere",
    "route53",
    "route53-recovery-cluster",
    "route53-recovery-control-config",
    "route53-recovery-readiness",
    "route53domains",
    "route53profiles",
    "route53resolver",
    "rum",
    "s3",
    "s3control",
    "s3outposts",
    "s3tables",
    "sagemaker",
    "sagemaker-a2i-runtime",
    "sagemaker-edge",
    "sagemaker-featurestore-runtime",
    "sagemaker-geospatial",
    "sagemaker-metrics",
    "sagemaker-runtime",
    "savingsplans",
    "scheduler",
    "schemas",
    "sdb",
    "secretsmanager",
    "security-ir",
    "securityhub",
    "securitylake",
    "serverlessrepo",
    "service-quotas",
    "servicecatalog",
    "servicecatalog-appregistry",
    "servicediscovery",
    "ses",
    "sesv2",
    "shield",
    "signer",
    "simspaceweaver",
    "sms",
    "snow-device-management",
    "snowball",
    "sns",
    "socialmessaging",
    "sqs",
    "ssm",
    "ssm-contacts",
    "ssm-guiconnect",
    "ssm-incidents",
    "ssm-quicksetup",
    "ssm-sap",
    "sso",
    "sso-admin",
    "sso-oidc",
    "stepfunctions",
    "storagegateway",
    "sts",
    "supplychain",
    "support",
    "support-app",
    "swf",
    "synthetics",
    "taxsettings",
    "textract",
    "timestream-influxdb",
    "timestream-query",
    "timestream-write",
    "tnb",
    "transcribe",
    "transfer",
    "translate",
    "trustedadvisor",
    "verifiedpermissions",
    "voice-id",
    "vpc-lattice",
    "waf",
    "waf-regional",
    "wafv2",
    "wellarchitected",
    "wisdom",
    "workdocs",
    "workmail",
    "workmailmessageflow",
    "workspaces",
    "workspaces-instances",
    "workspaces-thin-client",
    "workspaces-web",
    "xray",
]
ResourceServiceName = Literal[
    "cloudformation",
    "cloudwatch",
    "dynamodb",
    "ec2",
    "glacier",
    "iam",
    "opsworks",
    "s3",
    "sns",
    "sqs",
]
PaginatorName = Literal[
    "describe_activations",
    "describe_association_execution_targets",
    "describe_association_executions",
    "describe_automation_executions",
    "describe_automation_step_executions",
    "describe_available_patches",
    "describe_effective_instance_associations",
    "describe_effective_patches_for_patch_baseline",
    "describe_instance_associations_status",
    "describe_instance_information",
    "describe_instance_patch_states",
    "describe_instance_patch_states_for_patch_group",
    "describe_instance_patches",
    "describe_instance_properties",
    "describe_inventory_deletions",
    "describe_maintenance_window_execution_task_invocations",
    "describe_maintenance_window_execution_tasks",
    "describe_maintenance_window_executions",
    "describe_maintenance_window_schedule",
    "describe_maintenance_window_targets",
    "describe_maintenance_window_tasks",
    "describe_maintenance_windows",
    "describe_maintenance_windows_for_target",
    "describe_ops_items",
    "describe_parameters",
    "describe_patch_baselines",
    "describe_patch_groups",
    "describe_patch_properties",
    "describe_sessions",
    "get_inventory",
    "get_inventory_schema",
    "get_ops_summary",
    "get_parameter_history",
    "get_parameters_by_path",
    "get_resource_policies",
    "list_association_versions",
    "list_associations",
    "list_command_invocations",
    "list_commands",
    "list_compliance_items",
    "list_compliance_summaries",
    "list_document_versions",
    "list_documents",
    "list_nodes",
    "list_nodes_summary",
    "list_ops_item_events",
    "list_ops_item_related_items",
    "list_ops_metadata",
    "list_resource_compliance_summaries",
    "list_resource_data_sync",
]
WaiterName = Literal["command_executed"]
RegionName = Literal[
    "af-south-1",
    "ap-east-1",
    "ap-east-2",
    "ap-northeast-1",
    "ap-northeast-2",
    "ap-northeast-3",
    "ap-south-1",
    "ap-south-2",
    "ap-southeast-1",
    "ap-southeast-2",
    "ap-southeast-3",
    "ap-southeast-4",
    "ap-southeast-5",
    "ap-southeast-7",
    "ca-central-1",
    "ca-west-1",
    "eu-central-1",
    "eu-central-2",
    "eu-north-1",
    "eu-south-1",
    "eu-south-2",
    "eu-west-1",
    "eu-west-2",
    "eu-west-3",
    "il-central-1",
    "me-central-1",
    "me-south-1",
    "mx-central-1",
    "sa-east-1",
    "us-east-1",
    "us-east-2",
    "us-west-1",
    "us-west-2",
]
