# 5.Patterns
# Write a program that receives a number and creates the following pattern. The number represents the largest count of stars on one row.
#
# Input
# 3
#
# Output
# *
# **
# ***
# **
# *

a = int(input())

for i in range(1, a +1):
    for j in range(1, i + 1):
        print("*", end = "")
    print()

for i in range(a - 1, 0, -1):
    for j in range(i, 0, -1):
        print("*", end = "")
    print()
