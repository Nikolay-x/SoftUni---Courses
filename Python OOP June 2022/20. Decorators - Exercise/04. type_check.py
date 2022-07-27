# 4.Type Check
# Create a decorator called type_check. It should receive a type (int/float/str/…), and it should check if the parameter passed to the decorated function is of the type given to the decorator. If it is, execute the function and return the result, otherwise return "Bad Type".
#
# Test Code
# @type_check(int)
# def times2(num):
#     return num*2
# print(times2(2))
# print(times2('Not A Number'))
#
# Output
# 4
# Bad Type

def type_check(input_type):
    def decorator(func_ref):
        def wrapper(*args):
            for arg in args:
                if type(arg) != input_type:
                    return "Bad Type"
            return func_ref(*args)

        return wrapper

    return decorator


@type_check(int)
def times2(num):
    return num*2


@type_check(str)
def first_letter(word):
    return word[0]


print(times2(2))
print(times2('Not A Number'))

print(first_letter('Hello World'))
print(first_letter(['Not', 'A', 'String']))
