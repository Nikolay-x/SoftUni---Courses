# 4.Maximal Sum
# Write a program that reads a rectangular matrix's dimensions and finds the 3x3 square with a maximum sum of its elements. There will be no case with two or more 3x3 squares with equal maximal sum.
# Input
# On the first line, you will receive the rows and columns in the format "{rows} {columns}" – integers in the range [1, 20]
# On the following lines, you will receive each row with its columns - integers, separated by a single space in the range [-20, 20]
# Output
# On the first line, print the maximum sum of the elements in the 3x3 square in the format "Sum = {sum}"
# On the following 3 lines, print each element of the found submatrix, separated by a single space
#
# Input
# 4 5
# 1 5 5 2 4
# 2 1 4 14 3
# 3 7 11 2 8
# 4 8 12 16 4
#
# Output
# Sum = 75
# 1 4 14
# 7 11 2
# 8 12 16

def get_sum(matrix, row, col):
    return matrix[row][col] + matrix[row][col+1] + matrix[row][col+2] + \
           matrix[row+1][col] + matrix[row+1][col+1] + matrix[row+1][col+2] + \
           matrix[row+2][col] + matrix[row+2][col+1] + matrix[row+2][col+2]


def get_matrix(matrix, row, col):
    result = [
        [matrix[row][col], matrix[row][col + 1], matrix[row][col + 2]],
        [matrix[row + 1][col], matrix[row + 1][col + 1], matrix[row + 1][col + 2]],
        [matrix[row + 2][col], matrix[row + 2][col + 1], matrix[row + 2][col + 2]]
    ]
    return result


n, m = [int(x) for x in input().split()]
mm = [[int(x) for x in input().split()] for _ in range(n)]
max_sum = float('-inf')
max_mm = []

for i in range(n - 2):
    for j in range(m - 2):
        current_sum = get_sum(mm, i, j)
        if current_sum > max_sum:
            max_sum = current_sum
            max_mm = get_matrix(mm, i, j)

print(f'Sum = {max_sum}')
for i in range(3):
    print(" ".join(str(x) for x in max_mm[i]))
