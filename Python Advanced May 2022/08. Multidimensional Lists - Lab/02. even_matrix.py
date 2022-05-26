# 2.Even Matrix
# Write a program that receives a matrix of numbers and prints a new one only with the numbers that are even. Use nested comprehension for that problem.
# On the first line, you will receive the rows of the matrix. On the next rows, you will get elements for each column separated with a comma and a space ", ".
#
# Input
# 2
# 1, 2, 3
# 4, 5, 6
#
# Output
# [[2], [4, 6]]

# n = int(input())
# matrix = [[int(x) for x in input().split(", ")] for _ in range(n)]
# print([[x for x in row if x % 2 == 0] for row in matrix])

# n = int(input())
# print([[x for x in row if x % 2 == 0] for row in [[int(x) for x in input().split(", ")] for _ in range(n)]])

rows = int(input())
matrix = []

for _ in range(rows):
    row = [int(x) for x in input().split(", ")]
    matrix.append(row)

result = []

for row in matrix:
    row = [x for x in row if x % 2 == 0]
    result.append(row)

# evens = [[x for x in row if x % 2 == 0] for row in matrix]
# print(evens)

print(result)
