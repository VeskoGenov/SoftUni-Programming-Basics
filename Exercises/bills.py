month = int(input())

# •	1ви ред: "Electricity: {ток за всички месеци} lv"
# •	2ри ред: "Water: {вода за всички месеци} lv"
# •	3ти ред: "Internet: {интернет за всички месеци} lv"
# •	4ти ред: "Other: {други за всички месеци} lv"
# •	5ти ред: "Average: {средно всички разходи за месец} lv"

electricity = 0
water = 0
internet = 0
other = 0
average = 0

for month in range(1, month + 1):
    electricity_bill = float(input())

    electricity += electricity_bill
    water += 20
    internet += 15

    others_calc = electricity_bill + 20 + 15
    account = ((others_calc * 20) / 100) + others_calc
    other += account

print(f"Electricity: {electricity:.2f} lv")
print(f"Water: {water:.2f} lv")
print(f"Internet: {internet:.2f} lv")
print(f"Other: {other:.2f} lv")
print(f"Average: {(electricity + water + internet + other) / month:.2f} lv")