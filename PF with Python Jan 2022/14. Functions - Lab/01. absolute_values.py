# 1.Absolute Values
# Write a program that receives a sequence of numbers, separated by a single space, and prints their absolute value as a list. Use abs().
#
# Input
# 1 2.5 -3 -4.5
#
# Output
# [1.0, 2.5, 3.0, 4.5]

num_seq = input().split(" ")

abs_list = []

for num in num_seq:
    current_num = abs(float(num))
    abs_list.append(current_num)

print(abs_list)
