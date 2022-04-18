# 1.Which Are In?
# You will be given two sequences of strings, separated by ", ". Print a new list containing only the strings from the first input line, which are substrings of any string in the second input line.
#
# Input
# arp, live, strong
# lively, alive, harp, sharp, armstrong
#
# Output
# ['arp', 'live', 'strong']

substrings = input().split(", ")
strings = input().split(", ")

final_list = []

for substring in substrings:
    count = 0
    for string in strings:
        if substring in string:
            count += 1
        if substring in string and count == 1:
            final_list.append(substring)

print(final_list)

# substrings = input().split(", ")
# string = input()
# result = [substring for substring in substrings if substring in string]
# print(result)
