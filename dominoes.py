'''
1/ Creating variables storing domino set, domino snake, highest double, computer/player hand/highest double, status
2/ Splitting dominoes
    2.1> Stock: 14
    2.2> Computer hand: 7
    2.3> Player hand: 7
3/ Play card
    3.0> Command positive: right -> append 
    3.1> Command negative: left -> insert
    3.2> Command 0: Draw from stock / Skip if stock is empty
    3.3> Computer move: Compute for points of playable pairs and choose the lowest point one
4/ End conditions
    4.1> Computer/Player has no more pieces
    4.2> End piece appears 8 times in snake
5/ Info
    5.1> Stock length
    5.2> Computer length
    5.3> Your pieces
    5.4> Status
6/ Error Warning
    6.1> Command out of range: Invalid
    6.2> Not int command: Invalid
    6.3> Not match ends: Illegal move
'''
import random

class DominoesGame:
    def __init__(self):
        self.domino_set = [[a, b] for a in range(7) for b in range(7) if a <= b]
        self.double_set = [[a, b] for a in range(7) for b in range(7) if a == b]
        self.domino_snake = []
        self.stock = []
        self.computer_hand = []
        self.player_hand = []
        self.computer_double = []
        self.player_double = []
        self.highest_double = []
        self.status = ""
        self.highest_double = []
    
    def splitting(self):
        random.shuffle(self.domino_set)
        self.stock = self.domino_set[:14]
        self.computer_hand = self.domino_set[14:21]
        self.player_hand = self.domino_set[21:]

    def valid_command_checking(self):
        try:
            self.command = int(self.command)
        except ValueError:
            print("Invalid input. Please try again.")
            return False
        if self.command > len(self.player_hand) or self.command < -len(self.player_hand):
            print("Invalid input. Please try again.")
            return False
        return True
    
    def checking_double(self, hand):
        double = []
        for pair in hand:
            if pair in self.double_set:
                double.append(pair)
        return max(double) if double else None
    
    def legal_move_checking(self):
        self.piece_to_go = self.player_hand[abs(self.command)-1]
        if self.command > 0:
            for piece in self.piece_to_go:
                if piece == self.domino_snake[-1][-1]:
                    return True
        elif self.command < 0:
            for piece in self.piece_to_go:
                if piece == self.domino_snake[0][0]:
                    return True
        print("Illegal move. Please try again.")
        return False
    
    def first_to_move(self):
        if self.highest_double in self.computer_hand:
            self.computer_hand.remove(self.highest_double)
            self.status = "player"
        elif self.highest_double in self.player_hand:
            self.player_hand.remove(self.highest_double)
            self.status = "computer"
        self.domino_snake.append(self.highest_double)

    def player_play(self):
        if self.command > 0:
            if self.piece_to_go[0] == self.domino_snake[-1][-1]:
                self.domino_snake.append(self.piece_to_go)
            elif self.piece_to_go[1] == self.domino_snake[-1][-1]:
                reversed = self.piece_to_go[::-1]
                self.domino_snake.append(reversed)
        elif self.command < 0:
            if self.piece_to_go[0] == self.domino_snake[0][0]:
                reversed = self.piece_to_go[::-1]
                self.domino_snake.insert(0, reversed)
            elif self.piece_to_go[1] == self.domino_snake[0][0]:
                self.domino_snake.insert(0, self.piece_to_go)
        self.player_hand.remove(self.piece_to_go)
        self.status = "computer"
        
    def computer_play(self):
        dict_point = {0:1, 1:2, 2:4, 3:1, 4:3, 5:3, 6:0}
        playable_pairs = []
        score_list = []
        input("Status: Computer is about to make a move. Press Enter to continue...\n")
        for pair in self.computer_hand:
            for element in pair:
                if element == self.domino_snake[0][0] or element == self.domino_snake[-1][-1]:
                    playable_pairs.append(pair)
        if playable_pairs:
            for pair in playable_pairs:
                score = 0
                for element in pair:
                    score += dict_point[element]
                score_list.append(score)
            lowest_score = min(score_list)
            self.piece_to_go = playable_pairs[score_list.index(lowest_score)]
            if self.piece_to_go[0] == self.domino_snake[0][0]:
                reversed_piece = self.piece_to_go[::-1]
                self.domino_snake.insert(0, reversed_piece)
            elif self.piece_to_go[1] == self.domino_snake[0][0]:
                self.domino_snake.insert(0, self.piece_to_go)
            elif self.piece_to_go[0] == self.domino_snake[-1][-1]:
                self.domino_snake.append(self.piece_to_go)
            elif self.piece_to_go[1] == self.domino_snake[-1][1]:
                reversed_piece = self.piece_to_go[::-1]
                self.domino_snake.append(reversed_piece)
            self.computer_hand.remove(self.piece_to_go)
            self.status = "player"
        else:
            piece = random.choice(self.stock)
            self.computer_hand.append(piece)
            self.stock.remove(piece)
            self.status = "player"

    def checking_end(self):
        if len(self.computer_hand) == 0 and len(self.player_hand) > 0:
            print("Status: The game is over. The computer won!")
            return True
        elif len(self.computer_hand) > 0 and len(self.player_hand) == 0:
            print("Status: The game is over. You won!")
            return True
        counter = 0
        last_num = self.domino_snake[-1][-1]
        for pair in self.domino_snake:
            for element in pair:
                if element == last_num:
                    counter += 1
        if counter == 8:
            print("Status: The game is over. It's a draw!")
            return True
        return False
                
    def info(self):
        print("=" * 70)
        print(f"Stock size: {len(self.stock)}")
        print(f"Computer pieces: {len(self.computer_hand)}")
        print("")
        if len(self.domino_snake) < 7:
            print("".join(f"{pair}" for pair in self.domino_snake))
        else:
            print("".join(f"{pair}" for pair in self.domino_snake[:3]), "...", "".join(f"{pair}" for pair in self.domino_snake[-3:]), sep="")
        print("")
        print("Your pieces:")
        for posi, pair in enumerate(self.player_hand):
            print(f"{posi+1}:{pair}")
        print("")
        if self.status == "player":
            print("")

    def get_highest_double(self):
        if self.player_double != None and self.computer_double != None:
            self.highest_double = max(self.player_double, self.computer_double)
        elif self.player_double != None and self.computer_double == None:
            self.highest_double = self.player_double
        elif self.player_double == None and self.computer_double != None:
            self.highest_double = self.player_double
        
    def play(self):
        while True:
            self.splitting()
            self.player_double = self.checking_double(self.player_hand)
            self.computer_double = self.checking_double(self.computer_hand)
            if self.player_double == None or self.computer_double == None:
                continue
            else:
                self.get_highest_double()
                self.first_to_move()
                break
        while True:
            if self.checking_end():
                break
            self.info()
            if self.status == "player":
                print("Status: It's your turn to make a move. Enter your command.")
                while True:
                    self.command = input()
                    if self.command == "0":
                        if self.stock:
                            piece = random.choice(self.stock)
                            self.player_hand.append(piece)
                            self.stock.remove(piece)
                        self.status = "computer"
                        break
                    if not self.valid_command_checking():
                        continue
                    else:
                        if not self.legal_move_checking():
                            continue
                        else:
                            self.player_play()
                            break
            elif self.status == "computer":
                self.computer_play()

domino = DominoesGame()
domino.play()





