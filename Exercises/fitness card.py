available_fiat = float(input())
sex = input()
age = int(input())
sport = input()
cash = 0

sport_info = {
    "m": {
        "Gym": 42,
        "Boxing": 41,
        "Yoga": 45,
        "Zumba": 34,
        "Dances": 51,
        "Pilates": 39
    },
    "f": {
        "Gym": 35,
        "Boxing": 37,
        "Yoga": 42,
        "Zumba": 31,
        "Dances": 53,
        "Pilates": 37
    }
}

if age <= 19:
    cash = sport_info[sex][sport] - (sport_info[sex][sport] * 0.2)
    if available_fiat > cash:
        print(f"You purchased a 1 month pass for {sport}.")
    else:
        needed = abs(cash - available_fiat)
        print(f"You don't have enough money! You need ${needed:.2f} more.")
elif age > 19:
    if available_fiat > sport_info[sex][sport]:
        print(f"You purchased a 1 month pass for {sport}.")
    else:
        needed = abs(available_fiat - sport_info[sex][sport])
        print(f"You don't have enough money! You need ${needed:.2f} more.")

