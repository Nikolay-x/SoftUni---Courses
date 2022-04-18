# 4.Sum of Chars
# Write a program, which sums the ASCII codes of N characters and prints the sum on the console. On the first line, you will receive N – the number of lines. On the following N lines – you will receive a letter per line. Print the total sum in the following format: "The sum equals: {total_sum}".
# Note: n will be in the interval [1…20].
#
# Input
# 5
# A
# b
# C
# d
# E
#
# Output
# The sum equals: 399

n = int(input())

total_sum = 0

for i in range(n):
    letter = input()
    total_sum += ord(letter)

print(f"The sum equals: {total_sum}")
