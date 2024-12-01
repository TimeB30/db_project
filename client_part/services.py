import services_pb2_grpc
import services_pb2
import grpc
class UserService:
    def __init__(self,ip_port="localhost:50051"):
        self.ip_port = ip_port
    def GetUser(self, user_login, user_password):
        with grpc.insecure_channel(self.ip_port) as channel:
            stub = services_pb2_grpc.UserStub(channel)
            request = services_pb2.GetUserRequest(user_login=user_login,user_password=user_password)
            response = stub.GetUser(request)
            return response
    def CheckLogin(self,user_login):
        with grpc.insecure_channel(self.ip_port) as channel:
            stub = services_pb2_grpc.UserStub(channel)
            request = services_pb2.CheckLoginRequest(user_login=user_login)
            response = stub.CheckLogin(request)
            return response
    def Register(self,user_name, user_surname, user_middle_name, user_login, user_password):
        with grpc.insecure_channel(self.ip_port) as channel:
            stub = services_pb2_grpc.UserStub(channel)
            response = stub.Register(services_pb2.RegistrationRequest(user_name=user_name,user_surname=user_surname,
                                                                           user_middle_name=user_middle_name,user_login=user_login,
                                                                           user_password=user_password))
            return response
    def TaskDone(self,user_id,task_id):
        with grpc.insecure_channel(self.ip_port) as channel:
            stub = services_pb2_grpc.TasksStub(channel)
            response = stub.TaskDone(services_pb2.TaskDoneRequest(task_id=task_id,user_id=user_id))
            return response.is_done
    def GetUserTasks(self,user_id):
        with grpc.insecure_channel(self.ip_port) as channel:
            stub = services_pb2_grpc.TasksStub(channel)
            request = services_pb2.GetTasksRequest(user_id=user_id)
            response = stub.GetUserTasks(request)
            return response
    def AddHistory(self,user_info, action):
        with grpc.insecure_channel(self.ip_port) as channel:
            stub = services_pb2_grpc.HistoryStub(channel)
            request = services_pb2.AddHistoryRequest(user_id=user_info.user_id,block_id=user_info.block_id,
                                                     dorm_id=user_info.dorm_id,
                                                     action=action)
            response = stub.AddHistory(request)
            return response
    def GetUsers(self,block_id):
        with grpc.insecure_channel(self.ip_port) as channel:
            stub = services_pb2_grpc.UserStub(channel)
            request = services_pb2.GetUsersRequest(block_id=block_id)
            response = stub.GetUsers(request)
            return response
    def MakeTask(self,task_type, task_name, user_info):
        with grpc.insecure_channel(self.ip_port) as channel:
            stub = services_pb2_grpc.TasksStub(channel)
            request = services_pb2.MakeTaskRequest(task_type=task_type, task_name=task_name,sender_info=user_info)
            response = stub.MakeTask(request)
            return response

    def GetBlockTasks(self,block_id):
        with grpc.insecure_channel(self.ip_port) as channel:
            stub = services_pb2_grpc.TasksStub(channel)
            request = services_pb2.GetBlockTasksRequest(block_id=block_id)
            response = stub.GetBlockTasks(request)
            return response
    def DeleteTask(self,task_id,user_id):
        with grpc.insecure_channel(self.ip_port) as channel:
            stub = services_pb2_grpc.TasksStub(channel)
            request = services_pb2.DeleteTaskRequest(task_id=task_id,user_id=user_id)
            response = stub.DeleteTask(request)
            return response
    def GetBlockHistory(self,block_id):
        with grpc.insecure_channel(self.ip_port) as channel:
            stub = services_pb2_grpc.HistoryStub(channel)
            request = services_pb2.GetBlockHistoryRequest(block_id=block_id)
            response = stub.GetBlockHistory(request)
            return response

    def GetDormsBlocks(self,free = 1):
        with grpc.insecure_channel(self.ip_port) as channel:
            stub = services_pb2_grpc.DormStub(channel)
            request = services_pb2.GetDormsBlocksRequest(free=free)
            response = stub.GetDormsBlocks(request)
            return response
    def AddUser(self,user_id,user_role,block_id):
        with grpc.insecure_channel(self.ip_port) as channel:
            stub = services_pb2_grpc.DormStub(channel)
            request = services_pb2.AddUserRequest(user_id=user_id,user_role=user_role,block_id=block_id)
            response = stub.AddUser(request)
            return response
    def AddRequest(self,dorm_id, block_id,user_id):
        with grpc.insecure_channel(self.ip_port) as channel:
            stub = services_pb2_grpc.RequestStub(channel)
            request = services_pb2.AddRequestRequest(dorm_id=dorm_id,block_id=block_id,user_id=user_id)
            response = stub.AddRequest(request)
            return response
    def CancelRequest(self,request_id):
        with grpc.insecure_channel(self.ip_port) as channel:
            stub = services_pb2_grpc.RequestStub(channel)
            request = services_pb2.CancelRequestRequest(request_id=request_id)
            response = stub.CancelRequest(request)
            return response
    def GetRequest(self,user_id):
        with grpc.insecure_channel(self.ip_port) as channel:
            stub = services_pb2_grpc.RequestStub(channel)
            request = services_pb2.GetRequestRequest(user_id=user_id)
            response = stub.GetRequest(request)
            return response
    def GetRequests(self,block_id):
        with grpc.insecure_channel(self.ip_port) as channel:
            stub = services_pb2_grpc.RequestStub(channel)
            request = services_pb2.GetRequestsRequest(block_id=block_id)
            response = stub.GetRequests(request)
            return response
    def KickUser(self,user_id, block_id):
        with grpc.insecure_channel(self.ip_port) as channel:
            stub = services_pb2_grpc.DormStub(channel)
            request = services_pb2.KickUserRequest(user_id=user_id, block_id=block_id)
            response = stub.KickUser(request)
            return response
    def ChangeRole(self,user_id,role):
        with grpc.insecure_channel(self.ip_port) as channel:
            stub = services_pb2_grpc.UserStub(channel)
            request = services_pb2.ChangeRoleRequest(user_id=user_id, role=role)
            response = stub.ChangeRole(request)
            return response
    def SetRequestStatus(self,request_id,status):
        with grpc.insecure_channel(self.ip_port) as channel:
            stub = services_pb2_grpc.RequestStub(channel)
            request = services_pb2.SetRequestStatusRequest(request_id=request_id, status=status)
            response = stub.SetRequestStatus(request)
            return response
    def DeleteRequests(self,block_id):
        with grpc.insecure_channel(self.ip_port) as channel:
            stub = services_pb2_grpc.RequestStub(channel)
            request = services_pb2.DeleteRequestsRequest(block_id=block_id)
            response = stub.DeleteRequests(request)
            return response