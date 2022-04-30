import math

amount_magnolia = int(input())
amount_ziumbiul = int(input())
amount_roses = int(input())
amount_cactus = int(input())
gift = float(input())

magnolia = 3.25
ziumbiul = 4
roses = 3.50
cactus = 8

total = (amount_magnolia * magnolia) + (amount_ziumbiul * ziumbiul) + (amount_roses * roses) + (amount_cactus * cactus)
taxes = (total * 5) / 100
after_tax = total - taxes

remaining = gift - after_tax

if after_tax < gift:
    print(f"She will have to borrow {math.ceil(remaining)} leva.")
else:
    remaining = after_tax - gift
    print(f"She is left with {math.floor(remaining)} leva.")