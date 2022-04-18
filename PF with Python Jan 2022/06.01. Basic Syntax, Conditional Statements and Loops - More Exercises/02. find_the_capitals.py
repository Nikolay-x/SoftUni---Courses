# 2.Find the Capitals
# Write a program that takes a single string and prints a list of all the capital letters indices.
#
# Input
# pYtHoN
#
# Output
# [1, 3, 5]

string = input()

list = []

for i in range(len(string)):
    if 65 <= ord(string[i]) <= 90:
        list.append(i)

print(list)
