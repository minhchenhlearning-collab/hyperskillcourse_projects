import random


# Blank line
def blank_line():
    print("")
# Inviting friends to party
def inviting(party_guests, num_of_guests):
    blank_line()
    print("Enter the name of every friend (including you), each on a new line:")
    for i in range(num_of_guests):
        party_guests[input()] = 0
# Splitting bill
def splitting(bill_total, number_of_guests, party_guests):
    if lucky == False:
        splitted_bill = round((bill_total / number_of_guests), 2)
        for name in list(party_guests.keys()):
            party_guests[name] = splitted_bill
    else:
        splitted_bill = round((bill_total / (number_of_guests-1)), 2)
        for guest in list(party_guests.keys()):
            if guest != lucky_person:
                party_guests[guest] = splitted_bill
# Lucky mode
def lucky_mode(party_guests):
    blank_line()
    lucky_mode = input('Do you want to use the "Who is lucky?" feature? Write Yes/No:\n')
    blank_line()
    if lucky_mode == "No":
        print("No one is going to be lucky")
        return False
    else:
        global lucky_person
        lucky_person = random.choice(list(party_guests.keys()))
        print(f"{lucky_person} is the lucky one!")
        return True


# Main part
party_guests = {}
num_of_guests = int(input("Enter the number of friends joining (including you)\n"))
if num_of_guests <= 0:
    blank_line()
    print("No one is joining for the party")
else:
    inviting(party_guests, num_of_guests)
    blank_line()
    bill_total = int(input("Enter the total bill value:\n"))
    lucky = lucky_mode(party_guests)
    splitting(bill_total, num_of_guests, party_guests)
    blank_line()
    print(party_guests)