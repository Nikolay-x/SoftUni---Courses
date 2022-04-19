# 3.Substring
# On the first line, you will receive a string. On the second line, you will receive a second string. Write a program that removes all the occurrences of the first string in the second until there is no match. At the end, print the remaining string.
#
# Input
# ice
# piceoiciceet
#
# Output
# pot

first_line = input()
second_line = input()

while first_line in second_line:
    second_line = second_line.replace(first_line, "")

print(second_line)
