import sqlite3
import random

conn = sqlite3.connect('card.s3db')           #  SQLITE DATABASE ACCESS
cur = conn.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS card (id INTEGER PRIMARY KEY, number TEXT, pin TEXT, balance INTEGER DEFAULT 0)")
conn.commit()


def luhn_validation(numb_string):
    print(numb_string)  # method changed, not 9 but all digits checked now
    # sum of even digits
    numb_sum = sum(map(int, numb_string[1::2]))  
    
    # ...plus sum of odd digits multiplied by 2 and reduced by 9 if bigger than 10
    numb_sum += sum([(round(int(i) * 2 + int(i) / 8)) % 10 for i in numb_string[::2]])
    
    # last digit (checksum) calculated
    tenth_digit = 10 - numb_sum % 10
    
    # returning nine digit string plus checksum
    return numb_string + str(tenth_digit)[-1]


def add_client():
    cur = conn.cursor()                     #  SQLITE DATABASE ACCESS
    cur.execute("SELECT * FROM card")
    sqlite_accounts = cur.fetchall()        #  list of all accounts
    conn.commit()
    
    while True:            #  check to prevent account duplication
        new_account = int(random.random() * 1000000000)
        new_account = str(new_account).zfill(9)
        if new_account not in str(sqlite_accounts):
            break

    new_account = luhn_validation("400000" + new_account)
    new_pin = int(random.random() * 10000)
    new_pin = str(new_pin).zfill(4)
    print("Your card has been created")
    print("Your card number:")
    print(new_account)
    print("Your card PIN:")
    print(new_pin)
    # Saving new account to sqlite3 database card.s3db
    cur = conn.cursor()
    cur.execute("INSERT INTO card (number, pin) VALUES (?, ?)", (new_account, new_pin))
    conn.commit()


def log_client():
    cur = conn.cursor()                     #  SQLITE DATABASE ACCESS
    cur.execute("SELECT * FROM card")
    sqlite_accounts = cur.fetchall()        #  list of all accounts
    conn.commit()

    print("Enter your card number:")
    get_account = input()
    print("Enter your PIN:")
    get_pin = input()
    sqlite_account = []

    for i in sqlite_accounts:                    #  check if user input in accounts
        if get_account in i and get_pin in i:
            sqlite_account = list(i)           #  attach matching record (tuple)

    if not sqlite_account:                     # reject if no user input in accounts
        print("Wrong card number or PIN!")
        return
        
    print("You have successfully logged in!")
    
    while True:
        print("1. Balance\n2. Add income\n3. Do transfer\n4. Close account\n5. Log out\n0. Exit")
        get_action = input()
        
        if get_action == "0":
            print("Bye!")
            exit()

        if get_action == "5":
            print("You have successfully logged out!")
            return

        if get_action == "1":
            print("Balance: " + str(sqlite_account[3]))

        if get_action == "2":              #  Add income
            sqlite_account[3] += int(input("Enter income:\n"))
            cur = conn.cursor()
            cur.execute("UPDATE card SET balance = ? WHERE number = ?", (sqlite_account[3], sqlite_account[1]))
            conn.commit()
            print("Income was added!")

        if get_action == "3":          #  Do transfer
            transfer_card = input("Transfer\nEnter card number:\n")
            if luhn_validation(transfer_card[:-1]) != transfer_card:    # transfer card validation
                print("Probably you made a mistake in the card number. Please try again!")
                continue

            transfer_account = []
            for i in sqlite_accounts:                   # check if user input in accounts
                if transfer_card in i:
                    transfer_account = list(i)            # attach matching record (tuple)

            if not transfer_account:                      # reject if no user input in accounts
                print("Such a card does not exist.")
                continue
            else:
                transfer_amount = int(input("Enter how much money you want to transfer:\n"))
                if transfer_amount > sqlite_account[3]:
                    print("Not enough money!")
                    continue
                else:
                    sqlite_account[3] -= transfer_amount
                    transfer_account[3] += transfer_amount
                    cur = conn.cursor()
                    cur.execute("UPDATE card SET balance = ? WHERE number = ?", (sqlite_account[3], sqlite_account[1]))
                    cur.execute("UPDATE card SET balance = ? WHERE number = ?", (transfer_account[3], transfer_account[1]))
                    conn.commit()
                    print("Success!")

        if get_action == "4":     # Close account (account pin reset)
            cur = conn.cursor()
            cur.execute("DELETE FROM card WHERE number = ?", (sqlite_account[1],))
            conn.commit()
            print("The account has been closed!")


while True:
    print("1. Create an account\n2. Log into account\n0. Exit")
    client_choice = input()
    
    if client_choice == "0":
        print("Bye!")
        exit()
        
    if client_choice == "1":
        add_client()
        
    if client_choice == "2":
        log_client()
