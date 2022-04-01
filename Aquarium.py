length = int(input())
width = int(input())
height = int(input())
percentage = float(input()) / 100

aquarium_volume = length * width * height
liters_volume = aquarium_volume / 1000

needed_water_to_fill = liters_volume * (1 - percentage)

print(needed_water_to_fill)
