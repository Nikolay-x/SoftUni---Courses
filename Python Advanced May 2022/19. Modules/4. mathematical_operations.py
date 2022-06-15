# 4.Mathematical operations
# Create a module that does basic calculations. You will receive 2 numbers and a sign between them all in one string
# Input
# You will receive a single string in the following format
# "{number1} {sign} {number2}"
# onumber1 - a float number in the range (0.0, 1000.0)
# osign - a char that can be
# '/' - divide the first number with the second
# '*' - multiply the 2 numbers
# '-' - subtract the first number with the second
# '+' - add the 2 numbers
# '^' - raise the first number to the second
# onumber2 - an integer number in the range (0, 1000)
# Output
# Print only the result of the operation
# The result should be formatted to the second decimal point
#
# Input
# 2.5 * 2
#
# Output
# 5.00

# from math_op import math_operations
from math_op.math_operations import operations

input_data = input()

# math_operations.operations(input_data)
operations(input_data)
