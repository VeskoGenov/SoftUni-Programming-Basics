import math

days = int(input())
total_kg_food = float(input())

dog_food = 0
cat_food = 0
biscuits = 0

for days in range(1, days + 1):
    eaten_food_dog = int(input())
    eaten_food_cat = int(input())

    dog_food += eaten_food_dog
    cat_food += eaten_food_cat

    if days % 3 == 0:
        bonus =(eaten_food_cat + eaten_food_dog) * 0.10
        biscuits += bonus

eaten_food = dog_food + cat_food
total_percentage = ((dog_food + cat_food) / total_kg_food) * 100
total_percentage_dog = (dog_food / eaten_food) * 100
total_percentage_cat = (cat_food / eaten_food) * 100

print(f"Total eaten biscuits: {round(biscuits)}gr.")
print(f"{total_percentage:.2f}% of the food has been eaten.")
print(f"{total_percentage_dog:.2f}% eaten from the dog.")
print(f"{total_percentage_cat:.2f}% eaten from the cat.")