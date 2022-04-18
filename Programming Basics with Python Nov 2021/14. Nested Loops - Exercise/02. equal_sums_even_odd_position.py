# 2.Еднакви суми на четни и нечетни позиции
# Напишете програма, която чете от конзолата две шестцифрени цели числа. Винаги първото въведено число ще бъде по-малко от второто. На конзолата да се отпечатат на 1, ред разделени с интервал, всички числа, които се намират между двете, прочетени от конзолата числа и отговарят на условието сумата от цифрите на четни и нечетни позиции да са равни. Ако няма числа, отговарящи на условието на конзолата не се извежда резултат.
#
# Вход
# 100000
# 100050
#
# Изход
# 100001 100012 100023 100034 100045

start = int(input())
end = int(input())

for number in range(start, end + 1):
    even_sum = 0
    odd_sum = 0
    for index, digit in enumerate(str(number)):
        if (index + 1) % 2 == 0:
            even_sum += int(digit)
        else:
            odd_sum += int(digit)
    if even_sum == odd_sum:
        print(number, end = " ")