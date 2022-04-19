# 2.ASCII Sumator
# Write a program that prints the sum of all found characters between two given characters (their ASCII code). On each of the first two lines, you will receive a single character. On the last line, you get a random string. Print the sum of the ASCII values of all characters in the random string between the two given characters in the ASCII table.
#
# Input
# .
# @
# dsg12gr5653feee5
#
# Output
# 363

start = ord(input())
end = ord(input())
line = input()
result = 0

for ch in line:
    if start < ord(ch) < end:
        result += ord(ch)

print(result)
