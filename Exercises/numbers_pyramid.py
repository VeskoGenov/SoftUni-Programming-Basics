number = int(input())

current_number = 1
flag = False

for rows in range(1, number + 1):
    for columns in range(1, rows + 1):

        if current_number > number:
            flag = True
            break
        print(f"{current_number}" + "", end=" ")
        current_number += 1
    if flag:
        break
    print()