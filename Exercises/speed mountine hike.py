import math

record_in_seconds = float(input())
distance_in_meters = float(input())
time_to_climb_meter = float(input())

time_to_climb = distance_in_meters * time_to_climb_meter
slowdown_climbing = math.floor(distance_in_meters / 50)
slowdown_climbing = slowdown_climbing * 30
total_time_to_climb = (time_to_climb + slowdown_climbing)
difference = total_time_to_climb - record_in_seconds

if total_time_to_climb >= record_in_seconds:
    print(f"No! He was {difference:.2f} seconds slower.")
else:
    print(f"Yes! The new record is {total_time_to_climb:.2f} seconds.")