# 1.No Vowels
# Using comprehension, write a program that receives a text and removes all its vowels, case insensitive. Print the new text string after removing the vowels. The vowels that should be considered are 'a', 'o', 'u', 'e', 'i'.
#
# Input
# Python
#
# Output
# Pythn

vowels_list = ["a", "o", "u", "e", "i"]
text = input()

# no_vowels_text = []

no_vowels = [ch for ch in text if ch not in vowels_list]

# for ch in text:
#     if ch not in vowels_list:
#         no_vowels_text.append(ch)
#
# print("".join(no_vowels_text))

print("".join(no_vowels))
