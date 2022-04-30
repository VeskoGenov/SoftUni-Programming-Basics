city = input()
sales = float(input())
percentage = 0

comissions_info = {
    "Sofia": {
        "0 - 500": 5,
        "500 - 1000": 7,
        "1000 - 10000": 8,
        "10000": 12
    },
    "Varna":{
        "0 - 500": 4.5,
        "500 - 1000": 7.5,
        "1000 - 10000": 10,
        "10000": 13
    },
    "Plovdiv": {
        "0 - 500": 5.5,
        "500 - 1000": 8,
        "1000 - 10000": 12,
        "10000": 14.5
    }
}

if city in comissions_info and sales > 0:
    if 0 <= sales <= 500:
        percentage = comissions_info[city]["0 - 500"] * sales / 100
    elif 500 <= sales <= 1000:
        percentage = comissions_info[city]["500 - 1000"] * sales / 100
    elif 1000 <= sales <= 10000:
        percentage = comissions_info[city]["1000 - 10000"] * sales / 100
    elif sales > 10000:
        percentage = comissions_info[city]["10000"] * sales / 100
    print(f"{percentage:.2f}")
else:
    print("error")