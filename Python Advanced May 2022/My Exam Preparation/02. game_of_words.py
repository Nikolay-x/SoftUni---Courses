# Problem 2 - Game of Words
# You will be given a string. Then, you will be given an integer N for the size of the field with square shape. On the next N lines, you will receive the rows of the field. The player will be placed on a random position, marked with "P". On random positions there will be letters. All of the empty positions will be marked with "-".
# Each turn you will be given commands for the player’s movement. If he moves to a letter, he consumes it, concatеnates it to the initial string and the letter disappears from the field. If he tries to move outside of the field, he is punished - he loses the last letter in the string, if there are any, and the player’s position is not changed.
# At the end print all letters and the field.
# Input
# On the first line, you are given the initial string
# On the second line, you are given the integer N - the size of the square matrix
# The next N lines holds the values for every row
# On the next line you receive a number M
# On the next M lines you will get a move command
# Output
# On the first line the final state of the string
# In the end print the matrix
# Constraints
# The size of the square matrix will be between [2…10]
# The player position will be marked with "P"
# The letters on the field will be any letter except for "P"
# Move commands will be: "up", "down", "left", "right"
#
# Input
# Hello
# 4
# P---
# Mark
# -l-y
# --e-
# 4
# down
# right
# right
# right
#
# Output
# HelloMark
# ----
# ---P
# -l-y
# --e-

def move_func(def_row, def_col, def_direction):

    if def_direction == "up":
        def_row -= 1
    elif def_direction == "down":
        def_row += 1
    elif def_direction == "left":
        def_col -= 1
    elif def_direction == "right":
        def_col += 1

    return def_row, def_col


string = input()
size = int(input())
field = []
player_row = 0
player_col = 0

for i in range(size):
    row = list(map(str, input()))
    if "P" in row:
        player_row = i
        player_col = row.index("P")
    field.append(row)

command_count = int(input())
for i in range(command_count):

    direction = input()
    field[player_row][player_col] = "-"

    next_row, next_col = move_func(player_row, player_col, direction)

    if 0 <= next_row < size and 0 <= next_col < size:
        player_row, player_col = next_row, next_col
        if field[player_row][player_col].isalpha():
            string += field[player_row][player_col]
    else:
        if string:
            string = string[0:-1]

    field[player_row][player_col] = "P"

print(string)
for row in field:
    print(f"{''.join(row)}")
