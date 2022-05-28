# 6.Matrix Shuffling
# Write a program that reads a matrix from the console and performs certain operations with its elements. User input is provided similarly to the problems above - first, you read the dimensions and then the data.
# Your program should receive commands in the format: "swap {row1} {col1} {row2} {col2}" where ("row1", "col1") and ("row2", "col2") are the coordinates of two points in the matrix. A valid command starts with the "swap" keyword along with four valid coordinates (no more, no less), separated by a single space.
# If the command is valid, you should swap the values at the given indexes and print the matrix at each step (thus, you will be able to check if the operation was performed correctly).
# If the command is not valid (does not contain the keyword "swap", has fewer or more coordinates entered, or the given coordinates are not valid), print "Invalid input!" and move on to the following command. A negative value makes the coordinates not valid.
# Your program should finish when the command "END" is entered.
#
# Input
# 2 3
# 1 2 3
# 4 5 6
# swap 0 0 1 1
# swap 10 9 8 7
# swap 0 1 1 0
# END
#
# Output
# 5 2 3
# 4 1 6
# Invalid input!
# 5 4 3
# 2 1 6

def command_is_valid(command, rows, cols):
    return command[0] == "swap" and len(command) == 5 \
           and 0 <= int(command[1]) < rows and 0 <= int(command[2]) < cols\
           and 0 <= int(command[3]) < rows and 0 <= int(command[4]) < cols


r, c = [int(x) for x in input().split()]
mm = [[int(x) for x in input().split()] for _ in range(r)]

while True:
    line = input().split()

    if line[0] == "END":
        break

    if command_is_valid(line, r, c):
        r1 = int(line[1])
        c1 = int(line[2])
        r2 = int(line[3])
        c2 = int(line[4])
        # r1, c1, r2, c2 = [int(x) for x in line[1:]]

        mm[r1][c1], mm[r2][c2] = mm[r2][c2], mm[r1][c1]

        for i in range(r):
            print(" ".join([str(x) for x in mm[i]]))
        # for row in mm:
        #     print(*row, sep=" ")

    else:
        print("Invalid input!")
