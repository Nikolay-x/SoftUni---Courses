# 8.Редица цели числа
# Напишете програма, която чете n на брой цели числа. Принтирайте най-голямото и най-малкото число сред въведените.
#
# вход
# 5
# 10
# 20
# 304
# 0
# 50
#
# изход
# Max number: 304
# Min number: 0

from sys import maxsize

n = int(input())

max_number = -maxsize
min_number = maxsize

for i in range(n):
    number = int(input())
    if max_number < number:
        max_number = number
    if min_number > number:
        min_number = number

print(f"Max number: {max_number}")
print(f"Min number: {min_number}")
