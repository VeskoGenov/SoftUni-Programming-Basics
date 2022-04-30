kilometers = float(input())
day = input()

taxi_start_price = 0.70
taxi_day = 0.79
taxi_night = 0.90
bus_price = 0.09
train_price = 0.06
cost = 0

if kilometers < 20:
    if day == "day":
        cost = (kilometers * taxi_day) + taxi_start_price
    else:
        cost = (kilometers * taxi_night) + taxi_start_price
elif kilometers < 100:
    cost = kilometers * bus_price
elif kilometers >= 100:
    cost = kilometers * train_price

print(f"{cost:.2f}")