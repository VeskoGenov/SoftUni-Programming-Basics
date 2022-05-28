bottle_washing_fluid = int(input())

amount_of_washing_fluid = 750 * bottle_washing_fluid

cycle_dishes = 0
pots_washed = 0
dishes_washed = 0

dishes_to_wash = input()

while True:
    if dishes_to_wash == "End":
        break
    dishes_to_wash = int(dishes_to_wash)
    cycle_dishes += 1

    if not cycle_dishes % 3 == 0:
            fluid_used = dishes_to_wash * 5
            amount_of_washing_fluid -= fluid_used
            dishes_washed += dishes_to_wash

    if cycle_dishes % 3 == 0:
            fluid_used = dishes_to_wash * 15
            amount_of_washing_fluid -= fluid_used
            pots_washed += dishes_to_wash

    if amount_of_washing_fluid <= 0:
        print(f"Not enough detergent, {abs(amount_of_washing_fluid)} ml. more necessary!")

    dishes_to_wash = input()

if dishes_to_wash == "End" and amount_of_washing_fluid >= 0:
    print("Detergent was enough!")
    print(f"{dishes_washed} dishes and {pots_washed} pots were washed.")
    print(f"Leftover detergent {amount_of_washing_fluid} ml.")
else:
    print(f"Not enough detergent, {abs(amount_of_washing_fluid)} ml. more necessary!")
