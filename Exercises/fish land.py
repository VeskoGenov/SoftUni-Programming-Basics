mackerel = float(input())
sprat = float(input())
bonito_kg = float(input())
scad_kg = float(input())
clam_kg = int(input())
clam_cost = clam_kg * 7.50

bonito_cost = (mackerel + ((mackerel * 60) / 100)) * bonito_kg
scad_cost = (sprat + ((sprat * 80) / 100)) * scad_kg
total = clam_cost + bonito_cost + scad_cost
print(f"{total:.2f}")

