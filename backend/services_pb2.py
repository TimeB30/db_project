# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: services.proto
# Protobuf Python Version: 5.28.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    28,
    1,
    '',
    'services.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0eservices.proto\"2\n\x11\x43hangeRoleRequest\x12\x0f\n\x07user_id\x18\x01 \x01(\x05\x12\x0c\n\x04role\x18\x02 \x01(\t\"(\n\x12\x43hangeRoleResponse\x12\x12\n\nis_changed\x18\x01 \x01(\x08\"#\n\x0fGetUsersRequest\x12\x10\n\x08\x62lock_id\x18\x01 \x01(\x05\"8\n\x10GetUsersResponse\x12$\n\nusers_info\x18\x01 \x03(\x0b\x32\x10.GetUserResponse\"\x83\x01\n\x13RegistrationRequest\x12\x11\n\tuser_name\x18\x01 \x01(\t\x12\x14\n\x0cuser_surname\x18\x02 \x01(\t\x12\x18\n\x10user_middle_name\x18\x03 \x01(\t\x12\x12\n\nuser_login\x18\x04 \x01(\t\x12\x15\n\ruser_password\x18\x05 \x01(\t\"\'\n\x14RegistrationResponse\x12\x0f\n\x07user_id\x18\x01 \x01(\x05\"\'\n\x11\x43heckLoginRequest\x12\x12\n\nuser_login\x18\x01 \x01(\t\"%\n\x12\x43heckLoginResponse\x12\x0f\n\x07is_busy\x18\x01 \x01(\x08\";\n\x0eGetUserRequest\x12\x12\n\nuser_login\x18\x01 \x01(\t\x12\x15\n\ruser_password\x18\x02 \x01(\t\"k\n\x0fGetUserResponse\x12\x0f\n\x07user_id\x18\x01 \x01(\x05\x12\x11\n\tuser_role\x18\x02 \x01(\t\x12\x11\n\tuser_name\x18\x03 \x01(\t\x12\x10\n\x08\x62lock_id\x18\x04 \x01(\x05\x12\x0f\n\x07\x64orm_id\x18\x05 \x01(\x05\"5\n\x11\x44\x65leteTaskRequest\x12\x0f\n\x07user_id\x18\x01 \x01(\x05\x12\x0f\n\x07task_id\x18\x02 \x01(\x05\"(\n\x12\x44\x65leteTaskResponse\x12\x12\n\nis_deleted\x18\x01 \x01(\x08\"i\n\tUserTasks\x12\x0f\n\x07user_id\x18\x01 \x01(\x05\x12\x11\n\tuser_name\x18\x02 \x01(\t\x12\x14\n\x0cuser_surname\x18\x03 \x01(\t\x12\x0f\n\x07task_id\x18\x04 \x01(\x05\x12\x11\n\ttask_name\x18\x05 \x01(\t\"(\n\x14GetBlockTasksRequest\x12\x10\n\x08\x62lock_id\x18\x01 \x01(\x05\"7\n\x15GetBlockTasksResponse\x12\x1e\n\nusers_task\x18\x01 \x03(\x0b\x32\n.UserTasks\"^\n\x0fMakeTaskRequest\x12\x11\n\ttask_type\x18\x01 \x01(\t\x12\x11\n\ttask_name\x18\x02 \x01(\t\x12%\n\x0bsender_info\x18\x03 \x01(\x0b\x32\x10.GetUserResponse\"$\n\x10MakeTaskResponse\x12\x10\n\x08is_maded\x18\x01 \x01(\x08\"3\n\x0fTaskDoneRequest\x12\x0f\n\x07task_id\x18\x01 \x01(\x05\x12\x0f\n\x07user_id\x18\x02 \x01(\x05\"#\n\x10TaskDoneResponse\x12\x0f\n\x07is_done\x18\x01 \x01(\x05\"\"\n\x0fGetTasksRequest\x12\x0f\n\x07user_id\x18\x01 \x01(\x05\"*\n\x04task\x12\x0f\n\x07task_id\x18\x01 \x01(\x05\x12\x11\n\ttask_name\x18\x02 \x01(\t\"(\n\x10GetTasksResponse\x12\x14\n\x05tasks\x18\x01 \x03(\x0b\x32\x05.task\"z\n\x0bHistoryLine\x12\x0f\n\x07\x64orm_id\x18\x01 \x01(\x05\x12\x10\n\x08\x62lock_id\x18\x02 \x01(\x05\x12\x0f\n\x07user_id\x18\x03 \x01(\x05\x12\x11\n\tuser_name\x18\x04 \x01(\t\x12\x14\n\x0cuser_surname\x18\x05 \x01(\t\x12\x0e\n\x06\x61\x63tion\x18\x06 \x01(\t\"*\n\x16GetBlockHistoryRequest\x12\x10\n\x08\x62lock_id\x18\x01 \x01(\x05\"8\n\x17GetBlockHistoryResponse\x12\x1d\n\x07history\x18\x01 \x03(\x0b\x32\x0c.HistoryLine\"W\n\x11\x41\x64\x64HistoryRequest\x12\x0f\n\x07user_id\x18\x01 \x01(\x05\x12\x10\n\x08\x62lock_id\x18\x02 \x01(\x05\x12\x0f\n\x07\x64orm_id\x18\x03 \x01(\x05\x12\x0e\n\x06\x61\x63tion\x18\x04 \x01(\t\"&\n\x12\x41\x64\x64HistoryResponse\x12\x10\n\x08is_added\x18\x01 \x01(\x08\"4\n\x0fKickUserRequest\x12\x0f\n\x07user_id\x18\x01 \x01(\x05\x12\x10\n\x08\x62lock_id\x18\x02 \x01(\x05\"%\n\x10KickUserResponse\x12\x11\n\tis_kicked\x18\x01 \x01(\x08\"F\n\x0e\x41\x64\x64UserRequest\x12\x0f\n\x07user_id\x18\x01 \x01(\x05\x12\x11\n\tuser_role\x18\x02 \x01(\t\x12\x10\n\x08\x62lock_id\x18\x04 \x01(\x05\"#\n\x0f\x41\x64\x64UserResponse\x12\x10\n\x08is_added\x18\x01 \x01(\x08\"/\n\x05\x62lock\x12\x14\n\x0c\x62lock_number\x18\x01 \x01(\x05\x12\x10\n\x08\x62lock_id\x18\x02 \x01(\x05\"H\n\nDormBlocks\x12\x0f\n\x07\x64orm_id\x18\x01 \x01(\x05\x12\x11\n\tdorm_name\x18\x02 \x01(\t\x12\x16\n\x06\x62locks\x18\x03 \x03(\x0b\x32\x06.block\"%\n\x15GetDormsBlocksRequest\x12\x0c\n\x04\x66ree\x18\x01 \x01(\x05\":\n\x16GetDormsBlocksResponse\x12 \n\x0b\x44ormsBlocks\x18\x01 \x03(\x0b\x32\x0b.DormBlocks\")\n\x15\x44\x65leteRequestsRequest\x12\x10\n\x08\x62lock_id\x18\x01 \x01(\x05\"-\n\x16\x44\x65leteRequestsResponse\x12\x13\n\x0b\x61re_deleted\x18\x01 \x01(\x08\"=\n\x17SetRequestStatusRequest\x12\x12\n\nrequest_id\x18\x01 \x01(\x05\x12\x0e\n\x06status\x18\x02 \x01(\t\".\n\x18SetRequestStatusResponse\x12\x12\n\nis_changed\x18\x01 \x01(\x08\"\x81\x01\n\x07request\x12\x12\n\nrequest_id\x18\x01 \x01(\x05\x12\x0f\n\x07user_id\x18\x02 \x01(\x05\x12\x11\n\tuser_name\x18\x03 \x01(\t\x12\x14\n\x0cuser_surname\x18\x04 \x01(\t\x12\x18\n\x10user_middle_name\x18\x05 \x01(\t\x12\x0e\n\x06status\x18\x06 \x01(\t\"&\n\x12GetRequestsRequest\x12\x10\n\x08\x62lock_id\x18\x01 \x01(\x05\"1\n\x13GetRequestsResponse\x12\x1a\n\x08requests\x18\x01 \x03(\x0b\x32\x08.request\"$\n\x11GetRequestRequest\x12\x0f\n\x07user_id\x18\x01 \x01(\x05\"\x84\x01\n\x12GetRequestResponse\x12\x12\n\nrequest_id\x18\x01 \x01(\x05\x12\x0f\n\x07\x64orm_id\x18\x02 \x01(\x05\x12\x11\n\tdorm_name\x18\x03 \x01(\t\x12\x10\n\x08\x62lock_id\x18\x04 \x01(\x05\x12\x14\n\x0c\x62lock_number\x18\x05 \x01(\x05\x12\x0e\n\x06status\x18\x06 \x01(\t\"*\n\x14\x43\x61ncelRequestRequest\x12\x12\n\nrequest_id\x18\x01 \x01(\x05\"-\n\x15\x43\x61ncelRequestResponse\x12\x14\n\x0cis_cancelled\x18\x01 \x01(\x08\"&\n\x12\x41\x64\x64RequestResponse\x12\x10\n\x08is_added\x18\x01 \x01(\x05\"G\n\x11\x41\x64\x64RequestRequest\x12\x0f\n\x07\x64orm_id\x18\x01 \x01(\x05\x12\x10\n\x08\x62lock_id\x18\x02 \x01(\x05\x12\x0f\n\x07user_id\x18\x03 \x01(\x05\x32\x8c\x02\n\x04User\x12,\n\x07GetUser\x12\x0f.GetUserRequest\x1a\x10.GetUserResponse\x12/\n\x08GetUsers\x12\x10.GetUsersRequest\x1a\x11.GetUsersResponse\x12\x35\n\nCheckLogin\x12\x12.CheckLoginRequest\x1a\x13.CheckLoginResponse\x12\x37\n\x08Register\x12\x14.RegistrationRequest\x1a\x15.RegistrationResponse\x12\x35\n\nChangeRole\x12\x12.ChangeRoleRequest\x1a\x13.ChangeRoleResponse2\x95\x02\n\x05Tasks\x12\x33\n\x0cGetUserTasks\x12\x10.GetTasksRequest\x1a\x11.GetTasksResponse\x12/\n\x08TaskDone\x12\x10.TaskDoneRequest\x1a\x11.TaskDoneResponse\x12/\n\x08MakeTask\x12\x10.MakeTaskRequest\x1a\x11.MakeTaskResponse\x12>\n\rGetBlockTasks\x12\x15.GetBlockTasksRequest\x1a\x16.GetBlockTasksResponse\x12\x35\n\nDeleteTask\x12\x12.DeleteTaskRequest\x1a\x13.DeleteTaskResponse2\x86\x01\n\x07History\x12\x35\n\nAddHistory\x12\x12.AddHistoryRequest\x1a\x13.AddHistoryResponse\x12\x44\n\x0fGetBlockHistory\x12\x17.GetBlockHistoryRequest\x1a\x18.GetBlockHistoryResponse2\xa8\x01\n\x04\x44orm\x12\x41\n\x0eGetDormsBlocks\x12\x16.GetDormsBlocksRequest\x1a\x17.GetDormsBlocksResponse\x12,\n\x07\x41\x64\x64User\x12\x0f.AddUserRequest\x1a\x10.AddUserResponse\x12/\n\x08KickUser\x12\x10.KickUserRequest\x1a\x11.KickUserResponse2\xfd\x02\n\x07Request\x12\x35\n\nAddRequest\x12\x12.AddRequestRequest\x1a\x13.AddRequestResponse\x12>\n\rCancelRequest\x12\x15.CancelRequestRequest\x1a\x16.CancelRequestResponse\x12\x35\n\nGetRequest\x12\x12.GetRequestRequest\x1a\x13.GetRequestResponse\x12\x38\n\x0bGetRequests\x12\x13.GetRequestsRequest\x1a\x14.GetRequestsResponse\x12G\n\x10SetRequestStatus\x12\x18.SetRequestStatusRequest\x1a\x19.SetRequestStatusResponse\x12\x41\n\x0e\x44\x65leteRequests\x12\x16.DeleteRequestsRequest\x1a\x17.DeleteRequestsResponseb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'services_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_CHANGEROLEREQUEST']._serialized_start=18
  _globals['_CHANGEROLEREQUEST']._serialized_end=68
  _globals['_CHANGEROLERESPONSE']._serialized_start=70
  _globals['_CHANGEROLERESPONSE']._serialized_end=110
  _globals['_GETUSERSREQUEST']._serialized_start=112
  _globals['_GETUSERSREQUEST']._serialized_end=147
  _globals['_GETUSERSRESPONSE']._serialized_start=149
  _globals['_GETUSERSRESPONSE']._serialized_end=205
  _globals['_REGISTRATIONREQUEST']._serialized_start=208
  _globals['_REGISTRATIONREQUEST']._serialized_end=339
  _globals['_REGISTRATIONRESPONSE']._serialized_start=341
  _globals['_REGISTRATIONRESPONSE']._serialized_end=380
  _globals['_CHECKLOGINREQUEST']._serialized_start=382
  _globals['_CHECKLOGINREQUEST']._serialized_end=421
  _globals['_CHECKLOGINRESPONSE']._serialized_start=423
  _globals['_CHECKLOGINRESPONSE']._serialized_end=460
  _globals['_GETUSERREQUEST']._serialized_start=462
  _globals['_GETUSERREQUEST']._serialized_end=521
  _globals['_GETUSERRESPONSE']._serialized_start=523
  _globals['_GETUSERRESPONSE']._serialized_end=630
  _globals['_DELETETASKREQUEST']._serialized_start=632
  _globals['_DELETETASKREQUEST']._serialized_end=685
  _globals['_DELETETASKRESPONSE']._serialized_start=687
  _globals['_DELETETASKRESPONSE']._serialized_end=727
  _globals['_USERTASKS']._serialized_start=729
  _globals['_USERTASKS']._serialized_end=834
  _globals['_GETBLOCKTASKSREQUEST']._serialized_start=836
  _globals['_GETBLOCKTASKSREQUEST']._serialized_end=876
  _globals['_GETBLOCKTASKSRESPONSE']._serialized_start=878
  _globals['_GETBLOCKTASKSRESPONSE']._serialized_end=933
  _globals['_MAKETASKREQUEST']._serialized_start=935
  _globals['_MAKETASKREQUEST']._serialized_end=1029
  _globals['_MAKETASKRESPONSE']._serialized_start=1031
  _globals['_MAKETASKRESPONSE']._serialized_end=1067
  _globals['_TASKDONEREQUEST']._serialized_start=1069
  _globals['_TASKDONEREQUEST']._serialized_end=1120
  _globals['_TASKDONERESPONSE']._serialized_start=1122
  _globals['_TASKDONERESPONSE']._serialized_end=1157
  _globals['_GETTASKSREQUEST']._serialized_start=1159
  _globals['_GETTASKSREQUEST']._serialized_end=1193
  _globals['_TASK']._serialized_start=1195
  _globals['_TASK']._serialized_end=1237
  _globals['_GETTASKSRESPONSE']._serialized_start=1239
  _globals['_GETTASKSRESPONSE']._serialized_end=1279
  _globals['_HISTORYLINE']._serialized_start=1281
  _globals['_HISTORYLINE']._serialized_end=1403
  _globals['_GETBLOCKHISTORYREQUEST']._serialized_start=1405
  _globals['_GETBLOCKHISTORYREQUEST']._serialized_end=1447
  _globals['_GETBLOCKHISTORYRESPONSE']._serialized_start=1449
  _globals['_GETBLOCKHISTORYRESPONSE']._serialized_end=1505
  _globals['_ADDHISTORYREQUEST']._serialized_start=1507
  _globals['_ADDHISTORYREQUEST']._serialized_end=1594
  _globals['_ADDHISTORYRESPONSE']._serialized_start=1596
  _globals['_ADDHISTORYRESPONSE']._serialized_end=1634
  _globals['_KICKUSERREQUEST']._serialized_start=1636
  _globals['_KICKUSERREQUEST']._serialized_end=1688
  _globals['_KICKUSERRESPONSE']._serialized_start=1690
  _globals['_KICKUSERRESPONSE']._serialized_end=1727
  _globals['_ADDUSERREQUEST']._serialized_start=1729
  _globals['_ADDUSERREQUEST']._serialized_end=1799
  _globals['_ADDUSERRESPONSE']._serialized_start=1801
  _globals['_ADDUSERRESPONSE']._serialized_end=1836
  _globals['_BLOCK']._serialized_start=1838
  _globals['_BLOCK']._serialized_end=1885
  _globals['_DORMBLOCKS']._serialized_start=1887
  _globals['_DORMBLOCKS']._serialized_end=1959
  _globals['_GETDORMSBLOCKSREQUEST']._serialized_start=1961
  _globals['_GETDORMSBLOCKSREQUEST']._serialized_end=1998
  _globals['_GETDORMSBLOCKSRESPONSE']._serialized_start=2000
  _globals['_GETDORMSBLOCKSRESPONSE']._serialized_end=2058
  _globals['_DELETEREQUESTSREQUEST']._serialized_start=2060
  _globals['_DELETEREQUESTSREQUEST']._serialized_end=2101
  _globals['_DELETEREQUESTSRESPONSE']._serialized_start=2103
  _globals['_DELETEREQUESTSRESPONSE']._serialized_end=2148
  _globals['_SETREQUESTSTATUSREQUEST']._serialized_start=2150
  _globals['_SETREQUESTSTATUSREQUEST']._serialized_end=2211
  _globals['_SETREQUESTSTATUSRESPONSE']._serialized_start=2213
  _globals['_SETREQUESTSTATUSRESPONSE']._serialized_end=2259
  _globals['_REQUEST']._serialized_start=2262
  _globals['_REQUEST']._serialized_end=2391
  _globals['_GETREQUESTSREQUEST']._serialized_start=2393
  _globals['_GETREQUESTSREQUEST']._serialized_end=2431
  _globals['_GETREQUESTSRESPONSE']._serialized_start=2433
  _globals['_GETREQUESTSRESPONSE']._serialized_end=2482
  _globals['_GETREQUESTREQUEST']._serialized_start=2484
  _globals['_GETREQUESTREQUEST']._serialized_end=2520
  _globals['_GETREQUESTRESPONSE']._serialized_start=2523
  _globals['_GETREQUESTRESPONSE']._serialized_end=2655
  _globals['_CANCELREQUESTREQUEST']._serialized_start=2657
  _globals['_CANCELREQUESTREQUEST']._serialized_end=2699
  _globals['_CANCELREQUESTRESPONSE']._serialized_start=2701
  _globals['_CANCELREQUESTRESPONSE']._serialized_end=2746
  _globals['_ADDREQUESTRESPONSE']._serialized_start=2748
  _globals['_ADDREQUESTRESPONSE']._serialized_end=2786
  _globals['_ADDREQUESTREQUEST']._serialized_start=2788
  _globals['_ADDREQUESTREQUEST']._serialized_end=2859
  _globals['_USER']._serialized_start=2862
  _globals['_USER']._serialized_end=3130
  _globals['_TASKS']._serialized_start=3133
  _globals['_TASKS']._serialized_end=3410
  _globals['_HISTORY']._serialized_start=3413
  _globals['_HISTORY']._serialized_end=3547
  _globals['_DORM']._serialized_start=3550
  _globals['_DORM']._serialized_end=3718
  _globals['_REQUEST']._serialized_start=3721
  _globals['_REQUEST']._serialized_end=4102
# @@protoc_insertion_point(module_scope)
