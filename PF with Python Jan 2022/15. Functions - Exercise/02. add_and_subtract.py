# 2.Add and Subtract
# You will receive three integer numbers.
# Write functions named:
# sum_numbers() that returns the sum of the first two integers
# subtract() that returns the difference between the returned result of the first function and the third integer
# Wrap the two functions in a function named add_and_subtract() which will receive the three numbers as parameters. Print the result of the subtract() function on the console.
#
# Input
# 23
# 6
# 10
#
# Output
# 19

def sum_numbers(a, b):
    return a + b

def subtract(sum, c):
    return sum - c

def add_and_subtract(a, b, c):
    return subtract(sum_numbers(a, b), c)

num1 = int(input())
num2 = int(input())
num3 = int(input())

result = add_and_subtract(num1, num2, num3)

print(result)
