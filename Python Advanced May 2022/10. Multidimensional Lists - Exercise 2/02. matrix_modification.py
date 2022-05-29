# 2.Matrix Modification
# Write a program that reads a matrix from the console and changes its values. On the first line, you will get the matrix's rows - N. You will get elements for each column on the following N lines, separated with a single space. You will be receiving commands in the following format:
# "Add {row} {col} {value}" – Increase the number at the given coordinates with the value.
# "Subtract {row} {col} {value}" – Decrease the number at the given coordinates by the value.
# If the coordinate is invalid, you should print "Invalid coordinates". A coordinate is valid if both of the given indexes are in range [0; len() – 1].
# When you receive "END", you should print the matrix and stop the program.
#
# Input
# 4
# 1 2 3 4
# 5 6 7 8
# 8 7 6 5
# 4 3 2 1
# Add 4 4 100
# Add 3 3 100
# Subtract -1 -1 42
# Subtract 0 0 42
# END
#
# Output
# Invalid coordinates
# Invalid coordinates
# -41 2 3 4
# 5 6 7 8
# 8 7 6 5
# 4 3 2 101

def is_inside(row, col, matrix_rows, matrix_cols):
    return 0 <= row < matrix_rows and 0 <= col < matrix_cols


n = int(input())

mm = [[int(x) for x in input().split()] for _ in range(n)]

mm_rows = n
mm_cols = 0
max_row = 0
for r in mm:
    if len(r) > max_row:
        max_row = len(r)
        mm_cols = len(r)

while True:
    command = input().split()
    if command[0] == "END":
        break
    operation = command[0]
    r, c, value = [int(x) for x in command[1:]]
    if is_inside(r, c, mm_rows, mm_cols):
        if operation == "Add":
            mm[r][c] += value
        elif operation == "Subtract":
            mm[r][c] -= value
    else:
        print("Invalid coordinates")

for r in mm:
    print(*r)
