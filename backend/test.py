import crypt
import grpc
import services_pb2_grpc
import services_pb2
with grpc.insecure_channel('localhost:50051') as channel:
    stub = services_pb2_grpc.TasksStub(channel)
    request = services_pb2.GetTasksRequest(user_id=17)
    response = stub.GetUserTasks(request)
    for i in response.tasks:
        print(i.task_id)