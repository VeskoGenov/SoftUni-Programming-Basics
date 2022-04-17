city = input()
sales = float(input())
percentage = 0

if city == "Sofia":
    if 0 <= sales <= 500:
        percentage = (sales * 5) / 100
    elif 500 <= sales <= 1000:
        percentage = (sales * 7) / 100
    elif 1000 <= sales <= 10000:
        percentage = (sales * 8) / 100
    elif 10000 <= sales:
        percentage = (sales * 12) / 100
elif city == "Varna":
    if 0 <= sales <= 500:
        percentage = (sales * 4.5) / 100
    elif 500 <= sales <= 1000:
        percentage = (sales * 7.5) / 100
    elif 1000 <= sales <= 10000:
        percentage = (sales * 10) / 100
    elif 10000 <= sales:
        percentage = (sales * 13) / 100
elif city == "Plovdiv":
    if 0 <= sales <= 500:
        percentage = (sales * 5.5) / 100
    elif 500 <= sales <= 1000:
        percentage = (sales * 8) / 100
    elif 1000 <= sales <= 10000:
        percentage = (sales * 12) / 100
    elif 10000 <= sales:
        percentage = (sales * 14.5) / 100
if percentage <= 0:
    print("error")
else:
    print(f"{percentage:.2f}")