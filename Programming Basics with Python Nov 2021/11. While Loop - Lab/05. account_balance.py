# 5.Баланс по сметка
# Напишете програма, която пресмята колко общо пари има в сметката, след като направите определен брой вноски. На всеки ред ще получавате сумата, която трябва да внесете в сметката, до получаване на команда  "NoMoreMoney ". При всяка получена сума на конзолата трябва да се извежда "Increase: " + сумата и тя да се прибавя в сметката. Ако получите число по-малко от 0 на конзолата трябва да се изведе "Invalid operation!"  и програмата да приключи. Когато програмата приключи трябва да се принтира "Total: " + общата сума в сметката форматирана до втория знак след десетичната запетая.
#
# вход
# 5.51
# 69.42
# 100
# NoMoreMoney
#
# изход
# Increase: 5.51
# Increase: 69.42
# Increase: 100.00
# Total: 174.93

input_sum = input()

total_sum = 0

while input_sum != "NoMoreMoney":

    input_sum = float(input_sum)

    if input_sum < 0:
        print("Invalid operation!")
        break
    else:
        print(f"Increase: {input_sum:.2f}")
        total_sum += input_sum

    input_sum = input()

print(f"Total: {total_sum:.2f}")
