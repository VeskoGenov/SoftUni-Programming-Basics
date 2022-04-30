film_budget = float(input())
statist = int(input())
clothes_cost = float(input())

decor = film_budget * 0.1
clothes_cost_total = clothes_cost * statist

if statist > 150:
    clothes_cost_total = clothes_cost_total * 0.9

total_to_spend = clothes_cost_total + decor

if total_to_spend > film_budget:
    left = total_to_spend - film_budget
    print("Not enough money!")
    print(f"Wingard needs {left:.2f} leva more.")
else:
    left = film_budget - total_to_spend
    print("Action!")
    print(f"Wingard starts filming with {left:.2f} leva left.")