number1 = int(input())
number2 = int(input())
operator = input()

if number1 == 0:
    print(f"Cannot divide {number2} by zero")
elif number2 == 0:
    print(f"Cannot divide {number1} by zero")

elif operator == "+":
    total = number1 + number2
    if total % 2 == 0:
        print(f"{number1} + {number2} = {total} - even")
    else:
        print(f"{number1} + {number2} = {total} - odd")

elif operator == "-":
    total = number1 - number2
    if total % 2 == 0:
        print(f"{number1} - {number2} = {total} - even")
    else:
        print(f"{number1} - {number2} = {total} - odd")

elif operator == "*":
    total = number1 * number2
    if total % 2 == 0:
        print(f"{number1} * {number2} = {total} - even")
    else:
        print(f"{number1} * {number2} = {total} - odd")

elif operator == "/":
    total = number1 / number2
    print(f"{number1} / {number2} = {total:.2f}")

elif operator == "%":
    total = number1 % number2
    print(f"{number1} % {number2} = {total}")