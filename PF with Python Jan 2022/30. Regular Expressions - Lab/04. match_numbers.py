# 4.Match Numbers
# Write a program that finds all integer and floating-point numbers in a string.
# You can follow the table below to help with composing your RegEx:
#
# Match ALL of these
# 1 -1 123 -123 123.456 -123.456
#
# Match NONE of these
# 1s s2 s-s -1- _55_ s-2 s-3.5 s-1.1 00.5
#
# Input
# 1 -1 1s 123 s-s -123 _55_ _f 123.456 -123.456 s-1.1 s2 -1- zs-2 s-3.5 00.5
#
# Output
# 1 -1 123 -123 123.456 -123.456

import re

numbers_string = input()
regex = r"(^|(?<=\s))-?([0]|[1-9][0-9]*)(\.\d+)?($|(?=\s))"

matches = re.finditer(regex, numbers_string)

# output = list()
# for match in matches:
#     output.append(match.group())
#
# print(" ".join(output))

for match in matches:
    print(match.group(), end=" ")
