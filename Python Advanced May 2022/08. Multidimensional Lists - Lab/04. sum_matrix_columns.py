# 4.Sum Matrix Columns
# Write a program that reads a matrix from the console and prints the sum for each column on separate lines.
# On the first line, you will get matrix sizes in format "{rows}, {columns}". On the next rows, you will get elements for each column separated with a single space.
#
# Input
# 3, 6
# 7 1 3 3 2 1
# 1 3 9 8 5 6
# 4 6 7 9 1 0
#
# Output
# 12
# 10
# 19
# 20
# 8
# 7


import sys
from io import StringIO

test_input1 = '''3, 6
7 1 3 3 2 1
1 3 9 8 5 6
4 6 7 9 1 0
'''

test_input2 = '''3, 3
1 2 3
4 5 6
7 8 9
'''

# sys.stdin = StringIO(test_input1)
# sys.stdin = StringIO(test_input2)


# def get_columns_sums(matrix, rows_count, columns_count):
#     cols_sum = [0 for _ in range(m)]#
#     for row_index in range(rows_count):
#         for col_index in range(columns_count):
#             cols_sum[col_index] += matrix[row_index][col_index]
#     return cols_sum
#
#
# n, m = [int(x) for x in input().split(", ")]
# input_matrix = []
#
# for _ in range(n):
#     row = [int(x) for x in input().split()]
#     input_matrix.append(row)
#
# [print(x) for x in get_columns_sums(input_matrix, n, m)]


# def get_columns_sums2(matrix, rows_count, columns_count):
#     cols_sum = []
#     for col_index in range(columns_count):
#         cols_sum.append(0)
#         for row_index in range(rows_count):
#             cols_sum[-1] += matrix[row_index][col_index]
#     return cols_sum
#
#
# n, m = [int(x) for x in input().split(", ")]
# input_matrix = []
#
# for _ in range(n):
#     row = [int(x) for x in input().split()]
#     input_matrix.append(row)
#
# [print(x) for x in get_columns_sums2(input_matrix, n, m)]


n, m = [int(x) for x in input().split(", ")]
matrix = []

for _ in range(n):
    row = [int(x) for x in input().split()]
    matrix.append(row)

cols_sum = [0 for _ in range(m)]

for row_index in range(n):
    for col_index in range(m):
        cols_sum[col_index] += matrix[row_index][col_index]

# [print(x) for x in cols_sum]

for col_sum in cols_sum:
    print(col_sum)
