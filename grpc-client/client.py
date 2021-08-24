import grpc

import subscribers_pb2_grpc
import subscribers_pb2


client = grpc.insecure_channel('localhost:3000')
stub = subscribers_pb2_grpc.SubscribersServiceStub(client)

while(True):
  command = input("[1] Create\n[2] Find All\n[3] Find One\n[4] Exit\n> ")
  response = ""
  if(command == "1"):
    name = input("Insira o nome: ")
    email = input("Insira o email: ")
    response = stub.CreateSubscriber(subscribers_pb2.CreateSubscriberDto(name=name, email=email))
  elif(command == "2"):  
    response = stub.FindAllSubscribers(subscribers_pb2.google_dot_protobuf_dot_empty__pb2.Empty())
  elif(command == "3"):
    id = input("Insira uma id: ")
    response = stub.FindOneSubscribers(subscribers_pb2.FindOneSubscriberRequest(id=id))
  elif(command == "4"):
    break
  print(response)

print("Finalizado!")