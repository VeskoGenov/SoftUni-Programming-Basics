budget_people = int(input())
season = input()
fishers = int(input())
price = 0
final_cost = 0
seasons_discount = ["Spring", "Summer", "Winter"]

if season == "Summer":
    price = 4200
    if fishers <= 6:
        discount = (price * 10) / 100
        price = price - discount
    elif 7 <= fishers <= 11:
        discount = (price * 15) / 100
        price = price - discount
    elif fishers > 12:
        discount = (price * 25) / 100
        price = price - discount

if season == "Autumn":
    price = 4200
    if fishers <= 6:
        discount = (price * 10) / 100
        price = price - discount
    elif 7 <= fishers <= 11:
        discount = (price * 15) / 100
        price = price - discount
    elif fishers > 12:
        discount = (price * 25) / 100
        price = price - discount

elif season == "Spring":
    price = 3000
    if fishers <= 6:
        discount = (price * 10) / 100
        price = price - discount
    elif 7 <= fishers <= 11:
        discount = (price * 15) / 100
        price = price - discount
    elif fishers > 12:
        discount = (price * 25) / 100
        price = price - discount

if season == "Winter":
    price = 2600
    if fishers <= 6:
        discount = (price * 10) / 100
        price = price - discount
    elif 7 <= fishers <= 11:
        discount = (price * 15) / 100
        price = price - discount
    elif fishers > 12:
        discount = (price * 25) / 100
        price = price - discount

if season in seasons_discount:
    if fishers % 2 == 0:
        discount = (price * 5) / 100
        discount_tot = price - discount

final_cost = budget_people - price

if final_cost >= 0:
    print(f"Yes! You have {final_cost:.2f} leva left.")
else:
    print(f"Not enough money! You need {(-1)*final_cost:.2f} leva.")