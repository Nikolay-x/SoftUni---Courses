# 2.Multiples List
# Write a program that receives two numbers (factor and count). It should create a list with a length of the given count that contains only integer numbers, which are multiples of the given factor. The numbers should be only positive, and they should be arranged in ascending order, starting from the value of the factor.
#
# Input
# 2
# 5
#
# Output
# [2, 4, 6, 8, 10]

factor = int(input())
count = int(input())

list = list()

for i in range(1, count+1):
    list.append(i * factor)

print(list)
