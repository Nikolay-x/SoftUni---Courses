# 2. Елемент, равен на сумата на останалите
# Да се напише програма, която чете n-на брой цели числа, въведени от потребителя,и проверява дали сред тях съществува число, което е равно на сумата на всички останали.
# Ако има такъв елемент печата "Yes" и на нов ред "Sum = "  + неговата стойност
# Ако няма такъв елемент печата "No" и на нов ред "Diff = " + разликата между най-големия елемент и сумата на останалите (по абсолютна стойност)
#
# вход
# 7
# 3
# 4
# 1
# 1
# 2
# 12
# 1
#
# изход
# Yes
# Sum = 12

from sys import maxsize

n = int(input())

max_number = -maxsize
total_sum = 0

for i in range(1, n+1):
    number = int(input())
    total_sum += number
    if number > max_number:
        max_number = number

if total_sum - max_number == max_number:
    print("Yes")
    print(f"Sum = {max_number}")
else:
    print("No")
    print(f"Diff = {abs(total_sum - max_number - max_number)}")
