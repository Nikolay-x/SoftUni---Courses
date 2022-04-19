# 3.Find Occurrences of Word in Sentence
# Write a program that finds how many times a word is used in a string. The output is a single number indicating the number of times the string contains the word. Note that letter case does not matter – it is case-insensitive.
#
# Input
# The waterfall was so high, that the child couldn't see its peak.
# the
#
# Output
# 2

import re

sentence = input()
key_word = input()

regex = rf"\b{key_word}\b"

matches = re.findall(regex, sentence, re.IGNORECASE)

print(len(matches))
