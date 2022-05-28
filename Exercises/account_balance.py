balance = 0

while True:
    cash = input()
    if cash == "NoMoreMoney":
        break
    cash = float(cash)
    if cash >= 0:
        balance += cash
        print(f"Increase: {cash:.2f}")
    else:
        print("Invalid operation!")
        break

print(f"Total: {balance:.2f}")