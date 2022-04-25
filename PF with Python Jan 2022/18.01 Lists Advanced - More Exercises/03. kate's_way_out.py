# 3.Kate's Way Out
# Kate is stuck in a maze. You should help her to find her way out.
# On the first line, you will be given how many rows there are in the maze. On the following n lines, you will be given the maze itself. Here is a legend for the maze:
# "#" - means a wall; Kate cannot go through there
# " " - means empty space; Kate can go through there
# "k" - the initial position of Kate; start looking for a way out from there
# There are two options: Kate either gets out or not:
# If Kate can get out, print the following:
# "Kate got out in {number_of_moves} moves".
# Note: If there are two or more ways out, she always chooses the longest one.
# Otherwise, print: "Kate cannot get out".
#
# Input
# 4
# ######
# ##  k#
# ## ###
# ## ###
#
# Output
# Kate got out in 5 moves

maze_rows = int(input())

maze = []
all_paths = []
maze_edges = []
maze_empty_cells = []

for row in range(maze_rows):
    temp_list = [x for x in input()]
    maze.append(temp_list)
    if "k" in temp_list:
        index = temp_list.index("k")
        temp_list[index] = 0

maze_cols = max(len(x) for x in maze)

for row in range(maze_rows):
    if len(maze[row]) < maze_cols:
        maze[row] += (maze_cols - len(maze[row])) * " "

for row in range(maze_rows):
    for col in range(maze_cols):
        if row == 0 or row == maze_rows - 1 or col == 0 or col == maze_cols - 1:
            maze_edges.append((row, col))
        if maze[row][col] == " ":
            maze_empty_cells.append((row, col))

for i in range(len(maze_empty_cells) + 1):
    for row in range(maze_rows):
        for col in range(maze_cols):
            if maze[row][col] == i:
                if 0 <= row + 1 < maze_rows and maze[row + 1][col] == " ":
                    maze[row + 1][col] = i + 1
                if 0 <= row - 1 < maze_rows and maze[row - 1][col] == " ":
                    maze[row - 1][col] = i + 1
                if 0 <= col + 1 < maze_cols and maze[row][col + 1] == " ":
                    maze[row][col + 1] = i + 1
                if 0 <= col - 1 < maze_cols and maze[row][col - 1] == " ":
                    maze[row][col - 1] = i + 1

for edge in maze_edges:
    if str(maze[edge[0]][edge[1]]).isnumeric():
        all_paths.append(maze[edge[0]][edge[1]] + 1)

if len(all_paths) > 0:
    moves = max(all_paths)
    print(f"Kate got out in {moves} moves")
else:
    print("Kate cannot get out")

# for row in range(maze_rows):
#     for col in range(maze_cols):
#         print(maze[row][col], end="")
#     print()
# print(all_paths)
