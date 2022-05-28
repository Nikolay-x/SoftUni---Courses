# 2.Diagonal Difference
# Write a program that finds the difference between the sums of the square matrix diagonals (absolute value).
#
# On the first line, you will receive an integer N - the size of a square matrix. The following N lines hold the values for each column - N numbers separated by a single space. Print the absolute difference between the primary and the secondary diagonal sums.
#
# Input
# 3
# 11 2 4
# 4 5 6
# 10 8 -12
#
# Output
# 15

n = int(input())
matrix = [[int(x) for x in input().split()] for _ in range(n)]
primary_diagonal = []
secondary_diagonal = []

for i in range(n):
    primary_diagonal.append(matrix[i][i])
    secondary_diagonal.append(matrix[i][n-1 - i])

print(abs(sum(primary_diagonal) - sum(secondary_diagonal)))
