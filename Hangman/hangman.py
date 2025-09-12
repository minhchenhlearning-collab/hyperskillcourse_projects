import random

class Hangman:
    def reveal_letter(self, letter_guess):
        if letter_guess in self.guessed_letters:
            print("You've already guessed this letter.")
        elif letter_guess not in self.word:
            print("That letter doesn't appear in the word.")
            self.mistakes += 1
        else:
            for index in range(len(self.word)):
                if letter_guess == self.word[index]:
                    self.hidden_word = list(self.hidden_word)
                    self.hidden_word[index] = letter_guess
                    self.hidden_word = "".join(self.hidden_word)

    def error_checking(self, input):
        if (len(input) > 1 and input.isalpha()) or input == "":
            print("Please, input a single letter")
            return True
        elif not input.islower() or not input.isalpha():
            print("Please, enter a lowercase letter from the English alphabet.")
            return True
        return False
    
    def ending_conditions(self):
        if self.mistakes == 8 and "-" in self.hidden_word:
            print("You lost!")
            self.lose_times += 1
            return True
        elif "-" not in self.hidden_word:
            print(f"You guessed the word {self.word}!")
            print("You survived!")
            self.win_times += 1
            return True
        return False

    def play(self):
        self.mistakes = 0
        self.word = random.choice(["python", "java", "swift", "javascript"])
        self.hidden_word = "-" * len(self.word)
        self.guessed_letters = []
        while True:
            print("")
            print(self.hidden_word)
            letter_guess = input("Input a letter: ")
            if self.error_checking(letter_guess):
                continue
            self.reveal_letter(letter_guess)
            self.guessed_letters.append(letter_guess)
            if self.ending_conditions():
                break

    def start_game(self):
        self.win_times = 0
        self.lose_times = 0
        print("H A N G M A N")
        while True:
            command = input('Type "play" to play the game, "results" to show the scoreboard, and "exit" to quit:')
            if command == "play":
                self.play()
            elif command == "exit":
                break
            elif command == "results":
                print(f"You won: {self.win_times} times.")
                print(f"You lost: {self.lose_times} times.")

    
hangman = Hangman()
hangman.start_game()

