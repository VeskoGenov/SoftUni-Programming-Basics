bought_food = int(input())
food_to_mg = bought_food * 1000

count_eaten_food = 0

eaten_food = input()
while eaten_food != "Adopted":
    eaten_food = int(eaten_food)
    count_eaten_food += eaten_food
    eaten_food = input()

leftovers = abs(food_to_mg - count_eaten_food)
if food_to_mg >= count_eaten_food:
    print(f"Food is enough! Leftovers: {leftovers} grams.")
else:
    print(f"Food is not enough. You need {leftovers} grams more.")