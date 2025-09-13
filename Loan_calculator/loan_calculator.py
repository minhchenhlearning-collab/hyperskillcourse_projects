import math
import argparse

def command_checking():
    args_dict = vars(args)
    not_passed = 0
    if not args.type or args.type not in ["diff", "annuity"]:
        print("Incorrect parameters")
        return False
    elif args.type == "diff" and args.payment:
        print("Incorrect parameters")
        return False
    elif not args.interest:
        print("Incorrect parameters")
        return False
    if any([x is not None and x < 0 for x in [payment, principal, periods, interest]]):
        print("Incorrect parameters")
        return False
    if [payment, principal, periods, interest, type].count(None) > 1:
        print("Incorrect parameters")
        return False
    return True
def annuity():
    global payment, periods, principal, interest
    i = (1/12)*(interest/100)
    if not args.periods:
        periods = math.ceil(math.log(payment / (payment - i * principal),(1+i)))
        years = periods // 12
        if years != 0:
            months = periods - (12 * years)
            if months != 0:
                print(f"It will take {years} years and {months} months to repay this loan!")
            else:
                print(f"It will take {years} years to repay this loan!")
        else:
            months = periods
            print(f"It will take {months} months to repay this loan!")
    if not args.payment:
        payment = math.ceil(principal * (i * math.pow(1+i, periods) / (math.pow(1+i, periods) - 1)))
        print(f"Your monthly payment = {payment}!")
    if not args.principal:
        principal = round(payment / ((i * math.pow(1+i, periods)) / (math.pow(i+1, periods) - 1)))
        print(f"Your loan principal = {principal}!")
    overpayment = payment * periods - principal
    print(f"Overpayment = {overpayment}")

def set_up():        
    parser = argparse.ArgumentParser()
    parser.add_argument("--payment", type=float)
    parser.add_argument("--principal", type=int)
    parser.add_argument("--periods", type=int)
    parser.add_argument("--interest", type=float)
    parser.add_argument("--type", type=str)
    args = parser.parse_args()
    return args

def diff():
    global payment, periods, principal, interest
    i = (1/12)*(interest/100)
    total_payment = 0
    for month in range(1, periods+1):
        payment = math.ceil(principal / periods + i * (principal - ((principal * (month - 1)) / periods)))
        print(f"Month {month}: payment is {payment}")   
        total_payment += payment
    print("")
    print(f"Overpayment = {total_payment - principal}")

args = set_up()
interest, payment, principal, periods, type = args.interest, args.payment, args.principal, args.periods, args.type
if command_checking():
    if args.type == "annuity":
        annuity()
    elif args.type == "diff":
        diff()
