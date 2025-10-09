import os
import json
from io import StringIO
from collections import defaultdict
import builtins
import argparse

def print(msg):
    global memory_file
    builtins.print(msg)
    memory_file.write(msg + "\n" if "\n" not in msg else msg)

def input(msg=None):
    global memory_file
    if msg == None:
        user_input = builtins.input()
    else:
        user_input = builtins.input(msg)
        memory_file.write(msg + "\n" if "\n" not in msg else msg)
    memory_file.write(user_input)
    return user_input

def add_term():
    global cards_lst
    while True:
        term = input()
        if term in cards_lst:
            print(f'The term "{term}" already exists. Try again:')
            continue
        return term

def add_definition():
    while True:
        definition = input()
        if definition in cards_lst.values():
            print(f'The definition "{definition}" already exists. Try again:')
            continue
        return definition

def add_card():
    global cards_lst
    print("The card:")
    term = add_term()
    print("The definition of the card:")
    definition = add_definition()
    cards_lst[term] = definition
    print(f'The pair ("{term}":"{definition}") has been added.')

def remove_card():
    global cards_lst
    card = input("Which card?\n")
    if card in cards_lst:
        del cards_lst[card]
        print("The card has been removed.")
    else:
        print(f'Can\'t remove "{card}": there is no such card.')

def ask():
    global mistakes
    ask_times = int(input("How many times to ask?\n"))
    counter = 0
    while counter < ask_times:
        for term, definition in cards_lst.items():
            print(f'Print the definition of "{term}":')
            answer = input()
            if answer == definition:
                print("Correct!")
            elif answer in cards_lst.values():
                index_position = list(cards_lst.values()).index(answer)
                correct_term = list(cards_lst.keys())[index_position]
                print(f'Wrong. The right answer is "{definition}", but your definition is correct for "{correct_term}".')
                mistakes[term] += 1
            else:
                print(f'Wrong. The right answer is "{definition}".')
                mistakes[term] += 1
            counter += 1
            if counter == ask_times:
                break

def export_card():
    global cards_lst
    fname = input("File name:\n") if not export_file else export_file
    with open(fname, "w") as file:
        for card in cards_lst.items():
            term, definition = card
            json.dump({term:definition}, file)
            file.write("\n")
    num = len(cards_lst)
    print(f'{num} cards have been saved.')

def import_card():
    global cards_lst
    fname = input("File name:\n") if not import_file else import_file
    if os.path.exists(fname):
        with open(fname, "r") as file:
            lines = file.readlines() 
        num = len(lines)
        cards_import = [json.loads(line.strip()) for line in lines]
        for card in cards_import:
            for term, definition in card.items():   
                cards_lst[term] = definition
        print(f"{num} cards have been loaded.")
    else:
        print("File not found.")

def hardest_card():
    global mistakes
    if len(mistakes) == 0:
        print("There are no cards with errors.")
    else:
        lst_hardest_card = []
        hardest = max(mistakes.values())
        for card, times in mistakes.items():
            if times == hardest:
                lst_hardest_card.append(card)
        if len(lst_hardest_card) > 1:
            print(f'The hardest cards are "{'", "'.join(lst_hardest_card)}". You have {hardest} errors answering them.')
        elif len(lst_hardest_card) == 1:
            print(f'The hardest card is "{lst_hardest_card[0]}". You have {hardest} errors answering it.')

def reset_stats():
    global mistakes
    mistakes.clear()
    print("Card statistics have been reset.")

def log():
    global memory_file
    fname = input("File name:\n")
    memory_file.seek(0)
    with open(fname, "w") as f:
        for line in memory_file:
            f.write(line)
    print("The log has been saved.")


menu = {"add": add_card, "remove": remove_card, "ask": ask, "reset stats": reset_stats,
        "import": import_card, "export": export_card, "hardest card": hardest_card, "log": log}
cards_lst = {}
mistakes = defaultdict(int)
memory_file = StringIO()
parser = argparse.ArgumentParser()
parser.add_argument('--import_from')
parser.add_argument('--export_to')
args = parser.parse_args()
import_file = args.import_from
export_file = args.export_to
print(export_file)
if import_file:
    import_card() 
while True:
    action = input("Input the action (add, remove, import, export, ask, exit, log, hardest card, reset stats):\n")
    if action == "exit":
        if export_file:
            export_card()
        print("Bye bye!")
        break
    else:
        menu[action]()
