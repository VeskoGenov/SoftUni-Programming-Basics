fruit = input()
week_day = input()
quantity = float(input())
price = 0



fruits_info = {
    "work days": {
        "banana": 2.5,
        "apple": 1.2,
        "orange": 0.85,
        "grapefruit": 1.45,
        "kiwi": 2.7,
        "pineapple": 5.5,
        "grapes": 3.85
    },
    "weekend": {
        "banana": 2.7,
        "apple": 1.25,
        "orange": 0.9,
        "grapefruit": 1.6,
        "kiwi": 3,
        "pineapple": 5.6,
        "grapes": 4.2
    }
}

days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
weekend = ["Saturday", "Sunday"]

if week_day in days and fruit in fruits_info["work days"]:
    price = fruits_info["work days"].get(fruit) * quantity
    print(f"{price:.2f}")
elif week_day in weekend and fruit in fruits_info["weekend"]:
    price = fruits_info["weekend"].get(fruit) * quantity
    print(f"{price:.2f}")
else:
    print("error")