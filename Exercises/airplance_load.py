boot_capacity = float(input())

suitcase_count = 0
avai_space = 0

while True:
    suitcase = input()

    if suitcase == "End":
        print(f"Congratulations! All suitcases are loaded!\nStatistic: {suitcase_count} suitcases loaded.")
        break

    suitcase_count += 1
    suitcase = float(suitcase)

    if suitcase_count % 3 == 0:
        boot_capacity -= suitcase * 0.10

    if suitcase > boot_capacity:
        suitcase_count -= 1
        print(f"No more space!\nStatistic: {suitcase_count} suitcases loaded.")
        break

    boot_capacity -= suitcase