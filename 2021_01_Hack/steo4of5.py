###############  ALL BAD

import socket
import sys
from string import ascii_lowercase, digits
from itertools import product

args = sys.argv
chars = ascii_lowercase + digits


def brut_force(word):
    for i in range(1, len(word) + 1):
        for brut_message in product(word, repeat=i):
            yield "".join(brut_message)


def from_list(filename):
    with open(filename) as f:
        for f_line in f:
            for is_pass in product(*((i.lower(), i.upper()) for i in f_line.strip("\n"))):
                yield is_pass


def login_list(filename):
    with open(filename) as f:
        for f_line in f:
            is_pass = "{ 'login' : '" + f_line.strip("\n") + "', 'password' : ' ' }"
            yield is_pass


with socket.socket() as client_s:


    address_port = (args[1], int(args[2]))
    client_s.connect(address_port)
    resp = ""
    while True:
        o = open("logss.txt", "w")
        list_message = next(login_list("C:\\Temp\\logins.txt"))
        o.write(list_message)
        o.close()
        resp = ""
        try:
            client_s.send(list_message.encode())
            resp = client_s.recv(1024).decode()
        except:
            print(list_message)
            exit()
        if resp == '{    "result": "Connection success!"}':
            break
print(list_message)
