# 3.Word Reverse
# Write a program that receives a single word, reverses it, and prints it.
#
# Input
# Python
#
# Output
# nohtyP

word = input()

reversed_word = ""

for i in range(len(word)-1, -1, -1):
    reversed_word += word[i]

print(reversed_word)
