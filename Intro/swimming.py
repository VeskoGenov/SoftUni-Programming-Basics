record_seconds = float(input())
distance_meters = float(input())
time_to_swim = float(input())

needed_seconds_to_swim = distance_meters * time_to_swim
slowdown_seconds = distance_meters // 15 * 12.5

total_seconds = needed_seconds_to_swim + slowdown_seconds

if record_seconds < total_seconds:
    total_seconds_failure = total_seconds - record_seconds
    print(f"No, he failed! He was {total_seconds_failure:.2f} seconds slower.")
else:
    print(f"Yes, he succeeded! The new world record is {total_seconds:.2f} seconds.")
