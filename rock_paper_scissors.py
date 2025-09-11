import csv
import random
import re

def update_rating(user_name, rating):
    with open("rating.txt", "r") as file:
        lines = file.readlines()
    with open("rating.txt", "w") as file:
        for line in lines:
            matching = re.match(user_name, line)
            if not matching:
                file.write(line)
            else:
                file.write(f"{user_name} {rating}")

def get_rating():
    global rating
    with open("rating.txt", "r+") as rating_file:
        reader = csv.reader(rating_file, delimiter=" ")
        for line in reader:
            if user_name == line[0]:
                rating = int(line[1])
        if rating == None:
            rating_file.write(f"{user_name} {0}\n")
            rating = 0

def original_game():
    global rating
    winning_cases = {"scissors":"rock", "rock":"paper", "paper":"scissors"}
    shapes = ["scissors", "paper", "rock"]
    while True:
        user_input = input()
        if user_input == "!rating":
            print(f"Your rating: {rating}")
            continue
        elif user_input == "!exit":
            print("Bye!")
            break
        elif user_input not in shapes:
            print("Invalid input")
            continue
        computer_shape = random.choice(shapes)
        if user_input == computer_shape:
            print(f"There is a draw ({computer_shape})")
            rating += 50
            update_rating(user_name, rating)
        elif winning_cases[computer_shape] == user_input:
            print(f"Well done. The computer chose {computer_shape} and failed")
            rating += 100
            update_rating(user_name, rating)
        else:
            print(f"Sorry, but the computer chose {computer_shape}")
        
def extended_version():
    global rating
    while True:
        user_input = input()
        if user_input == "!rating":
            print(f"Your rating: {rating}")
            continue
        elif user_input == "!exit":
            print("Bye!")
            break
        elif user_input not in set_up:
            print("Invalid input")
            continue
        place_of_input = set_up.index(user_input)
        new_list = set_up[place_of_input+1:] + set_up[:place_of_input]
        computer_shape = random.choice(set_up)
        if user_input == computer_shape:
            print(f"There is a draw ({computer_shape})")
            rating += 50
            update_rating(user_name, rating)
        elif computer_shape in new_list[int(len(new_list)/2):]:
            print(f"Well done. The computer chose {computer_shape} and failed")
            rating += 100
            update_rating(user_name, rating)
        else:
            print(f"Sorry, but the computer chose {computer_shape}")
        

rating = None
user_name = input("Enter your name:")
get_rating()
print(f"Hello, {user_name}")
if (set_up := input().split(",")) == ['']:
    print("Okay, let's start normal mode")
    original_game()
else:
    print("Okay, let's start extended mode")
    extended_version()
