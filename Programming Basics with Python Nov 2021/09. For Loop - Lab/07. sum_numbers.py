# 7.Сумиране на числа
# Да се напише програма, която чете n-на брой цели числа, въведени от потребителя и ги сумира.
# От първия ред на входа се въвежда броят числа n.
# От следващите n реда се въвежда по едно цяло число.
# Програмата трябва да прочете числата, да ги сумира и да отпечата сумата им.
#
# вход
# 2
# 10
# 20
#
# изход
# 30

n = int(input())

sum = 0

for i in range(n):
    number = int(input())
    sum += number

print(sum)
