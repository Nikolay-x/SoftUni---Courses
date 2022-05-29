# 1.Flatten Lists
# Write a program to flatten several lists of numbers received in the following format:
# String with numbers or empty strings separated by "|"
# Values are separated by spaces (" ", one or several)
# Order the output list from the last to the first matrix sub-lists and their values from left to right as shown below
#
# Input
# 1 2 3 |4 5 6 |  7  88
#
# Output
# 7 88 4 5 6 1 2 3

input_list = input().split("|")

result = []

for i in range(len(input_list)-1, -1, -1):
    current_element = input_list[i].split()
    result.extend(current_element)

print(" ".join(result))
