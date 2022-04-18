# 3.Decrypting Messages
# On the first line, you will receive a key (integer). On the second line, you will receive n – the number of lines, which will follow. On the next n lines – you will receive a lower and an uppercase letter per line.
# You should add the key to each of the characters and append them to a message. In the end, print the decrypted message.
#
# Input
# 3
# 7
# P
# l
# c
# q
# R
# k
# f
#
# Output
# SoftUni

key = int(input())
lines_count = int(input())

decrypted_message = ""

for l in range(lines_count):
    current_line = input()
    decrypted_message += chr(ord(current_line) + key)

print(decrypted_message)
