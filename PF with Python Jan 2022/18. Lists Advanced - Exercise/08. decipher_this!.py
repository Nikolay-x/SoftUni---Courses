# 8.Decipher This!
# You are given a secret message you should decipher. To do that, you need to know that in each word:
# the second and the last letter are switched (e.g., Holle means Hello)
# the first letter is replaced by its character code (e.g., 72 means H)
#
# Input
# 72olle 103doo 100ya
#
# Output
# Hello good day

message = input().split(" ")

final_message = []

for word in message:

    first_letter_list = []
    final_word = []
    char_counter = 0

    for char in range(len(word)):
        if ord(word[char]) < 48 or ord(word[char]) > 57:
            char_counter += 1
            final_word.append(word[char])
        if char_counter == 0 and 48 <= ord(word[char]) <= 57:
            first_letter_list.append(word[char])

    first_letter = chr(int("".join(first_letter_list)))
    final_word[0], final_word[-1] = final_word[-1], final_word[0]
    final_word.insert(0, first_letter)
    final_message.append("".join(final_word))

print(" ".join(final_message))
