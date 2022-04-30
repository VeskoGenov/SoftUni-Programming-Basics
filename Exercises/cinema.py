week_day = input()

ticket_info = {
    "Monday": 12,
    "Tuesday": 12,
    "Wednesday": 14,
    "Thursday": 14,
    "Friday": 12,
    "Saturday": 16,
    "Sunday": 16,
}

if week_day in ticket_info:
    print(ticket_info.get(week_day))