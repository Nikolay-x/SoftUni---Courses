# 4.Squares
# Create a generator function called squares that should receive a number n. It should generate the squares of all numbers from 1 to n (inclusive).
# Note: Submit only the function in the judge system
#
# Test Code
# print(list(squares(5)))
#
# Output
# [1, 4, 9, 16, 25]

def squares(n):
    i = 1
    while i < n + 1:
        yield i ** 2
        i += 1


print(list(squares(5)))
