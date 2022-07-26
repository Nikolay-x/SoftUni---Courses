# 4.Multiply
# Having the following code:
#
# def multiply(times):
#
#     def decorator(function):
#
#         # TODO: Implement
#
#     return decorator
#
# Complete the code, so it works as expected.
#
# Test Code
# @multiply(3)
# def add_ten(number):
#     return number + 10
#
# print(add_ten(3))
#
# Output
# 39

from functools import wraps


def multiply(times):
    def decorator(function):
        @wraps(function)
        def wrapper(*args):
            result = times * function(*args)
            return result
        return wrapper
    return decorator


@multiply(3)
def add_ten(number):
    return number + 10


print(add_ten(3))
print(add_ten.__name__)
print(add_ten.__doc__)


@multiply(5)
def add_ten(number):
    return number + 10


print(add_ten(6))
