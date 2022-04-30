food = input()

# •	Плодовете "fruit" имат следните възможни стойности:  banana, apple, kiwi, cherry, lemon и grapes;
# •	Зеленчуците "vegetable" имат следните възможни стойности:  tomato, cucumber, pepper и carrot;
# •	Всички останали са "unknown".


food_info = {
    "banana": "fruit",
    "apple": "fruit",
    "kiwi": "fruit",
    "cherry": "fruit",
    "lemon": "fruit",
    "grapes": "fruit",
    "tomato": "vegetable",
    "cucumber": "vegetable",
    "pepper": "vegetable",
    "carrot": "vegetable",
    1: "unknown"
}

if food in food_info:
    print(food_info.get(food))
else:
    print(food_info[1])