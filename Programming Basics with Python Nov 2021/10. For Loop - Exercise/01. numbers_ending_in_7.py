# 1.Числа до 1000, завършващи на 7
# Напишете програма, която отпечатва числата в диапазона от 1 до 1000, които завършват на 7.
#
# вход
# (няма)
#
# изход
# 7
# 17
# 27
# …
# 997
#
# # for numbers in range(7, 1001, 10):
# #     print(numbers)

for numbers in range(1, 1001):
    if numbers % 10 == 7:
        print(numbers)
