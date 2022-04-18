# 3.Longer Line
# You will be given the coordinates of four points. The first and the second pair of points form two different lines. Create a function that prints the longer line in the format "({X1}, {Y1})({X2}, {Y2})" starting from the point which is closer to the center of the coordinate system (0, 0). You can reuse the method that you wrote for the previous problem. If the lines are of equal length, print only the first one. The resulting coordinates must be formatted to the lower integer.
#
# Input
# 2
# 4
# -1
# 2
# -5
# -5
# 4
# -3
#
# Output
# (4, -3)(-5, -5)

from math import sqrt, floor

def closer_point(x1, y1, x2, y2):

    distance1 = sqrt(abs(x1) ** 2 + abs(y1) ** 2)
    distance2 = sqrt(abs(x2) ** 2 + abs(y2) ** 2)

    if distance2 < distance1:
        # result = f"p1({floor(x2)},{floor(y2)}) p2({floor(x1)},{floor(y1)})"
        result = f"({floor(x2)}, {floor(y2)})({floor(x1)}, {floor(y1)})"
    else:
        # result = f"p1({floor(x1)},{floor(y1)}), p2({floor(x2)},{floor(y2)})"
        result = f"({floor(x1)}, {floor(y1)})({floor(x2)}, {floor(y2)})"

    return result

def longer_line(x1_ln1, y1_ln1, x2_ln1, y2_ln1, x1_ln2, y1_ln2, x2_ln2, y2_ln2):

    line1 = sqrt(abs(x1_ln1 - x2_ln1)**2 + abs(y1_ln1 - y2_ln1)**2)
    line2 = sqrt(abs(x1_ln2 - x2_ln2)**2 + abs(y1_ln2 - y2_ln2)**2)

    if line1 > line2:
        result = closer_point(x1_ln1, y1_ln1, x2_ln1, y2_ln1)
    else:
        result = closer_point(x1_ln2, y1_ln2, x2_ln2, y2_ln2)

    # result = f"Longer line points (x, y) are: {result} \nLine 1 length = {line1:.2f}, Line 2 length = {line2:.2f}"

    return result

a1_ln1 = float(input())
b1_ln1 = float(input())
a2_ln1 = float(input())
b2_ln1 = float(input())
a1_ln2 = float(input())
b1_ln2 = float(input())
a2_ln2 = float(input())
b2_ln2 = float(input())

print(longer_line(a1_ln1, b1_ln1, a2_ln1, b2_ln1, a1_ln2, b1_ln2, a2_ln2, b2_ln2))
