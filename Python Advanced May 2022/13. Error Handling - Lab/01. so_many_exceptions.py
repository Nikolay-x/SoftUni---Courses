# 1.So Many Exceptions
# You are provided with the following code:
#
# numbers_list = input().split(", ")
# result = 0
#
# for i in range(numbers_list):
#     number = numbers_list[i + 1]
#     if number < 5:
#         result *= number
#     elif number > 5 and number > 10:
#         result /= number
#
# print(result)
#
# This code raises many exceptions. Fix it, so it works correctly.
#
# Input
# 1, 4, 5
# 4, 5, 6, 1, 3
# 2, 5, 10
#
# Output
# 20
# 10
# 1

# import sys
# from io import StringIO
#
# test_input1 = '''1, 4, 5
# '''
#
# test_input2 = '''4, 5, 6, 1, 3
# '''
#
# test_input3 = '''2, 5, 10
# '''
#
# # sys.stdin = StringIO(test_input1)
# # sys.stdin = StringIO(test_input2)
# sys.stdin = StringIO(test_input3)
#
# numbers_list = [int(x) for x in input().split(", ")]
# result = 1
#
# for i in range(len(numbers_list)):
#     number = numbers_list[i]
#     if number <= 5:
#         result *= number
#     elif number <= 10:
#         result /= number
#
# print(result)
#
# print(f'''Expected:
# 20
# 10
# 1''')

numbers_list = [int(x) for x in input().split(", ")]
result = 1

for i in range(len(numbers_list)):
    number = numbers_list[i]
    if number <= 5:
        result *= number
    elif 5 < number <= 10:
        result /= number

print(result)
