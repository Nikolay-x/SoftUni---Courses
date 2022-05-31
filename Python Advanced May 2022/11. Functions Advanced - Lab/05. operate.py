# 5.Operate
# Write a function called operate that receives an operator ("+", "-", "*" or "/") as first argument and multiple numbers (integers) as additional arguments (*args). The function should return the result of the operator applied to all the numbers. For more clarification, see the examples below.
# Submit only your function in the Judge system.
# Note: Be careful when you have multiplication and division
#
# Test Code
# print(operate("+", 1, 2, 3))
# print(operate("*", 3, 4))
#
# Output
# 6
# 12

def operate(operator, *args):

    def add():
        result = 0
        for num in args:
            result += num
        return result

    # def add(*args):
    #     return sum(args)

    def subtract():
        result = args[0]
        for num in args[1:]:
            result += -num
        return result

    # def subtract(x, *args):
    #     return x + sum(-y for y in args)

    def multiply():
        result = 1
        for num in args:
            result *= num
        return result

    def divide():
        result = args[0]
        for num in args[1:]:
            result /= num
        return result

    if operator == "+":
        return add()
    elif operator == "-":
        return subtract()
    elif operator == "*":
        return multiply()
    elif operator == "/":
        return divide()


print(operate("+", 1, 2, 3))
print(operate("*", 3, 4))
