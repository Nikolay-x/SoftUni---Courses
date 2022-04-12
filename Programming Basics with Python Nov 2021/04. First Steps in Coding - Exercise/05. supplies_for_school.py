# 5.Учебни материали
# Учебната година вече е започнала и отговорничката на 10Б клас - Ани трябва да купи определен брой пакетчета с химикали, пакетчета с маркери, както и препарат за почистване на дъска. Тя е редовна клиентка на една книжарница, затова има намаление за нея, което представлява някакъв процент от общата сума. Напишете програма, която изчислява колко пари ще трябва да събере Ани, за да плати сметката, като имате предвид следния ценоразпис:
# •Пакет химикали - 5.80 лв.
# •Пакет маркери - 7.20 лв.
# •Препарат - 1.20 лв (за литър)
# Вход
# От конзолата се четат 4 числа:
# Брой пакети химикали - цяло число в интервала [0...100]
# Брой пакети маркери - цяло число в интервала [0...100]
# Литри препарат за почистване на дъска - цяло число в интервала [0…50]
# Процент намаление - цяло число в интервала [0...100]
# Изход
# Да се отпечата на конзолата колко пари ще са нужни на Ани, за да си плати сметката.
#
# Вход
# 2
# 3
# 4
# 25
#
# Изход
# 28.5

pen_box_price = 5.8
marker_box_price = 7.20
detergent_liter_price = 1.2

pen_box_number = int(input())
marker_box_number = int(input())
detergent_liter = int(input())
discount_percentage = int(input())

pen_total_price = pen_box_number * pen_box_price
marker_total_price = marker_box_number * marker_box_price
detergent_total_price = detergent_liter * detergent_liter_price
total_price = pen_total_price + marker_total_price + detergent_total_price
final_price = total_price - (total_price * discount_percentage /100)

print(final_price)
