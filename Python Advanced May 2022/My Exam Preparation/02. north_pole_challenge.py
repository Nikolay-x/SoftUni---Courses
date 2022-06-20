# 02. North Pole Challenge
# You are visiting Santa Claus' workshop, and it is complete chaos. You will need to help Santa find all items scattered around the workshop.
# You will be given the size of the matrix in the format "{rows}, {columns}". It is the Santa's workshop represented as some symbols separated by a single space:
# Your position is marked with the symbol "Y"
# Christmas decorations are marked with the symbol "D"
# Gifts are marked with the symbol "G"
# Cookies are marked with the symbol "C"
# All of the empty positions will be marked with "."
# After the field state, you will be given commands until you receive the command "End". The commands will be in the format "right/left/up/down-{steps}". You should move in the given direction with the given steps and collect all the items that come across. If you go out of the field, you should continue to traverse the field from the opposite side in the same direction. You should mark your path with "x". Your current position should always be marked with "Y".
# Keep track of all collected items. If you've collected all items at any point, end the program and print: "Merry Christmas!".
# Input
# On the first line, you will receive the number of rows and columns in the format "{rows}, {columns}"
# On the next lines, you will receive each row with its columns - symbols, separated by a single space.
# On the following lines, you will receive commands in the format described above until you receive the command "End" or until you collect all items.
# Output
# On the first line, if you have collected all items, print:
# o"Merry Christmas!"
# oOtherwise, skip the line
# Next, print the number of collected items in the format:
# o"You've collected:
# o- {number_of_decoration} Christmas decorations
# o- {number_of_gifts} Gifts
# o- {number_of_cookies} Cookies"
# Finally, print the field, as shown in the examples.
# Constrains
# All the commands will be valid
# There will always be at least one item
# The dimensions of the matrix will be integers in the range [1, 20]
# The field will always have only one "Y"
# On the field, there will always be only the symbols shown above.
#
# Input
# 6, 5
# . . . . .
# C . . G .
# . C . . .
# G . . C .
# . D . . D
# Y . . . G
# left-3
# up-1
# left-2
# right-7
# up-1
# End
#
# Output
# You've collected:
# - 2 Christmas decorations
# - 1 Gifts
# - 0 Cookies
# . . . . .
# C . . G .
# . C . . .
# G . Y C .
# x x x x x
# x . x x x

def move_func(def_row, def_col, def_rows, def_cols, def_direction):
    if def_direction == "up":
        def_row -= 1
        if def_row < 0:
            def_row = def_rows - 1

    elif def_direction == "down":
        def_row += 1
        if def_row > def_rows - 1:
            def_row = 0

    elif def_direction == "left":
        def_col -= 1
        if def_col < 0:
            def_col = def_cols - 1

    elif def_direction == "right":
        def_col += 1
        if def_col > def_cols - 1:
            def_col = 0

    return def_row, def_col


rows, columns = [int(x) for x in input().split(", ")]
workshop = []
start_row = 0
start_col = 0

items_dict = {
    "decorations": 0,
    "gifts": 0,
    "cookies": 0
}
collected_items = [0, 0, 0]
items_collected = False

for i in range(rows):
    column = input().split(" ")
    if "Y" in column:
        start_row = i
        start_col = column.index("Y")
    workshop.append(column)

for i in range(rows):
    for j in range(columns):
        if workshop[i][j] == "D":
            items_dict["decorations"] += 1
        if workshop[i][j] == "G":
            items_dict["gifts"] += 1
        if workshop[i][j] == "C":
            items_dict["cookies"] += 1

current_row, current_column = start_row, start_col

while True:
    command = input()
    if command == "End":
        break
    command = command.split("-")
    direction = command[0]
    steps = int(command[1])

    for step in range(steps):
        next_row, next_column = move_func(current_row, current_column, rows, columns, direction)
        workshop[current_row][current_column] = "x"
        if workshop[next_row][next_column] == "D":
            items_dict["decorations"] -= 1
            collected_items[0] += 1
            if sum(items_dict.values()) == 0:
                items_collected = True
        if workshop[next_row][next_column] == "G":
            items_dict["gifts"] -= 1
            collected_items[1] += 1
            if sum(items_dict.values()) == 0:
                items_collected = True
        if workshop[next_row][next_column] == "C":
            items_dict["cookies"] -= 1
            collected_items[2] += 1
            if sum(items_dict.values()) == 0:
                items_collected = True

        current_row, current_column = next_row, next_column
        workshop[next_row][next_column] = "Y"

        if items_collected:
            break

    if items_collected:
        break

if items_collected:
    print("Merry Christmas!")
print("You've collected:")
print(f"- {collected_items[0]} Christmas decorations")
print(f"- {collected_items[1]} Gifts")
print(f"- {collected_items[2]} Cookies")
for row in workshop:
    print(*row)
