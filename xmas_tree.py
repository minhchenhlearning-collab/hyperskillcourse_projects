import random 

def make_tree(height):
    rows = []
    rows.append("X")
    rows.append("^")
    for i in range(height-1):
        rows.append(list(f'/{("*"*(i*2+1))}\\'))
    rows.append("| |")
    return rows

def add_decorates(tree, interval):
    counter = 0
    for index, row in enumerate(tree[3:-1]):
        for place in range(1, len(row[1:-1])):
            if place % 2 == 0:
                if interval == 1:
                    tree[index+3][place] = "O"
                    continue
                counter += 1
                if interval > 1 and counter % interval == 1:
                        tree[index+3][place] = "O"
    return tree

def complete_tree(height, interval):
    tree = make_tree(height)
    return add_decorates(tree, interval)

def make_card():
    card = []
    card.append(list("-" * 50))
    for i in range(28):
        card.append(list(f"|{' ' * 48}|"))
    card.append(list("-" * 50))
    card[26] = f"|{"Merry Xmas".center(48)}|"
    return card

def tree_on_card():
    card = make_card()
    num_trees = len(args) // 4 
    trees_info = []
    slice_ = 0
    for i in range(num_trees):
        trees_info.append(args[slice_:(slice_+4)])
        slice_ += 4
    all_trees = [complete_tree(arg[0], arg[1]) for arg in trees_info]
    for i, info in enumerate(trees_info):
        line = info[2] + 1
        column = info[3]
        column_end = column + 1
        for tree in all_trees[i:]:
            card[line][column] = tree[0]
            line += 1
            card[line][column] = tree[1]
            for row in tree[2:-1]:
                line += 1
                column -= 1
                column_end += 1
                card[line][column:column_end] = row
            card[line+1][info[3]-1:info[3]+2] = tree[-1]
            break
        # A lil snow falls
        for i in range(20):
            card[random.randint(1, 20)][random.randint(1, 49)] = "+"
    return card

args = list(map(int, input().split()))
if len(args) == 2:
    height = args[0]
    interval = args[1]
    tree = complete_tree(height, interval)
    for row in tree:
        print(("".join(row).center(height*2-1)))
else:
    card = tree_on_card()
    for i in card:
        print("".join(i))