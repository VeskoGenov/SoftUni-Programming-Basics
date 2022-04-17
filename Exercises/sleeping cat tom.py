holidays = int(input())
year = 365
time_to_play = 30000

working_days = year - holidays
days_to_minutes = (working_days * 63) + (holidays * 127)
difference = abs(time_to_play - days_to_minutes)
minutes_to_hours = difference // 60
minutes = difference % 60

if days_to_minutes >= time_to_play:
    print("Tom will run away")
    print(f"{minutes_to_hours} hours and {minutes} minutes more for play")
else:
    print("Tom sleeps well")
    print(f"{minutes_to_hours} hours and {minutes} minutes less for play")