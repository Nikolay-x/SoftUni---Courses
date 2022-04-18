# 3.Calculations
# Create a function that receives three parameters, calculates a result depending on the given operator, and returns it. Print the result of the function.
# The input comes as three parameters – an operator as a string and two integer numbers. The operator can be one of the following:  "multiply", "divide", "add", "subtract".
#
# Input
# subtract
# 5
# 4
#
# Output
# 1

def calculator(a, b, operator):
    result = None
    if operator == "multiply":
        result = a * b
    elif operator == "divide":
        result = int(a / b)
    elif operator == "add":
        result = a + b
    elif operator == "subtract":
        result = a - b
    return result

input_operator = input()
a_num = int(input())
b_num = int(input())

print(calculator(a_num, b_num, input_operator))
