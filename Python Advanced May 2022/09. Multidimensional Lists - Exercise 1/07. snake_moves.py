# 7.Snake Moves
# You are tasked to visualize a snake's zigzag path in a rectangular matrix with a size N x M.
# A string represents the snake. It starts moving from the top-left corner to the right. When the snake reaches the end of the row, it slithers its way down to the next row and turns left. The moves are repeated to the very end.
# The first cell is filled with the first symbol of the snake. The second cell is filled with the second symbol, etc. The snake's path is as long as it takes to fill the matrix completely - if you reach the end of the string representing the snake, start again at the first symbol. In the end, you should print the snake's path.
# Input
# The input data consists of exactly two lines:
# On the first line, you will receive the dimensions N x M of the field in format: "{rows} {columns}".
# On the second line, you will receive the string representing the snake
# Output
# You should print the snake's zigzag path of size N x M (rows x columns)
# Constraints
# The dimensions N and M of the matrix will be integers in the range [1 … 12]
# The snake will be a string with length in the range [1 … 20] and will not contain any whitespace characters
#
# Input
# 5
# 6
# SoftUni
#
# Output
# SoftUn
# UtfoSi
# niSoft
# foSinU
# tUniSo

# rows, cols = [int(x) for x in input().split()]
# word = input()
# index = 0
#
# for row in range(rows):
#     elements = [None] * cols
#     start, end, step = (0, cols, 1) if row % 2 == 0 else (cols-1, -1, -1)
#     for col in range(start, end, step):
#         elements[col] = word[index % len(word)]
#         index += 1
#     print("".join(elements))

n, m = [int(x) for x in input().split()]
word = input()
matrix = [["None" for x in range(m)] for _ in range(n)]
index = 0

for i in range(n):
    if i % 2 == 0:
        for j in range(0, m, 1):
            matrix[i][j] = word[index % len(word)]
            index += 1
    else:
        for j in range(m-1, -1, -1):
            matrix[i][j] = word[index % len(word)]
            index += 1

for row in matrix:
    print(*row, sep="")
