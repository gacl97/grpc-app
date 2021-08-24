import grpc
import subscribers_pb2_grpc
from concurrent import futures
from subscribers import Subscribers

server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
subscribers_pb2_grpc.add_SubscribersServiceServicer_to_server(Subscribers(), server)
server.add_insecure_port('[::]:3000')
server.start()
server.wait_for_termination()