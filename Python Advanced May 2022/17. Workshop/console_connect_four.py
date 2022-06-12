# Workshop: Console Connect Four
# In this workshop, we are going to create a simple two player connect four game.
# Here is how the game is going to look in the end:
#
# Player 2, please choose a column (1-7): 4
# [0, 0, 0, 0, 0, 0, 0]
# [0, 0, 0, 0, 0, 0, 0]
# [0, 0, 0, 2, 0, 0, 0]
# [0, 0, 2, 1, 0, 0, 0]
# [0, 2, 1, 2, 0, 0, 0]
# [2, 1, 1, 1, 0, 0, 0]
# The winner is player 2
#
# The Main Logic
# A player wins when he/she connects four slots.
# The winning connected slots must be consecutive
# A connection can be
# oHorizontal
# oVertical
# oDiagonal
#
# BONUS
# Try writing validation logic for:
# oMore than one player
# oReset logic
# Try adding error messages for invalid column

def get_board(rows, columns):
    board = [[None for _ in range(columns)] for _ in range(rows)]
    return board


def cell_value(cell):
    return 0 if cell is None else cell


def print_board(board):
    [print([cell_value(x) for x in row]) for row in board]


def get_move(player, def_board):
    column = None
    while True:
        try:
            column = int(input(f"Player {player}, please choose a column (1-{len(def_board[0])}): "))
        except ValueError:
            print(f"The users can only choose from the integer numbers 1 to {len(def_board[0])}")
            continue

        if column < 1 or column > len(def_board[0]):
            print(f"The users can only choose from the integer numbers 1 to {len(def_board[0])}")
            continue

        if 1 <= column <= len(def_board[0]):
            break

    return column - 1


def apply_move(board, player, def_player_row, def_player_move):
    board[def_player_row][def_player_move] = player
    return board


def winning_condition(def_player, def_player_row, def_player_column, board):
    directions = {
        "horizontal": [(0, -1), (0, 1)],
        "vertical": [(-1, 0), (1, 0)],
        "primary_diagonal": [(-1, -1), (1, 1)],
        "secondary_diagonal": [(1, -1), (-1, 1)]
    }

    is_winner = False

    for key in directions:
        current_player_row = def_player_row
        current_player_column = def_player_column
        counter = 1

        direction1 = directions[key][0]
        direction2 = directions[key][1]
        r1_step, c1_step = direction1
        r2_step, c2_step = direction2

        while True:
            current_player_row += r1_step
            current_player_column += c1_step
            if 0 <= current_player_row < len(board) \
                    and 0 <= current_player_column < len(board[0]) \
                    and board[current_player_row][current_player_column] == def_player:
                counter += 1
            else:
                break

        current_player_row = def_player_row
        current_player_column = def_player_column

        while True:
            current_player_row += r2_step
            current_player_column += c2_step
            if 0 <= current_player_row < len(board) \
                    and 0 <= current_player_column < len(board[0]) \
                    and board[current_player_row][current_player_column] == def_player:
                counter += 1
            else:
                break

        if counter >= 4:
            is_winner = True

    return is_winner


def play(b):
    current_player, next_player = player1, player2
    available_bottom_rows = [r - 1 for _ in range(c)]

    while True:

        player_column = get_move(current_player, b)
        player_row = available_bottom_rows[player_column]
        b = apply_move(b, current_player, player_row, player_column)
        print_board(b)
        if available_bottom_rows[player_column] < 0:
            print("The selected column is full, please choose another column")
            continue
        available_bottom_rows[player_column] -= 1

        if winning_condition(current_player, player_row, player_column, b):
            print(f"The winner is player {current_player}")
            reset = input("Do you want to play again [Y/N]? ")
            if reset in ["Y", "y"]:
                b = get_board(r, c)
                available_bottom_rows = [r - 1 for _ in range(c)]
                continue
            else:
                break
        current_player, next_player = next_player, current_player


player1 = 1
player2 = 2

r = 6
c = 7
play_board = get_board(r, c)

play(play_board)
