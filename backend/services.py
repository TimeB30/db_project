import services_pb2
import services_pb2_grpc
import crypt
class UserService(services_pb2_grpc.UserServicer):
    def __init__(self,db):
        self.db = db
    def GetUser(self, request, context):
        user_login = request.user_login
        user_password_hash = self.db.get_user_password(user_login)
        if user_password_hash == None:
            return services_pb2.GetUserResponse(user_id=0)
        user_password_hash = user_password_hash[0]
        is_password = crypt.verify_password(request.user_password,user_password_hash)
        if not (is_password):
            return services_pb2.GetUserResponse(user_id=0)
        user_info = self.db.get_user_info(user_login)
        return services_pb2.GetUserResponse(user_id = user_info[0], user_role = user_info[1], user_name=user_info[2],block_id=user_info[3],dorm_id=user_info[4])
    def GetUsers(self,request,context):
        block_id = request.block_id
        users = self.db.get_users_info(block_id)
        answer = []
        for i in users:
            answer.append(services_pb2.GetUserResponse(user_id = i[0], user_role = i[1], user_name=i[2],block_id=i[3],dorm_id=i[4]))
        return services_pb2.GetUsersResponse(users_info=answer)
    def CheckLogin(self, request, context):
        user_login = request.user_login
        is_busy = self.db.is_user(user_login)
        return services_pb2.CheckLoginResponse(is_busy=is_busy)
    def Register(self,request,context):
        user_password = crypt.hash_password(request.user_password)
        user_id = self.db.insert_user(request.user_name, request.user_surname, request.user_middle_name,
                            request.user_login, user_password)
        return services_pb2.RegistrationResponse(user_id=user_id)
    def ChangeRole(self,request,context):
        user_id = request.user_id
        role = request.role
        is_changed = self.db.change_role(user_id, role)
        return services_pb2.ChangeRoleResponse(is_changed=is_changed)
class TasksService(services_pb2_grpc.TasksServicer):
    def __init__(self,db):
        self.db = db
    def GetUserTasks(self,request,context):
        user_id = request.user_id
        tasks = self.db.get_user_tasks(user_id)
        answer_tasks = []
        for i in tasks:
            answer_tasks.append(services_pb2.task(task_id=i[0], task_name=i[1]))
        return services_pb2.GetTasksResponse(tasks=answer_tasks)
    def TaskDone(self,request,context):
        is_done = self.db.task_done(request.user_id,request.task_id)
        return services_pb2.TaskDoneResponse(is_done=is_done)
    def MakeTask(self, request, context):
        is_maded = self.db.make_task(request.task_type, request.task_name, request.sender_info)
        return services_pb2.MakeTaskResponse(is_maded=is_maded)
    def GetBlockTasks(self,request,context):
        block_id = request.block_id
        block_tasks = self.db.get_block_tasks(block_id)
        answer = []
        for i in block_tasks:
            answer.append(services_pb2.UserTasks(user_id=i[0], user_name=i[1], user_surname=i[2], task_id=i[3], task_name=i[4]))
        response =  services_pb2.GetBlockTasksResponse(users_task=answer)
        return response
    def DeleteTask(self,request,context):
        task_id = request.task_id
        user_id = request.user_id
        is_deleted  = self.db.delete_task(task_id,user_id)
        return services_pb2.DeleteTaskResponse(is_deleted=is_deleted)
class HistoryService(services_pb2_grpc.HistoryServicer):
    def __init__(self,db):
        self.db = db
    def AddHistory(self, request, context):
        user_id = request.user_id
        block_id = request.block_id
        dorm_id = request.dorm_id
        action = request.action
        is_added = self.db.add_history(user_id,block_id,dorm_id,action)
        return (services_pb2.AddHistoryResponse(is_added=is_added))

    def GetBlockHistory(self,request,context):
        history = self.db.get_block_history(request.block_id)
        answer = []
        for i in history:
            answer.append(services_pb2.HistoryLine(dorm_id=i[0],block_id=i[1],user_id=i[2],user_name=i[3],user_surname=i[4],action=i[5]))
        return services_pb2.GetBlockHistoryResponse(history=answer)

class DormService(services_pb2_grpc.DormServicer):
    def __init__(self,db):
        self.db = db
    def GetDormsBlocks(self,request,context):
        is_free = request.free
        answer = []
        dorms_blocks = self.db.get_dorms_blocks(is_free)
        if len(dorms_blocks) == 0:
            return services_pb2.GetDormsBlocksResponse(DormsBlocks=[])
        dorm_id = dorms_blocks[0][0]
        dorm_name = dorms_blocks[0][1]
        Blocks = []
        for i in dorms_blocks:
            if i[0] == dorm_id:
                Blocks.append(services_pb2.block(block_id=i[2],block_number= i[3]))
            else:
                answer.append(services_pb2.DormBlocks(dorm_id = dorm_id, dorm_name = dorm_name, blocks=Blocks))
                dorm_id = i[0]
                dorm_name = i[1]
                Blocks  = []
                Blocks.append(services_pb2.block(block_id=i[2],block_number= i[3]))
        answer.append(services_pb2.DormBlocks(dorm_id=dorm_id, dorm_name=dorm_name, blocks=Blocks))
        return services_pb2.GetDormsBlocksResponse(DormsBlocks=answer)
    def AddUser(self,request,context):
        user_id = request.user_id
        user_role = request.user_role
        block_id = request.block_id
        answer = self.db.AddUser(user_id,user_role,block_id)
        return services_pb2.AddUserResponse(is_added=answer)
    def KickUser (self,request,context):
        user_id = request.user_id
        block_id = request.block_id
        is_kicked = self.db.kick_user(user_id,block_id)
        return services_pb2.KickUserResponse(is_kicked=is_kicked)
class RequestService(services_pb2_grpc.RequestServicer):
    def __init__(self,db):
        self.db = db
    def AddRequest(self,request,context):
        dorm_id = request.dorm_id
        block_id = request.block_id
        user_id = request.user_id
        is_added = self.db.add_request(dorm_id,block_id,user_id)
        return  services_pb2.AddRequestResponse(is_added=is_added)
    def CancelRequest(self,request,context):
        request_id = request.request_id
        is_cancelled = self.db.cancel_request(request_id)
        return services_pb2.CancelRequestResponse(is_cancelled=is_cancelled)
    def GetRequest(self,request,context):
        user_id = request.user_id
        request_info = self.db.get_request(user_id)
        if (request_info):
            return services_pb2.GetRequestResponse(request_id=request_info[0],dorm_id=request_info[1],
                                                   dorm_name=request_info[2], block_id=request_info[3],block_number=request_info[4],status=request_info[5])
        return services_pb2.GetRequestResponse(request_id = 0)
    def GetRequests(self,request,context):
        block_id = request.block_id
        requests = self.db.get_requests(block_id)
        answer = []
        if (requests):
            for i in requests:
                answer.append(services_pb2.request(request_id=i[0],user_id=i[1], user_name = i[2],
                                                       user_surname = i[3], user_middle_name=i[4]))
            return services_pb2.GetRequestsResponse(requests=answer)
        return services_pb2.GetRequestsResponse()
    def SetRequestStatus(self,request,context):
        request_id = request.request_id
        status = request.status
        response = self.db.set_request_status(request_id,status)
        return services_pb2.SetRequestStatusResponse(is_changed=response)

    def DeleteRequests(self,request,context):
        block_id = request.block_id
        are_deleted = self.db.delete_requests(block_id)
        return services_pb2.DeleteRequestsResponse(are_deleted=are_deleted)