cost_kg_vegetables = float(input())
cost_kg_fruits = float(input())
total_kg_vegetables = int(input())
total_kg_fruits = int(input())

calculate_vegetable_cost = cost_kg_vegetables * total_kg_vegetables
calculate_fruits_cost = cost_kg_fruits * total_kg_fruits
total = calculate_vegetable_cost + calculate_fruits_cost

leva_to_euro = total / 1.94
print(f"{leva_to_euro:.2f}")