# 1.Valid Usernames
# Write a program that reads usernames on a single line (separated by ", ") and prints all valid usernames on separate lines.
# A valid username:
# has length between 3 and 16 characters inclusive
# can contain only letters, numbers, hyphens, and underscores
# has no redundant symbols before, after, or in between
#
# Input
# sh, too_long_username, !lleg@l ch@rs, jeffbutt
#
# Output
# jeffbutt

# import string
#
#
# def valid_username(data):
#     expected_elements = string.digits + string.ascii_letters + "-" + "_"
#     for name in data:
#         flag = 0
#         if 3 > len(name) or len(name) > 16:
#             flag = 1
#         elif len([x for x in name if x in expected_elements]) != len(name):
#             flag = 1
#         elif flag == 0:
#             print(name)
#
#
# d = input().split(", ")
# valid_username(d)

import string

usernames = input().split(", ")

allowed_characters = string.digits + string.ascii_letters + "-" + "_"

for username in usernames:
    if 3 <= len(username) <= 16:
        if len([x for x in username if x in allowed_characters]) == len(username):
            print(username)
