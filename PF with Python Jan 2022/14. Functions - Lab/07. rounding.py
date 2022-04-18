# 7.Rounding
# Write a program that rounds all the given numbers, separated by a single space, and prints the result as a list. Use round().
#
# Input
# 1.0 2.5 3.0 4.5
#
# Output
# [1, 2, 3, 4]

def rounding(a):
    float_num = list(map(float, a))
    result = []
    for i in float_num:
        result.append(round(i))
    return result

input_num = input().split(" ")

print(rounding(input_num))
