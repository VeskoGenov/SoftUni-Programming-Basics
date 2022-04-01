number = int(input())
below = "Less than 100"
middle = "Between 100 and 200"
after = "Greater than 200"


if number < 100:
    print(below)
elif number < 201:
    print(middle)
else:
    print(after)
