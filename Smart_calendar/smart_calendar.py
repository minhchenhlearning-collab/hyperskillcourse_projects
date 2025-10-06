from datetime import datetime
from dateutil import parser
import json

def write_to_file(lst):
    with open("data.txt", 'a+') as file:
        for entry in lst:
            json.dump(entry, file)
            file.write("\n")

def get_string_note(obj):
    pattern = "%Y-%m-%d %H:%M"
    now = datetime.now()
    remain_time = datetime.strptime(obj["date"], pattern) - now
    day = remain_time.days
    hour = remain_time.seconds // 3600
    minute = ((remain_time.seconds - (hour * 3600)) // 60) + 1
    if minute == 60:
        minute = 0
        hour += 1
    if hour == 24:
        hour = 0
        day += 1
    return f'Note: "{obj["text"]}" - {day} day(s), {hour} hour(s), {minute} minute(s)'

def get_next_birth(birth_obj):
    pattern = "%Y-%m-%d"
    now = datetime.now()
    birthday = datetime.strptime(birth_obj, pattern)
    birthday = birthday.replace(year=now.year)
    if birthday <= now:
        birthday = birthday.replace(year=(now.year + 1))
    return birthday

def get_string_birth(obj):
    pattern = "%Y-%m-%d"
    now = datetime.now().date()
    birthday = datetime.strptime(obj["birth_day"], pattern).date()
    age = (now.year - birthday.year)
    birthday = birthday.replace(year=now.year)
    if birthday <= now:
        age += 1
        birthday = birthday.replace(year=(now.year + 1))
    rem_days = (birthday - now).days
    return f'Birthday: "{obj["text"]} (turns {age})" - {rem_days} day(s)'

def check_birth_format(date, pattern):
    try:
        parser.parse(date)
        datetime.strptime(date, pattern)
    except parser.ParserError:
        print("Incorrect date or time values")
        return False
    except ValueError:
        print("Incorrect format")
        return False
    return True

def get_note_type():
    while True:
        note_type = input("Specify type (note, birthday): ")
        if note_type not in ["note", "birthday"]:
            print("Incorrect type")
            continue
        return note_type

def get_num_note(type):
    while True:
        try:
            if type == "note":
                print("How many notes would you like to add: ", end="")
            else:
                print("How many dates of birth would you like to add: ", end="")
            num_note = int(input())
            if num_note <= 0:
                print("Incorrect number")
                continue
            return num_note
        except ValueError:
            print("Incorrect number")
            continue

def add():
    note_lst = []
    birth_lst = []
    note_type = get_note_type()
    num_note = get_num_note(note_type)
    if note_type == "note":
        pattern = "%Y-%m-%d %H:%M"
        for i in range(1, num_note+1):
            while True:
                date = input(f'{i}. Enter datetime in "YYYY-MM-DD HH:MM" format: ')
                if check_birth_format(date, pattern):
                    break
            note = input("Enter text: ")
            note_lst.append({"date": date, "text": note, "type": "note"})
        for note in note_lst:
            print(get_string_note(note))
        write_to_file(note_lst)
    elif note_type == "birthday":
        pattern = "%Y-%m-%d"
        for i in range(1, num_note+1):
            while True:
                date = input(f'{i}. Enter date of birth in "YYYY-MM-DD" format: ')
                if check_birth_format(date, pattern):
                    break
            name = input("Enter name: ")
            birth_lst.append({"date": get_next_birth(date).strftime("%Y-%m-%d"), "text": name,
                              "type": "birthday", "birth_day": date})
        for birth in birth_lst:
            print(get_string_birth(birth))
        write_to_file(birth_lst)

def get_view_command():
    while True:
       v_command = input("Specify filter (all, date, text, birthdays, notes, sorted): ")
       if v_command not in ["all", "date", "text", "birthdays", "notes", "sorted"]:
           print("Incorrect filter")
           continue
       return v_command

def parse_date(date):
    while True:
        for pattern in ["%Y-%m-%d", "%Y-%m-%d %H:%M"]:
            try:
                return datetime.strptime(date, pattern)
            except ValueError:
                continue

def view():
   to_display = []
   try:
       with open("data.txt", "r") as f:
           all_entries = [json.loads(line) for line in f]
   except FileNotFoundError:
        all_entries = []
   v_command = get_view_command()
   if v_command == "all" or v_command == "birthdays":
       for entry in all_entries:
           if entry["type"] == "birthday":
               to_display.append(entry)
   if v_command == "all" or v_command == "notes":
       for entry in all_entries:
           if entry["type"] == "note":
               to_display.append(entry)
   elif v_command == "date":
       pattern = "%Y-%m-%d"
       while True:
           date = input('Enter date in "YYYY-MM-DD" format: ')
           if check_birth_format(date, pattern):
               break
       filter_date = datetime.strptime(date, pattern).date()
       for entry in all_entries:
           if entry["type"] == "note":
               if datetime.strptime(entry["date"], "%Y-%m-%d %H:%M").date() == filter_date:
                   to_display.append(entry)
           elif entry["type"] == "birthday":
               if datetime.strptime(entry["birth_day"], "%Y-%m-%d").date().month == filter_date.month \
               and datetime.strptime(entry["birth_day"], "%Y-%m-%d").date().day == filter_date.day:
                   to_display.append(entry)
   elif v_command == "text":
       filter_text = input("Enter text: ").lower()
       for entry in all_entries:
           if filter_text in entry["text"].lower():
               to_display.append(entry)
   elif v_command == "sorted":
       to_display = sorted(all_entries, key=lambda x: (parse_date(x["date"]), x["text"]))
       while True:
           print("Specify way (ascending, descending): ", end="")
           sort_type = input()
           if sort_type not in ["ascending", "descending"]:
               print("Incorrect way")
               continue
           break
       if sort_type == "descending":
           to_display = to_display[::-1]
   for entry in to_display:
       print(get_string_note(entry) if entry["type"] == "note" else get_string_birth(entry))

def delete():
   try:
       with open("data.txt", "r") as f:
            all_entries = [json.loads(line) for line in f]
   except FileNotFoundError:
       all_entries = []
   for i, entry in enumerate(all_entries, 1):
       print(f"{i}. ", end="")
       print(get_string_note(entry) if entry["type"] == "note" else get_string_birth(entry))
   ids_delete = [i for i in input("Enter ids:").split(",") if i.isnumeric()]
   ids_delete = sorted(list(map(int, ids_delete)), reverse=True)
   to_delete = [line for i, line in enumerate(all_entries, 1) if i in ids_delete]
   with open("data.txt", "w") as f:
       for entry in all_entries:
           if entry not in to_delete:
                json.dump(entry, f)
                f.write("\n")

# --- Main
curr_date = datetime.now()
print(f"Current date and time:\n{curr_date.strftime("%Y-%m-%d %H:%M")}")
while True:
    while True:
        command = input("Enter the command (add, view, delete, exit): ")
        if command not in ["add", "view", "delete", "exit"]:
            print("Incorrect command")
            continue
        break
    if command == "exit":
        print("Goodbye!")
        break
    elif command == "add":
        add()
    elif command == "view":
        view()
    elif command == "delete":
        delete()
