hour = int(input())
week_day = input()

week_info = {
    "Monday": "open",
    "Tuesday": "open",
    "Wednesday": "open",
    "Thursday": "open",
    "Friday": "open",
    "Saturday": "open",
    "Sunday": "closed",
    "closed": "closed"
}

if week_day in week_info and (10 <= hour <= 18):
    print(week_info.get(week_day))
else:
    print(week_info["closed"])