# Problem 2 - Darts
# Two players bare-handedly throw small sharp-pointed missiles known as darts at a round target known as a dartboard. Who is going to win this game?
# You will be given a matrix with 7 rows and 7 columns representing the dartboard. For example:
# 1	    2	3	4	5	6	7
# 24    D	D	D	D	D	8
# 23	D	T	T	T	D	9
# 22	D	T	B	T	D	10
# 21	D	T	T	T	D	11
# 20	D	D	D	D	D	12
# 19	18	17	16	15	14	13
#
# Each of the two players starts with a score of 501 and they take turns to throw a dart – one throw for each player. The score for each turn is deducted from the player’s total score. The first player who reduces their score to zero or less wins the game.
# You are going to receive the information for every throw on a separate line. The coordinate information of a hit will be in the format: "({row}, {column})".
# If a player hits outside the dartboard, he does not score any points.
# If a player hits a number, it is deducted from his total.
# If a player hits a "D" the sum of the 4 corresponding numbers per column and row is doubled and then deducted from his total.
# If a player hits a "T" the sum of the 4 corresponding numbers per column and row is tripled and then deducted from his total.
# "B" is the bullseye. If a player hits it, he wins the game, and the program ends.
# For example, if Peter hits position with coordinates (2, 1), he wins (23 + 2 + 9 + 18) * 2 = 104 points and they are deducted from his total.
# Your job is to find who won the game and with how many turns.
# Input
# The name of the first player and the name of the second player, separated by ", "
# 7 lines – the dartboard (separated by single space)
# On the next lines - the coordinates in the format: "({row}, {column})"
# Output
# You should print only one line containing the winner and his count of throws:
# "{name} won the game with {count_turns} throws!"
# Constrains
# There will always be exactly 7 lines
# There will always be a winner
# The points will be in range [1, 24]
# The coordinates will be in range [0, 100]
#
# Input
# George, Hristo
# 17 8 21 6 13 3 24
# 16 D D D D D 14
# 7 D T T T D 15
# 23 D T B T D 2
# 9 D T T T D 22
# 19 D D D D D 10
# 12 18 4 20 5 11 1
# (1, 0)
# (2, 3)
# (0, 0)
# (4, 2)
# (5, 1)
# (3, 1)
# (0, 0)
# (2, 3)
#
# Output
# Hristo won the game with 4 throws!

def get_points(r, c, board):
    score = int(board[r][0]) + int(board[r][size-1]) + int(board[0][c]) + int(board[size-1][c])
    return score


player1, player2 = input().split(", ")
player1_score = 501
player2_score = 501
player1_throws = 0
player2_throws = 0

is_b_hit = False

size = 7
dartboard = []
for _ in range(size):
    row = input().split(" ")
    dartboard.append(row)

current_player, other_player = player1, player2
current_score, other_score = player1_score, player2_score
current_player_throws, other_player_throws = player1_throws, player2_throws

while current_score > 0 and other_score > 0:
    current_player_throws += 1
    line = input().strip("(").strip(")").split(", ")
    row = int(line[0])
    col = int(line[1])

    if row < 0 or row > size-1 or col < 0 or col > size-1:
        current_player, other_player = other_player, current_player
        current_score, other_score = other_score, current_score
        current_player_throws, other_player_throws = other_player_throws, current_player_throws
        continue

    if dartboard[row][col] == "B":
        is_b_hit = True
        print(f"{current_player} won the game with {current_player_throws} throws!")
        break

    if dartboard[row][col].isnumeric():
        current_score -= int(dartboard[row][col])
    elif dartboard[row][col] == "D":
        current_score -= 2 * get_points(row, col, dartboard)
    elif dartboard[row][col] == "T":
        current_score -= 3 * get_points(row, col, dartboard)

    current_player, other_player = other_player, current_player
    current_score, other_score = other_score, current_score
    current_player_throws, other_player_throws = other_player_throws, current_player_throws

if not is_b_hit:
    print(f"{other_player} won the game with {other_player_throws} throws!")
