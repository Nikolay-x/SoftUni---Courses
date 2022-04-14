# 5.Монети
# Производителите на вендинг машини искали да направят машините си да връщат възможно най-малко монети ресто. Напишете програма, която приема сума - рестото, което трябва да се върне и изчислява с колко най-малко монети може да стане това.
#
# Вход
# 1.23
#
# Изход
# 4

change = float(input())
coins = 0

while change > 0:

    if change >= 2:
        change -= 2

    elif change >= 1:
        change -= 1

    elif change >= 0.50:
        change -= 0.50

    elif change >= 0.20:
        change -= 0.20

    elif change >= 0.10:
        change -= 0.10

    elif change >= 0.05:
        change -= 0.05

    elif change >= 0.02:
        change -= 0.02

    elif change >= 0.01:
        change -= 0.01

    change = round(change, 2)
    coins += 1

print(coins)
