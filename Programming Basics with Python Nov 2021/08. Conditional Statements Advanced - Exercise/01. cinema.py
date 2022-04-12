# 1.Кино
# В една кинозала столовете са наредени в правоъгълна форма в r реда и c колони. Има три вида прожекции с билети на различни цени:
# Premiere - премиерна прожекция, на цена 12.00 лева;
# Normal - стандартна прожекция, на цена 7.50 лева;
# Discount - прожекция за деца, ученици и студенти на намалена цена от 5.00 лева.
# Напишете програма, която чете тип прожекция (текст), брой редове и брой колони в залата (цели числа), въведени от потребителя, и изчислява общите приходи от билети при пълна зала. Резултатът да се отпечата във формат 2 знака след десетичната точка.
#
# вход
# Premiere
# 10
# 12
#
# изход
# 1440.00 leva

projection_type = input()
row_number = int(input())
column_number = int(input())

tickets_income = 0

if projection_type == 'Premiere':
    tickets_income = row_number * column_number * 12
elif projection_type == 'Normal':
    tickets_income = row_number * column_number * 7.5
elif projection_type == 'Discount':
    tickets_income = row_number * column_number * 5

print(f"{tickets_income:.2f}")
