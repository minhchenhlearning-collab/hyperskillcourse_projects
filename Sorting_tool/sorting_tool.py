import argparse
import math
from collections import Counter

def print_info(lst, type=None):
    if not output_file:
        if sort == "natural":
            print(f"Total {type}: {length}.")
            if type in ["numbers", "words"]:
                print(f"Sorted data: {lst}")
            else:
                print(f"Sorted data:")
                for data in lst:
                    print(data)
        else:
            print(f"Total numbers: {length}.")
            for num, count in lst:
                print(f"{num}: {count} time(s), {math.floor(count/length*100)}%")
    else:
        with open(output_file, "w") as file:
            if sort == "natural":
                file.write(f"Total {type}: {length}.\n")
                if type in ["numbers", "words"]:
                    file.write(f"Sorted data: {lst}")
                else:
                    file.write("Sorted data:\n")
                    for data in lst:
                        file.write(f"{data}\n")  
            else:
                file.write(f"Total numbers: {length}.\n")
                for num, count in lst:
                    file.write(f"{num}: {count} time(s), {math.floor(count/length*100)}%\n")

def natural(data_type):
    global nums, length
    if data_type == "long":
        nums = list(map(int, nums))
        nums.sort()
        nums_str = " ".join(str(num) for num in nums)
        print_info(nums_str, "numbers")
    elif data_type == "word":
        nums.sort()
        nums_str = " ".join(nums)
        print_info(nums_str, "words")
    elif data_type == "line":
        nums.sort()
        print_info(nums, "lines")

def count(data_type):
    global nums, length
    if data_type == "long":
        nums = list(map(int, nums))
    nums.sort()
    counter = dict(Counter(nums))
    counter = sorted(counter.items(), key=lambda item: item[1])
    print_info(counter)

def error_check():
    global type, sort
    if type == False:
        print("No data type defined!")
        return True
    elif sort == False:
        print("No sorting type defined!")
        return True
    return False

def input_check():
    global nums
    if type == "long":
        not_numeric = []
        for num in nums:
            if num.isalpha():
                not_numeric.append(num)
                print(f'"{num}" is not a long. It will be skipped.')
        for num in not_numeric:
            nums.remove(num)

parser = argparse.ArgumentParser()
parser.add_argument("-dataType", nargs="?", const=False)
parser.add_argument("-sortingType", nargs="?", const=False, default="natural")
parser.add_argument("-inputFile")
parser.add_argument("-outputFile")
args, unknown_args = parser.parse_known_args()
input_file = args.inputFile
output_file = args.outputFile
type = args.dataType
sort = args.sortingType
if unknown_args:
    for arg in unknown_args:
        print(f'"{arg}" is not valid parameter. It will be skipped.')
if not error_check():
    nums = []
    if not input_file:
        while True:
            try:
                data = input()
                if type == "line":
                    nums.append(data)
                else:
                    nums += data.split()
            except EOFError:
                break
    else:
        with open(input_file, "r") as file:
            for line in file:
                if type == "line":
                    nums.append(line)
                else:
                    nums += line.split()   
    input_check()
    length = len(nums)
    if sort == "byCount":
        count(type)
    elif sort == "natural":
        natural(type)
