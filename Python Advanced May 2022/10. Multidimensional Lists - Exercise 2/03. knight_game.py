# 3.Knight Game
# Chess is the oldest game, but it is still popular these days. It will be used only one chess piece for this task - the Knight.
# A chess knight has 8 possible moves it can make, as illustrated. It can move to the nearest square but not on the same row, column, or diagonal. (e.g., it can move two squares horizontally, then one square vertically, or it can move one square horizontally then two squares vertically - i.e., in an "L" pattern.) 
# The knight game is played on a board with dimensions N x N.
# You will receive a board with "K" for knights and "0" for empty cells. Your task is to remove knights until no knights that can attack one another with one move are left.
# Input
# On the first line, you will receive integer N - the size of the board
# On the following N lines, you will receive strings with "K" and "0"
# Output
# Print a single integer with the minimum number of knights that need to be removed
# Constraints
# The size of the board will be 0 < N < 30
# Time limit: 0.3 sec. Memory limit: 16 MB
#
# Input
# 5
# 0K0K0
# K000K
# 00K00
# K000K
# 0K0K0
#
# Output
# 1

# def get_count(matrix, row, col):
#     moves = [
#         [row-2, col-1],
#         [row-2, col+1],
#         [row-1, col-2],
#         [row-1, col+2],
#         [row+1, col-2],
#         [row+1, col+2],
#         [row+2, col-1],
#         [row+2, col+1]
#     ]
#
#     result = 0
#     for r, c in moves:
#         if 0 <= r < len(matrix) and 0 <= c < len(matrix) and matrix[r][c] == "K":
#             result += 1
#     return result
#
#
# n = int(input())
#
# mm = []
# for _ in range(n):
#     mm.append(list(input()))
# removed_knights_counter = 0
#
# while True:
#     best_count = 0
#     knight_row = 0
#     knight_col = 0
#     for i in range(n):
#         for j in range(n):
#             if mm[i][j] == "0":
#                 continue
#             count = get_count(mm, i, j)
#             if count > best_count:
#                 best_count = count
#                 knight_row = i
#                 knight_col = j
#     if best_count == 0:
#         break
#
#     mm[knight_row][knight_col] = "0"
#     removed_knights_counter += 1
#
# print(removed_knights_counter)

def is_inside(row, col, size):
    return 0 <= row < size and 0 <= col < size


def get_targets(row, col, matrix):
    ts = []
    if is_inside(row-2, col+1, n) and matrix[row-2][col+1] == "K":
        ts.append((row-2, col+1))
    if is_inside(row-1, col+2, n) and matrix[row-1][col+2] == "K":
        ts.append((row-1, col+2))
    if is_inside(row+1, col+2, n) and matrix[row+1][col+2] == "K":
        ts.append((row+1, col+2))
    if is_inside(row+2, col+1, n) and matrix[row+2][col+1] == "K":
        ts.append((row+2, col+1))
    if is_inside(row+2, col-1, n) and matrix[row+2][col-1] == "K":
        ts.append((row+2, col-1))
    if is_inside(row+1, col-2, n) and matrix[row+1][col-2] == "K":
        ts.append((row+1, col-2))
    if is_inside(row-1, col-2, n) and matrix[row-1][col-2] == "K":
        ts.append((row-1, col-2))
    if is_inside(row-2, col-1, n) and matrix[row-2][col-1] == "K":
        ts.append((row-2, col-1))
    return ts


n = int(input())
mm = [[x for x in input()] for _ in range(n)]
knights = []
for i in range(n):
    for j in range(n):
        if mm[i][j] == "K":
            knights.append((i, j))

count = 0
while True:
    max_targets = 0
    knight_row = 0
    knight_col = 0
    for knight in knights:
        r, c = knight
        targets = get_targets(r, c, mm)
        if len(targets) > max_targets:
            max_targets = len(targets)
            knight_row = r
            knight_col = c
    if max_targets > 0:
        mm[knight_row][knight_col] = "0"
        knights.remove((knight_row, knight_col))
    else:
        break
    count += 1

print(count)
