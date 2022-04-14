# Задача 2. Щанд за гривни
# Остават 5 дни до рождения ден на брата на Тереза. Тя иска да му купи подарък и решава да си направи малък щанд и да продава плетени гривнички с мъниста, за да събере достатъчно пари.
# Вашата задача е да напишете програма, която да изчислява сумата, която Тереза е успяла да събере и да даде отговор на момичето, дали тя ще може да купи подарък или не. Трябва да се вземат предвид нейните разходи и цената на подаръка.
# Вход
# От конзолата се четат 4 реда:
# Първи ред – джобните на Тереза на ден – реално число в интервала [1.00 ...100.00]
# Втори ред – парите, които тя печели на ден от продажби – реално число в интервала [1.00...1000.00]
# Трети ред – разходите на Тереза за целия период – реално число в интервала [1.00...1000.00]
# Четвърти ред – цената на подаръка – реално число в интервала [1.00...10000.00]
# Изход
# На конзолата да се отпечата:
# Ако са изработени достатъчно пари за подарък:
# o"Profit: {всички спестени пари} BGN, the gift has been purchased."
# Ако са изработени по-малко нужните пари:
# o"Insufficient money: {сумата, която не достига} BGN."
# Числата трябва да са форматирани до втория знак след десетичната запетая.
#
# Вход
# 5.12
# 32.05
# 15
# 150
#
# Изход
# Profit: 170.85 BGN, the gift has been purchased.

teresa_pocket_money = float(input())
daily_profit = float(input())
teresa_expenses = float(input())
present_price = float(input())

total_pocket_money = teresa_pocket_money * 5
total_profit_money = daily_profit * 5

total_saved_money = total_pocket_money + total_profit_money
total_money = total_saved_money - teresa_expenses

if total_money >= present_price:
    print(f"Profit: {total_money:.2f} BGN, the gift has been purchased.")
else:
    print(f"Insufficient money: {(present_price - total_money):.2f} BGN.")
