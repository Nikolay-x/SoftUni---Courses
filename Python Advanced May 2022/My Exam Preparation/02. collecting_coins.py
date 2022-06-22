# 02. Collecting Coins
# You are playing a game, and your goal is to collect 100 coins.
# On the first line, you will be given a number representing the size of the field with a square shape. On the following few lines, you will be given the field with:
# One player - randomly placed in it and marked with the symbol "P"
# Numbers for coins placed at different positions of the field
# Walls marked with "X"
# After the field state, you will be given commands for the player's movement. Commands can be: "up", "down", "left", "right". If the command is invalid, you should ignore it.
# The player moves in the given direction with one step for each command and collects all the coins that come across. If he goes out of the field, he should continue to traverse the field from the opposite side in the same direction.
# Note: He can go through the same path many times, but he can collect the coins just once (the first time).
# There are only two possible outcomes of the game:
# The player hits a wall, loses the game, and his coins are reduced to 50% and rounded down to the next-lowest number.
# The player collects at least 100 coins and wins the game.
# For more clarifications, see the examples below.
# Input
# A number representing the size of the field (matrix NxN)
# A matrix representing the field (each position separated by a single space)
# On each of the following lines, you will get a move command.
# Output
# If the player won the game, print: "You won! You've collected {total_coins} coins."
# If the player loses the game, print: "Game over! You've collected {total_coins} coins."
# Collected coins have to be rounded down to the next-lowest number.
# The player's path as cooridnates in lists on separate lines:
# "Your path:
# [{row_position1}, {column_position1}]
# [{row_position2}, {column_position2}]
# …
# [{row_positionN}, {column_positionN}]"
# Constrains
# There will be no case in which less than 100 coins will be in the field
# All given numbers will be valid integers in the range [0, 100]
#
# Input
# 5
# 1 X 7 9 11
# X 14 46 62 0
# 15 33 21 95 X
# P 14 3 4 18
# 9 20 33 X 0
# left
# right
# right
# up
# up
# right
#
# Output
# You won! You've collected 125 coins.
# Your path:
# [3, 0]
# [3, 4]
# [3, 0]
# [3, 1]
# [2, 1]
# [1, 1]
# [1, 2]

from math import floor


def get_player_location(def_row, def_col, def_size, def_direction):
    if def_direction == "up":
        def_row -= 1
        if def_row < 0:
            def_row = def_size - 1

    elif def_direction == "down":
        def_row += 1
        if def_row > def_size - 1:
            def_row = 0

    elif def_direction == "left":
        def_col -= 1
        if def_col < 0:
            def_col = def_size - 1

    elif def_direction == "right":
        def_col += 1
        if def_col > def_size - 1:
            def_col = 0

    return def_row, def_col


size = int(input())
board = []
player_row = 0
player_col = 0
player_coins = 0
path = []
game_over = False

for i in range(size):
    row = input().split(" ")
    if "P" in row:
        player_row = i
        player_col = row.index("P")
    board.append(row)

path.append((player_row, player_col))

directions = ["up", "down", "left", "right"]
while player_coins < 100:
    direction = input()
    if direction not in directions:
        continue
    player_row, player_col = get_player_location(player_row, player_col, size, direction)
    path.append((player_row, player_col))
    if board[player_row][player_col].isnumeric():
        player_coins += int(board[player_row][player_col])
        board[player_row][player_col] = "0"
    elif board[player_row][player_col] == "X":
        player_coins /= 2
        game_over = True
        break

if not game_over:
    print(f"You won! You've collected {floor(player_coins)} coins.")
else:
    print(f"Game over! You've collected {floor(player_coins)} coins.")
print("Your path:")
for point in path:
    print(f"[{point[0]}, {point[1]}]")
