# 1.Count Chars in a String
# Write a program that counts all characters in a string except for space (" ").
# Print all the occurrences in the following format:
# "{char} -> {occurrences}"
#
# Input
# text
#
# Output
# t -> 2
# e -> 1
# x -> 1

characters_line = input()
char_dict = dict()

for ch in characters_line:
    if ch not in char_dict and ch != " ":
        char_dict[ch] = 0
    if ch != " ":
        char_dict[ch] += 1

for (character, occurrences) in char_dict.items():
    print(f"{character} -> {occurrences}")

# from collections import Counter
#
# line = input()
# result = Counter(line)
#
# for key, value in result.items():
#     if key != " ":
#         print(f'{key} -> {value}')
