deposit = float(input())
months = int(input())
percentage_year = float(input())

accumulated_percentage = deposit * percentage_year / 100
monthly_percentage = accumulated_percentage / 12
total_deposit = deposit + months * monthly_percentage

print(total_deposit)
