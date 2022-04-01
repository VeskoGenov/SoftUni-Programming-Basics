# settings
puzzle = 2.60
barbie1 = 3
bear = 4.10
minion = 8.20
kamion4e = 2
discount = 25
rent = 10

# inputs
trip_cost = float(input())
qty_puzzle = int(input())
qty_barbies = int(input())
qty_bears = int(input())
qty_minions = int(input())
qty_kamion4e = int(input())

sum_order = qty_puzzle * puzzle + qty_bears * bear + qty_barbies * barbie1 + qty_minions * minion + qty_kamion4e * kamion4e
qty_ordered = qty_bears + qty_minions + qty_kamion4e + qty_barbies + qty_puzzle


if qty_ordered > 50:
    sum_order = ((sum_order * 25) / 100) - sum_order

rent = (sum_order * 10) / 100
income = sum_order - rent
result = income - trip_cost

if result > trip_cost:
    print(f"Yes! {result} lv left.")
else:
    result = trip_cost - income
    print(f"Not enough money! {result} lv needed.")
