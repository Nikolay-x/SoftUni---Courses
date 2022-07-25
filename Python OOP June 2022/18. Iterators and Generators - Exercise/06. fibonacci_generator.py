# 6.Fibonacci Generator
# Create a generator function called fibonacci() that generates the Fibonacci numbers infinitely. The first two numbers in the sequence are always 0 and 1. Each following Fibonacci number is created by the sum of the current number with the previous one.
# Note: Submit only the function in the judge system
#
# Test Code
# generator = fibonacci()
# for i in range(5):
#     print(next(generator))
#
# Output
# 0
# 1
# 1
# 2
# 3

def fibonacci():
    first_num = 0
    yield first_num
    second_num = 1
    yield second_num
    while True:
        following_number = second_num + first_num
        yield following_number
        second_num, first_num = following_number, second_num


generator = fibonacci()
for i in range(5):
    print(next(generator))
