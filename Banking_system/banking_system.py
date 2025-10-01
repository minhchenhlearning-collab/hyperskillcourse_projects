import random
import sqlite3

class Stop(Exception): pass

def blank_line():
    print("")

def create_database():
    conn = sqlite3.connect("card.s3db")
    curr = conn.cursor()
    create_table_command = """CREATE TABLE card (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    number VARCHAR(16),
    pin VARCHAR(4),
    balance INTEGER DEFAULT 0);"""
    curr.execute(create_table_command)
    conn.commit()

def store_credit(info):
    conn = sqlite3.connect("card.s3db")
    curr = conn.cursor()
    for credit in info:
        curr.execute("INSERT INTO card (number, pin) VALUES (?, ?)", (credit, info[credit]["pin"]))
    conn.commit()

def luhn_algorithm(card_num):
    check_lst = list(map(int, list(card_num)))
    for i in range(len(check_lst)):
        if i % 2 == 0:
            check_lst[i] *= 2
    for index, digit in enumerate(check_lst):
        if digit > 9:
            check_lst[index] -= 9
    if sum(check_lst) % 10 == 0:
        return True
    return False    

def card_generator(): 
    card_num = "400000" + str(random.randint(100000000, 999999999))
    check_lst = list(map(int, list(card_num)))
    for i in range(len(check_lst)):
        if i % 2 == 0:
            check_lst[i] *= 2
    for index, digit in enumerate(check_lst):
        if digit > 9:
            check_lst[index] -= 9
    checksum_digit = 10 - (sum(check_lst) % 10)
    if checksum_digit == 10:
        checksum_digit = 1
    card_num += str(checksum_digit)
    return card_num

def credit_generator():
    global credit_info
    pin = ""
    for i in range(4):
        pin += str(random.randint(0, 9))
    while True:
        card_number = card_generator()
        if card_number not in credit_info:
            credit_info[card_number] = {}
            credit_info[card_number]["pin"] = pin
            credit_info[card_number]["balance"] = 0
            break

    blank_line()
    print("Your card has been created")
    print(f"Your card number:\n{card_number}")
    print(f"Your card pin:\n{pin}")

def log_in():
    global credit_info
    blank_line()
    card_num = input("Enter your card number:\n")
    pin = input("Enter your PIN:\n")
    if card_num not in credit_info or pin != credit_info[card_num]["pin"]:
        blank_line()
        print("Wrong card number or PIN!")
        return False
    blank_line()
    print("You have successfully logged in!")
    return card_num

def balance_check(curr_card):
    blank_line()
    print(f"Balance: {credit_info[curr_card]["balance"]}")

def add_income(curr_card):
    blank_line()
    add_num = int(input("Enter income:\n"))
    credit_info[curr_card]["balance"] += add_num
    print("Income was added!")    

def transfer(curr_card):
    blank_line()
    print("Transfer")
    card_recv = input("Enter card number:\n")
    if not luhn_algorithm(card_recv):
        print("Probably you made a mistake in the card number. Please try again!")
    elif card_recv not in credit_info:
        print("Such a card does not exist.")
    else:
        trans_num = int(input("Enter how much money you want to transfer:\n"))
        if trans_num > credit_info[curr_card]["balance"]:
            print("Not enough money!")
        else:
            credit_info[curr_card]["balance"] -= trans_num
            credit_info[card_recv]["balance"] += trans_num
            print("Success!")

def del_account(curr_card):
    del credit_info[curr_card]
    blank_line()
    print("The account has been closed!")
    raise Stop

# curr_card parameter should not be here but for later practice
def log_out(curr_card):
    blank_line()
    print("You have successfully logged out!")
    raise Stop

def exit_(curr_card): 
    global entry_command
    entry_command = "0"
    raise Stop



create_database()
credit_info = {}
menu = {"1": balance_check, "2": add_income, "3": transfer,
        "4": del_account, "5":log_out, "0":exit_}
while True:
    blank_line()
    entry_command = input("1. Create an account\n2. Log into account\n0. Exit\n")
    if entry_command == "1":
        credit_generator()
    elif entry_command == "2":
        if (curr_card:=log_in()) is not False:
            while True:
                blank_line()
                action = input("1. Balance\n2. Add income\n3. Do transfer\n4. Close account\n5. Log out\n0. Exit\n")
                try:
                    menu[action](curr_card)
                except Stop:
                    break
    if entry_command == "0":
        store_credit(credit_info)
        blank_line()
        print("Bye!")
        break
