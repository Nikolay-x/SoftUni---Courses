# 8.Execution Time
# Import the time module. Create a decorator called exec_time. It should calculate how much time a function needs to be executed. See the examples for more clarification.
# Note: You might have different results from the given ones. The solutions to this problem cannot be submitted in the judge system.
#
# Test Code
# @exec_time
# def loop(start, end):
#     total = 0
#     for x in range(start, end):
#         total += x
#     return total
# print(loop(1, 10000000))
#
# Output
# 0.8342537879943848

from time import time


def exec_time(func_ref):
    def wrapper(*args):
        start_time = time()
        result = func_ref(*args)
        end_time = time()
        return f"Function {func_ref.__name__}{args} was called. It returned {result} for {end_time - start_time}s"

    return wrapper


@exec_time
def loop(start, end):
    total = 0
    for x in range(start, end):
        total += x
    return total


@exec_time
def concatenate(strings):
    result = ""
    for string in strings:
        result += string
    return result


@exec_time
def loop1():
    count = 0
    for i in range(1, 999999):
        count += 1
    return count


print(loop(1, 10000000))
print(concatenate(["a" for i in range(8)]))
print(loop1())
