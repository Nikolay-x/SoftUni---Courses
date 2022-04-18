# 2.Таблица за умножение
# Отпечатайте на конзолата таблицата за умножение за числата от 1 до 10 във формат:
# "{първи множител} * {втори множител} = {резултат}".
#
# Вход
# (няма вход)
#
# Изход
# 1 * 1 = 1
# 1 * 2 = 2
# 1 * 3 = 3
# 1 * 4 = 4
# 1 * 5 = 5
# 1 * 6 = 6
# 1 * 7 = 7
# 1 * 8 = 8
# 1 * 9 = 9
# 1 * 10 = 10
# ...
# 10 * 1 = 10
# 10 * 2 = 20
# 10 * 3 = 30
# 10 * 4 = 40
# 10 * 5 = 50
# 10 * 6 = 60
# 10 * 7 = 70
# 10 * 8 = 80
# 10 * 9 = 90
# 10 * 10 = 100

for first_multiplier in range(1, 11):
    for second_multiplier in range(1, 11):
        print(f"{first_multiplier} * {second_multiplier} = {first_multiplier * second_multiplier}")