student_name = input()

year_count = 0
grade_count = 0
failed_years = 0

while True:
    year_grade = float(input())
    year_count += 1

    if year_grade < 4:
        failed_years += 1

        if failed_years == 2:
            print(f"{student_name} has been excluded at {year_count} grade")
            break

        year_count -= 1
    else:
        grade_count += year_grade
        average = grade_count / 12

    if year_count == 12:
        print(f"{student_name} graduated. Average grade: {average:.2f}")
        break
