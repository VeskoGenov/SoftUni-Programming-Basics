import math

length = float(input())
width = float(input())
corridor = 100
desk_width = 70
desk_length = 120

width = math.floor(((width * 100) - corridor) / desk_width)
length = math.floor(((length * 100) / desk_length))
other = 3

total_space = width * length - other
print(total_space)
