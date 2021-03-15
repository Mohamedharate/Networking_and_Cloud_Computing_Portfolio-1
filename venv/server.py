import socket
import os
from _thread import *

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = '0.0.0.0'
port = 2345
RECV_BUFFER = 4096

server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

try:
    server_socket.bind((host, port))
except socket.error as e:
    print(str(e))

print('Socket is listening..')
server_socket.listen(5)

class Client_class():
    def __init__(self, username, user_socket):
        self.username = username
        self.user_socket = user_socket

clientsArray = []

def multi_threaded_client(connection, user):
    while True:

        msg_to_clients = input('Me: ')
        for one_client in clientsArray:
            try:
                if one_client.user_socket:
                    one_client.user_socket.send(str.encode(msg_to_clients))

            except:
                print(one_client.username.upper() + " disconnected!\n")
                clientsArray.remove(one_client)

        for one_client in clientsArray:
            try:
                data = one_client.user_socket.recv(RECV_BUFFER)
                if data:
                    print(f"{one_client.username.upper()}: " + data.decode())
            except:
                print(one_client.username.upper() + " disconnected!\n")
                clientsArray.remove(one_client)

while True:
    client_socket, address = server_socket.accept()
    user = client_socket.recv(RECV_BUFFER).decode()
    clientsArray.append(Client_class(user, client_socket))
    print(f'{user.upper()} is connected with IP address ' + address[0] + ', and Port: ' + str(address[1]))

    start_new_thread(multi_threaded_client, (client_socket, user))

server_socket.close()