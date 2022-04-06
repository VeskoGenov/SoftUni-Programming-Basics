video_cards = 250

budget = float(input())
qty_video_cards = int(input())
qty_processor = int(input())
qty_ram = int(input())

video_cards_sum = qty_video_cards * video_cards

processor_sum = (video_cards_sum * 35) / 100
processor_sum_total = qty_processor * processor_sum

ram_sum = (video_cards_sum * 10) / 100
ram_sum_total = ram_sum * qty_ram

total_cost = video_cards_sum + processor_sum_total + ram_sum_total

if qty_video_cards > qty_processor:
    discount = (total_cost * 15) / 100
    total_cost = total_cost - discount

if total_cost <= budget:
    remaining_money = budget - total_cost
    print(f"You have {remaining_money} leva left!")
elif total_cost > budget:
    needed_money = total_cost - budget
    print(f"Not enough money! You need {needed_money:.2f} leva more!")