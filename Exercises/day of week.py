number = int(input())

week_info = {
    1: "Monday",
    2: "Tuesday",
    3: "Wednesday",
    4: "Thursday",
    5: "Friday",
    6: "Saturday",
    7: "Sunday"
}

if number in week_info:
    print(week_info.get(number))
else:
    print("Error")