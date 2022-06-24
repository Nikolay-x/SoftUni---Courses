# Numbers search
# Write a function called numbers_searching which receives a different amount of parameters. All parameters will be integer numbers forming a sequence of consecutive numbers. Your task is to find an unknown amount of duplicates from the given sequence and a missing value, such that all the duplicate values and the missing value are between the smallest and the biggest received number.
# The function should return a list with the last missing number as a first argument and a sorted list, containing the duplicates found, in ascending order.
# For example: if we have the following numbers: 1, 2, 4, 2, 5, 4 will return 3 as missing number and 2, 4 as duplicate numbers in the following format: [3, [2, 4]]
# Input
# There will be no input
# Parameters will be passed to your function
# Output
# The function should return a list in the following format: [missing number, [duplicate_numbers separated with comma and space]]
# Constraints
# The missing number will always be between the smallest and the biggest received number
#
# Input
# print(numbers_searching(1, 2, 4, 2, 5, 4))
#
# Output
# [3, [2, 4]]

def numbers_searching(*args):
    min_number = min(args)
    max_number = max(args)
    numbers_dict = {}
    missing_number = 0
    duplicate_values = []

    for num in range(min_number, max_number + 1):
        numbers_dict[num] = 0

    for arg in args:
        numbers_dict[arg] += 1

    for num in numbers_dict:
        if numbers_dict[num] == 0:
            missing_number = num
        if numbers_dict[num] > 1:
            duplicate_values.append(num)

    result = [missing_number, duplicate_values]
    return result


print(numbers_searching(1, 2, 4, 2, 5, 4))
print(numbers_searching(5, 5, 9, 10, 7, 8, 7, 9))
print(numbers_searching(50, 50, 47, 47, 48, 45, 49, 44, 47, 45, 44, 44, 48, 44, 48))
