# 5. ASCII Values
# Write a program that receives a list of characters separated by ", ". It should create a dictionary with each character as a key and its ASCII value as a value. Try solving that problem using comprehension.
#
# Input
# a, b, c, a
#
# Output
# {'a': 97, 'b': 98, 'c': 99}

characters_list = input().split(", ")

dictionary = {char: ord(char) for char in characters_list}

print(dictionary)
