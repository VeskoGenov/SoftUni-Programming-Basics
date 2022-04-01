year_fee_to_play = int(input())

#Цена на тренировките за година: 365
#Цена на баскетболните кецове: 365 – 40% = 219
#Цена на баскетболен екип: 219 – 20% = 175.20
#Цена на баскетболна топка: 1 / 4 от 175.20 = 43.80
#Цена на баскетболни аксесоари: 1 /  5 от 43.80 = 8.76
#Обща цена за екипировката: 365 + 219 + 175.20 + 43.80 + 8.76 = 811.76

shoes_cost = (year_fee_to_play * 40) / 100
shoes_cost_total = year_fee_to_play - shoes_cost

clothes_cost = (shoes_cost_total * 20) / 100
clothes_cost_total = shoes_cost_total - clothes_cost

ball_cost = clothes_cost_total / 4
accessory_cost = ball_cost / 5

total_cost = year_fee_to_play + shoes_cost_total + clothes_cost_total + ball_cost + accessory_cost

print(total_cost)
