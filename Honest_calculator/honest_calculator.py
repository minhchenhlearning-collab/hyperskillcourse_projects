def calculate(x, oper, y):
    if oper not in "+-*/":
        print("Yes ... an interesting math operation. You've slept through all classes, haven't you?")
        return "False"
    check(x, y, oper)
    if oper == "+":
        result = x + y
    elif oper == "-":
        result = x - y
    elif oper == "*":
        result = x * y
    elif oper == "/" and y != 0:
        result = x / y
    else:
        print("Yeah... division by zero. Smart move...")
        return "False"
    return result

def is_one_digit(v):
    if 10 > v > -10 and v.is_integer():
        return True
    return False

def check(num1, num2, oper):
    msg_6 = " ... lazy"
    msg_7 = " ... very lazy"
    msg_8 = " ... very, very lazy"
    msg_9 = "You are"
    msg = ""
    if is_one_digit(num1) and is_one_digit(num2):
        msg += msg_6
    if (num1 == 1 or num2 == 1) and oper == "*":
        msg += msg_7
    if (num1 == 0 or num2 == 0) and (oper == "*" or oper == "+" or oper == "-"):
        msg += msg_8
    if msg != "":
        msg = msg_9 + msg
    print(msg)

M = 0.0
while True:
    x, oper, y = input("Enter an equation\n").split()
    try:
        x = float(x) if x != "M" else M
        y = float(y) if y != "M" else M
    except ValueError:
        print("Do you even know what numbers are? Stay focused!")
        continue
    result = calculate(x, oper, y)
    if result == "False":
        continue
    print(result)
    if input("Do you want to store the result? (y / n):\n") == "y":
        if is_one_digit(float(result)):
            if input("Are you sure? It is only one digit! (y / n)\n") == "y":
                if input("Don't be silly! It's just one number! Add to the memory? (y / n)\n") == "y":
                    if input("Last chance! Do you really want to embarrass yourself? (y / n)\n") == "y":
                        M = float(result)
        else:
            M = float(result)
    if input("Do you want to continue calculations? (y / n):\n") == "y":
        continue
    break
