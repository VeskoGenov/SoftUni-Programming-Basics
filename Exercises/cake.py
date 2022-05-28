#Cake size input
cake_length = int(input())
cake_width = int(input())
#Total cake piece calculation
cake_piece_left = cake_width * cake_length
#Calculating eaten pieces
while True:
    eaten_piece = input()

    if eaten_piece == "STOP":
        print(f"{cake_piece_left} pieces are left.")
        break
    else:
        cake_piece_left -= int(eaten_piece)

    if cake_piece_left <= 0:
        print(f"No more cake left! You need {abs(cake_piece_left)} pieces more.")
        break