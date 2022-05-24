# 4.Count Symbols
# Write a program that reads a text from the console and counts the occurrences of each character in it. Print the results in alphabetical (lexicographical) order.
#
# Input
# SoftUni rocks
#
# Output
#  : 1 time/s
# S: 1 time/s
# U: 1 time/s
# c: 1 time/s
# f: 1 time/s
# i: 1 time/s
# k: 1 time/s
# n: 1 time/s
# o: 2 time/s
# r: 1 time/s
# s: 1 time/s
# t: 1 time/s

text = input()

text_dict = {}

for ch in text:
    if ch not in text_dict:
        text_dict[ch] = 0
    text_dict[ch] += 1

for ch, occurrences in sorted(text_dict.items()):
    print(f"{ch}: {occurrences} time/s")
