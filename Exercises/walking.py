steps_count = 0
steps_going_home_count = 0

steps = input()

while True:
    if steps == "Going home":
        steps = int(input())
        steps_going_home_count += steps
        if (steps_going_home_count + steps_count) <= 10000:
            print(f"{abs((steps_going_home_count + steps_count) - 10000)} more steps to reach goal.")
        else:
            print("Goal reached! Good job!")
            print(f"{abs(steps_count + steps_going_home_count - 10000)} steps over the goal!")
        break
    else:
        steps = int(steps)
    steps_count += steps

    if steps_count >= 10000:
        print("Goal reached! Good job!")
        print(f"{steps_count - 10000} steps over the goal!")
        break
    steps = input()