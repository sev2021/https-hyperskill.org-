###############  TEST FILE
###########################

import socket, random

# dome = input("What domain?: ")

al = "abcdefghijklmnopqrstuvwxyz"


for i in range(10):
    dome = "".join(random.choices(al, k=3))
    try:
        respo = socket.gethostbyname(dome + ".com")
        print(dome + ".com - ", respo) 
    except: 
        print(dome + ".com - Error")
