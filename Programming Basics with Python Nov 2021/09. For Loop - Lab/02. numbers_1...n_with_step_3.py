# 2.Числата от 1 до N през 3
# Напишете програма, която чете число n, въведено от потребителя и отпечатва числата от 1 до n през 3.
#
# вход
# 10
#
# изход
# 1
# 4
# 7
# 10

n = int(input())

for number in range(1, n + 1, 3):
    print(number)
