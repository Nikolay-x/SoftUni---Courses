# Snake
#
# Everybody remembers the old snake game. Now it is time to create your own.
#
# You will be given an integer n for the size of the snake territory with square shape. On the next n lines, you will receive the rows of the territory. The snake will be placed on a random position, marked with the letter 'S'. On random positions there will be food, marked with '*'. There might also be a lair on the territory. The lair has two burrows. They are marked with the letter - 'B'. All of the empty positions will be marked with '-'.
# Each turn, you will be given command for the snake’s movement. When the snake moves it leaves a trail marked with '.'
# Move commands will be: "up", "down", "left", "right".
# If the snake moves to a food, it eats the food and increases the food quantity with one.
# If it goes inside of a burrow, it goes out on the position of the other burrow and then both burrows disappear. If the snake goes out of its territory, it loses, can't return back and the program ends. The snake needs at least 10 food quantity to win.
# When the snake has gone outside of its territory or has eaten enough food, the game ends.
# Input
# On the first line, you are given the integer n – the size of the square matrix.
# The next n lines holds the values for every row.
# On each of the next lines you will get a move command.
# Output
# On the first line:
# oIf the snake goes out of its territory, print: "Game over!"
# oIf the snake eat enough food, print: "You won! You fed the snake."
# On the second line print all food eaten: "Food eaten: {food quantity}"
# In the end print the matrix.
# Constraints
# The size of the square matrix will be between [2…10].
# There will always be 0 or 2 burrows, marked with - 'B'.
# The snake position will be marked with 'S'.
# The snake will always either go outside its territory or eat enough food.
# There will be no case in which the snake will go through itself.
#
# Input
# 6
# -----S
# ----B-
# ------
# ------
# --B---
# --*---
# left
# down
# down
# down
# left
#
# Output
# Game over!
# Food eaten: 1
# ----..
# ----.-
# ------
# ------
# --.---
# --.---

def move_snake(def_row, def_col, def_direction):

    if def_direction == "up":
        def_row -= 1
    elif def_direction == "down":
        def_row += 1
    elif def_direction == "left":
        def_col -= 1
    elif def_direction == "right":
        def_col += 1

    return def_row, def_col


size = int(input())
territory = []
snake_row = 0
snake_col = 0
lair_burrows = []
food_quantity = 0
snake_out = False

for i in range(size):
    row = list(map(str, input()))
    territory.append(row)

for row in range(size):
    for col in range(size):
        if territory[row][col] == "S":
            snake_row = row
            snake_col = col
        elif territory[row][col] == "B":
            burrow_row = row
            burrow_col = col
            lair_burrows.append((burrow_row, burrow_col))

while True:
    direction = input()
    territory[snake_row][snake_col] = "."
    snake_row, snake_col = move_snake(snake_row, snake_col, direction)

    if snake_row < 0 or snake_row > size-1 or snake_col < 0 or snake_col > size -1:
        snake_out = True
        break

    if territory[snake_row][snake_col] == "*":
        food_quantity += 1
    elif territory[snake_row][snake_col] == "B":
        territory[snake_row][snake_col] = "."
        lair_burrows.remove((snake_row, snake_col))
        snake_row, snake_col = lair_burrows[0]

    territory[snake_row][snake_col] = "S"

    if food_quantity >= 10:
        break

if snake_out:
    print("Game over!")
if food_quantity >= 10:
    print("You won! You fed the snake.")
print(f"Food eaten: {food_quantity}")

for row in territory:
    print(*row, sep="")
