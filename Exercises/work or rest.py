day = input()

day_info = {
    "Monday": "Working day",
    "Tuesday": "Working day",
    "Wednesday": "Working day",
    "Thursday": "Working day",
    "Friday": "Working day",
    "Saturday": "Weekend",
    "Sunday": "Weekend",
    1: "Error"
}

if day in day_info:
    print(day_info.get(day))
else:
    print(day_info[1])