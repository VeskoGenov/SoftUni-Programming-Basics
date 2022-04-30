fruit = input()
set_size = input()
set_ordered = int(input())

set_info = {
    "small": {
        "Watermelon": 56,
        "Mango": 36.66,
        "Pineapple": 42.10,
        "Raspberry": 20,
        "set": 2
    },
    "big": {
        "Watermelon": 28.70,
        "Mango": 19.60,
        "Pineapple": 24.80,
        "Raspberry": 15.20,
        "set": 5
    },
    "Watermelon": "Watermelon",
    "Mango": "Mango",
    "Pineapple": "Pineapple",
    "Raspberry": "Raspberry",
}

if set_size == "small":
    set_ordered = set_ordered * set_info["small"]["set"]
elif set_size == "big":
    set_ordered = set_ordered * set_info["big"]["set"]

if fruit in set_info and set_size in set_info:
    cost_set = set_ordered * set_info[set_size][fruit]

if 400 < cost_set <= 1000:
    discount = (cost_set * 15) / 100
    cost_set = cost_set - discount
elif cost_set > 1000:
    cost_set = cost_set / 2

print(f"{cost_set:.2f} lv.")
