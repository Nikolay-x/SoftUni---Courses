# 4.Double Char
# You will be given a string. You should print a string in which each character (case-sensitive) is repeated twice.
#
# Input
# Hello World
#
# Output
# HHeelllloo  WWoorrlldd

word = input()

result = ""

for i in range(len(word)):
    result += word[i] * 2

print(result)
