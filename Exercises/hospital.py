# period = int(input())
#
# visited_patients = 0
# in_line_patients = 0
# doctors = 7
# new_doctors = 0
#
# for period in range(1, period + 1):
#     patients_arrived = int(input())
#
#     if period % 3 == 0 and in_line_patients > visited_patients:
#         new_doctors += 1
#
#     if patients_arrived <= (doctors + new_doctors):
#         visited_patients += patients_arrived
#
#     else:
#         visited_patients += + (doctors + new_doctors)
#         in_line_patients += + patients_arrived - (doctors + new_doctors)
#
# print(f"Treated patients: {visited_patients}.")
# print(f"Untreated patients: {in_line_patients}.")


period = int(input())

visited_patients = 0
in_line_patients = 0
doctors = 7

for period in range(1, period + 1):
    patients_arrived = int(input())

    if period % 3 == 0 and in_line_patients > visited_patients:
        doctors += 1

    if patients_arrived <= doctors:
        visited_patients += patients_arrived

    else:
        count_patients = patients_arrived - doctors
        in_line_patients += count_patients
        visited_patients += doctors

print(f"Treated patients: {visited_patients}.")
print(f"Untreated patients: {in_line_patients}.")