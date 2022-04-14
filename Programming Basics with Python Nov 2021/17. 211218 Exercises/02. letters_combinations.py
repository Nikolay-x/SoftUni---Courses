# 2.Комбинации от букви
# Напишете програма, която да принтира на конзолата всички комбинации от 3 букви в зададен интервал, като се пропускат комбинациите съдържащи зададена от конзолата буква. Накрая трябва да се изпринтира броят на отпечатаните комбинации.
# Вход
# Входът се чете от конзолата и съдържа точно 3 реда:
# Ред 1.Малка буква от английската азбука за начало на интервала – от ‘a’ до ‚z’.
# Ред 2.Малка буква от английската азбука за край на интервала  – от първата буква до ‚z’.
# Ред 3.Малка буква от английската азбука – от ‘a’ до ‚z’ – като комбинациите съдържащи тази буквата се пропускат.
# Изход
# Да се отпечатат на един ред всички комбинации отговарящи на условието плюс броят им разделени с интервал.
#
# Вход
# a
# c
# b
#
# Изход
# aaa aac aca acc caa cac cca ccc 8

first_letter = input()
last_letter = input()
excluded_letter = input()

combinations_count = 0

for a in range(ord(first_letter), ord(last_letter) +1):
    for b in range(ord(first_letter), ord(last_letter) +1):
        for c in range(ord(first_letter), ord(last_letter) +1):
            if chr(a) != excluded_letter and chr(b) != excluded_letter and chr(c) != excluded_letter:
                combinations_count += 1
                print(f"{chr(a)}{chr(b)}{chr(c)}", end = " ")
print(combinations_count)
