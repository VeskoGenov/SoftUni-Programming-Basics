first_number = int(input())
last_number = int(input())
magic_number = int(input())
flag = False
combinations = 0

for start in range(first_number, last_number + 1):
    for end in range(first_number, last_number + 1):

        combinations += 1

        if start + end == magic_number:
            flag = True
            print(f"Combination N:{combinations} ({start} + {end} = {start + end})")
            break

    if flag:
        break

if not flag:
    print(f"{combinations} combinations - neither equals {magic_number}")
