# Problem 3 - Magic Triangle
# Create a function called get_magic_triangle which will receive a single parameter (integer n) and it should create a magic triangle which follows those rules:
# We start with this simple triangle [[1], [1, 1]]
# We generate the next rows until we reach n amount of rows
# Each number in each row is equal to the sum of the two numbers right above it in the triangle
# If the current number has no neighbor to the upper left/right, we just take the existing neighbor
# After you create the magic triangle, return it as a multidimensional list. Here is an example with n = 5
#
#     1
#    1 1
#   1 2 1
#  1 3 3 1
# 1 4 6 4 1
#
# Note: Submit only the function in the judge system
# Input
# There will be no inputs
# The function will be tested by passing different values of n
# You can test your function with the test code below
# Constraints
# N will be in range [2, 100]
#
# Test Code
# print(get_magic_triangle(5))
#
# Output
# [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]

def get_magic_triangle(n):
    result = []

    # for i in range(1, n+1):
    #     if i == 1:
    #         result.append([1])
    #     elif i == 2:
    #         result.append([1, 1])
    #     else:
    #         row = []
    #         for j in range(i):
    #             if j == 0 or j == i - 1:
    #                 next_number = 1
    #             else:
    #                 next_number = result[i - 2][j] + result[i - 2][j - 1]
    #             row.append(next_number)
    #         result.append(row)

    for i in range(0, n):
        if i == 0:
            result.append([1])
        elif i == 1:
            result.append([1, 1])
        else:
            row = []
            for j in range(i+1):
                if j == 0 or j == i:
                    next_number = 1
                else:
                    next_number = result[i - 1][j] + result[i - 1][j - 1]
                row.append(next_number)
            result.append(row)

    return result


print(get_magic_triangle(5))
