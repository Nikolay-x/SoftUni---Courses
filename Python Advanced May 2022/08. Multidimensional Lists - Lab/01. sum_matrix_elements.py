# 1.Sum Matrix Elements
# Write a program that reads a matrix from the console and prints:
# The sum of all numbers in the matrix
# The matrix itself
# On the first line, you will receive the matrix sizes in the format "{rows}, {columns}". On the next rows, you will get elements for each column separated by a comma and a space ", ".
#
# Input
# 3, 6
# 7, 1, 3, 3, 2, 1
# 1, 3, 9, 8, 5, 6
# 4, 6, 7, 9, 1, 0
#
# Output
# 76
# [[7, 1, 3, 3, 2, 1], [1, 3, 9, 8, 5, 6], [4, 6, 7, 9, 1, 0]]

rows, cols = [int(x) for x in input().split(", ")]
matrix = []
elements_sum = 0

for _ in range(rows):
    row = [int(x) for x in input().split(", ")]
    matrix.append(row)
    elements_sum += sum(row)

print(elements_sum)
print(matrix)
