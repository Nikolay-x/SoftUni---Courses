# 6. Replace Repeating Chars
# Write a program that reads a string from the console and replaces any sequence of the same letters with a single corresponding letter.
#
# Input
# aaaaabbbbbcdddeeeedssaa
#
# Output
# abcdedsa

text = input()
result = ""

for i in range(len(text)):
    if i + 1 < len(text):
        if text[i] != text[i+1]:
            result += text[i]
    else:
        result += text[-1]

print(result)
