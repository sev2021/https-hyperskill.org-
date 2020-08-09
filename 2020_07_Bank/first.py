# Write your code here
import random
all_clients = {"0":"0000"}

while True:
    print("1. Create an account\n2. Log into account\n0. Exit")
    client_choice = input()
    if client_choice == "0":
        print("Bye!")
        exit()
    if client_choice == "1":
        all_clients = add_client(all_clients)
    if client_choice == "2":
        log_client(all_clients)

def add_client(all_clients = all_clients):
    new_account = "0"
    while new_account in all_clients.keys():
        new_account = int(random.random() * 10000000000)
        new_account = str(new_account).zfill(10)
    new_pin = int(random.random() * 10000)
    all_clients[new_account] = str(new_pin).zfill(4)  
    print("Your card has been created")
    print("Your card number:")
    print("400000" + "new_account")
    print("Your card PIN:")
    print(all_clients[new_account])
    return all_clients

def log_client(all_clients = all_clients):
    print("Enter your card number:")
    get_account = input()
    print("Enter your PIN:")
    get_pin = input()
    if all_clients[get_account[6:]] != get_pin
        print("Wrong card number or PIN!")
        break
    print("You have successfully logged in!")
    while True:
        print("1. Balance\n2. Log out\n0. Exit")
        get_action = input()
        if get_action == "0":
            print("Bye!")
            exit()
        if get_action == "1":
            print("Balance: 0")
        if get_action == "2":
            print("You have successfully logged out!")
            break
