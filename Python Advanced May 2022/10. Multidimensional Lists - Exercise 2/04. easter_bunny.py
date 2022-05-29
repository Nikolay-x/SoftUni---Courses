# 4.Easter Bunny
# Your task is to collect as many eggs as possible.
# On the first line, you will be given a number representing the size of the field. On the following few lines, you will be given a field with:
# One bunny - randomly placed in it and marked with the symbol "B"
# Number of eggs placed at different positions of the field and traps marked with "X"
# Your job is to determine the direction in which the bunny should go to collect the maximum number of eggs. The directions that should be considered as possible are up, down, left, and right. If you reach a trap while checking some of the directions, you should not consider the fields after the trap in this direction. For more clarifications, see the examples below.
# Note: Consider ONLY the paths from which the bunny has collected 1 or more eggs.
# Input
# A number representing the size of the field
# The matrix representing the field (each position separated by a single space)
# Output
# The direction which should be considered as best (lowercase)
# The field positions from which we are collecting eggs as lists
# The total number of eggs collected
# Constraints
# There will NOT be two or more paths consisting of the same total amount of eggs.
#
# Input
# 5
# 1 3 7 9 11
# X 5 4 X 63
# 7 3 21 95 1
# B 1 73 4 9
# 9 2 33 2 0
#
# Output
# right
# [3, 1]
# [3, 2]
# [3, 3]
# [3, 4]
# 87

# n = int(input())
# mm = []
#
# bunny_row = 0
# bunny_col = 0
#
# for row in range(n):
#     row_el = input().split()
#     for col in range(n):
#         if row_el[col] == "B":
#             bunny_row = row
#             bunny_col = col
#     mm.append(row_el)
#
# directions = {
#     'right': lambda r, c: (r, c+1),
#     'left': lambda r, c: (r, c-1),
#     'up': lambda r, c: (r-1, c),
#     'down': lambda r, c: (r+1, c)
# }
#
# best_sum = float('-inf')
# best_dir = ''
# best_path = []
#
# for direction in directions:
#     current_sum = 0
#     row, col = directions[direction](bunny_row, bunny_col)
#     current_path = []
#
#     while 0 <= row < n and 0 <= col < n and mm[row][col] != "X":
#         current_sum += int(mm[row][col])
#         current_path.append([row, col])
#         row, col = directions[direction](row, col)
#
#     if current_sum > best_sum and current_path:
#         best_sum = current_sum
#         best_dir = direction
#         best_path = current_path
#
# print(best_dir)
# print(*best_path, sep='\n')
# print(best_sum)

def is_inside(def_row, def_col, size):
    return 0 <= def_row < size and 0 <= def_col < size


def get_bunny_location(direction, start_row, start_col):
    r, c = start_row, start_col
    if direction == "left":
        r, c = start_row, start_col-1
    elif direction == "right":
        r, c = start_row, start_col+1
    elif direction == "up":
        r, c = start_row-1, start_col
    elif direction == "down":
        r, c = start_row+1, start_col

    return r, c


n = int(input())
mm = [[x for x in input().split()] for _ in range(n)]
bunny_row = 0
bunny_col = 0

for row in range(n):
    for col in range(n):
        if mm[row][col] == "B":
            bunny_row = row
            bunny_col = col

directions = ["up", "down", "left", "right"]
best_eggs_sum = float('-inf')
best_dir = ""
best_path = []

for d in directions:
    eggs = 0
    row, col = get_bunny_location(d, bunny_row, bunny_col)
    eggs_coordinates = []

    while is_inside(row, col, n) and mm[row][col] != "X":
        eggs += int(mm[row][col])
        eggs_coordinates.append([row, col])
        row, col = get_bunny_location(d, row, col)

    if eggs > best_eggs_sum and eggs_coordinates:
        best_eggs_sum = eggs
        best_dir = d
        best_path = eggs_coordinates

print(best_dir)
print(*best_path, sep='\n')
print(best_eggs_sum)
