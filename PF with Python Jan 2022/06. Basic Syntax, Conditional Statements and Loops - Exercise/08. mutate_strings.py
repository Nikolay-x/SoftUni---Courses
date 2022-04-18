# 8.* Mutate Strings
# You will be given two strings. Transform the first string into the second one, letter by letter. Print only the unique strings.
# Note: the strings will have the same lengths.
#
# Input
# bubble gum
# turtle hum
#
# Output
# tubble gum
# turble gum
# turtle gum
# turtle hum

first_word = input()
second_word = input()

for i in range(len(first_word)):
    if first_word[i] != second_word[i]:
        first_word = first_word[0: i: 1] + second_word[i] + first_word[i+1: len(first_word): 1]
        print(first_word)
