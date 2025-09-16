import random

class Last_pencil:
    def __init__(self):
        print("How many pencils would you like to use:")
        while True:
            self.base_pencil = input()
            if not self.base_pencil.isnumeric():
                print("The number of pencils should be numeric")
            elif int(self.base_pencil) < 1:
                print("The number of pencils should be positive")
            else:
                self.base_pencil = int(self.base_pencil)
                break
        self.turn = input("Who will be the first (John, Jack):\n")
        while self.turn not in ["John", "Jack"]:
            print("Choose between 'John' and 'Jack'")
            self.turn = input()
    
    def player_turn(self):
        print(f"{self.turn}'s turn!")
        while True:
            pencils_taken = input()
            if pencils_taken not in ["1", "2", "3"]:
                print("Possible values: '1', '2' or '3'")
            elif int(pencils_taken) > self.base_pencil:
                print("Too many pencils were taken")
            else:
                return int(pencils_taken)

    def bot_turn(self):
        print(f"{self.turn}'s turn:")
        example_pencils = self.base_pencil % 4
        if self.base_pencil == 1 or example_pencils == 2:
            pencils_taken = 1
        elif example_pencils == 0:
            pencils_taken = 3
        elif example_pencils == 1:
            pencils_taken = random.choice([1, 2, 3])
        elif example_pencils == 3:
            pencils_taken = 2
        print(pencils_taken)
        return pencils_taken
        

    def play(self):
        while True:
            print("|" * self.base_pencil)
            if self.turn == "Jack":
                pencils_taken = self.bot_turn()
            else:
                pencils_taken = self.player_turn()
            self.base_pencil -= pencils_taken
            self.turn = "Jack" if self.turn == "John" else "John"
            if self.base_pencil <= 0:
                print(f"{self.turn} won!")
                break

game = Last_pencil()
game.play()
