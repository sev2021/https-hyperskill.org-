######### sekurak
#!/usr/bin/env python

import socket

def server():
    protocol = socket.getprotobyname('tcp')
    serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM, protocol)
    
    serv.bind(("localhost", 2222))
    serv.listen(1)
    return serv     ##  returns serv in listen() state
    
serv = server()

while True:
    conn, addr = serv.accept()
    while True:
        message = conn.recv(64).decode()
        if message:
            conn.send(('Hi, I am server, I received: ' + message).encode())
        else:
            break
            
    conn.close()
