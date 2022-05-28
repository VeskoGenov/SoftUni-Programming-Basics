floors = int(input())
floor_rooms = int(input())

room_number = 0
room_type = ""

for floors_number in range(floors, 0, -1):
    for rooms in range(floor_rooms):
        room_number = floors_number * 10 + rooms

        if floors_number == floors:
            room_type = f"L{room_number}"
        elif floors_number % 2 != 0:
            room_type = f"A{room_number}"
        else:
            room_type = f"O{room_number}"
        print(room_type, end=" ")
    print()