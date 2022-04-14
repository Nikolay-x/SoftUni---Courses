# 8.Завършване
# Напишете програма, която изчислява средната оценка на ученик от цялото му обучение. На първия ред ще получите името на ученика, а на всеки следващ ред неговите годишни оценки. Ученикът преминава в следващия клас, ако годишната му оценка е по-голяма или равна на 4.00. Ако ученикът бъде скъсан повече от един път, то той бива изключен и програмата приключва, като се отпечатва името на ученика и в кой клас бива изключен.
#  При успешно завършване на 12-ти клас да се отпечата :
# "{име на ученика} graduated. Average grade: {средната оценка от цялото обучение}"
# В случай, че ученикът е изключен от училище, да се отпечата:
# "{име на ученика} has been excluded at {класа, в който е бил изключен} grade"
# Стойността трябва да бъде форматирана до втория знак след десетичната запетая.
#
# вход
# Gosho
# 5
# 5.5
# 6
# 5.43
# 5.5
# 6
# 5.55
# 5
# 6
# 6
# 5.43
# 5
#
# изход
# Gosho graduated. Average grade: 5.53

student_name = input()

current_class = 1
mark_sum = 0
excluded_number = 0

while current_class <= 12:
    mark = float(input())

    if mark >= 4:
        mark_sum += mark
        current_class +=1
    else:
        excluded_number += 1

    if excluded_number > 1:
        print(f"{student_name} has been excluded at {current_class} grade")
        break

avg_mark = mark_sum / 12

if excluded_number <= 1:
    print(f"{student_name} graduated. Average grade: {avg_mark:.2f}")
