# 6.Odd Occurrences
# Write a program that prints all elements from a given sequence of words that occur an odd number of times (case-insensitive) in it.
# Words are given on a single line, space-separated.
# Print the result elements in lowercase, in their order of appearance.
#
# Input
# Java C# PHP PHP JAVA C java
#
# Output
# java c# c

words_line = input().split(" ")
# words_line = list(map(lambda x: x.lower(), words_line))
words_dict = dict()

for word in words_line:

    word_lower = word.lower()
    if word_lower not in words_dict:
        words_dict[word_lower] = 0
    words_dict[word_lower] += 1

    # if word not in words_dict:
    #     words_dict[word] = 1
    # else:
    #     words_dict[word] += 1

for word in words_dict:
    if words_dict[word] % 2 != 0:
        print(word, end=" ")

# for (key, value) in words_dict.items():
#     if value % 2 != 0:
#         print(key, end=" ")
