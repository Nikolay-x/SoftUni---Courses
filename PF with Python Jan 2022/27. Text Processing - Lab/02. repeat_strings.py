# 2.Repeat Strings
# Write a program that reads a sequence of strings, separated by a single space. Each string should be repeated N times, where N is the length of the string. Print the final strings concatenated into one string.
#
# Input
# hi abc add
#
# Output
# hihiabcabcabcaddaddadd

strings_list = input().split(" ")
result = ""

for word in strings_list:
    result += word * len(word)

print(result)
