# write your code here
import sys, socket, itertools

chars = " abcdefghijklmnopqrstuvwxyz0123456789"

def get_pass(ip_address, port, message):        #  This was step 1 of 5 
    client_socket = socket.socket()             #  Create a new socket
    client_socket.connect((ip_address, int(port)))   #  Connect to a host and a port using the socket
    client_socket.send(message.encode())        #  Send a message
    resp = client_socket.recv(1024)             #  Receive the server’s response
    client_socket.close()                       #  Close the socket
    resp = resp.decode()
    return resp

def get_million(ip_address, port, key):
    client_socket = socket.socket()       #  Create a new socket
    client_socket.connect((ip_address, int(port)))  #  Connect to a host and a port using the socket
    m = 0
    for i in itertools.combinations_with_replacement(key, 4):
        m += 1
        if m == 1:                                #  Skip first opton with empty string ""
            continue
        if m > 1000000:                           #  Number of tries limitted
            break
        message = "".join(i).lstrip()
        client_socket.send(message.encode('utf-8'))    #  Send a message
        resp = client_socket.recv(1024)         #  Receive the server’s response
        if resp.decode('utf-8') == "Connection success!":
            print(message)
            break
    client_socket.close()                      # Close the socket

if __name__ == '__main__':

  if len(sys.argv) == 4:                  #  Call function from step 1 of 5 
    print(get_pass(sys.argv[1], sys.argv[2], sys.argv[3]))

  if len(sys.argv) == 3:                  #  Call function from step 2 of 5 
    print(get_million(sys.argv[1], sys.argv[2], chars))
