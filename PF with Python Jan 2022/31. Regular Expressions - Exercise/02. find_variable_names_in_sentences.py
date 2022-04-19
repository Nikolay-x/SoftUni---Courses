# 2.Find Variable Names in Sentences
# Write a program that finds all variable names in each string. A variable name starts with an underscore ("_") and contains only capital and non-capital letters and digits. Extract only their names without the underscore. Try to do this only with regular expressions.
# The output consists of all variable names extracted and printed on a single line, separated by a comma.
#
# Input
# The _id and _age variables are both integers.
#
# Output
# id,age

import re

str_line = input()
final_matches = []

regex = r"\b_[A-Za-z0-9]+\b"
matches = re.findall(regex, str_line)

# for match in matches:
#     final_matches.append(match[1:])

for match in matches:
    final_match = ""
    for i in range(1, len(match)):
        final_match += match[i]
    final_matches.append(final_match)

print(",".join(final_matches))
