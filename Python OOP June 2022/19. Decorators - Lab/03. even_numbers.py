# 3.Even Numbers
# Having the following code:
#
# def even_numbers(function):
#
#     def wrapper(numbers):
#
#         # TODO: Implement
#
#     return wrapper
#
# Complete the code, so it works as expected.
#
# Test Code
# @even_numbers
# def get_numbers(numbers):
#     return numbers
# print(get_numbers([1, 2, 3, 4, 5]))
#
# Output
# [2, 4]

from functools import wraps


def even_numbers(function):
    @wraps(function)
    def wrapper(numbers):
        result = function(numbers)
        even_nums = [x for x in result if x % 2 == 0]
        return even_nums
    return wrapper


@even_numbers
def get_numbers(numbers):
    return numbers


print(get_numbers([1, 2, 3, 4, 5]))
print(get_numbers.__name__)
print(get_numbers.__doc__)
