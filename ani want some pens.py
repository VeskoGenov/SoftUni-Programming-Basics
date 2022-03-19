box_pens = int(input())
box_markers = int(input())
cleaning_agent = int(input())
discount_percentage = int(input()) / 100

total_cost_pens = box_pens * 5.80
total_cost_markers = box_markers * 7.20
total_cost_cleaning_agent = cleaning_agent * 1.20
total_cost_everything = total_cost_pens + total_cost_markers + total_cost_cleaning_agent
discounted_total = total_cost_everything-(total_cost_everything * discount_percentage)

print(discounted_total)
