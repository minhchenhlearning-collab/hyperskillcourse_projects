def winning_conditions():
    global rows, ls
    columns = [rows[0][0] + rows[1][0] + rows[2][0], rows[0][1] + rows[1][1] + rows[2][1], rows[0][2] + rows[1][2] + rows[2][2]]
    diagonals = [rows[0][0] + rows[1][1] + rows[2][2], rows[0][2] + rows[1][1] + rows[2][0]]
    ls = [*rows, *columns, *diagonals]
    for i in ls:
        if "".join(i) == "OOO":
            print("O wins")
            return True
        elif "".join(i) == "XXX":
            print("X wins")
            return True
    return False

def draw_conditions():
    if not winning_conditions():
        for i in ls:
            if " " in i:
                return False
        print("Draw")
        return True

def print_grid():
    print(f"""{'-' * 9}
| {" ".join(rows[0])} |
| {" ".join(rows[1])} |
| {" ".join(rows[2])} |
{'-' * 9}""")

def player_move():
    while True:
        for turn in ["X", "O"]:
            try:
                row, cell = map(int, input().split())
            except ValueError:
                print("You should enter numbers!")
                continue
            if row > 3 or row < 1 or cell > 3 or cell < 1: 
                print("Coordinates should be from 1 to 3!")
                continue
            elif rows[row-1][cell-1] != " ":
                print("This cell is occupied! Choose another one!")   
                continue
            rows[row-1][cell-1] = turn
            print_grid()
            if winning_conditions() or draw_conditions():
                break
        else:
            continue
        break
            
moves = [x for x in (" " * 9)]
rows = [moves[:3], moves[3:6], moves[6:]]
print_grid()
player_move()
