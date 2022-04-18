# 9.Password Validator
# Write a function that checks if a given password is valid. Password validations are:
# It should be 6 - 10 (inclusive) characters long
# It should consist only of letters and digits
# It should have at least 2 digits
# If a password is valid, print "Password is valid".
# Otherwise, for every unfulfilled rule, print a message:
# "Password must be between 6 and 10 characters"
# "Password must consist only of letters and digits"
# "Password must have at least 2 digits"
#
# Input
# logIn
#
# Output
# Password must be between 6 and 10 characters
# Password must have at least 2 digits

def password_validator(n):

    pass_length_is_valid = False
    pass_symbols_are_valid = False
    pass_digit_count = False
    symbols_count = 0
    digit_count = 0

    if 6 <= len(n) <= 10:
        pass_length_is_valid = True
    for i in range(len(n)):
        if 48 <= ord(n[i]) <= 57 or 65 <= ord(n[i]) <= 90 or 97 <= ord(n[i]) <= 122:
            symbols_count += 1
        if 48 <= ord(n[i]) <= 57:
            digit_count += 1

    if symbols_count == len(n):
        pass_symbols_are_valid = True
    if digit_count >= 2:
        pass_digit_count = True

    if pass_length_is_valid and pass_symbols_are_valid and pass_digit_count:
        print("Password is valid")
    if pass_length_is_valid == False:
        print("Password must be between 6 and 10 characters")
    if pass_symbols_are_valid == False:
        print("Password must consist only of letters and digits")
    if pass_digit_count == False:
        print("Password must have at least 2 digits")

password = input()
password_validator(password)
