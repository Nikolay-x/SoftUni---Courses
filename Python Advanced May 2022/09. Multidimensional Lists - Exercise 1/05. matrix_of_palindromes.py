# 5.Matrix of Palindromes
# Write a program to generate the following matrix of palindromes of 3 letters with r rows and c columns like the one in the examples below.
# Rows define the first and the last letter: row 0  'a', row 1  'b', row 2  'c', …
# Columns + rows define the middle letter:
# ocolumn 0, row 0  'a', column 1, row 0  'b', column 2, row 0  'c', …
# ocolumn 0, row 1  'b', column 1, row 1  'c', column 2, row 1  'd', …
# Input
# The numbers r and c stay at the first line at the input in the format "{rows} {columns}"
# r and c are integers in the range [1, 26]
#
# Input
# 4 6
#
# Output
# aaa aba aca ada aea afa
# bbb bcb bdb beb bfb bgb
# ccc cdc cec cfc cgc chc
# ddd ded dfd dgd dhd did

import string

letters = string.ascii_lowercase

rows, cols = [int(x) for x in input().split()]

for i in range(rows):
    current_row = []
    for j in range(cols):
        current_string = letters[i] + letters[i+j] + letters[i]
        current_row.append(current_string)
    print(" ".join(current_row))
