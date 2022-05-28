# 9.*Miner
# You are going to create a game called "Miner".
# First, you will receive the size of a square field in which the miner should move.
# On the second line, you will receive the commands for the miner's movement, separated by a single space. The possible commands are "left", "right", "up" and "down".
# In the end, you will receive each row of the field on a separate line. The possible characters that may appear on the screen are:
# * - a regular position on the field
# e - the end of the route
# c - coal
# s - miner
# The miner starts moving from the position "s". He should perform the given commands successively, moving with only one position in the given direction. If the miner has reached the edge of the field and the following command indicates that he has to get out of the area, he must remain in his current position and ignore the command.
# When the miner finds coal, he collects it and replaces it with "*". Keep track of the collected coal. In the end, you should print whether the miner has succeeded in collecting the coal or not and his final position:
# If the miner has collected all coal in the field, the program stops, and you should print the message: "You collected all coal! ({row_index}, {col_index})".
# If the miner steps at "e", the game is over (the program stops), and you should print the message: "Game over! ({row_index}, {col_index})".
# If there are no more commands and none of the above cases had happened, you should print the message: "{number_of_remaining_coal} pieces of coal left. ({row_index}, {col_index})".
# Input
# Field size - an integer number
# Commands to move the miner - a sequence of directions, separated by single whitespace (" ")
# The field: some of the following characters ("*", "e", "c ", "s"), separated by a single whitespace (" ")
# Output
# There are three types of output as mentioned above.
# Constraints
# The field size will be a 32-bit integer in the range [0 … 2 147 483 647]
# The field will always have only one "s"
#
# Input
# 4
# up right right right down
# * * * e
# * * c *
# * s * c
# * * * *
#
# Output
# You collected all coal! (2, 3)

def get_miner_location(matrix, command, start_row, start_col):
    r, c = 0, 0
    if command == "left":
        r, c = start_row, start_col-1
    elif command == "right":
        r, c = start_row, start_col+1
    elif command == "up":
        r, c = start_row-1, start_col
    elif command == "down":
        r, c = start_row+1, start_col

    if 0 <= r < n and 0 <= c < n:
        return r, c
    else:
        return start_row, start_col


n = int(input())
commands = input().split()
mm = []

miner_row = 0
miner_col = 0
coal_locations = []

for i in range(n):
    row = input().split()
    if "s" in row:
        miner_row = i
        miner_col = row.index("s")
    mm.append(row)

for i in range(n):
    for j in range(n):
        if mm[i][j] == "c":
            coal_locations.append((i, j))

not_break = True

for com in commands:
    miner_row, miner_col = get_miner_location(mm, com, miner_row, miner_col)
    if mm[miner_row][miner_col] == "e":
        print(f"Game over! ({miner_row}, {miner_col})")
        not_break = False
        break
    if mm[miner_row][miner_col] == "c":
        coal_locations.remove((miner_row, miner_col))
        mm[miner_row][miner_col] = "*"
    if not coal_locations:
        print(f"You collected all coal! ({miner_row}, {miner_col})")
        not_break = False
        break

if not_break:
    print(f'{len(coal_locations)} pieces of coal left. ({miner_row}, {miner_col})')
