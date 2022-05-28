height = int(input())
length = int(input())
width = int(input())

room_size = height * length * width

boxes_to_move = input()

while True:
    if boxes_to_move == "Done":
        print(f"{room_size} Cubic meters left.")
        break
    else:
        boxes_to_move = int(boxes_to_move)
        room_size -= boxes_to_move

    if room_size <= 0:
        print(f"No more free space! You need {abs(room_size)} Cubic meters more.")
        break
    boxes_to_move = input()