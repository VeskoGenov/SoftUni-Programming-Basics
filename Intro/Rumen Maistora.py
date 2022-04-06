#•	Предпазен найлон - 1.50 лв. за кв. метър
#•	Боя - 14.50 лв. за литър
#•	Разредител за боя - 5.00 лв. за литър

#1.	Необходимо количество найлон (в кв.м.) - цяло число в интервала [1... 100]
#2.	Необходимо количество боя (в литри) - цяло число в интервала [1…100]
#3.	Количество разредител (в литри) - цяло число в интервала [1…30]
#4.	Часовете, за които майсторите ще свършат работата - цяло число в интервала [1…9]

#•	"{сумата на всички разходи}"

plastic_wrap = int(input())
paint_liters = int(input())
diluent_liters = int(input())
working_hours = int(input())
plastic_bag = 0.4

sum_wrap = (plastic_wrap + 2) * 1.5
sum_paint_percentage = (paint_liters * 1.1) * 14.5
sum_diluent = diluent_liters * 5
total_cost_materials = sum_wrap + sum_paint_percentage + sum_diluent + plastic_bag
hr_cost = (total_cost_materials * 0.3) * working_hours

total_cost_invoice = total_cost_materials + hr_cost
print(total_cost_invoice)
