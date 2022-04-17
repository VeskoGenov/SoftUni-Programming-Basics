flower_type = input()
amount_flowers = int(input())
budget = int(input())

if flower_type == "Roses":
    flowers_cost = amount_flowers * 5
    if amount_flowers > 80:
        discount = (flowers_cost * 10) / 100
        flowers_cost = abs(discount - flowers_cost)
    if flowers_cost > budget:
        needed = abs(flowers_cost - budget)
        print(f"Not enough money, you need {needed:.2f} leva more.")
    else:
        remaining = abs(flowers_cost - budget)
        print(f"Hey, you have a great garden with {amount_flowers} {flower_type} and {remaining:.2f} leva left.")

elif flower_type == "Dahlias":
    flowers_cost = amount_flowers * 3.80
    if amount_flowers > 90:
        discount = (flowers_cost * 15) / 100
        flowers_cost = abs(discount - flowers_cost)
    if flowers_cost > budget:
        needed = abs(flowers_cost - budget)
        print(f"Not enough money, you need {needed:.2f} leva more.")
    else:
        remaining = abs(flowers_cost - budget)
        print(f"Hey, you have a great garden with {amount_flowers} {flower_type} and {remaining:.2f} leva left.")

elif flower_type == "Tulips":
    flowers_cost = amount_flowers * 2.80
    if amount_flowers > 80:
        discount = (flowers_cost * 15) / 100
        flowers_cost = abs(discount - flowers_cost)
    if flowers_cost > budget:
        needed = abs(flowers_cost - budget)
        print(f"Not enough money, you need {needed:.2f} leva more.")
    else:
        remaining = abs(flowers_cost - budget)
        print(f"Hey, you have a great garden with {amount_flowers} {flower_type} and {remaining:.2f} leva left.")

elif flower_type == "Narcissus":
    flowers_cost = amount_flowers * 3
    if amount_flowers < 120:
        discount = (flowers_cost * 15) / 100
        flowers_cost = abs(discount + flowers_cost)
    if flowers_cost > budget:
        needed = abs(flowers_cost - budget)
        print(f"Not enough money, you need {needed:.2f} leva more.")
    else:
        remaining = abs(flowers_cost - budget)
        print(f"Hey, you have a great garden with {amount_flowers} {flower_type} and {remaining:.2f} leva left.")

elif flower_type == "Gladiolus":
    flowers_cost = amount_flowers * 2.50
    if amount_flowers < 80:
        discount = (flowers_cost * 20) / 100
        flowers_cost = abs(discount + flowers_cost)
    if flowers_cost > budget:
        needed = abs(flowers_cost - budget)
        print(f"Not enough money, you need {needed:.2f} leva more.")
    else:
        remaining = abs(flowers_cost - budget)
        print(f"Hey, you have a great garden with {amount_flowers} {flower_type} and {remaining:.2f} leva left.")
