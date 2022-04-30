import math
x = int(input())
y = float(input())
z = int(input())
workers = int(input())
wine_apart = 0.40
needed_kg_per_liter = 2.5

grapes_total = x * y
production_wine = (grapes_total * wine_apart) / needed_kg_per_liter


if production_wine >= z:
    wine_left = production_wine - z
    wine_per_worker = wine_left / workers
    print(f"Good harvest this year! Total wine: {math.floor(production_wine)} liters.")
    print(f"{math.ceil(wine_left)} liters left -> {math.ceil(wine_per_worker)} liters per person.")
else:
    wine = abs(production_wine - z)
    print(f"It will be a tough winter! More {math.floor(wine)} liters wine needed.")