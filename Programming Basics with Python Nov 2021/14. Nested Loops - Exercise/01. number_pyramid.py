# 1.Пирамида от числа
# Напишете програма, която чете цяло число n, въведено от потребителя, и отпечатва пирамида от числа като в примерите:
#
# вход
# 7
#
# изход
# 1
# 2 3
# 4 5 6
# 7

n = int(input())

current = 0
is_current_bigger_than_n = False

for row in range(1, n + 1):
    for col in range(1, row + 1):

        current +=1
        print(current, end = " ")

        if current == n:
            is_current_bigger_than_n = True
            break

    if is_current_bigger_than_n:
        break

    print()
