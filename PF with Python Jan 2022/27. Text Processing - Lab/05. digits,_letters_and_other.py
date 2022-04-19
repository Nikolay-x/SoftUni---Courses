# 5.Digits, Letters, and Other
# Write a program that receives a single string. On the first line, print all the digits found in the string, on the second – all the letters, and on the third – all the other characters. There will always be at least one digit, one letter, and one other character.
#
# Input
# Agd#53Dfg^&4F53
#
# Output
# 53453
# AgdDfgF
# #^&

string = input()
digits_string = ""
letters_string = ""
symbols_string = ""

# for ch in string:
#     if ch.isalnum():
#         if ch.isdigit():
#             digits_string += ch
#         else:
#             letters_string += ch
#     else:
#         symbols_string += ch

# for ch in string:
#     if ch.isdigit():
#         digits_string += ch
#     elif ch.isalpha():
#         letters_string += ch
#     else:
#         symbols_string += ch

for ch in string:
    if ch.isdigit():
        digits_string += ch
    elif ch.islower() or ch.isupper():
        letters_string += ch
    else:
        symbols_string += ch

# code only for symbols:
# for ch in string:
#     if not ch.isdigit() and not ch.isalpha():
#         symbols_string += ch

print(digits_string)
print(letters_string)
print(symbols_string)
