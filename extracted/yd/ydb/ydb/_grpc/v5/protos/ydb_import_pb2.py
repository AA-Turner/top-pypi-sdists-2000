# -*- coding: utf-8 -*-
# flake8: noqa
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: protos/ydb_import.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from ydb._grpc.v5.protos.annotations import validation_pb2 as protos_dot_annotations_dot_validation__pb2
from ydb._grpc.v5.protos import ydb_export_pb2 as protos_dot_ydb__export__pb2
from ydb._grpc.v5.protos import ydb_operation_pb2 as protos_dot_ydb__operation__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x17protos/ydb_import.proto\x12\nYdb.Import\x1a#protos/annotations/validation.proto\x1a\x17protos/ydb_export.proto\x1a\x1aprotos/ydb_operation.proto\x1a\x1fgoogle/protobuf/timestamp.proto\"\xee\x01\n\x0eImportProgress\"\xdb\x01\n\x08Progress\x12\x18\n\x14PROGRESS_UNSPECIFIED\x10\x00\x12\x16\n\x12PROGRESS_PREPARING\x10\x01\x12\x1a\n\x16PROGRESS_TRANSFER_DATA\x10\x02\x12\x1a\n\x16PROGRESS_BUILD_INDEXES\x10\x03\x12\x11\n\rPROGRESS_DONE\x10\x04\x12\x19\n\x15PROGRESS_CANCELLATION\x10\x05\x12\x16\n\x12PROGRESS_CANCELLED\x10\x06\x12\x1f\n\x1bPROGRESS_CREATE_CHANGEFEEDS\x10\x07\"\xa0\x01\n\x12ImportItemProgress\x12\x13\n\x0bparts_total\x18\x01 \x01(\r\x12\x17\n\x0fparts_completed\x18\x02 \x01(\r\x12.\n\nstart_time\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12,\n\x08\x65nd_time\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\"\x80\x05\n\x14ImportFromS3Settings\x12\x16\n\x08\x65ndpoint\x18\x01 \x01(\tB\x04\x90\xe6*\x01\x12\x37\n\x06scheme\x18\x02 \x01(\x0e\x32\'.Ydb.Import.ImportFromS3Settings.Scheme\x12\x14\n\x06\x62ucket\x18\x03 \x01(\tB\x04\x90\xe6*\x01\x12\x18\n\naccess_key\x18\x04 \x01(\tB\x04\x90\xe6*\x01\x12\x18\n\nsecret_key\x18\x05 \x01(\tB\x04\x90\xe6*\x01\x12\x34\n\x05items\x18\x06 \x03(\x0b\x32%.Ydb.Import.ImportFromS3Settings.Item\x12\x1c\n\x0b\x64\x65scription\x18\x07 \x01(\tB\x07\xa2\xe6*\x03\x18\x80\x01\x12\x19\n\x11number_of_retries\x18\x08 \x01(\r\x12\x0e\n\x06region\x18\t \x01(\t\x12\"\n\x1a\x64isable_virtual_addressing\x18\n \x01(\x08\x12\x0e\n\x06no_acl\x18\x0b \x01(\x08\x12 \n\x18skip_checksum_validation\x18\x0c \x01(\x08\x12\x15\n\rsource_prefix\x18\r \x01(\t\x12\x18\n\x10\x64\x65stination_path\x18\x0e \x01(\t\x12;\n\x13\x65ncryption_settings\x18\x0f \x01(\x0b\x32\x1e.Ydb.Export.EncryptionSettings\x1aZ\n\x04Item\x12\x17\n\rsource_prefix\x18\x01 \x01(\tH\x00\x12\x15\n\x0bsource_path\x18\x03 \x01(\tH\x00\x12\x18\n\x10\x64\x65stination_path\x18\x02 \x01(\tB\x08\n\x06Source\".\n\x06Scheme\x12\x0f\n\x0bUNSPECIFIED\x10\x00\x12\x08\n\x04HTTP\x10\x01\x12\t\n\x05HTTPS\x10\x02\"\x14\n\x12ImportFromS3Result\"\xb9\x01\n\x14ImportFromS3Metadata\x12\x32\n\x08settings\x18\x01 \x01(\x0b\x32 .Ydb.Import.ImportFromS3Settings\x12\x35\n\x08progress\x18\x02 \x01(\x0e\x32#.Ydb.Import.ImportProgress.Progress\x12\x36\n\x0eitems_progress\x18\x03 \x03(\x0b\x32\x1e.Ydb.Import.ImportItemProgress\"\x8a\x01\n\x13ImportFromS3Request\x12\x39\n\x10operation_params\x18\x01 \x01(\x0b\x32\x1f.Ydb.Operations.OperationParams\x12\x38\n\x08settings\x18\x02 \x01(\x0b\x32 .Ydb.Import.ImportFromS3SettingsB\x04\x90\xe6*\x01\"D\n\x14ImportFromS3Response\x12,\n\toperation\x18\x01 \x01(\x0b\x32\x19.Ydb.Operations.Operation\"\xab\x03\n\x1dListObjectsInS3ExportSettings\x12\x16\n\x08\x65ndpoint\x18\x01 \x01(\tB\x04\x90\xe6*\x01\x12\x37\n\x06scheme\x18\x02 \x01(\x0e\x32\'.Ydb.Import.ImportFromS3Settings.Scheme\x12\x14\n\x06\x62ucket\x18\x03 \x01(\tB\x04\x90\xe6*\x01\x12\x18\n\naccess_key\x18\x04 \x01(\tB\x04\x90\xe6*\x01\x12\x18\n\nsecret_key\x18\x05 \x01(\tB\x04\x90\xe6*\x01\x12=\n\x05items\x18\x06 \x03(\x0b\x32..Ydb.Import.ListObjectsInS3ExportSettings.Item\x12\x19\n\x11number_of_retries\x18\x07 \x01(\r\x12\x0e\n\x06region\x18\x08 \x01(\t\x12\"\n\x1a\x64isable_virtual_addressing\x18\t \x01(\x08\x12\x0e\n\x06prefix\x18\n \x01(\t\x12;\n\x13\x65ncryption_settings\x18\x0b \x01(\x0b\x32\x1e.Ydb.Export.EncryptionSettings\x1a\x14\n\x04Item\x12\x0c\n\x04path\x18\x01 \x01(\t\"\x99\x01\n\x1bListObjectsInS3ExportResult\x12;\n\x05items\x18\x01 \x03(\x0b\x32,.Ydb.Import.ListObjectsInS3ExportResult.Item\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\x1a$\n\x04Item\x12\x0e\n\x06prefix\x18\x01 \x01(\t\x12\x0c\n\x04path\x18\x02 \x01(\t\"\xd1\x01\n\x1cListObjectsInS3ExportRequest\x12\x39\n\x10operation_params\x18\x01 \x01(\x0b\x32\x1f.Ydb.Operations.OperationParams\x12\x41\n\x08settings\x18\x02 \x01(\x0b\x32).Ydb.Import.ListObjectsInS3ExportSettingsB\x04\x90\xe6*\x01\x12\x1f\n\tpage_size\x18\x03 \x01(\x03\x42\x0c\xb2\xe6*\x08<= 10000\x12\x12\n\npage_token\x18\x04 \x01(\t\"M\n\x1dListObjectsInS3ExportResponse\x12,\n\toperation\x18\x01 \x01(\x0b\x32\x19.Ydb.Operations.Operation\" \n\rYdbDumpFormat\x12\x0f\n\x07\x63olumns\x18\x01 \x03(\t\"\x12\n\x10ImportDataResult\"\xae\x01\n\x11ImportDataRequest\x12\x39\n\x10operation_params\x18\x01 \x01(\x0b\x32\x1f.Ydb.Operations.OperationParams\x12\x0c\n\x04path\x18\x02 \x01(\t\x12\x17\n\x04\x64\x61ta\x18\x03 \x01(\x0c\x42\t\xa2\xe6*\x05\x18\x80\x80\x80\x08\x12-\n\x08ydb_dump\x18\x04 \x01(\x0b\x32\x19.Ydb.Import.YdbDumpFormatH\x00\x42\x08\n\x06\x66ormat\"B\n\x12ImportDataResponse\x12,\n\toperation\x18\x01 \x01(\x0b\x32\x19.Ydb.Operations.OperationBV\n\x16tech.ydb.proto.import_Z9github.com/ydb-platform/ydb-go-genproto/protos/Ydb_Import\xf8\x01\x01\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'protos.ydb_import_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\026tech.ydb.proto.import_Z9github.com/ydb-platform/ydb-go-genproto/protos/Ydb_Import\370\001\001'
  _IMPORTFROMS3SETTINGS.fields_by_name['endpoint']._options = None
  _IMPORTFROMS3SETTINGS.fields_by_name['endpoint']._serialized_options = b'\220\346*\001'
  _IMPORTFROMS3SETTINGS.fields_by_name['bucket']._options = None
  _IMPORTFROMS3SETTINGS.fields_by_name['bucket']._serialized_options = b'\220\346*\001'
  _IMPORTFROMS3SETTINGS.fields_by_name['access_key']._options = None
  _IMPORTFROMS3SETTINGS.fields_by_name['access_key']._serialized_options = b'\220\346*\001'
  _IMPORTFROMS3SETTINGS.fields_by_name['secret_key']._options = None
  _IMPORTFROMS3SETTINGS.fields_by_name['secret_key']._serialized_options = b'\220\346*\001'
  _IMPORTFROMS3SETTINGS.fields_by_name['description']._options = None
  _IMPORTFROMS3SETTINGS.fields_by_name['description']._serialized_options = b'\242\346*\003\030\200\001'
  _IMPORTFROMS3REQUEST.fields_by_name['settings']._options = None
  _IMPORTFROMS3REQUEST.fields_by_name['settings']._serialized_options = b'\220\346*\001'
  _LISTOBJECTSINS3EXPORTSETTINGS.fields_by_name['endpoint']._options = None
  _LISTOBJECTSINS3EXPORTSETTINGS.fields_by_name['endpoint']._serialized_options = b'\220\346*\001'
  _LISTOBJECTSINS3EXPORTSETTINGS.fields_by_name['bucket']._options = None
  _LISTOBJECTSINS3EXPORTSETTINGS.fields_by_name['bucket']._serialized_options = b'\220\346*\001'
  _LISTOBJECTSINS3EXPORTSETTINGS.fields_by_name['access_key']._options = None
  _LISTOBJECTSINS3EXPORTSETTINGS.fields_by_name['access_key']._serialized_options = b'\220\346*\001'
  _LISTOBJECTSINS3EXPORTSETTINGS.fields_by_name['secret_key']._options = None
  _LISTOBJECTSINS3EXPORTSETTINGS.fields_by_name['secret_key']._serialized_options = b'\220\346*\001'
  _LISTOBJECTSINS3EXPORTREQUEST.fields_by_name['settings']._options = None
  _LISTOBJECTSINS3EXPORTREQUEST.fields_by_name['settings']._serialized_options = b'\220\346*\001'
  _LISTOBJECTSINS3EXPORTREQUEST.fields_by_name['page_size']._options = None
  _LISTOBJECTSINS3EXPORTREQUEST.fields_by_name['page_size']._serialized_options = b'\262\346*\010<= 10000'
  _IMPORTDATAREQUEST.fields_by_name['data']._options = None
  _IMPORTDATAREQUEST.fields_by_name['data']._serialized_options = b'\242\346*\005\030\200\200\200\010'
  _IMPORTPROGRESS._serialized_start=163
  _IMPORTPROGRESS._serialized_end=401
  _IMPORTPROGRESS_PROGRESS._serialized_start=182
  _IMPORTPROGRESS_PROGRESS._serialized_end=401
  _IMPORTITEMPROGRESS._serialized_start=404
  _IMPORTITEMPROGRESS._serialized_end=564
  _IMPORTFROMS3SETTINGS._serialized_start=567
  _IMPORTFROMS3SETTINGS._serialized_end=1207
  _IMPORTFROMS3SETTINGS_ITEM._serialized_start=1069
  _IMPORTFROMS3SETTINGS_ITEM._serialized_end=1159
  _IMPORTFROMS3SETTINGS_SCHEME._serialized_start=1161
  _IMPORTFROMS3SETTINGS_SCHEME._serialized_end=1207
  _IMPORTFROMS3RESULT._serialized_start=1209
  _IMPORTFROMS3RESULT._serialized_end=1229
  _IMPORTFROMS3METADATA._serialized_start=1232
  _IMPORTFROMS3METADATA._serialized_end=1417
  _IMPORTFROMS3REQUEST._serialized_start=1420
  _IMPORTFROMS3REQUEST._serialized_end=1558
  _IMPORTFROMS3RESPONSE._serialized_start=1560
  _IMPORTFROMS3RESPONSE._serialized_end=1628
  _LISTOBJECTSINS3EXPORTSETTINGS._serialized_start=1631
  _LISTOBJECTSINS3EXPORTSETTINGS._serialized_end=2058
  _LISTOBJECTSINS3EXPORTSETTINGS_ITEM._serialized_start=2038
  _LISTOBJECTSINS3EXPORTSETTINGS_ITEM._serialized_end=2058
  _LISTOBJECTSINS3EXPORTRESULT._serialized_start=2061
  _LISTOBJECTSINS3EXPORTRESULT._serialized_end=2214
  _LISTOBJECTSINS3EXPORTRESULT_ITEM._serialized_start=2178
  _LISTOBJECTSINS3EXPORTRESULT_ITEM._serialized_end=2214
  _LISTOBJECTSINS3EXPORTREQUEST._serialized_start=2217
  _LISTOBJECTSINS3EXPORTREQUEST._serialized_end=2426
  _LISTOBJECTSINS3EXPORTRESPONSE._serialized_start=2428
  _LISTOBJECTSINS3EXPORTRESPONSE._serialized_end=2505
  _YDBDUMPFORMAT._serialized_start=2507
  _YDBDUMPFORMAT._serialized_end=2539
  _IMPORTDATARESULT._serialized_start=2541
  _IMPORTDATARESULT._serialized_end=2559
  _IMPORTDATAREQUEST._serialized_start=2562
  _IMPORTDATAREQUEST._serialized_end=2736
  _IMPORTDATARESPONSE._serialized_start=2738
  _IMPORTDATARESPONSE._serialized_end=2804
# @@protoc_insertion_point(module_scope)
