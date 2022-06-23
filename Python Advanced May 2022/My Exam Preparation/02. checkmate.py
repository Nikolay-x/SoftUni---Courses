# 02. Checkmate
# You will be given a chess board (8x8). On the board there will be 3 types of symbols:
# "." – empty square
# "Q" – a queen
# "K" – the king
# Your job is to find which queens can capture the king and print them. The moves that the queen can do is to move diagonally, horizontally and vertically (basically all the moves that all the other figures can do except from the knight). Beware that there might be queens that stand in the way of other queens and can stop them from capturing the king. For more clarification see the examples.
# Input
# 8 lines – the state of the board (each square separated by single space)
# Output
# The positions of the queens that can capture the king as lists
# If the king cannot be captured, print: "The king is safe!"
# The order of output does not matter
# Constrains
# There will always be exactly 8 lines
# There will always be exactly one King
# Only the 3 symbols described above will be present in the input
#
# Input
# . . . . . . . .
# Q . . . . . . .
# . K . . . Q . .
# . . . Q . . . .
# Q . . . Q . . .
# . Q . . . . . .
# . . . . . . Q .
# . Q . Q . . . .
#
# Output
# [2, 5]
# [5, 1]
# [1, 0]

def move_func(def_row, def_col, def_direction):

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


chess_board_size = 8
chess_board = []
king_row = 0
king_col = 0
queens_list = []

for i in range(chess_board_size):
    row = input().split(" ")
    if "K" in row:
        king_row = i
        king_col = row.index("K")
    chess_board.append(row)

directions = ["up", "down", "left", "right", "pr_d_up", "pr_d_down", "sec_d_up", "sec_d_down"]
for direction in directions:
    current_row, current_col = king_row, king_col
    while 0 <= current_row < chess_board_size and 0 <= current_col < chess_board_size:
        if chess_board[current_row][current_col] == "Q":
            queens_list.append((current_row, current_col))
            break
        current_row, current_col = move_func(current_row, current_col, direction)

if queens_list:
    for queen in queens_list:
        print(f"[{queen[0]}, {queen[1]}]")
else:
    print("The king is safe!")
