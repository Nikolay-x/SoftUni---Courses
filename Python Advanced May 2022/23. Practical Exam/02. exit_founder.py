# 2. Exit Founder
# Tom and Jerry decided to play a game together. The game is a maze of which they need to find a way out. Monitor their moves closely and find out who the winner will be!
# First, you will be given the names "Tom" and "Jerry", separated by a comma and a space ", ". The order in which they are received determines the order in which they will take turns. The first player starts first.
# Next, you will be given a matrix with 6 rows and 6 columns representing the maze board. It consists of:
# Only one Exit - marked with the "E" letter
# Trap (one, many, or none) - marked with the "T" letter
# Wall (one, many, or none) - marked with the "W" letter
# Empty positions will be marked with "."
# In the beginning, Tom and Jerry are outside the board. On each line, after the matrix is given, you will be receiving coordinates for each of the players. They will be taking turns and stepping on different positions on the board until one of them find the Exit or falls into a Trap. Here are the rules:
# If a player hits the letter "E", he escapes the maze and wins the game.
# oPrint "{player} found the Exit and wins the game!" and end the program.
# If the letter "T" is hit, the player falls into a Trap, the game ends, and his opponent wins automatically.
# oPrint "{player} is out of the game! The winner is {winner}." and end the program.
# If the letter "W" is hit, the player hits a wall, and he needs to rest. The player's next move is ignored.
# oPrint "{player} hits a wall and needs to rest."
# If a player steps on an empty position ".", nothing happens.
# Both players can step in the same position at the same time.
# Input
# On the first line, you will receive "Tom" and "Jerry" separated by ", ". The first player starts first.
# On the following 6 lines, you will receive the maze board (elements will be separated by a space)
# On the following lines, you will be receiving coordinates in the format: "({row}, {column})"
# Output
# You should print the output as described above.
# The input coordinates will always be valid.
#
# Input
# Tom, Jerry
# . . T . . .
# . . . . . .
# . . W . . .
# . . W . . E
# . . . . . .
# . T . W . .
# (3, 2)
# (1, 3)
# (5, 1)
# (5, 1)
#
# Output
# Tom hits a wall and needs to rest.
# Jerry is out of the game! The winner is Tom.

current_player, other_player = input().split(", ")
chess_board_size = 6
maze_board = []

for i in range(chess_board_size):
    row = input().split(" ")
    maze_board.append(row)

current_player_need_to_rest = False
other_player_need_to_rest = False

while True:
    current_row, current_col = [int(x) for x in input().strip("(").strip(")").split(", ")]

    if current_player_need_to_rest:
        current_player_need_to_rest = False
        current_player, other_player = other_player, current_player
        current_player_need_to_rest, other_player_need_to_rest = other_player_need_to_rest, current_player_need_to_rest
        continue

    if maze_board[current_row][current_col] == "E":
        print(f"{current_player} found the Exit and wins the game!")
        break

    if maze_board[current_row][current_col] == "T":
        print(f"{current_player} is out of the game! The winner is {other_player}.")
        break

    if maze_board[current_row][current_col] == "W":
        print(f"{current_player} hits a wall and needs to rest.")
        current_player_need_to_rest = True

    current_player, other_player = other_player, current_player
    current_player_need_to_rest, other_player_need_to_rest = other_player_need_to_rest, current_player_need_to_rest
