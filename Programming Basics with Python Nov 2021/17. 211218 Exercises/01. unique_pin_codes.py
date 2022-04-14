# 1.Уникални PIN кодове
# Да се напише програма, която генерира трицифрени PIN кодове, като цифрите на всеки PIN код са в определен интервал. За да бъде валиден един PIN код той трябва да отговаря на следните условия:
# Първата и третата цифра трябва да бъдат четни.
# Втората цифра трябва да бъде просто число в диапазона [2...7].
# Вход
# От конзолата се четат 3 реда:
# Горната граница на първото число - цяло число в диапазона [1...9]
# Горната граница на второто число - цяло число в диапазона [1...9]
# Горната граница на третото число - цяло число в диапазона [1...9]
# Изход
# Да се отпечатат на конзолата всички валидни трицифрени PIN кодове, чиито цифри отговарят на съответните интервали.
#
# Вход
# 3
# 5
# 5
#
# Изход
# 2 2 2
# 2 2 4
# 2 3 2
# 2 3 4
# 2 5 2
# 2 5 4

first_digit_upper_limit = int(input())
second_digit_upper_limit = int(input())
third_digit_upper_limit = int(input())

a_check = False
b_check = False
c_check = False

for a in range(1, first_digit_upper_limit +1):
    for b in range(1, second_digit_upper_limit +1):
        for c in range(1, third_digit_upper_limit +1):
            if a % 2 == 0:
                a_check = True
            if b == 2 or b == 3 or b == 5 or b == 7:
                b_check = True
            if c % 2 == 0:
                c_check = True
            if a_check == True and b_check == True and c_check == True:
                print(f"{a} {b} {c}")
            a_check = False
            b_check = False
            c_check = False
