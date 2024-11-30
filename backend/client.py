import grpc
import services_pb2
import services_pb2_grpc
def run():
    # Подключаемся к серверу
    channel = grpc.insecure_channel('localhost:50051')
    stub = service_pb2_grpc.EntryStub(channel)
    # Создаем запрос
    request = service_pb2.EntryRequest(user_login="timeb",user_password="user")

    # Отправляем запрос и получаем ответ
    response = stub.Enter(request)
    print(response.tasks[0].task_id)
    print("Received message:", response.tasks)


if __name__ == '__main__':
    run()
