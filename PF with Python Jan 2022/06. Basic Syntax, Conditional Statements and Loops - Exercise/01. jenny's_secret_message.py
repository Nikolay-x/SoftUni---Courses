# 1.Jenny's Secret Message
# Jenny studies programming with Python and wants to create a program that greets users when they give their names. The greeting should be in the format "Hello, {name}!". However, Jenny is in love with Johnny and would like to greet him differently: "Hello, my love!". Could you help her?
#
# Input
# Peter
#
# Output
# Hello, Peter!

name = input()

if name == "Johnny":
    print("Hello, my love!")
else:
    print(f"Hello, {name}!")
