# 3.Четни степени на 2
# Да се напише програма, която чете число n, въведено от потребителя, и печата четните степени на 2 ≤ 2n: 20, 22, 24, 26, …, 2n.
#
# вход
# 3
#
# изход
# 1
# 4

n = int(input())

for i in range(0, n + 1):
    if i % 2 == 0:
        print(2 ** i)
