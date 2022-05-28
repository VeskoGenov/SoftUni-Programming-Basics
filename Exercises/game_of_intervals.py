game_moves = int(input())

from_zero_to_nine = 0
from_ten_to_nineteen = 0
from_twenty_to_twenties = 0
from_thirties_to_thirty_nine = 0
from_fourths_to_fifty = 0
invalid_numbers = 0
total_numbers = 0

for game_moves in range(1, game_moves + 1):
    number_to_check = int(input())

    if 0 <= number_to_check <= 9:
        from_zero_to_nine += 1
        total_numbers += number_to_check * 0.20
    elif 10 <= number_to_check <= 19:
        from_ten_to_nineteen += 1
        total_numbers += number_to_check * 0.30
    elif 20 <= number_to_check <= 29:
        from_twenty_to_twenties +=1
        total_numbers += number_to_check * 0.40
    elif 30 <= number_to_check <= 39:
        from_thirties_to_thirty_nine += 1
        total_numbers += 50
    elif 40 <= number_to_check <= 50:
        total_numbers += 100
        from_fourths_to_fifty += 1
    else:
        total_numbers = total_numbers / 2
        invalid_numbers += 1
    print()

print(f"{total_numbers:.2f}")
print(f"From 0 to 9: {(from_zero_to_nine / game_moves) * 100:.2f}%")
print(f"From 10 to 19: {(from_ten_to_nineteen / game_moves) * 100:.2f}%")
print(f"From 20 to 29: {(from_twenty_to_twenties / game_moves) * 100:.2f}%")
print(f"From 30 to 39: {(from_thirties_to_thirty_nine / game_moves) * 100:.2f}%")
print(f"From 40 to 50: {(from_fourths_to_fifty / game_moves) * 100:.2f}%")
print(f"Invalid numbers: {(invalid_numbers / game_moves) * 100:.2f}%")
