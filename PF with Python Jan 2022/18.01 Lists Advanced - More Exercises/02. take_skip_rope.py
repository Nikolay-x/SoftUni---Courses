# 2.Take/Skip Rope
# Write a program, which reads a string and skips through it, extracting a hidden message. The algorithm you should implement is as follows:
# Let us take the string "skipTest_String044170" as an example.
# Take every digit from the string and transfer it somewhere. After this operation, you should have two lists of items - a numbers list and a non-numbers list:
# Numbers' list: [0, 4, 4, 1, 6, 0]
# Non-numbers: [s, k, i, p, T, e, s, t, _, S, t, r, i, n, g]
# After that, take every digit in the numbers list and split it up into a take list and a skip list. In the take list, you should keep all digits at an even index. In the skip list, you should keep all digits at an odd index.
# Numbers' list: [0, 4, 4, 1, 6, 0]
# Take list: [0, 4, 6]
# Skip list: [4, 1, 0]
# Afterward, iterate over both lists:
# First, take m characters from the non-numbers list and store it in a result string
# Then, skip n characters from the non-numbers list
# Note that the skipped characters are summed up as they go. The process would look like this:
# 1.Current string: "skipTest_String". Take 0 characters and skip 4 characters:
# Taken string: ""
# Skipped string: "skip"
# 2.The remaining string looks like this: "Test_String". Take 4 characters and skip 1 character:
# Taken string: "Test"
# Skipped string: "_"
# 3.The string looks like this: "String". Take 6 characters and skip 0 characters:
# Taken string: "String"
# Skipped string: ""
# 4.The final string is "TestString".
# After that, print the final string on the console.
# Constraints
# The count of digits in the input string will always be even.
# The encrypted message will contain any printable ASCII character.
#
# Input
# T2exs15ti23ng1_3cT1h3e0_Roppe
#
# Output
# TestingTheRope

string_list = [ch for ch in input()]

number_list = []
non_numbers_list = []
take_list = []
skip_list = []
result_string = []

for ch in string_list:
    if 48 <= ord(ch) <= 57:
        number_list.append(int(ch))
    else:
        non_numbers_list.append(ch)

for num in range(len(number_list)):
    count = 0
    if num % 2 == 0:
        take_list.append(number_list[num])
        count += number_list[num]
        if count <= len(non_numbers_list):
            for i in range(count):
                result_string.append(non_numbers_list[i])
            for i in range(count):
                non_numbers_list.pop(0)
        else:
            for i in range(len(non_numbers_list)):
                result_string.append(non_numbers_list[i])
            for i in range(len(non_numbers_list)):
                non_numbers_list.pop(0)
    else:
        skip_list.append(number_list[num])
        count += number_list[num]
        if count <= len(non_numbers_list):
            for i in range(count):
                non_numbers_list.pop(0)
        else:
            for i in range(len(non_numbers_list)):
                non_numbers_list.pop(0)

print("".join(result_string))
