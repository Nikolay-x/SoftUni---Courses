# 2.Pawn Wars
# Link to Judge: https://judge.softuni.org/Contests/Practice/Index/3374#1
#
# a8 b8 c8 d8 e8 f8 g8 h8
# a7 b7 c7 d7 e7 f7 g7 h7
# a6 b6 c6 d6 e6 f6 g6 h6
# a5 b5 c5 d5 e5 f5 g5 h5
# a4 b4 c4 d4 e4 f4 g4 h4
# a3 b3 c3 d3 e3 f3 g3 h3
# a2 b2 c2 d2 e2 f2 g2 h2
# a1 b1 c1 d1 e1 f1 g1 h1
#
# A chessboard has 8 rows and 8 columns. Rows, also called ranks, are marked from number 1 to 8, and columns are marked from A to H. We have a total of 64 squares. Each square is represented by a combination of letters and a number (a1, b1, c1, etc.). In this problem colors of the board will be ignored.
# We will play the game with two pawns, white (w) and black (b), where they can:
# Only move forward in a straight line:
# White (w) moves from the 1st rank to the 8th rank direction.
# Black (b) moves from 8th rank to the 1st rank direction.
# Can move only 1 square at a time.
# Can capture another pawn in from of them only diagonally:
#
# - - - - - - - -
# - - - - - - - -
# - - - - - - - -
# - - - - b - - -
# - - - - - w - -
# - - - - - - - -
# - - - - - - - -
# - - - - - - - -
#
# When a pawn reaches the last rank (for the white one - this is the 8th rank, and for the black one - this is the 1st rank), can be promoted to a queen.
# Two pawns (w and b) will be placed on two random squares of the bord. The first move is always made by the white pawn (w), then black moves (b), then white (w) again, and so on.
#
# Some rules apply when moving paws:
# If the two pawns interact diagonally, the player, in turn, must capture the opponent's pawn. When a pawn captures another pawn, the game is over.
# If no capture is possible, the pawns keep on moving until one of them reaches the last rank.
# Input
# On 8 lines, you will receive each row with its 8 columns, each element separated by a single space:
# oEmpty positions are marked with "-".
# oWhite pawn is marked with "w"
# oBlack pawn is marked with "b"
# Output
# Print either one of the following:
# If a pawn captures the other, print:
# o"Game over! {White/Black} win, capture on {square}."
# If a pawn reaches the last rank, print:
# o"Game over! {White/Black} pawn is promoted to a queen at {square}."
# Constraints
# The input will always be valid.
# The matrix will always be 8x8.
# There will be no case where two pawns are placed on the same square.
# There will be no case where two pawns are placed on the same column.
# There will be no case where black/white will be placed on the last rank.
#
# Input
# - - - - - - b -
# - - - - - - - -
# - - - - - - - -
# - - - - - - - -
# - - - - - - - -
# - w - - - - - -
# - - - - - - - -
# - - - - - - - -
#
# Output
# Game over! White pawn is promoted to a queen at b8.

def board_mapping(d_r, d_c):
    rows = [8, 7, 6, 5, 4, 3, 2, 1]
    cols = ["a", "b", "c", "d", "e", "f", "g", "h"]
    number = rows[d_r]
    letter = cols[d_c]
    return f"{letter}{number}"


rows_number = 8
cols_number = 8
board = []
player_w_location = 0, 0
player_b_location = 0, 0

for _ in range(rows_number):
    row = input().split(" ")
    board.append(row)

for r in range(rows_number):
    for c in range(cols_number):
        if board[r][c] == "w":
            player_w_location = (r, c)
        if board[r][c] == "b":
            player_b_location = (r, c)

player_w_delta = -1
player_b_delta = 1
player_w = "White"
player_b = "Black"
current_player_location, other_player_location = player_w_location, player_b_location
current_player, other_player = player_w, player_b
current_delta, other_delta = player_w_delta, player_b_delta
c_row, c_col = current_player_location
o_row, o_col = other_player_location

while True:
    if abs(c_row - o_row) == 1 and abs(c_col - o_col) == 1:
        print(f"Game over! {current_player} win, capture on {board_mapping(*other_player_location)}.")
        break
    next_row = c_row + current_delta
    next_col = c_col
    if next_row == rows_number-1 or next_row == 0:
        print(f"Game over! {current_player} pawn is promoted to a queen at {board_mapping(next_row, next_col)}.")
        break
    current_player_location = next_row, next_col
    c_row, c_col = next_row, next_col
    current_player_location, other_player_location = other_player_location, current_player_location
    current_player, other_player = other_player, current_player
    current_delta, other_delta = other_delta, current_delta
    c_row, o_row = o_row, c_row
    c_col, o_col = o_col, c_col
