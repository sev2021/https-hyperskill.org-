import socket, json

server_socket = socket.socket()
server_socket.bind(('localhost', 8090))
server_socket.listen(5)
connection, sender = server_socket.accept()

while True:
    data = connection.recv(64)
    if data == b"":
        break
    print(data)
    try:
        print(json.loads(data.decode('utf8'))['login'])   # JSON verificaion
    except Exception as e:
        print(e)
        
        
############# COONNECT? ##############
  
import socket
s = socket.socket()
s.connect(9'localhost', 8090)0                # must match server.bind
s.send(b"lkjlkjlK")                           # NOT A JSON
s.send(json.dumps({"login":"k"}).encode())    # THIS IS JSON
s.send('{"login":"k"}')                       # THIS WILL ALSO SHOW AS JSON !!!
