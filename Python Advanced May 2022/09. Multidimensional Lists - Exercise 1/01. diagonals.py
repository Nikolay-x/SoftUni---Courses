# 1.Diagonals
# Using a nested list comprehension, write a program that reads rows of a square matrix and its elements, separated
# by a comma and a space ", ". You should find the matrix's diagonals, prints them and their sum in the format:
# "Primary diagonal: {element1}, {element2}, … {elementN}. Sum: {sum_of_primary}
# Secondary diagonal: {element1}, {element2}, … {elementN}. Sum: {sum_of_secondary}".
#
# Input
# 3
# 1, 2, 3
# 4, 5, 6
# 7, 8, 9
#
# Output
# Primary diagonal: 1, 5, 9. Sum: 15
# Secondary diagonal: 3, 5, 7. Sum: 15

n = int(input())
matrix = []
for _ in range(n):
    row = [int(x) for x in input().split(', ')]
    matrix.append(row)

primary_diagonal = []
secondary_diagonal = []

for i in range(n):
    primary_diagonal.append(matrix[i][i])
    secondary_diagonal.append(matrix[i][n-1 - i])

print(f'Primary diagonal: {", ".join([str(x) for x in primary_diagonal])}. Sum: {sum(primary_diagonal)}')
print(f'Secondary diagonal: {", ".join([str(x) for x in secondary_diagonal])}. Sum: {sum(secondary_diagonal)}')
