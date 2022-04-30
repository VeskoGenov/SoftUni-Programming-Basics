exam_hour = int(input())
exam_minutes = int(input())
arrival_hour = int(input())
arrival_minutes = int(input())

exam_start = (exam_hour * 60) + exam_minutes
arrival_time = (arrival_hour * 60) + arrival_minutes

time_left = (exam_start - arrival_time) / 60
minutes_left = (exam_start - arrival_time) % 60

if arrival_time >= exam_start:
    arrival = arrival_time - exam_start
else:
    arrival = exam_start - arrival_time

if arrival == exam_start:
    print("On time")
if minutes_left > 30:
    print("Early")
