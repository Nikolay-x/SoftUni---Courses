# 3.Flattening Matrix
# Write a program that receives a matrix and prints the flattened version of it (a list with all the values). For example, the flattened list of the matrix: [[1, 2], [3, 4]] will be [1, 2, 3, 4].
# On the first line, you will receive the number of a matrix's rows. On the next rows, you will get the elements for each column separated with a comma and a space ", ".
#
# Input
# 2
# 1, 2, 3
# 4, 5, 6
#
# Output
# [1, 2, 3, 4, 5, 6]

n = int(input())
matrix = []

for _ in range(n):
    row = [int(x) for x in input().split(", ")]
    matrix.append(row)

result = [num for row in matrix for num in row]

print(result)
