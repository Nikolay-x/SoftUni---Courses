# 6.Пребоядисване
# Румен иска да пребоядиса хола и за целта е наел майстори. Напишете програма, която изчислява разходите за ремонта, предвид следните цени:
# Предпазен найлон - 1.50 лв. за кв. метър
# Боя - 14.50 лв. за литър
# Разредител за боя - 5.00 лв. за литър
# За всеки случай, към необходимите материали, Румен иска да добави още 10% от количеството боя и 2 кв.м. найлон, разбира се и 0.40 лв. за торбички. Сумата, която се заплаща на майсторите за 1 час работа, е равна на 30% от сбора на всички разходи за материали.
# Вход
# Входът се чете от конзолата и съдържа точно 4 реда:
# 1.Необходимо количество найлон (в кв.м.) - цяло число в интервала [1... 100]
# 2.Необходимо количество боя (в литри) - цяло число в интервала [1…100]
# 3.Количество разредител (в литри) - цяло число в интервала [1…30]
# 4.Часовете, за които майсторите ще свършат работата - цяло число в интервала [1…9]
# Изход
# Да се отпечата на конзолата един ред:
# "{сумата на всички разходи}"
#
# Вход
# 10
# 11
# 4
# 8
#
# Изход
# 727.09

protective_nylon_m2_price = 1.5
paint_liter_price = 14.5
paint_thinner_liter_price = 5

protective_nylon_quantity_m2 = int(input())
paint_quantity_liters = int(input())
paint_thinner_quantity_liters = int(input())
workers_job_hours = int(input())

protective_nylon_total_price = (protective_nylon_quantity_m2 + 2) * protective_nylon_m2_price
paint_total_price = paint_quantity_liters * 1.1 * paint_liter_price
paint_thinner_total_price = paint_thinner_quantity_liters * paint_thinner_liter_price
plastics_total_price = 0.4
total_materials_price = protective_nylon_total_price + paint_total_price + paint_thinner_total_price + \
                        plastics_total_price
workers_total_price = total_materials_price * 0.3 * workers_job_hours
total_sum = total_materials_price + workers_total_price

print(total_sum)
