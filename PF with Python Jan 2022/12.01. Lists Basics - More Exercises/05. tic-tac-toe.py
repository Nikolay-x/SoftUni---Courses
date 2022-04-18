# 5.Tic-Tac-Toe
# You will receive a field of a tic-tac-toe game in three lines containing numbers, separated by a single space.
# Legend:
# 0 - empty space
# 1 - first player move
# 2 - second player move
# Find out who the winner is. If the first player wins, print "First player won". If the second player wins, print "Second player won". Otherwise, print "Draw!".
#
# Input
# 2 0 1
# 0 1 0
# 1 0 2
#
# Output
# First player won

line_1 = input().split(" ")
line_2 = input().split(" ")
line_3 = input().split(" ")

first_player_win = False
second_player_win = False

col1 = [line_1[0], line_2[0], line_3[0]]
col2 = [line_1[1], line_2[1], line_3[1]]
col3 = [line_1[2], line_2[2], line_3[2]]
d_tl_br = [line_1[0], line_2[1], line_3[2]]
d_bl_tr = [line_3[0], line_2[1], line_1[2]]

if line_1[0] == "1" and line_1[1] == "1" and line_1[2] == "1":
    first_player_win = True
elif line_1[0] == "2" and line_1[1] == "2" and line_1[2] == "2":
    second_player_win = True

if line_2[0] == "1" and line_2[1] == "1" and line_2[2] == "1":
    first_player_win = True
elif line_2[0] == "2" and line_2[1] == "2" and line_2[2] == "2":
    second_player_win = True

if line_3[0] == "1" and line_3[1] == "1" and line_3[2] == "1":
    first_player_win = True
elif line_3[0] == "2" and line_3[1] == "2" and line_3[2] == "2":
    second_player_win = True

if col1[0] == "1" and col1[1] == "1" and col1[2] == "1":
    first_player_win = True
elif col1[0] == "2" and col1[1] == "2" and col1[2] == "2":
    second_player_win = True

if col2[0] == "1" and col2[1] == "1" and col2[2] == "1":
    first_player_win = True
elif col2[0] == "2" and col2[1] == "2" and col2[2] == "2":
    second_player_win = True

if col3[0] == "1" and col3[1] == "1" and col3[2] == "1":
    first_player_win = True
elif col3[0] == "2" and col3[1] == "2" and col3[2] == "2":
    second_player_win = True

if d_tl_br[0] == "1" and d_tl_br[1] == "1" and d_tl_br[2] == "1":
    first_player_win = True
elif d_tl_br[0] == "2" and d_tl_br[1] == "2" and d_tl_br[2] == "2":
    second_player_win = True

if d_bl_tr[0] == "1" and d_bl_tr[1] == "1" and d_bl_tr[2] == "1":
    first_player_win = True
elif d_bl_tr[0] == "2" and d_bl_tr[1] == "2" and d_bl_tr[2] == "2":
    second_player_win = True

if first_player_win:
    print("First player won")
if second_player_win:
    print("Second player won")
if first_player_win == False and second_player_win == False:
    print("Draw!")
