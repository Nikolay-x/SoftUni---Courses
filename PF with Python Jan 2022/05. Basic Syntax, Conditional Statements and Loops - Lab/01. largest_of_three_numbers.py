# 1.Largest of Three Numbers
# Write a program that receives three whole numbers and prints the largest one.
#
# Input
# 3
# -1
# 5
#
# Output
# 5

a = int(input())
b = int(input())
c = int(input())

max_num = a

if a >= b and a >= c:
    max_num = a
if b >= a and b >= c:
    max_num = b
if c >= a and c >= b:
    max_num = c

print(max_num)
