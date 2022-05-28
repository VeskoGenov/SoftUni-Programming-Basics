destination = input()

while destination != "End":
    budged_needed = float(input())
    total_saved = 0
    while True:
        savings = float(input())
        total_saved += savings
        if total_saved >= budged_needed:
            total_saved = 0
            print(f"Going to {destination}!")
            break
    destination = input()
