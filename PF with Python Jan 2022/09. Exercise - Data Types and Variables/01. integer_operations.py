# 1.Integer Operations
# Write a program that reads four integer numbers. It should add the first to the second number, integer divide the sum by the third number, and multiply the result by the fourth number. Print the final result.
#
# Input
# 10
# 20
# 3
# 3
#
# Output
# 30

a = int(input())
b = int(input())
c = int(input())
d = int(input())

result = int((a + b) / c) * d

print(result)
