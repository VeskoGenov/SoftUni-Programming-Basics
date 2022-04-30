budget = float(input())
season = input().lower()

if budget <= 100:
    if season == "summer":
        price = budget * 0.3
    elif season == "winter":
        price = budget * 0.7
    place_to_visit = "Bulgaria"
elif budget <= 1000:
    if season == "summer":
        price = budget * 0.4
    elif season == "winter":
        price = budget * 0.8
    place_to_visit = "Balkans"
else:
    price = budget * 0.9
    place_to_visit = "Europe"

if season == "summer":
    place_to_stay = "Camp"
else:
    place_to_stay = "Hotel"

if budget <= 100:
    print(f"Somewhere in {place_to_visit}")
    print(f"{place_to_stay} - {price:.2f}")
elif budget <= 1000:
    print(f"Somewhere in {place_to_visit}")
    print(f"{place_to_stay} - {price:.2f}")
else:
    print(f"Somewhere in {place_to_visit}")
    print(f"Hotel - {price:.2f}")

