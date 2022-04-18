# 4.Balanced Brackets
# On the first line, you will receive n – the number of lines, which will follow. On the following n lines, you will receive one of the following:
# Opening bracket – "(",
# Closing bracket – ")" or
# Random string
# Your task is to find out if the brackets are balanced. That means after every closing bracket should follow an opening one. Nested parentheses are not valid, and if, for example, two consecutive opening brackets exist, the expression should be marked as unbalanced. You should print "BALANCED" if the parentheses are balanced and "UNBALANCED" otherwise.
#
# Input
# 8
# (
#         5 + 10
# )
# *2 +
# (
#     5
# )
# -12
#
# Output
# BALANCED

n = int(input())

opening_bracket_count = 0
closing_bracket_count = 0

is_brackets_balanced = True

for l in range(n):
    current_line = input()
    if current_line == "(":
        opening_bracket_count += 1
    elif current_line == ")":
        closing_bracket_count += 1
    if abs(opening_bracket_count - closing_bracket_count) > 1:
        is_brackets_balanced = False

if opening_bracket_count != closing_bracket_count:
    is_brackets_balanced = False

if is_brackets_balanced == True:
    print("BALANCED")
else:
    print("UNBALANCED")
