# 10.*Fill the Box
# Write a function called fill_the_box that receives a different number of arguments representing:
# the height of a box
# the length of a box
# the width of a box
# n-times a different number of cubes with exact size 1 x 1 x 1
# a string "Finish"
# Your task is to fill the box with the given cubes until the current argument equals "Finish".
# Note: Submit only the function in the judge system
# Input
# There will be no input. Just parameters passed to your function.
# Output
# The function should return a string in the following format:
# If, at the end, there is free space left in the box, print:
# o"There is free space in the box. You could put {free space in cubes} more cubes."
# If there is no free space in the box, print:
# o"No more free space! You have {cubes left} more cubes."
#
# Test Code
# print(fill_the_box(2, 8, 2, 2, 1, 7, 3, 1, 5, "Finish"))
#
# Output
# There is free space in the box. You could put 13 more cubes.

from collections import deque


def fill_the_box(height, length, width, *args):
    volume = height * length * width

    # left_cubes = 0
    # for el in args:
    #     if el == 'Finish':
    #         break
    #     if volume >= el:
    #         volume -= el
    #     else:
    #         el -= volume
    #         left_cubes += el
    #         volume = 0

    cubes = deque(args)
    while True:
        current_cube = cubes.popleft()
        if current_cube == "Finish":
            break
        if volume - current_cube >= 0:
            volume -= current_cube
        else:
            if volume > 0:
                current_cube -= volume
                volume = 0
                cubes.append(current_cube)
            else:
                cubes.append(current_cube)

    if volume:
        return f"There is free space in the box. You could put {volume} more cubes."
    else:
        return f"No more free space! You have {sum(cubes)} more cubes."
        # return f"No more free space! You have {left_cubes} more cubes."


print(fill_the_box(2, 8, 2, 2, 1, 7, 3, 1, 5, "Finish"))
print(fill_the_box(5, 5, 2, 40, 11, 7, 3, 1, 5, "Finish"))
print(fill_the_box(10, 10, 10, 1001, "Finish", 2, 15, 30))
