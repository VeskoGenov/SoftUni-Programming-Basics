budget_people = int(input())
season = input()
fishers = int(input())
price = 0
final_cost = 0

if season == "Summer" or season == "Autumn":
    price = 4200
elif season == "Spring":
    price = 3000
else:
    price = 2600

if fishers <= 6:
    discount = price * 0.9
elif fishers >= 12:
    discount = price * 0.75
else:
    discount = price * 0.85


if (fishers % 2 == 0 and season != "Autumn"):
     discount *= .95

final_cost = budget_people - discount

if final_cost >= 0:
    print(f"Yes! You have {final_cost:.2f} leva left.")
else:
    print(f"Not enough money! You need {((-1)*final_cost):.2f} leva.")