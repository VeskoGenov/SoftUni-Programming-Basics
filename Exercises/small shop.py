product = input()
city = input()
amount = float(input())

price_info = {
    "Sofia": {
        "coffee": 0.5,
        "water": 0.8,
        "beer": 1.2,
        "sweets": 1.45,
        "peanuts": 1.6
    },
    "Plovdiv": {
        "coffee": 0.4,
        "water": 0.7,
        "beer": 1.15,
        "sweets": 1.3,
        "peanuts": 1.5
    },
    "Varna": {
        "coffee": 0.45,
        "water": 0.7,
        "beer": 1.1,
        "sweets": 1.35,
        "peanuts": 1.55
    }
}

cost = price_info[city][product] * amount
print(f"{cost:.2f}")