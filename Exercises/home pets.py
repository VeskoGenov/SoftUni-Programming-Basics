import math

amount_days = int(input())
food_left_kg = int(input())
dog_food_daily = float(input())
cat_food_daily = float(input())
turtle_food_daily = float(input())


needed_dog_food = amount_days * dog_food_daily
needed_cat_food = amount_days * cat_food_daily
needed_turtle_food = (amount_days * turtle_food_daily) / 1000

total_food = needed_turtle_food + needed_cat_food + needed_dog_food
food_left = food_left_kg - total_food

if total_food <= food_left_kg:
    print(f"{math.floor(food_left)} kilos of food left.")
else:
    total_food = total_food - food_left_kg
    print(f"{math.ceil(total_food)} more kilos of food are needed.")