# 1.Logged
# Create a decorator called logged. It should return the name of the function that is being called and its parameters. It should also return the result of the execution of the function being called. See the examples for more clarification.
#
# Test Code
# @logged
# def func(*args):
#     return 3 + len(args)
# print(func(4, 4, 4))
#
# Output
# you called func(4, 4, 4)
# it returned 6

def logged(func_ref):
    def wrapper(*args):
        result = func_ref(*args)
        return f"you called {func_ref.__name__}({args})\nit returned {result}"
    return wrapper


@logged
def func(*args):
    return 3 + len(args)


@logged
def sum_func(a, b):
    return a + b


print(func(4, 4, 4))
print(sum_func(1, 4))
