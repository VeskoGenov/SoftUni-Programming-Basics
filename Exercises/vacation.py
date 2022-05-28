# First inputs
money_needed_vacation = float(input())
available_money = float(input())

#Initial variables
spend_count = 0
days_count = 0

#Count how many times Jessy spent or saved
while available_money < money_needed_vacation and spend_count < 5:
    command = input()
    cash = float(input())
    days_count += 1

#Here we check wheter the money were saved or spent
    if command == "save":
        available_money += cash
        spend_count = 0
    elif command == "spend":
        available_money -= cash
        spend_count += 1
        if available_money < 0:
            available_money = 0

#Here we check if Jessy spent for more than 5 days
    if spend_count == 5:
        print("You can't save the money.")
        print(days_count)
        break
    if available_money >= money_needed_vacation:
        print(f"You saved the money for {days_count} days.")
        break

