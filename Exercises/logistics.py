number_of_loads = int(input())

total_tons_loads = 0
three_tons = 0
from_four_to_eleven = 0
twelve_to_more = 0
bus = 0
truck = 0
train = 0

for number_of_loads in range(1, number_of_loads + 1):
    tons_per_load = int(input())
    total_tons_loads += tons_per_load

    if tons_per_load <= 3:
        three_tons += tons_per_load * 200
        bus += tons_per_load
    elif 4 <= tons_per_load <= 11:
        truck += tons_per_load
        from_four_to_eleven += tons_per_load * 175
    elif tons_per_load >= 12:
        train += tons_per_load
        twelve_to_more += tons_per_load * 120

average_price_per_ton = (three_tons + from_four_to_eleven + twelve_to_more) / total_tons_loads

print(f"{average_price_per_ton:.2f}")
print(f"{(bus / total_tons_loads) * 100:.2f}%")
print(f"{(truck / total_tons_loads) * 100:.2f}%")
print(f"{(train / total_tons_loads) * 100:.2f}%")