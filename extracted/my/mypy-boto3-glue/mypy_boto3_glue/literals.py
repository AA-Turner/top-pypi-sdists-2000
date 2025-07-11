"""
Type annotations for glue service literal definitions.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_glue/literals/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from mypy_boto3_glue.literals import AdditionalOptionKeysType

    data: AdditionalOptionKeysType = "observations.scope"
    ```
"""

import sys

if sys.version_info >= (3, 12):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = (
    "AdditionalOptionKeysType",
    "AggFunctionType",
    "AllowFullTableExternalDataAccessEnumType",
    "AuthenticationTypeType",
    "BackfillErrorCodeType",
    "BlueprintRunStateType",
    "BlueprintStatusType",
    "CatalogEncryptionModeType",
    "CloudWatchEncryptionModeType",
    "ColumnStatisticsStateType",
    "ColumnStatisticsTypeType",
    "CompactionStrategyType",
    "ComparatorType",
    "CompatibilityType",
    "CompressionTypeType",
    "ComputationTypeType",
    "ComputeEnvironmentType",
    "ConnectionPropertyKeyType",
    "ConnectionStatusType",
    "ConnectionTypeType",
    "CrawlStateType",
    "CrawlerHistoryStateType",
    "CrawlerLineageSettingsType",
    "CrawlerStateType",
    "CsvHeaderOptionType",
    "CsvSerdeOptionType",
    "DQCompositeRuleEvaluationMethodType",
    "DQStopJobOnFailureTimingType",
    "DQTransformOutputType",
    "DataFormatType",
    "DataOperationType",
    "DataQualityEncryptionModeType",
    "DataQualityModelStatusType",
    "DataQualityRuleResultStatusType",
    "DatabaseAttributesType",
    "DeleteBehaviorType",
    "DeltaTargetCompressionTypeType",
    "DescribeEntityPaginatorName",
    "EnableHybridValuesType",
    "ExecutionClassType",
    "ExecutionStatusType",
    "ExistConditionType",
    "FieldDataTypeType",
    "FieldFilterOperatorType",
    "FieldNameType",
    "FilterLogicalOperatorType",
    "FilterOperationType",
    "FilterOperatorType",
    "FilterValueTypeType",
    "GetClassifiersPaginatorName",
    "GetConnectionsPaginatorName",
    "GetCrawlerMetricsPaginatorName",
    "GetCrawlersPaginatorName",
    "GetDatabasesPaginatorName",
    "GetDevEndpointsPaginatorName",
    "GetJobRunsPaginatorName",
    "GetJobsPaginatorName",
    "GetPartitionIndexesPaginatorName",
    "GetPartitionsPaginatorName",
    "GetResourcePoliciesPaginatorName",
    "GetSecurityConfigurationsPaginatorName",
    "GetTableVersionsPaginatorName",
    "GetTablesPaginatorName",
    "GetTriggersPaginatorName",
    "GetUserDefinedFunctionsPaginatorName",
    "GetWorkflowRunsPaginatorName",
    "GlueRecordTypeType",
    "GlueServiceName",
    "HudiTargetCompressionTypeType",
    "HyperTargetCompressionTypeType",
    "IcebergNullOrderType",
    "IcebergSortDirectionType",
    "IcebergStructTypeEnumType",
    "IcebergTargetCompressionTypeType",
    "InclusionAnnotationValueType",
    "IntegrationStatusType",
    "JDBCConnectionTypeType",
    "JDBCDataTypeType",
    "JdbcMetadataEntryType",
    "JobBookmarksEncryptionModeType",
    "JobModeType",
    "JobRunStateType",
    "JoinTypeType",
    "LanguageType",
    "LastCrawlStatusType",
    "ListBlueprintsPaginatorName",
    "ListConnectionTypesPaginatorName",
    "ListEntitiesPaginatorName",
    "ListJobsPaginatorName",
    "ListRegistriesPaginatorName",
    "ListSchemaVersionsPaginatorName",
    "ListSchemasPaginatorName",
    "ListTableOptimizerRunsPaginatorName",
    "ListTriggersPaginatorName",
    "ListUsageProfilesPaginatorName",
    "ListWorkflowsPaginatorName",
    "LogicalOperatorType",
    "LogicalType",
    "MLUserDataEncryptionModeStringType",
    "MetadataOperationType",
    "NodeTypeType",
    "OAuth2GrantTypeType",
    "PaginatorName",
    "ParamTypeType",
    "ParquetCompressionTypeType",
    "PartitionIndexStatusType",
    "PermissionType",
    "PermissionTypeType",
    "PiiTypeType",
    "PrincipalTypeType",
    "PropertyTypeType",
    "QuoteCharType",
    "RecrawlBehaviorType",
    "RegionName",
    "RegistryStatusType",
    "ResourceActionType",
    "ResourceServiceName",
    "ResourceShareTypeType",
    "ResourceStateType",
    "ResourceTypeType",
    "S3EncryptionModeType",
    "ScheduleStateType",
    "ScheduleTypeType",
    "SchemaDiffTypeType",
    "SchemaStatusType",
    "SchemaVersionStatusType",
    "SeparatorType",
    "ServiceName",
    "SessionStatusType",
    "SettingSourceType",
    "SortDirectionTypeType",
    "SortType",
    "SourceControlAuthStrategyType",
    "SourceControlProviderType",
    "StartingPositionType",
    "StatementStateType",
    "StatisticEvaluationLevelType",
    "TableAttributesType",
    "TableOptimizerEventTypeType",
    "TableOptimizerTypeType",
    "TargetFormatType",
    "TaskRunSortColumnTypeType",
    "TaskStatusTypeType",
    "TaskTypeType",
    "TransformSortColumnTypeType",
    "TransformStatusTypeType",
    "TransformTypeType",
    "TriggerStateType",
    "TriggerTypeType",
    "UnionTypeType",
    "UnnestSpecType",
    "UpdateBehaviorType",
    "UpdateCatalogBehaviorType",
    "ViewDialectType",
    "ViewUpdateActionType",
    "WorkerTypeType",
    "WorkflowRunStatusType",
)


