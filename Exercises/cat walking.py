walking_time_minutes = int(input())
walking_times_daily = int(input())
calories_assumed = int(input())

calories_to_burn = calories_assumed / 2

calories_burned = (walking_times_daily * walking_time_minutes)  * 5

if calories_burned >= calories_to_burn:
    print(f"Yes, the walk for your cat is enough. Burned calories per day: {calories_burned}.")
else:
    print(f"No, the walk for your cat is not enough. Burned calories per day: {calories_burned}.")
