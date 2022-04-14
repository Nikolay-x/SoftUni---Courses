# Задача 4. Изпит
# Напишете програма, която да пресмята статистика за оценки от изпит. В началото програмата получава броя на студентите явили се на изпита и за всеки студент неговата оценка. На края програмата трябва да отпечата процента студенти с оценка между 2.00 и 2.99, между 3.00 и 3.99, между 4.00 и 4.99, 5.00 или повече. Също така и средния успех на изпита.
# Вход:
# От конзолата се четат:
# На първия ред – броя на студентите явили се на изпит – цяло число в интервала [1...1000]
# За всеки един студент на отделен ред – оценката от изпита – реално число в интервала [2.00...6.00]
# Изход:
# Да се отпечатат на конзолата 5 реда, които съдържат следната информация:
# Ред 1 -"Top students: {процент студенти с успех 5.00 или повече}%"
# Ред 2 -"Between 4.00 and 4.99: {между 4.00 и 4.99 включително}%"
# Ред 3 -"Between 3.00 and 3.99: {между 3.00 и 3.99 включително}%"
# Ред 4 -"Fail: {по-малко от 3.00}%"
# Ред 5 -"Average: {среден успех}"
# Всички числа трябва да са форматирани до втория знак след десетичната запетая.
#
# Вход
# 10
# 3.00
# 2.99
# 5.68
# 3.01
# 4
# 4
# 6.00
# 4.50
# 2.44
# 5
#
# Изход
# Top students: 30.00%
# Between 4.00 and 4.99: 30.00%
# Between 3.00 and 3.99: 20.00%
# Fail: 20.00%
# Average: 4.06

student_count = int(input())

mark_200_299_count = 0
mark_300_399_count = 0
mark_400_499_count = 0
mark_500_and_above_count = 0
total_marks = 0

for i in range(1, student_count + 1):
    student_mark = float(input())
    total_marks += student_mark
    if 2<= student_mark < 3:
        mark_200_299_count += 1
    elif 3<= student_mark <4:
        mark_300_399_count += 1
    elif 4<= student_mark < 5:
        mark_400_499_count += 1
    elif student_mark >= 5:
        mark_500_and_above_count += 1

mark_200_299_per = mark_200_299_count / student_count * 100
mark_300_399_per = mark_300_399_count / student_count * 100
mark_400_499_per = mark_400_499_count / student_count * 100
mark_500_and_above_per = mark_500_and_above_count / student_count * 100
avg_mark = total_marks / student_count

print(f"Top students: {mark_500_and_above_per:.2f}%")
print(f"Between 4.00 and 4.99: {mark_400_499_per:.2f}%")
print(f"Between 3.00 and 3.99: {mark_300_399_per:.2f}%")
print(f"Fail: {mark_200_299_per:.2f}%")
print(f"Average: {avg_mark:.2f}")
