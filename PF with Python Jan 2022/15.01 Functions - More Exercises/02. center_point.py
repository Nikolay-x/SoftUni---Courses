# 2.Center Point
# You will be given the coordinates of two points on a Cartesian coordinate system - X1, Y1, X2, and Y2 on separate lines. Write a function that prints the point which is closest to the center of the coordinate system (0, 0) in the format: "({X}, {Y})"
# If the points are at the same distance from the center, print only the first one. The resulting coordinates must be formatted to the lower integer.
#
# Input
# 2
# 4
# -1
# 2
#
# Output
# (-1, 2)

from math import sqrt, floor

def center_point(x1, y1, x2, y2):

    # distance1 = (abs(x1) ** 2 + abs(y1) ** 2) ** 1/2
    # distance2 = (abs(x2) ** 2 + abs(y2) ** 2) ** 1/2

    distance1 = sqrt(abs(x1) ** 2 + abs(y1) ** 2)
    distance2 = sqrt(abs(x2) ** 2 + abs(y2) ** 2)

    if distance2 < distance1:
        result = f"({floor(x2)}, {floor(y2)})"
    else:
        result = f"({floor(x1)}, {floor(y1)})"
    return result

a1 = float(input())
b1 = float(input())
a2 = float(input())
b2 = float(input())

print(center_point(a1, b1, a2, b2))
