#################################################################
####################### SIMPLE SOCKET SERVER ####################

import socket

def server():
    server_socket = socket.socket()
    server_socket.bind(('localhost', 8090))
    server_socket.listen(1)
    return server_socket.accept()


connection, sender = server()                  # makes instance of server()
while True:
    message = connection.recv(64).decode()
    if message == "":                           # you cant send empty string
        break                                    # break only if connection closed
    print(message)
connection.close()                              # good practice

#################################################################
#################### TO CONNECT / SEND:  ########################

import socket

s = socket.socket()
s.connect(('localhost', 8090))        # must be same as server.bind value
s.send(b"abcdefg")                    # can use .decode()
s.close()                             # good practice
