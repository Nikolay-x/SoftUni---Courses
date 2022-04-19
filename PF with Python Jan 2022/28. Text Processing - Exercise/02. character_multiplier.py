# 2. Character Multiplier
# Create a program that receives two strings on a single line separated by a single space. Then, it prints the sum of their multiplied character codes as follows: multiply str1[0] with str2[0] and add the result to the total sum, then continue with the next two characters. If one of the strings is longer than the other, add the remaining character codes to the total sum without multiplication.
#
# Input
# George Peter
#
# Output
# 52114

# two_strings = input().split(" ")
# result = 0
#
# if len(two_strings[0]) >= len(two_strings[1]):
#     for i in range(len(two_strings[1])):
#         result += ord(two_strings[0][i]) * ord(two_strings[1][i])
#     j = len(two_strings[0]) - i
#     for q in range(-1, -1-j+1, -1):
#         result += ord(two_strings[0][q])
# else:
#     for i in range(len(two_strings[0])):
#         result += ord(two_strings[0][i]) * ord(two_strings[1][i])
#     j = len(two_strings[1]) - i
#     for q in range(-1, -1-j+1, -1):
#         result += ord(two_strings[1][q])
#
# print(result)

two_strings = input().split(" ")
result = 0

if len(two_strings[0]) >= len(two_strings[1]):
    for i in range(len(two_strings[0]) - len(two_strings[1])):
        two_strings[1] += ""
else:
    for i in range(len(two_strings[1]) - len(two_strings[0])):
        two_strings[0] += ""

for i in range(len(two_strings[0])):
    result += ord(two_strings[0][i]) * ord(two_strings[1][i])

print(result)
