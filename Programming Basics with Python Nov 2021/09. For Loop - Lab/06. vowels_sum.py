# 6.Сумиране на гласните букви
# Да се напише програма, която чете текст (стринг), въведен от потребителя, и изчислява и отпечатва сумата от стойностите на гласните букви според таблицата по-долу:
# буква	a	e	i	o	u
# стойност	1	2	3	4	5
#
# вход
# hello
#
# изход
# 6

text = input()

sum_a = 0
sum_e = 0
sum_i = 0
sum_o = 0
sum_u = 0

for letter in text:
    if letter == "a":
        sum_a += 1
    elif letter == "e":
        sum_e += 2
    elif letter == "i":
        sum_i += 3
    elif letter == "o":
        sum_o += 4
    elif letter == "u":
        sum_u += 5

print(sum_a + sum_e + sum_i + sum_o + sum_u)
