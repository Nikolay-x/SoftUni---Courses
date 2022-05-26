# 6.Symbol in Matrix
# Write a program that reads a number - N, representing the rows and columns of a square matrix. On the next N lines, you will receive rows of the matrix. Each row consists of ASCII characters. After that, you will receive a symbol. Find the first occurrence of that symbol in the matrix and print its position in the format: "({row}, {col})". You should start searching from the top left. If there is no such symbol, print the message "{symbol} does not occur in the matrix".
#
# Input
# 3
# ABC
# DEF
# X!@
# !
#
# Output
# (2, 1)

# def find_symbol(matrix, symbol):
#     # for row_index in range(n):
#     #     for col_index in range(n):
#     #         if matrix[row_index][col_index] == symbol:
#     #             return row_index, col_index
#
#     for row_index in range(n):
#         if symbol in matrix[row_index]:
#             col_index = matrix[row_index].index(symbol)
#             return row_index, col_index
#
#
# n = int(input())
# mm = [list(input()) for _ in range(n)]
# s = input()
#
# if find_symbol(mm, s):
#     print(find_symbol(mm, s))
# else:
#     print(f"{s} does not occur in the matrix")

n = int(input())
mm = []

for _ in range(n):
    row = list(input())
    mm.append(row)

s = input()
symbol_found = False

for i in range(n):
    if symbol_found:
        break
    for j in range(n):
        if mm[i][j] == s:
            print((i, j))
            symbol_found = True
            break

if not symbol_found:
    print(f"{s} does not occur in the matrix")
