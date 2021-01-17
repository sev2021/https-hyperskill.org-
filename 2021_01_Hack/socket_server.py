### based on https://steelkiwi.com/blog/working-tcp-sockets
### server and client connection exercise
#########################################
###  SERVER (simplified)

#!/usr/bin/env pythno

import socket
s = socket.socket()            ## stream details removed
s.bind(('localhost', 5700))    ## changed port
s.listen(1)
conn, addr = s.accept()
while 1:
    data = conn.recv(1024)
    print(data)                ## print() added
    if not data:
        break
    conn.sendall(data)
conn.close()


#########################################
###  CLIENT (simplified)

import socket
s = socket.socket()                   ## socket.socket() must run each time after close()
s.connect(('localhost', 5700))         ## must match SERVER
s.sendall('Hello, world'.encode())     ## it didnt work without encode() ??
data = s.recv(1024)                   
s.close()
print 'Received', repr(data)