AdditionalOptionKeysType = Literal["observations.scope", "performanceTuning.caching"]
AggFunctionType = Literal[
    "avg",
    "count",
    "countDistinct",
    "first",
    "kurtosis",
    "last",
    "max",
    "min",
    "skewness",
    "stddev_pop",
    "stddev_samp",
    "sum",
    "sumDistinct",
    "var_pop",
    "var_samp",
]
AllowFullTableExternalDataAccessEnumType = Literal["False", "True"]
AuthenticationTypeType = Literal["BASIC", "CUSTOM", "IAM", "OAUTH2"]
BackfillErrorCodeType = Literal[
    "ENCRYPTED_PARTITION_ERROR",
    "INTERNAL_ERROR",
    "INVALID_PARTITION_TYPE_DATA_ERROR",
    "MISSING_PARTITION_VALUE_ERROR",
    "UNSUPPORTED_PARTITION_CHARACTER_ERROR",
]
BlueprintRunStateType = Literal["FAILED", "ROLLING_BACK", "RUNNING", "SUCCEEDED"]
BlueprintStatusType = Literal["ACTIVE", "CREATING", "FAILED", "UPDATING"]
CatalogEncryptionModeType = Literal["DISABLED", "SSE-KMS", "SSE-KMS-WITH-SERVICE-ROLE"]
CloudWatchEncryptionModeType = Literal["DISABLED", "SSE-KMS"]
ColumnStatisticsStateType = Literal["FAILED", "RUNNING", "STARTING", "STOPPED", "SUCCEEDED"]
ColumnStatisticsTypeType = Literal[
    "BINARY", "BOOLEAN", "DATE", "DECIMAL", "DOUBLE", "LONG", "STRING"
]
CompactionStrategyType = Literal["binpack", "sort", "z-order"]
ComparatorType = Literal[
    "EQUALS", "GREATER_THAN", "GREATER_THAN_EQUALS", "LESS_THAN", "LESS_THAN_EQUALS"
]
CompatibilityType = Literal[
    "BACKWARD", "BACKWARD_ALL", "DISABLED", "FORWARD", "FORWARD_ALL", "FULL", "FULL_ALL", "NONE"
]
CompressionTypeType = Literal["bzip2", "gzip"]
ComputationTypeType = Literal["FULL", "INCREMENTAL"]
ComputeEnvironmentType = Literal["ATHENA", "PYTHON", "SPARK"]
ConnectionPropertyKeyType = Literal[
    "CLUSTER_IDENTIFIER",
    "CONFIG_FILES",
    "CONNECTION_URL",
    "CONNECTOR_CLASS_NAME",
    "CONNECTOR_TYPE",
    "CONNECTOR_URL",
    "CUSTOM_JDBC_CERT",
    "CUSTOM_JDBC_CERT_STRING",
    "DATABASE",
    "ENCRYPTED_KAFKA_CLIENT_KEYSTORE_PASSWORD",
    "ENCRYPTED_KAFKA_CLIENT_KEY_PASSWORD",
    "ENCRYPTED_KAFKA_SASL_PLAIN_PASSWORD",
    "ENCRYPTED_KAFKA_SASL_SCRAM_PASSWORD",
    "ENCRYPTED_PASSWORD",
    "ENDPOINT",
    "ENDPOINT_TYPE",
    "HOST",
    "INSTANCE_ID",
    "JDBC_CONNECTION_URL",
    "JDBC_DRIVER_CLASS_NAME",
    "JDBC_DRIVER_JAR_URI",
    "JDBC_ENFORCE_SSL",
    "JDBC_ENGINE",
    "JDBC_ENGINE_VERSION",
    "KAFKA_BOOTSTRAP_SERVERS",
    "KAFKA_CLIENT_KEYSTORE",
    "KAFKA_CLIENT_KEYSTORE_PASSWORD",
    "KAFKA_CLIENT_KEY_PASSWORD",
    "KAFKA_CUSTOM_CERT",
    "KAFKA_SASL_GSSAPI_KEYTAB",
    "KAFKA_SASL_GSSAPI_KRB5_CONF",
    "KAFKA_SASL_GSSAPI_PRINCIPAL",
    "KAFKA_SASL_GSSAPI_SERVICE",
    "KAFKA_SASL_MECHANISM",
    "KAFKA_SASL_PLAIN_PASSWORD",
    "KAFKA_SASL_PLAIN_USERNAME",
    "KAFKA_SASL_SCRAM_PASSWORD",
    "KAFKA_SASL_SCRAM_SECRETS_ARN",
    "KAFKA_SASL_SCRAM_USERNAME",
    "KAFKA_SKIP_CUSTOM_CERT_VALIDATION",
    "KAFKA_SSL_ENABLED",
    "PASSWORD",
    "PORT",
    "REGION",
    "ROLE_ARN",
    "SECRET_ID",
    "SKIP_CUSTOM_JDBC_CERT_VALIDATION",
    "USERNAME",
    "WORKGROUP_NAME",
]
ConnectionStatusType = Literal["FAILED", "IN_PROGRESS", "READY"]
ConnectionTypeType = Literal[
    "CUSTOM",
    "FACEBOOKADS",
    "GOOGLEADS",
    "GOOGLEANALYTICS4",
    "GOOGLESHEETS",
    "HUBSPOT",
    "INSTAGRAMADS",
    "INTERCOM",
    "JDBC",
    "JIRACLOUD",
    "KAFKA",
    "MARKETO",
    "MARKETPLACE",
    "MONGODB",
    "NETSUITEERP",
    "NETWORK",
    "SALESFORCE",
    "SALESFORCEMARKETINGCLOUD",
    "SALESFORCEPARDOT",
    "SAPODATA",
    "SERVICENOW",
    "SFTP",
    "SLACK",
    "SNAPCHATADS",
    "STRIPE",
    "VIEW_VALIDATION_ATHENA",
    "VIEW_VALIDATION_REDSHIFT",
    "ZENDESK",
    "ZOHOCRM",
]
CrawlStateType = Literal["CANCELLED", "CANCELLING", "ERROR", "FAILED", "RUNNING", "SUCCEEDED"]
CrawlerHistoryStateType = Literal["COMPLETED", "FAILED", "RUNNING", "STOPPED"]
CrawlerLineageSettingsType = Literal["DISABLE", "ENABLE"]
CrawlerStateType = Literal["READY", "RUNNING", "STOPPING"]
CsvHeaderOptionType = Literal["ABSENT", "PRESENT", "UNKNOWN"]
CsvSerdeOptionType = Literal["LazySimpleSerDe", "None", "OpenCSVSerDe"]
DQCompositeRuleEvaluationMethodType = Literal["COLUMN", "ROW"]
DQStopJobOnFailureTimingType = Literal["AfterDataLoad", "Immediate"]
DQTransformOutputType = Literal["EvaluationResults", "PrimaryInput"]
DataFormatType = Literal["AVRO", "JSON", "PROTOBUF"]
DataOperationType = Literal["READ", "WRITE"]
DataQualityEncryptionModeType = Literal["DISABLED", "SSE-KMS"]
DataQualityModelStatusType = Literal["FAILED", "RUNNING", "SUCCEEDED"]
DataQualityRuleResultStatusType = Literal["ERROR", "FAIL", "PASS"]
DatabaseAttributesType = Literal["NAME"]
DeleteBehaviorType = Literal["DELETE_FROM_DATABASE", "DEPRECATE_IN_DATABASE", "LOG"]
DeltaTargetCompressionTypeType = Literal["snappy", "uncompressed"]
DescribeEntityPaginatorName = Literal["describe_entity"]
EnableHybridValuesType = Literal["FALSE", "TRUE"]
ExecutionClassType = Literal["FLEX", "STANDARD"]
ExecutionStatusType = Literal["FAILED", "STARTED"]
ExistConditionType = Literal["MUST_EXIST", "NONE", "NOT_EXIST"]
FieldDataTypeType = Literal[
    "ARRAY",
    "BIGINT",
    "BOOLEAN",
    "BYTE",
    "DATE",
    "DECIMAL",
    "DOUBLE",
    "FLOAT",
    "INT",
    "LONG",
    "MAP",
    "SHORT",
    "SMALLINT",
    "STRING",
    "STRUCT",
    "TIMESTAMP",
]
FieldFilterOperatorType = Literal[
    "BETWEEN",
    "CONTAINS",
    "EQUAL_TO",
    "GREATER_THAN",
    "GREATER_THAN_OR_EQUAL_TO",
    "LESS_THAN",
    "LESS_THAN_OR_EQUAL_TO",
    "NOT_EQUAL_TO",
    "ORDER_BY",
]
FieldNameType = Literal["CRAWL_ID", "DPU_HOUR", "END_TIME", "START_TIME", "STATE"]
FilterLogicalOperatorType = Literal["AND", "OR"]
FilterOperationType = Literal["EQ", "GT", "GTE", "ISNULL", "LT", "LTE", "REGEX"]
FilterOperatorType = Literal["EQ", "GE", "GT", "LE", "LT", "NE"]
FilterValueTypeType = Literal["COLUMNEXTRACTED", "CONSTANT"]
GetClassifiersPaginatorName = Literal["get_classifiers"]
GetConnectionsPaginatorName = Literal["get_connections"]
GetCrawlerMetricsPaginatorName = Literal["get_crawler_metrics"]
GetCrawlersPaginatorName = Literal["get_crawlers"]
GetDatabasesPaginatorName = Literal["get_databases"]
GetDevEndpointsPaginatorName = Literal["get_dev_endpoints"]
GetJobRunsPaginatorName = Literal["get_job_runs"]
GetJobsPaginatorName = Literal["get_jobs"]
GetPartitionIndexesPaginatorName = Literal["get_partition_indexes"]
GetPartitionsPaginatorName = Literal["get_partitions"]
GetResourcePoliciesPaginatorName = Literal["get_resource_policies"]
GetSecurityConfigurationsPaginatorName = Literal["get_security_configurations"]
GetTableVersionsPaginatorName = Literal["get_table_versions"]
GetTablesPaginatorName = Literal["get_tables"]
GetTriggersPaginatorName = Literal["get_triggers"]
GetUserDefinedFunctionsPaginatorName = Literal["get_user_defined_functions"]
GetWorkflowRunsPaginatorName = Literal["get_workflow_runs"]
GlueRecordTypeType = Literal[
    "BIGDECIMAL", "BYTE", "DATE", "DOUBLE", "FLOAT", "INT", "LONG", "SHORT", "STRING", "TIMESTAMP"
]
HudiTargetCompressionTypeType = Literal["gzip", "lzo", "snappy", "uncompressed"]
HyperTargetCompressionTypeType = Literal["uncompressed"]
IcebergNullOrderType = Literal["nulls-first", "nulls-last"]
IcebergSortDirectionType = Literal["asc", "desc"]
IcebergStructTypeEnumType = Literal["struct"]
IcebergTargetCompressionTypeType = Literal["gzip", "lzo", "snappy", "uncompressed"]
InclusionAnnotationValueType = Literal["EXCLUDE", "INCLUDE"]
IntegrationStatusType = Literal[
    "ACTIVE", "CREATING", "DELETING", "FAILED", "MODIFYING", "NEEDS_ATTENTION", "SYNCING"
]
JDBCConnectionTypeType = Literal["mysql", "oracle", "postgresql", "redshift", "sqlserver"]
JDBCDataTypeType = Literal[
    "ARRAY",
    "BIGINT",
    "BINARY",
    "BIT",
    "BLOB",
    "BOOLEAN",
    "CHAR",
    "CLOB",
    "DATALINK",
    "DATE",
    "DECIMAL",
    "DISTINCT",
    "DOUBLE",
    "FLOAT",
    "INTEGER",
    "JAVA_OBJECT",
    "LONGNVARCHAR",
    "LONGVARBINARY",
    "LONGVARCHAR",
    "NCHAR",
    "NCLOB",
    "NULL",
    "NUMERIC",
    "NVARCHAR",
    "OTHER",
    "REAL",
    "REF",
    "REF_CURSOR",
    "ROWID",
    "SMALLINT",
    "SQLXML",
    "STRUCT",
    "TIME",
    "TIMESTAMP",
    "TIMESTAMP_WITH_TIMEZONE",
    "TIME_WITH_TIMEZONE",
    "TINYINT",
    "VARBINARY",
    "VARCHAR",
]
JdbcMetadataEntryType = Literal["COMMENTS", "RAWTYPES"]
JobBookmarksEncryptionModeType = Literal["CSE-KMS", "DISABLED"]
JobModeType = Literal["NOTEBOOK", "SCRIPT", "VISUAL"]
JobRunStateType = Literal[
    "ERROR",
    "EXPIRED",
    "FAILED",
    "RUNNING",
    "STARTING",
    "STOPPED",
    "STOPPING",
    "SUCCEEDED",
    "TIMEOUT",
    "WAITING",
]
JoinTypeType = Literal["equijoin", "left", "leftanti", "leftsemi", "outer", "right"]
LanguageType = Literal["PYTHON", "SCALA"]
LastCrawlStatusType = Literal["CANCELLED", "FAILED", "SUCCEEDED"]
ListBlueprintsPaginatorName = Literal["list_blueprints"]
ListConnectionTypesPaginatorName = Literal["list_connection_types"]
ListEntitiesPaginatorName = Literal["list_entities"]
ListJobsPaginatorName = Literal["list_jobs"]
ListRegistriesPaginatorName = Literal["list_registries"]
ListSchemaVersionsPaginatorName = Literal["list_schema_versions"]
ListSchemasPaginatorName = Literal["list_schemas"]
ListTableOptimizerRunsPaginatorName = Literal["list_table_optimizer_runs"]
ListTriggersPaginatorName = Literal["list_triggers"]
ListUsageProfilesPaginatorName = Literal["list_usage_profiles"]
ListWorkflowsPaginatorName = Literal["list_workflows"]
LogicalOperatorType = Literal["EQUALS"]
LogicalType = Literal["AND", "ANY"]
MLUserDataEncryptionModeStringType = Literal["DISABLED", "SSE-KMS"]
MetadataOperationType = Literal["CREATE"]
NodeTypeType = Literal["CRAWLER", "JOB", "TRIGGER"]
OAuth2GrantTypeType = Literal["AUTHORIZATION_CODE", "CLIENT_CREDENTIALS", "JWT_BEARER"]
ParamTypeType = Literal["bool", "complex", "float", "int", "list", "null", "str"]
ParquetCompressionTypeType = Literal[
    "brotli", "gzip", "lz4", "lzo", "none", "snappy", "uncompressed"
]
PartitionIndexStatusType = Literal["ACTIVE", "CREATING", "DELETING", "FAILED"]
PermissionType = Literal[
    "ALL",
    "ALTER",
    "CREATE_DATABASE",
    "CREATE_TABLE",
    "DATA_LOCATION_ACCESS",
    "DELETE",
    "DROP",
    "INSERT",
    "SELECT",
]
PermissionTypeType = Literal[
    "CELL_FILTER_PERMISSION", "COLUMN_PERMISSION", "NESTED_CELL_PERMISSION", "NESTED_PERMISSION"
]
PiiTypeType = Literal["ColumnAudit", "ColumnMasking", "RowAudit", "RowMasking"]
PrincipalTypeType = Literal["GROUP", "ROLE", "USER"]
PropertyTypeType = Literal["READ_ONLY", "SECRET", "SECRET_OR_USER_INPUT", "UNUSED", "USER_INPUT"]
QuoteCharType = Literal["disabled", "quillemet", "quote", "single_quote"]
RecrawlBehaviorType = Literal["CRAWL_EVENT_MODE", "CRAWL_EVERYTHING", "CRAWL_NEW_FOLDERS_ONLY"]
RegistryStatusType = Literal["AVAILABLE", "DELETING"]
ResourceActionType = Literal["CREATE", "UPDATE"]
ResourceShareTypeType = Literal["ALL", "FEDERATED", "FOREIGN"]
ResourceStateType = Literal["FAILED", "IN_PROGRESS", "QUEUED", "STOPPED", "SUCCESS"]
ResourceTypeType = Literal["ARCHIVE", "FILE", "JAR"]
S3EncryptionModeType = Literal["DISABLED", "SSE-KMS", "SSE-S3"]
ScheduleStateType = Literal["NOT_SCHEDULED", "SCHEDULED", "TRANSITIONING"]
ScheduleTypeType = Literal["AUTO", "CRON"]
SchemaDiffTypeType = Literal["SYNTAX_DIFF"]
SchemaStatusType = Literal["AVAILABLE", "DELETING", "PENDING"]
SchemaVersionStatusType = Literal["AVAILABLE", "DELETING", "FAILURE", "PENDING"]
SeparatorType = Literal["comma", "ctrla", "pipe", "semicolon", "tab"]
SessionStatusType = Literal["FAILED", "PROVISIONING", "READY", "STOPPED", "STOPPING", "TIMEOUT"]
SettingSourceType = Literal["CATALOG", "TABLE"]
SortDirectionTypeType = Literal["ASCENDING", "DESCENDING"]
SortType = Literal["ASC", "DESC"]
SourceControlAuthStrategyType = Literal["AWS_SECRETS_MANAGER", "PERSONAL_ACCESS_TOKEN"]
SourceControlProviderType = Literal["AWS_CODE_COMMIT", "BITBUCKET", "GITHUB", "GITLAB"]
StartingPositionType = Literal["earliest", "latest", "timestamp", "trim_horizon"]
StatementStateType = Literal["AVAILABLE", "CANCELLED", "CANCELLING", "ERROR", "RUNNING", "WAITING"]
StatisticEvaluationLevelType = Literal["Column", "Dataset", "Multicolumn"]
TableAttributesType = Literal["NAME", "TABLE_TYPE"]
TableOptimizerEventTypeType = Literal["completed", "failed", "in_progress", "starting"]
TableOptimizerTypeType = Literal["compaction", "orphan_file_deletion", "retention"]
TargetFormatType = Literal[
    "avro", "csv", "delta", "hudi", "hyper", "iceberg", "json", "orc", "parquet", "xml"
]
TaskRunSortColumnTypeType = Literal["STARTED", "STATUS", "TASK_RUN_TYPE"]
TaskStatusTypeType = Literal[
    "FAILED", "RUNNING", "STARTING", "STOPPED", "STOPPING", "SUCCEEDED", "TIMEOUT"
]
TaskTypeType = Literal[
    "EVALUATION", "EXPORT_LABELS", "FIND_MATCHES", "IMPORT_LABELS", "LABELING_SET_GENERATION"
]
TransformSortColumnTypeType = Literal[
    "CREATED", "LAST_MODIFIED", "NAME", "STATUS", "TRANSFORM_TYPE"
]
TransformStatusTypeType = Literal["DELETING", "NOT_READY", "READY"]
TransformTypeType = Literal["FIND_MATCHES"]
TriggerStateType = Literal[
    "ACTIVATED",
    "ACTIVATING",
    "CREATED",
    "CREATING",
    "DEACTIVATED",
    "DEACTIVATING",
    "DELETING",
    "UPDATING",
]
TriggerTypeType = Literal["CONDITIONAL", "EVENT", "ON_DEMAND", "SCHEDULED"]
UnionTypeType = Literal["ALL", "DISTINCT"]
UnnestSpecType = Literal["FULL", "NOUNNEST", "TOPLEVEL"]
UpdateBehaviorType = Literal["LOG", "UPDATE_IN_DATABASE"]
UpdateCatalogBehaviorType = Literal["LOG", "UPDATE_IN_DATABASE"]
ViewDialectType = Literal["ATHENA", "REDSHIFT", "SPARK"]
ViewUpdateActionType = Literal["ADD", "ADD_OR_REPLACE", "DROP", "REPLACE"]
WorkerTypeType = Literal["G.025X", "G.1X", "G.2X", "G.4X", "G.8X", "Standard", "Z.2X"]
WorkflowRunStatusType = Literal["COMPLETED", "ERROR", "RUNNING", "STOPPED", "STOPPING"]
GlueServiceName = Literal["glue"]
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
    "describe_entity",
    "get_classifiers",
    "get_connections",
    "get_crawler_metrics",
    "get_crawlers",
    "get_databases",
    "get_dev_endpoints",
    "get_job_runs",
    "get_jobs",
    "get_partition_indexes",
    "get_partitions",
    "get_resource_policies",
    "get_security_configurations",
    "get_table_versions",
    "get_tables",
    "get_triggers",
    "get_user_defined_functions",
    "get_workflow_runs",
    "list_blueprints",
    "list_connection_types",
    "list_entities",
    "list_jobs",
    "list_registries",
    "list_schema_versions",
    "list_schemas",
    "list_table_optimizer_runs",
    "list_triggers",
    "list_usage_profiles",
    "list_workflows",
]
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
