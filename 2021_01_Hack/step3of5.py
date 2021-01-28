# write your code here
import sys, socket, itertools

chars = " abcdefghijklmnopqrstuvwxyz0123456789"
with open("C:\\Python27\\passwords.txt") as f:
    pass_list = f.read().splitlines()

def get_pass(ip_address, port, message):
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
        if m == 1:
            continue
        if m > 1000000:
            break
        message = "".join(i).lstrip()
        client_socket.send(message.encode('utf-8'))    #  Send a message
        resp = client_socket.recv(1024)         #  Receive the server’s response
        if resp.decode('utf-8') == "Connection success!":
            print(message)
            break
    client_socket.close()                      # Close the socket

def get_from_file(ip_address, port, pass_list):
    client_socket = socket.socket()       #  Create a new socket
    client_socket.connect((ip_address, int(port)))  #  Connect to a host and a port using the socket
    for test_pass in pass_list:
        for product in itertools.product(*((i.lower(), i.upper()) for i in test_pass)):
            message = "".join(product)
            client_socket.send(message.encode('utf-8'))                                 #  Send a message
            resp = client_socket.recv(1024)                                          #  Receive the server’s response
            if resp.decode('utf-8') == "Connection success!":
                print(message)
                client_socket.close()                                                # Close the socket
                exit()

if __name__ == '__main__':

  if len(sys.argv) == 4:
    print(get_pass(sys.argv[1], sys.argv[2], sys.argv[3]))

  if len(sys.argv) == 3:
    print(get_from_file(sys.argv[1], sys.argv[2], pass_list))
