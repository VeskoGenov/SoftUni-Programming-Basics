chicken_menu = 10.35
fish_menu = 12.40
vegan_menu = 8.15
delivery = 2.50
desert = 0.2

qty_chicken_ordered = int(input())
qty_fish_ordered = int(input())
qty_vegan_ordered = int(input())

sum_ordered_chickens = qty_chicken_ordered * chicken_menu
sum_ordered_fish = qty_fish_ordered * fish_menu
sum_ordered_vegans = qty_vegan_ordered * vegan_menu
total_cost_order = sum_ordered_vegans + sum_ordered_fish + sum_ordered_chickens
desert_cost = (total_cost_order * 20) / 100

total_to_pay = total_cost_order + desert_cost + delivery

print(total_to_pay)