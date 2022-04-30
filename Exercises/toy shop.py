trip_cost = float(input())
amount_puzzle = int(input())
amount_dolls = int(input())
amount_bears = int(input())
amount_minions = int(input())
amount_trucks = int(input())

toys_info = {
    "puzzle": 2.60,
    "dolls": 3,
    "bears": 4.10,
    "minions": 8.20,
    "truck": 2,
}

total_cost_toys = (toys_info["puzzle"] * amount_puzzle) + (toys_info["dolls"] * amount_dolls) + (toys_info["bears"] * amount_bears) + (toys_info["minions"] * amount_minions) + (toys_info["truck"] * amount_trucks)
toys_qty = amount_trucks + amount_bears + amount_dolls + amount_puzzle + amount_minions

if toys_qty >= 50:
    discount = (total_cost_toys * 25) / 100
    total_cost_toys = total_cost_toys - discount

rent = (total_cost_toys * 10) / 100
total_cost_toys = total_cost_toys - rent

if total_cost_toys >= trip_cost:
    total_cost_toys += - trip_cost
    print(f"Yes! {total_cost_toys:.2f} lv left.")
else:
    total_cost_toys = trip_cost - total_cost_toys
    print(f"Not enough money! {total_cost_toys:.2f} lv needed.")