cost_trip = float(input())
puzzle = int(input())
barbies = int(input())
bears = int(input())
minions = int(input())
kamion4e = int(input())

cost_toys = puzzle * 2.6 + barbies * 3 + bears * 4.1 + minions * 8.2 + kamion4e * 2
quantity = puzzle + barbies + bears + minions + kamion4e

if quantity > 50:
    discount = ((cost_toys * 25) / 100)
    cost_toys = cost_toys - discount

rent = (cost_toys * 10) / 100

income = cost_toys - rent
income = income - cost_trip
if income > cost_trip:

    print(f"Yes! {income:.2f} lv left.")
else:
    print(f"Not enough money! {abs(income):.2f} lv needed.")
