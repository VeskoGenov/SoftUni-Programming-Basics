import math

series = input()
episode_minutes = int(input())
lunch_break = int(input())

lunch_time_calc = lunch_break / 8
time_to_relax_calc = lunch_break / 4

time_left = lunch_break - lunch_time_calc - time_to_relax_calc
time_left_total = abs(time_left - episode_minutes)

if time_left >= episode_minutes:
    print(f"You have enough time to watch {series} and left with {math.floor(time_left_total)} minutes free time.")

elif time_left < episode_minutes:
    print(f"You don't have enough time to watch {series}, you need {math.ceil(time_left_total)} more minutes.")
