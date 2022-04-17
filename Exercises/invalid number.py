number = int(input())

if 100 < number < 149:
    print("valid")
elif 1 < number < 100:
    print("invalid")
elif number > 200:
    print("invalid")
else:
    if number < 0:
        print("invalid")

