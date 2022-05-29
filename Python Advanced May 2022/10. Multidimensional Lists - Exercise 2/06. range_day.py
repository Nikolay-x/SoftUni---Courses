# 6.Range Day
# You are participating in a Firearm course. It is a training day at the shooting range.
# You will be given a matrix with 5 rows and 5 columns. It is a shotgun range represented as some symbols separated by a single space:
# Your position is marked with the symbol "A"
# Targets marked with symbol "x"
# All of the empty positions will be marked with "."
# After the field state, you will be given an integer representing the number of commands you will receive. The possible commands are:
# "move {right/left/up/down} {steps}" – you should move in the given direction with the given steps. You can only move if the field you want to step on is marked with ".".
# "shoot {right/left/up/down}" – you should shoot in the given direction (from your current position without moving). Beware that there might be targets that stand in the way of other targets, and you cannot reach them - you can shoot only the nearest target. When you have shot a target, the field becomes empty position (".").
# Validate the positions since they can be outside the field.
# Keep track of all the shot targets:
# If at any point there are no targets left, end the program and print: "Training completed! All {count_targets} targets hit.".
# If, after you perform all the commands, there are some targets left print: "Training not completed! {count_left_targets} targets left.".
# Finally, print the index positions of the targets that you hit, as shown in the examples.
# Input
# 5 lines representing the field (symbols, separated by a single space)
# N - count of commands
# On the following N lines - the commands in the format described above
# Output
# On the first line, print one of the following:
# oIf all the targets were shot
# "Training completed! All {count_targets} targets hit."
# oOtherwise:
#               	       "Training not completed! {count_left_targets} targets left."
# Finally, print the index positions "[{row}, {column}]" of the targets that you hit, as shown in the examples.
# Constrains
# All the commands will be valid
# There will always be at least one target
#
# Input
# . . . . .
# x . . . .
# . A . . .
# . . . x .
# . x . . x
# 3
# shoot down
# move right 4
# move left 1
#
# Output
# Training not completed! 3 targets left.
# [4, 1]

mm = []
player_row = 0
player_col = 0
targets = []
hit_targets = []

for i in range(5):
    row = input().split()
    mm.append(row)

for i in range(5):
    for j in range(5):
        if mm[i][j] == "A":
            player_row, player_col = i, j
        if mm[i][j] == "x":
            target_row, target_col = i, j
            targets.append((i, j))

directions = {
    'right': lambda r, c, s: (r, c+s),
    'left': lambda r, c, s: (r, c-s),
    'up': lambda r, c, s: (r-s, c),
    'down': lambda r, c, s: (r+s, c)
}

n = int(input())
for _ in range(n):
    mm[player_row][player_col] = "."
    command = input().split()
    direction = command[1]

    if command[0] == "move":
        steps = int(command[2])
        row, col = directions[direction](player_row, player_col, steps)
        if 0 <= row < 5 and 0 <= col < 5 and mm[row][col] == ".":
            player_row, player_col = row, col

    if command[0] == "shoot":
        s_row, s_col = directions[direction](player_row, player_col, 1)
        while 0 <= s_row < 5 and 0 <= s_col < 5:
            if mm[s_row][s_col] == "x":
                hit_targets.append([s_row, s_col])
                targets.remove((s_row, s_col))
                mm[s_row][s_col] = "."
                break
            if not targets:
                break
            s_row, s_col = directions[direction](s_row, s_col, 1)

    if not targets:
        break

if not targets:
    print(f"Training completed! All {len(hit_targets)} targets hit.")
    for target in hit_targets:
        print(target)
else:
    print(f"Training not completed! {len(targets)} targets left.")
    for target in hit_targets:
        print(target)
