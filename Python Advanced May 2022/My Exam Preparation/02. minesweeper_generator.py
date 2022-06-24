# Minesweeper Generator
# Everybody remembers the old mines game. Now it is time to create your own.
#
# You will be given an integer n for the size of the mines field with square shape and another one for the number of bombs that you have to place in the field. On the next n lines, you will receive the position for each bomb. Your task is to create the game field placing the bombs at the correct positions and mark them with "*", and calculate the numbers in each cell of the field. Each cell represents a number of all bombs directly near it (up, down, left, right and the 4 diagonals).
#
# * 2 *
# 2 3 2
# 1 * 1
#
# Input
# On the first line, you are given the integer n – the size of the square matrix.
# On the second line – the number of the bombs.
# The next n lines holds the position of each bomb.
# Output
# Print the matrix you've created.
# Constraints
# The size of the square matrix will be between [2…15].
#
# Input
# 4
# 4
# (0, 3)
# (1, 1)
# (2, 2)
# (3, 0)
#
# Output
# 1 1 2 *
# 1 * 3 2
# 2 3 * 1
# * 2 1 1

def map_bomb_area(def_row, def_col, def_direction):
    if def_direction == "up":
        def_row -= 1
    elif def_direction == "down":
        def_row += 1
    elif def_direction == "left":
        def_col -= 1
    elif def_direction == "right":
        def_col += 1
    elif def_direction == "pr_d_up":
        def_row -= 1
        def_col -= 1
    elif def_direction == "pr_d_down":
        def_row += 1
        def_col += 1
    elif def_direction == "sec_d_up":
        def_row -= 1
        def_col += 1
    elif def_direction == "sec_d_down":
        def_row += 1
        def_col -= 1

    return def_row, def_col


size = int(input())
field = [[0 for x in range(size)] for _ in range(size)]
bombs_list = []

bombs_count = int(input())
for i in range(bombs_count):
    bomb_row, bomb_col = [int(x) for x in input().strip("(").strip(")").split(", ")]
    bombs_list.append((bomb_row, bomb_col))
    field[bomb_row][bomb_col] = "*"

directions = ["up", "down", "left", "right", "pr_d_up", "pr_d_down", "sec_d_up", "sec_d_down"]
for bomb in bombs_list:
    for direction in directions:
        current_row, current_col = bomb
        current_row, current_col = map_bomb_area(current_row, current_col, direction)
        if 0 <= current_row < size and 0 <= current_col < size and field[current_row][current_col] != "*":
            field[current_row][current_col] += 1

for row in field:
    print(*row)
