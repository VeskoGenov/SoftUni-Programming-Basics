x = float(input())
y = float(input())
h = float(input())

#steni
lateral = x * y
windows_size = 1.5 * 1.5
laterals = 2 * (lateral - windows_size)
front_rear_wall = ((x * x) * 2) - (1.2 * 2)
total_size = laterals + front_rear_wall

#pokriv
top_roof = 2 * (x * y)
front_roof = 2 * (x * h / 2)
total_size_roof = top_roof + front_roof

#dye
green_dye = total_size / 3.4
red_dye = total_size_roof / 4.3

print(f"{green_dye:.2f}")
print(f"{red_dye:.2f}")