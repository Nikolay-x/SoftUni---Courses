# 3.Комбинации
# Напишете програма, която изчислява колко решения в естествените числа (включително и нулата) има уравнението:
# x1 + x2 + x3 = n
# Числото n е цяло число и се въвежда от конзолата.
#
# Вход
# 25
#
# Изход
# 351

n = int(input())

combinations_count = 0

for x1 in range(n+1):
    for x2 in range(n+1):
        for x3 in range(n+1):
            if x1 + x2 + x3 == n:
                combinations_count += 1
print(combinations_count)
