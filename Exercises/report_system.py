expected_money = int(input())

cycle_count = 0
credit_card_transactions = 0
cash_transactions = 0
money_collected = 0

items_price = input()
while True:
    if items_price == "End":
        break
    else:
        items_price = int(items_price)
        cycle_count += 1

    if cycle_count % 2 == 0:
        if 10 <= items_price <= 100:
            print("Product sold!")
        money_collected += items_price
    else:
        if items_price >= 100:
            print("Error in transaction!")
        elif items_price < 10:
            print("Error in transaction!")

    items_price = input()