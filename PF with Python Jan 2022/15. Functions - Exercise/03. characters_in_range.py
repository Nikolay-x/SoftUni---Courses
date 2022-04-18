# 3.Characters in Range
# Write a function that receives two characters and returns a single string with all the characters in between them (according to the ASCII code), separated by a single space. Print the result on the console.
#
# Input
# a
# d
#
# Output
# b c

def ascii_string(a, b):
    for i in range(ord(a)+1, ord(b)):
        print(chr(i), end=" ")

x = input()
y = input()

ascii_string(x, y)
