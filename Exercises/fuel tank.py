fuel_type = input()
liters = float(input())
fuel_list = ["diesel", "gasoline", "gas"]
fuel_type = fuel_type.lower()


if fuel_type in fuel_list and liters < 25:
    print(f"Fill your tank with {fuel_type}!")
elif fuel_type in fuel_list and liters >= 25:
    print(f"You have enough {fuel_type}.")
else:
    print("Invalid fuel!")