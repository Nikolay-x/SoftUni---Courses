# 8. *Letters Change Numbers
# John invented a game with numbers and letters from the English alphabet. The game was simple.
# You receive a string consisting of a number between two letters. For the given string, you should perform different mathematical operations to achieve a result:
# First, if the letter in front of the number is:
# oUppercase: divide the number by the letter's position in the alphabet (starting from 1)
# oLowercase: multiply the number with the letter's position in the alphabet (starting from 1)
# Next, if the letter after the number is:
# oUppercase: subtract its position from the resulting number (starting from 1)
# oLowercase: add its position to the resulting number (starting from 1)
# The game was too easy for John. He decided to complicate it by doing the same calculations to multiple strings keeping track of only the total sum of all results. Once he started to solve this with more strings and bigger numbers, it became quite hard to do it only in his mind.
# He kindly asks you to write a program that performs the operations described above and sums the final results of each string.
# Input
# The input comes from the console as a single line, holding a sequence of strings
# Strings are separated by one or more white spaces
# The input data will always be valid. There is no need to check it explicitly
# Output
# Print at the console a single number:
# oThe total sum of all processed numbers, formatted to the second decimal separator
# Constraints
# The count of the strings will be in the range [1 … 10]
# The numbers between the letters will be integers in the range [1 … 2 147 483 647]
# Time limit: 0.3 sec. Memory limit: 16 MB
#
# Input
# A12b s17G
#
# Output
# 330.00

# from string import ascii_lowercase
#
#
# def extract_func(text):
#     current_num = [num for num in text if num.isdigit()]
#     result = 0
#
#     for i in range(len(text)):
#         if text[i].isalpha():
#             index = ascii_lowercase.index(text[i].lower()) + 1
#
#             if i == 0:
#                 if text[i] == text[i].lower():
#                     result = int(''.join(current_num)) * index
#                 else:
#                     result = int(''.join(current_num)) / index
#             else:
#                 if text[i] == text[i].lower():
#                     result += index
#                 else:
#                     result -= index
#
#     return result
#
#
# def letters_change_numbers(data):
#     result = 0
#
#     for num in data:
#         result += extract_func(num)
#
#     print(f'{result:.2f}')
#
#
# input_data = input().split()
# letters_change_numbers(input_data)


import string

upper_cases = string.ascii_uppercase
lower_cases = string.ascii_lowercase

numbers_and_letters = input().split()
result = 0

for string in numbers_and_letters:
    d_m_operator = string[0]
    s_a_operator = string[-1]
    number = int(string[1:-1])
    string_result = 0

    for i in range(0, len(upper_cases)):
        if upper_cases[i] == d_m_operator:
            divide_operator = i + 1
        if upper_cases[i] == s_a_operator:
            subtract_operator = i + 1
    for q in range(0, len(lower_cases)):
        if lower_cases[q] == d_m_operator:
            multiply_operator = q + 1
        if lower_cases[q] == s_a_operator:
            add_operator = q + 1

    if d_m_operator.isupper():
        string_result += number / divide_operator
    elif d_m_operator.islower():
        string_result += number * multiply_operator

    if s_a_operator.isupper():
        string_result -= subtract_operator
    elif s_a_operator.islower():
        string_result += add_operator

    result += string_result

print(f"{result:.2f}")
