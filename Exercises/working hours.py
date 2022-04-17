hour = int(input())
week_day = input()

if 10 <= hour <= 18:
    if week_day == "Monday":
        print("open")
    elif week_day == "Tuesday":
        print("open")
    elif week_day == "Wednesday":
        print("open")
    elif week_day == "Thursday":
        print("open")
    elif week_day == "Friday":
        print("open")
    elif week_day == "Saturday":
        if hour > 0:
            print("closed")
    if week_day == "Sunday":
        if hour > 0:
            print("closed")
else:
    print("closed")