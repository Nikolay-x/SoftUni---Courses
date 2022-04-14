# 7.Най-малко число
# Напишете програма, която до получаване на командата "Stop", чете цели числа, въведени от потребителя, намира най-малкото измежду тях и го принтира. Въвежда се по едно число на ред.
#
# вход
# 100
# 99
# 80
# 70
# Stop
#
# изход
# 70

from sys import maxsize

number = input()

min_number = maxsize

while number != "Stop":
    number = int(number)
    if number < min_number:
        min_number = number
    number = input()

print(min_number)
