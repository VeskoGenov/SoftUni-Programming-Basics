week_day = int(input())

if week_day == 1:
    print("Monday")
elif week_day == 2:
    print("Tuesday")
elif week_day == 3:
    print("Wednesday")
elif week_day == 4:
    print("Thursday")
elif week_day == 5:
    print("Friday")
elif week_day == 6:
    print("Saturday")
elif week_day == 7:
    print("Sunday")
elif week_day < 1 or week_day > 7:
    print("Error")
