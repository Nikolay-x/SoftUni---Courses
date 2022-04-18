# 6.Sort
# Write a program that receives a sequence of numbers (integers) separated by a single space. It should print a sorted list of numbers in ascending order. Use sorted().
#
# Input
# 6 2 4
#
# Output
# [2, 4, 6]
#
# # x = lambda y: sorted(y)
# #
# # num = list(map(int, input().split(" ")))
# # print(x(num))

def ascending_order(n):
    n.sort(reverse=False)
    print(n)
    # n.sort(reverse=True)
    # print(f"descending order = {n}")

nums = list(map(int, input().split(" ")))

ascending_order(nums)
