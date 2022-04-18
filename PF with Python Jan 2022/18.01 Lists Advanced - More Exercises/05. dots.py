# 5.Dots
# You will be given a number n representing the number of rows of a board of dots and dashes. On the following n lines, you will receive each row of the board as a string with symbols (dots and dashes only), separated by a single space.
# Your task is to find and print the largest count of dots that could be connected at once. You could only connect horizontally or vertically.
#
# Input
# 5
# . . - - -
# . . - - -
# - - - - -
# - - - . .
# - - - . .
#
# Output
# 4

n = int(input())

board = []
paths_length = []
processed_points = []

for i in range(n):
    board_rows = input().split(" ")
    board.append(board_rows)
board_rows = n
board_cols = max(len(x) for x in board)

for row in range(board_rows):
    for col in range(board_cols):
        if (row, col) in processed_points:
            continue
        if board[row][col] == ".":
            temp_points = [(row, col)]
            while True:
                points = []
                for point in temp_points:
                    x, y = point
                    if x > 0:
                        if board[x-1][y] == "." and (x-1, y) not in temp_points:
                            points.append((x - 1, y))
                    if x < board_rows - 1:
                        if board[x+1][y] == "." and (x+1, y) not in temp_points:
                            points.append((x + 1, y))
                    if y > 0:
                        if board[x][y-1] == "." and (x, y-1) not in temp_points:
                            points.append((x, y - 1))
                    if y < board_cols - 1:
                        if board[x][y+1] == "." and (x, y+1) not in temp_points:
                            points.append((x, y + 1))

                if points:
                    for point in points:
                        if point not in temp_points:
                            temp_points.append(point)
                else:
                    processed_points.extend(temp_points)
                    paths_length.append(len(temp_points))
                    break

if paths_length:
    print(max(paths_length))
else:
    print(0)
