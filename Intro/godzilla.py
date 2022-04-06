project_budget = float(input())
employ = int(input())
clothes = float(input())

cost_decor = project_budget * 0.1
clothes_sum = employ * clothes

if employ > 150:
    clothes_sum = clothes_sum * 0.9

needed_money = cost_decor + clothes_sum
difference = abs(needed_money - project_budget)

if needed_money > project_budget:
    print("Not enough money!")
    print(f"Wingard needs {difference:.2f} leva more.")
else:
    print("Action!")
    print(f"Wingard starts filming with {difference:.2f} leva left.")