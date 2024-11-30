import grpc
from concurrent import futures
import time

from db import *
from services import *
import json



def serve(db):
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    services_pb2_grpc.add_UserServicer_to_server(UserService(db),server)
    services_pb2_grpc.add_TasksServicer_to_server(TasksService(db), server)
    services_pb2_grpc.add_HistoryServicer_to_server(HistoryService(db),server)
    services_pb2_grpc.add_DormServicer_to_server(DormService(db),server)
    services_pb2_grpc.add_RequestServicer_to_server(RequestService(db),server)
    server.add_insecure_port('[::]:50051')
    print("Server is starting...")
    server.start()
    try:
        while True:
            time.sleep(60 * 60 * 24)  # Сервер работает круглосуточно
    except KeyboardInterrupt:
        server.stop(0)

if __name__ == '__main__':
    with open("../params.json", "r") as file:
        db_params = json.load(file)
    db = Database(db_params)
    serve(db)
