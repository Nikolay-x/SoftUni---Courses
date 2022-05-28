# 3.2x2 Squares in Matrix
# Find the number of all 2x2 squares containing identical chars in a matrix. On the first line, you will receive the matrix's dimensions in the format "{rows} {columns}". On the following rows, you will receive characters separated by a single space. Print the number of all square matrices you have found.
#
# Input
# 3 4
# A B B D
# E B B B
# I J B B
#
# Output
# 2

def identical_chars_square(matrix, row, col):
    return matrix[row][col] == matrix[row][col + 1] == \
           matrix[row + 1][col] == matrix[row + 1][col + 1]


n, m = [int(x) for x in input().split()]
mm = [[x for x in input().split()] for _ in range(n)]
count = 0

for i in range(n - 1):
    for j in range(m - 1):
        if identical_chars_square(mm, i, j):
            count += 1

print(count)
