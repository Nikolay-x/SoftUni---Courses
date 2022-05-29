# 7.Present Delivery
# The presents are ready, and Santa has to deliver them to the kids.
# You will receive an integer m for the number of presents Santa has and an integer n for the size of the neighborhood with a square shape. On the following lines, you will receive the matrix, which represents the neighborhood.
# Santa will be in a random cell, marked with the letter "S". Each cell stands for a house where children may live. If the cell has "X" on it, that means there lives a naughty kid. Otherwise, if a nice kid lives there, the cell is marked by "V". There can also be cells marked with "C" for cookies. All of the empty positions will be marked with "-".
# Santa can move "up", "down", "left", "right" with one position each time. These will be the commands that you receive. If he moves to a house with a nice kid, the kid receives a present, but if Santa reaches a house with a naughty kid, he doesn't drop a present. If the command sends Santa to a cell marked with "C", Santa eats cookies and becomes happy and extra generous to all the kids around him* (meaning all of them will receive presents - it doesn't matter if naughty or nice). If Santa has been to a house, the cell becomes "-".
# Note: *around him means on his left, right, upwards, and downwards by one cell. In this case, Santa doesn't move to these cells, or if he does, he returns to the cell where the cookie was.
# If Santa runs out of presents or receives the command "Christmas morning", you should end the program.
# Keep in mind that you should check whether all the nice kids received presents.
# Input
# On the first line, you are given the integer m - the count of presents
# On the second - integer n - the size of the neighborhood
# The following n lines hold the values for every row
# On each of the following lines you will get a command
# Output
# On the first line:
# oIf Santa runs out of presents, but there are still some nice kids left print: "Santa ran out of presents!"
# Next, print the matrix.
# In the end, print one of these messages:
# oIf he manages to give all the nice kids presents, print:
# "Good job, Santa! {count_nice_kids} happy nice kid/s."
# oOtherwise, print:
# "No presents for {count nice kids} nice kid/s."
# Constraints
# The size of the square matrix will be between [2…10].
# Santa's position will be marked with 'S'.
# There will always be at least 1 nice kid.
# There won't be a case where the cookie is on the border of the matrix.
#
# Input
# 5
# 4
# - X V -
# - S - V
# - - - -
# X - - -
# up
# right
# down
# right
# Christmas morning
#
# Output
# - - - -
# - - - S
# - - - -
# X - - -
# Good job, Santa! 2 happy nice kid/s.

def get_cookies_present(size, def_row, def_col):
    h = []
    moves = [
        [def_row, def_col+1],
        [def_row, def_col-1],
        [def_row+1, def_col],
        [def_row-1, def_col]
    ]
    for move in moves:
        def_r, def_c = move
        if 0 <= def_r < size and 0 <= def_c < size:
            h.append(move)
    return h


presents = int(input())
n = int(input())
mm = [[x for x in input().split()] for _ in range(n)]
nice_kids = 0
santa_row = 0
santa_col = 0
for i in range(n):
    for j in range(n):
        if mm[i][j] == "S":
            santa_row = i
            santa_col = j
        if mm[i][j] == "V":
            nice_kids += 1
total_nice_kids = nice_kids

directions = {
    'right': lambda r, c, s: (r, c+s),
    'left': lambda r, c, s: (r, c-s),
    'up': lambda r, c, s: (r-s, c),
    'down': lambda r, c, s: (r+s, c)
}

while presents > 0:
    command = input()
    if command == "Christmas morning":
        break
    row, col = directions[command](santa_row, santa_col, 1)
    mm[santa_row][santa_col] = "-"
    if mm[row][col] == "V":
        presents -= 1
        nice_kids -= 1
        mm[row][col] = "-"
    if mm[row][col] == "X":
        mm[row][col] = "-"
    if mm[row][col] == "C":
        houses = get_cookies_present(n, row, col)
        for house in houses:
            r, c = house
            if mm[r][c] == "V":
                presents -= 1
                mm[r][c] = "-"
                nice_kids -= 1
            if mm[r][c] == "X":
                presents -= 1
                mm[r][c] = "-"
            if presents == 0:
                break
    santa_row = row
    santa_col = col
    mm[santa_row][santa_col] = "S"

if presents == 0 and nice_kids > 0:
    print("Santa ran out of presents!")
for row in mm:
    print(" ".join(row))
if nice_kids == 0:
    print(f"Good job, Santa! {total_nice_kids} happy nice kid/s.")
else:
    print(f"No presents for {nice_kids} nice kid/s.")
