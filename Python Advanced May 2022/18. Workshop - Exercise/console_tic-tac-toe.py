# In this workshop, we will create a simple two-player tic-tac-toe game.
# Here is how the game is going to look in the end:
#
# Player one name: Peter
# Player two name: Sofia
# Peter would you like to play with 'X' or 'O'? X
# This is the numeration of the board:
# |  01  |  02  |  03  |
# |  04  |  05  |  06  |
# |  07  |  08  |  09  |
# Peter starts first!
# Peter choose a free position [1-9]: 1
# |  X  |     |     |
# |     |     |     |
# |     |     |     |
# Sofia choose a free position [1-9]: 3
# |  X  |     |  O  |
# |     |     |     |
# |     |     |     |
# etc.
#
# 1.BONUS
# Try writing validation logic for:
# oThe signs can only be "X" and "O"
# oThe users can only choose from the numbers 1 to 9
# oThe users can only choose a free space
# Try adding error messages for those validations


def players_data():
    p1 = input("Player one name: ")
    p2 = input("Player two name: ")
    p1_sign = input(f"{p1} would you like to play with 'X' or 'O'? ")
    while p1_sign not in ["X", "x", "O", "o"]:
        print('The signs can only be "X" and "O"')
        p1_sign = input(f"{p1} would you like to play with 'X' or 'O'? ")
    p1_sign = p1_sign.upper()
    p2_sign = "X" if p1_sign == "O" else "O"
    return (p1, p1_sign), (p2, p2_sign)


def board_setup(size):
    def_board = [[None for _ in range(size)] for _ in range(size)]
    return def_board


def print_board_legend(d_board):
    counter = 1
    for r in range(len(d_board)):
        print("|", end="")
        for c in range(len(d_board)):
            print(f"  {counter:02d}  |", end="")
            counter += 1
        print()


def print_current_board(d_board):
    for r in range(len(d_board)):
        print("|", end="")
        for c in range(len(d_board)):
            print(f"  {d_board[r][c] if d_board[r][c] is not None else ' '}  |", end="")
        print()


def get_board_location(pos, s):

    if pos % s == 0:
        r = pos // s - 1
        c = s - 1
    else:
        r = pos // s
        c = pos % s - 1

    return r, c


def winning_condition(r, c, b, sign):
    directions = {
        "horizontal": [(0, -1), (0, 1)],
        "vertical": [(-1, 0), (1, 0)],
        "primary_diagonal": [(-1, -1), (1, 1)],
        "secondary_diagonal": [(1, -1), (-1, 1)]
    }

    s = len(b)
    is_winner = False

    for key in directions:
        current_player_row = r
        current_player_column = c
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
                    and board[current_player_row][current_player_column] == sign:
                counter += 1
            else:
                break

        current_player_row = r
        current_player_column = c

        while True:
            current_player_row += r2_step
            current_player_column += c2_step
            if 0 <= current_player_row < len(board) \
                    and 0 <= current_player_column < len(board[0]) \
                    and board[current_player_row][current_player_column] == sign:
                counter += 1
            else:
                break

        if counter == s:
            is_winner = True

    return is_winner


def play(p1_name, p1_sign, p2_name, p2_sign, def_board):
    current_name, current_sign = p1_name, p1_sign
    other_name, other_sign = p2_name, p2_sign
    size = len(def_board)
    move = 1
    print(f'{current_name} starts first!')
    while True:

        if move > size * size:
            print("Draw!")
            break

        try:
            position = int(input(f"{current_name} choose a free position [1-{size * size}]: "))
        except ValueError:
            print(f"The users can only choose from the numbers 1 to {size * size}")
            continue

        if position < 1 or position > size * size:
            print(f"The users can only choose from the numbers 1 to {size * size}")
            continue

        row, col = get_board_location(position, size)
        if def_board[row][col] is not None:
            print("The users can only choose a free space")
            continue

        def_board[row][col] = current_sign
        print_current_board(def_board)

        if winning_condition(row, col, def_board, current_sign):
            print(f'{current_name} won!')
            break

        move += 1
        current_name, other_name = other_name, current_name
        current_sign, other_sign = other_sign, current_sign


(player_one_name, player_one_sign), (player_two_name, player_two_sign) = players_data()

board_size = 3
board = board_setup(board_size)

print("This is the numeration of the board:")
print_board_legend(board)

play(player_one_name, player_one_sign, player_two_name, player_two_sign, board)
