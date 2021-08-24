import uuid
import subscribers_pb2_grpc
import subscribers_pb2

class Subscribers(subscribers_pb2_grpc.SubscribersService):
  subscribers = []
  
  def __init__(self):
    self.subscribers.append({
      "id": 'd21d5cbf-c1b6-465f-8a60-240e73668db4',
      "name": "Jose Lages",
      "email": "joseLages@gmail.com"
    })

    self.subscribers.append({
      "id": '9a47aa71-199a-4441-acf1-a695f124e4e4',
      "name": "Fernandes Lima",
      "email": "fernandesLima@gmail.com"
    })

  def CreateSubscriber(self, request, context):
    print("Criando subscriber")
    
    subscriber = {
      "id": str(uuid.uuid4()),
      "name": request.name,
      "email": request.email
    }

    self.subscribers.append(subscriber)
    
    return subscribers_pb2.SubscriberResponse(subscriber = subscriber)

  def FindAllSubscribers(self, request, context):
    print("Buscando todos os subscribers")
    return subscribers_pb2.FindAllSubscribersResponse(subscribers = self.subscribers)

  def FindOneSubscribers(self, request, context):
    print("Buscando pelo subscriber com id: ", request.id)

    for subscriber in self.subscribers:

      if(subscriber['id'] == request.id):
        return subscribers_pb2.SubscriberResponse(subscriber = subscriber)
    return subscribers_pb2.SubscriberResponse(id=-1)
