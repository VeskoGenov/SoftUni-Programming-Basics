change = float(input())

coins_count = 0


while change > 0:
    if change - 1:
        coins_count += 1
        change -= 1

    if change - 0.2:
        coins_count += 1
        change -= 0.2

    if change - 0.02:
        coins_count += 1
        change -= 0.02

    if change - 0.01:
        coins_count += 1
        change -= 0.01

    print(coins_count)
    break