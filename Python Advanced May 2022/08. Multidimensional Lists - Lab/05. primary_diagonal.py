# 5.Primary Diagonal
# Write a program that finds the sum of all numbers in a matrix's primary diagonal (runs from top left to bottom right). On the first line, you will receive an integer N – the size of a square matrix. The next N lines holds the values for each column - N numbers, separated by a single space.
#
# Input
# 3
# 11 2 4
# 4 5 6
# 10 8 -12
#
# Output
# 4

def get_primary_diagonal_sum(matrix, rows):
    primary_diagonal_sum = 0
    for index in range(rows):
        primary_diagonal_sum += matrix[index][index]
    return primary_diagonal_sum


# def get_secondary_diagonal_sum(matrix, rows):
#     secondary_diagonal_sum = 0
#     for index in range(rows):
#         secondary_diagonal_sum += matrix[index][rows - index - 1]
#     return secondary_diagonal_sum


n = int(input())
mm = []

for i in range(n):
    row = [int(x) for x in input().split()]
    mm.append(row)

print(get_primary_diagonal_sum(mm, n))
# print(get_secondary_diagonal_sum(mm, n))
