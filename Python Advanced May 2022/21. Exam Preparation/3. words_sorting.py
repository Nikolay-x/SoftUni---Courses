# 3.Words Sorting
# Link to Judge: https://judge.softuni.org/Contests/Practice/Index/3430#2
# Write a function words_sorting which receives a different number of words.
# Create a dictionary, which will have as keys the words that the function received. For each key, create a value that is the sum of all ASCII values of that key.
# Then, sort the dictionary:
# By values in descending order, if the sum of all values of the dictionary is odd
# By keys in ascending order, if the sum of all values of the dictionary is even
# Note: Submit only the function in the judge system
# Input
# There will be no input, just any number of words passed to your function
# Output
# The function should return a string in the format "{key} - {value}" for each key and value on a separate lines
# Constraints:
# There will be no case with capital letters.
# There will be no case with a string consisting of other than letters.
#
# Test Code
# print(
#     words_sorting(
#         'escape',
#         'charm',
#         'mythology'
#     ))
#
# Output
# charm - 523
# escape - 625
# mythology - 1004

def words_sorting(*words):
    words_dict = {}
    for word in words:
        key = word
        value = 0
        for ch in word:
            value += ord(ch)
        words_dict[key] = value
    if sum(words_dict.values()) % 2 != 0:
        sorted_words_dict = sorted(words_dict.items(), key=lambda x: x[1], reverse=True)
    else:
        sorted_words_dict = sorted(words_dict.items())
    result = []
    for el in sorted_words_dict:
        result.append(f"{el[0]} - {el[1]}")
    return '\n'.join(result)


print(
    words_sorting(
        'escape',
        'charm',
        'mythology'
  ))

print(
    words_sorting(
        'escape',
        'charm',
        'eye'
  ))

print(
    words_sorting(
        'cacophony',
        'accolade'
  ))
