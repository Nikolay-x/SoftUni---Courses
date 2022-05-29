# 5.Alice in Wonderland
# Alice is going to the mad tea party, to see her friends. On the way to the party, she needs to collect bags of tea.
# You will be given an integer n for the size of the Wonderland territory with a square shape. On the following n lines, you will receive the rows of the territory:
# Alice will be placed in a random position, marked with the letter "A".
# On the territory, there will be bags of tea, represented as numbers. If Alice steps on a number position, she collects the tea bags and increases the quantity with the corresponding number.
# There will always be one rabbit hole on the territory marked with the letter "R".
# All of the empty positions will be marked with ".".
# After the field state, you will be given commands for Alice's movements. Move commands can be: "up", "down", "left" or "right".
# When Alice collects at least 10 bags of tea, she is ready to go to the tea party, and she does not need to continue collecting. Otherwise, if she steps on the rabbit hole or goes out of the territory, she can't return, and the program ends.
# In the end, the path she walked had to be marked with '*'.
# For more clarifications, see the examples below.
# Input
# On the first line, you will be given the integer n – the size of the square matrix
# On the following n lines - matrix representing the field (each position separated by a single space)
# On each of the following lines, you will be given a move command
# Output
# On the first line:
# oIf Alice steps on the rabbit hole or she go out of the territory, print:
# "Alice didn't make it to the tea party."
# oIf she collected at least 10 bags of tea, print:
# "She did it! She went to the party."
# On the following lines, print the matrix.
# Constraints
# Alice will always either go outside the Wonderland or collect 10 bags of tea
# All the commands will be valid
# All of the given numbers will be valid integers in the range [0, 10]
#
# Input
# 5
# . A . . 1
# R . 2 . .
# 4 7 . 1 .
# . . . 2 .
# . 3 . . .
# down
# right
# left
# down
# up
# left
#
# Output
# Alice didn't make it to the tea party.
# . * . . 1
# * * * . .
# 4 * . 1 .
# . . . 2 .
# . 3 . . .

n = int(input())
mm = [[x for x in input().split()] for _ in range(n)]

alice_row = 0
alice_col = 0
for i in range(n):
    for j in range(n):
        if mm[i][j] == "A":
            alice_row = i
            alice_col = j

mm[alice_row][alice_col] = "*"

directions = {
    'right': lambda r, c: (r, c+1),
    'left': lambda r, c: (r, c-1),
    'up': lambda r, c: (r-1, c),
    'down': lambda r, c: (r+1, c)
}

tea_bags = 0
while True:
    direction = input()
    row, col = directions[direction](alice_row, alice_col)
    if row < 0 or col < 0 or row >= n or col >= n:
        print("Alice didn't make it to the tea party.")
        break
    if mm[row][col] == "R":
        print("Alice didn't make it to the tea party.")
        mm[row][col] = "*"
        break
    if mm[row][col] != "." and mm[row][col] != "*":
        tea_bags += int(mm[row][col])
        mm[row][col] = "*"
    else:
        mm[row][col] = "*"
    if tea_bags >= 10:
        print("She did it! She went to the party.")
        break
    alice_row = row
    alice_col = col

for row in mm:
    print(*row)
