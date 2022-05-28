students_for_the_day = int(input())

top_students = 0
between_4_and_5 = 0
between_3_and_4 = 0
below_3 = 0
total_votes = 0

for students_for_the_day in range(1, students_for_the_day + 1):
    exam_vote = float(input())
    total_votes += exam_vote

    if exam_vote >= 5:
        top_students += 1
    elif 4 <= exam_vote <= 4.99:
        between_4_and_5 += 1
    elif 3 <= exam_vote <= 3.99:
        between_3_and_4 += 1
    else:
        below_3 += 1

print(f"Top students: {(top_students / students_for_the_day) * 100:.2f}%")
print(f"Between 4.00 and 4.99: {(between_4_and_5 / students_for_the_day) * 100:.2f}%")
print(f"Between 3.00 and 3.99: {(between_3_and_4 / students_for_the_day) * 100:.2f}%")
print(f"Fail: {(below_3 / students_for_the_day) * 100:.2f}%")
print(f"Average: {total_votes / students_for_the_day:.2f}")