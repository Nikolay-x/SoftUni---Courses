# 5.Print Part of the ASCII Table
# Write a program that prints part of the ASCII table characters on the console, separated by a single space. On the first line of input, you will receive the char index you should start with. On the second line - the index of the last character you should print.
#
# Input
# 60
# 65
#
# Output
# < = > ? @ A

first_char_index = int(input())
last_char_index = int(input())

for i in range(first_char_index, last_char_index + 1):
    print(chr(i), end= " ")
