# 9.Лява и дясна сума
# Да се напише програма, която чете 2 * n-на брой цели числа, подадени от потребителя, и проверява дали сумата на първите n числа (лява сума) е равна на сумата на вторите n числа (дясна сума). При равенство печата "Yes, sum = " + сумата; иначе печата "No, diff = " + разликата. Разликата се изчислява като положително число (по абсолютна стойност).
#
# вход
# 2
# 10
# 90
# 60
# 40
#
# изход
# Yes, sum = 100

n = int(input())

left_sum = 0
right_sum = 0

for i in range(1, n * 2 + 1):
    number = int(input())
    if i <= n:
        left_sum += number
    else:
        right_sum += number

if left_sum == right_sum:
    print(f"Yes, sum = {left_sum}")
else:
    print(f"No, diff = {abs(left_sum - right_sum)}")
