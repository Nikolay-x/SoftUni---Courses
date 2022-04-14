# 6.Най-голямо число
# Напишете програма, която до получаване на командата "Stop", чете цели числа, въведени от потребителя,  намира най-голямото измежду тях и го принтира. Въвежда се по едно число на ред.
#
# вход
# 100
# 99
# 80
# 70
# Stop
#
# изход
# 100

from sys import maxsize

number = input()

max_number = -maxsize

while number != "Stop":
    number = int(number)
    if number > max_number:
        max_number = number
    number = input()

print(max_number)
