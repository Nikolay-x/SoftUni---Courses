# 4.Сума от две числа
# Напишете програма която проверява всички възможни комбинации от двойка числа в интервала от две дадени числа. На изхода се отпечатва, коя поред е комбинацията чиито сбор от числата е равен на дадено магическо число. Ако няма нито една комбинация отговаряща на условието се отпечатва съобщение, че не е намерено.
# Вход
# Входът се чете от конзолата и се състои от три реда:
# Първи ред – начало на интервала – цяло число в интервала [1...999]
# Втори ред – край на интервала – цяло число в интервала [по-голямо от първото число...1000]
# Трети ред – магическото число – цяло число в интервала [1...10000]
# Изход
# На конзолата трябва да се отпечата един ред, според резултата:
# Ако е намерена комбинация чиито сбор на числата е равен на магическото число
# o"Combination N:{пореден номер} ({първото число} + {второ число} = {магическото число})"
# Ако не е намерена комбинация отговаряща на условието
# o"{броят на всички комбинации} combinations - neither equals {магическото число}"
#
# Вход
# 1
# 10
# 5
#
# Изход
# Combination N:4 (1 + 4 = 5)

first_number = int(input())
second_number = int(input())
magic_number = int(input())

combination_count = 0
is_combination_magic_number = False

for i in range(first_number, second_number +1):
    for q in range(first_number, second_number +1):
        combination_count += 1
        if i + q == magic_number:
            is_combination_magic_number = True
            break
    if is_combination_magic_number == True:
        break

if is_combination_magic_number == True:
    print(f"Combination N:{combination_count} ({i} + {q} = {magic_number})")
else:
    print(f"{combination_count} combinations - neither equals {magic_number}")
