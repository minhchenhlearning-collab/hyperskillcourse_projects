import re
from collections import defaultdict
import json 
from datetime import datetime

def error_checking(document):
    # Check for type, pattern and requirements
    errors = {"bus_id": 0, "stop_id": 0, "stop_name": 0,
              "next_stop":0, "stop_type":0, "a_time":0}
    a_time_pattern = r"(^[01][0-9]|2[0-3]):[0-5][0-9]"
    stop_name_pattern = r"^[A-Z][a-z]*( [A-Z][a-z]*)* (Road|Avenue|Boulevard|Street)$"
    for bus in document:
        for info, value in bus.items():
            if info in ["bus_id", "stop_id", "next_stop"] and (not isinstance(value, int) or value == ""):
                errors[info] += 1
            elif info in ["stop_name", "a_time"]:
                if not isinstance(value, str) or value == "":
                    errors[info] += 1
                else:
                    if info == "stop_name" and not re.match(stop_name_pattern, value):
                        print(value)
                        errors[info] += 1
                    elif info == "a_time" and not re.match(a_time_pattern, value):
                        errors[info] += 1
            elif info == "stop_type":
                if not isinstance(value, str) or value not in "SOF":
                    errors[info] += 1
    # Checking if time is increasing
    bus_id_lst = list(set([bus["bus_id"] for bus in document]))
    for bus in bus_id_lst:
        for i in range(len(document) - 1):
            curr_bus = document[i]["bus_id"]
            next_bus = document[i+1]["bus_id"]
            if curr_bus == bus == next_bus:
                curr_time = datetime.strptime(document[i]["a_time"], "%H:%M")
                next_time = datetime.strptime(document[i+1]["a_time"], "%H:%M")
                if curr_time > next_time:
                    errors["a_time"] += 1
                    break
    return errors

def error_info(lst):
    total_error = sum(lst.values())
    print(f"Type and required field validation: {total_error} errors")
    for error, times in lst.items():
        print(f"{error}: {times}")


def num_stops(document):
    bus_line = defaultdict(list)
    for bus in document:
        bus_line[bus["bus_id"]].append(bus["stop_name"])
    return bus_line

def num_stops_info(line):
    print("")
    for bus, stops in line.items():
        print(f"bus_id: {bus} stops: {len(stops)}")

def stops_info(start, trans, finish, demand):
    print("")
    print(f"Start stops: {len(start)} {start}")
    print(f"Transfer stops: {len(trans)} {trans}")
    print(f"Finish stops: {len(finish)} {finish}")
    print(f"On demand stops: {len(demand)} {demand}")

def stops_check(document):
    bus_line = dict(num_stops(document)) # All stops for each bus_id
    start_stops_line = defaultdict(list)
    finish_stops_line = defaultdict(list)
    demand_stops = []
    # Check if a bus has no finish or start stop
    bus_type = document[0]["bus_id"]
    for bus in document:
        curr_bus = bus["bus_id"]
        if curr_bus != bus_type:
            if (not start_stops_line[bus_type] or not finish_stops_line[bus_type]):
                num_stops_info(bus_line)
                print(f"There is no start or end stop for the line: {bus_type}")
                return
            else:
                bus_type = curr_bus
        # Getting finish and start stops dicts
        if bus["stop_type"] == "F":
            finish_stops_line[curr_bus].append(bus["stop_name"])
        elif bus["stop_type"] == "S":
            start_stops_line[curr_bus].append(bus["stop_name"])
        elif bus["stop_type"] == "O":
            demand_stops.append(bus["stop_name"])
        # Check if the final bus has no finish or start stop
        if document.index(bus) == (len(document) -1):
            if (not start_stops_line[bus_type] or not finish_stops_line[bus_type]):
                num_stops_info(bus_line)
                print(f"There is no start or end stop for the line: {bus_type}")
                return
    # Get list of all stop types
    start_stops = sorted(list(set([name for stop in list(start_stops_line.values()) for name in stop])))
    finish_stops = sorted(list(set([name for stop in list(finish_stops_line.values()) for name in stop])))
    transfer_stops = [stop for trans in list(bus_line.values()) for stop in trans]
    transfer_stops = sorted(list(set(filter(lambda x: transfer_stops.count(x) > 1, transfer_stops))))
    true_demand_stops = []
    special_stops = [finish_stops, start_stops, transfer_stops]
    for d_stop in demand_stops:
        if not any(d_stop in stop for stop in special_stops):
            true_demand_stops.append(d_stop)
    num_stops_info(bus_line)
    stops_info(start_stops, transfer_stops, finish_stops, true_demand_stops)


document = json.loads(input())
bus = document[0]["bus_id"]
error_lst = error_checking(document)
error_info(error_lst)
stops_check(document)