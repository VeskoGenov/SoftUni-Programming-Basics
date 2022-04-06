sq_meters = float(input())

total_cost = sq_meters * 7.61
total_cost_discount = 0.18 * total_cost

final_cost = total_cost - total_cost_discount

print(f"The final price is: {final_cost} lv.")
print(f"The discount is: {total_cost_discount} lv.")
