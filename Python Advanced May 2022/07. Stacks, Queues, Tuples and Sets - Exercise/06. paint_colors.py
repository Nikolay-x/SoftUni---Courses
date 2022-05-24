# 6.Paint Colors
# You will have to find all possible color combinations that can be used.
# Write a program that finds colors in a string. You will be given a string on a single line containing substrings (separated by a single space) from which you will be able to form the following colors:
# Main colors: "red", "yellow", "blue"
# Secondary colors: "orange", "purple", "green"
# To form a color, you should concatenate the first and the last substrings and check if you can get any of the above colors' names. If there is only one substring left, you should use it to do the same check.
# You can only keep a secondary color if the two main colors needed for its creation could be formed from the given substrings:
# orange = red + yellow
# purple = red + blue
# green = yellow + blue
# Note: You could find some of the main colors needed to keep a secondary color after it is found.
# When you form a color, remove both substrings. Otherwise, you should remove the last character of each substring and return them in the middle of the original string. If the string contains an odd number of substrings, you should put the substrings one position ahead.
# For example, if you are given the string "re yellow bye" you could not form a color with the substring "re" and "bye", so you should remove the last character and return them in the middle of the string: "r by yellow".
# In the end, print out the list with colors in the order in which they are found.
# Input
# Single line string
# Output
# The list with the collected colors
# Constrains
# You will not receive an empty string
# Please consider only the colors mentioned above
# There won't be any cases with repeating colors
#
# Input
# d yel blu e low redd
#
# Output
# ['yellow', 'blue', 'red']

from collections import deque

string_parts = deque(input().split())

main_colors = {"red", "yellow", "blue"}
secondary_colors = {"orange", "purple", "green"}

colors_found = []

while string_parts:
    first = string_parts.popleft()
    last = string_parts.pop() if string_parts else ""

    result = first + last

    if result in main_colors or result in secondary_colors:
        colors_found.append(result)
        continue

    result = last + first

    if result in main_colors or result in secondary_colors:
        colors_found.append(result)
        continue

    first = first[:-1]
    last = last[:-1]

    if first:
        string_parts.insert(len(string_parts) // 2, first)
    if last:
        string_parts.insert(len(string_parts) // 2, last)

output_colors = []

secondary_color_validation = {
    'orange': ['red', 'yellow'],
    'purple': ['red', 'blue'],
    'green': ['yellow', 'blue']
}

for color in colors_found:
    if color in main_colors:
        output_colors.append(color)
        continue

    is_collected = True
    for validation_color in secondary_color_validation[color]:
        if validation_color not in colors_found:
            is_collected = False
            break
    if is_collected:
        output_colors.append(color)

print(output_colors)
