# 5.Even Numbers
# Write a program that receives a sequence of numbers (integers) separated by a single space. It should print a list of only the even numbers. Use filter().
#
# Input
# 1 2 3 4
#
# Output
# [2, 4]
#
# # result = list(filter(lambda x: x % 2 == 0, list(map(int, input().split(" ")))))
# # print(result)
#
# # def check_even(number):
# #     if number % 2 == 0:
# #         return True
# #     return False
# # result = filter(check_even, list(map(int, input().split(" "))))
# # print(list(result))

def filter_even_numbers(n):

    filtered_list = []

    for i in n:
        if i % 2 == 0:
            filtered_list.append(i)
    return filtered_list

nums = list(map(int, input().split(" ")))

print(filter_even_numbers(nums))
