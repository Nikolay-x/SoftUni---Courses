# 5.Word Count
# Write a program that reads a list of words from the file words.txt and finds how many times each of the words is contained in another file text.txt. Matching should be case-insensitive.
# The results should be written to other text files. Sort the words by frequency in descending order.
#
# words.txt
# quick is fault
#
# input.txt
# -I was quick to judge him, but it wasn't his fault.
# -Is this some kind of joke?! Is it?
# -Quick, hide here…It is safer.
#
# output.txt
# is - 3
# quick - 2
# fault - 1

import re

words_path = './words.txt'
input_path = './input.txt'

words_file = open(words_path, 'r')
words_list = [x for x in ''.join(words_file.readlines()).split()]

input_file = open(input_path, 'r')
input_string = ''.join(input_file.readlines())
words_finder_regex = r"\b\S+\b"
words_in_input_file = re.findall(words_finder_regex, input_string)

match_words_dict = {}
for word in words_list:
    if word not in match_words_dict:
        match_words_dict[word] = 0

for word in words_list:
    for input_word in words_in_input_file:
        if word.lower() == input_word.lower():
            match_words_dict[word] += 1

sorted_dict = sorted(match_words_dict.items(), key=lambda x: x[1], reverse=True)
result = '\n'.join([f'{w} - {c}' for w, c in sorted_dict])

output_path = './output.txt'
output_file = open(output_path, "w")
output_file.write(result)

words_file.close()
input_file.close()
output_file.close()
