import math

form = input()

square = "square"
rectangle = "rectangle"
circle = "circle"
triangle = "triangle"

if form == square:
    area_a = float(input())
    cal = area_a * area_a
elif form == rectangle:
    area_a = float(input())
    area_b = float(input())
    cal = area_a * area_b
elif form == circle:
    radius = float(input())
    cal = radius * radius * math.pi
elif form == triangle:
    area_a = float(input())
    area_b = float(input())
    cal = (area_a * area_b) / 2

print(f"{cal:.3f}")