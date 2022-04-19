# Problem 2 - Emoji Detector
# Problem for exam preparation for the Programming Fundamentals Course @SoftUni.
# Submit your solutions in the SoftUni judge system at https://judge.softuni.org/Contests/Practice/Index/2302#1.
#
# Your task is to write a program that extracts emojis from a text and find the threshold based on the input.
# You have to get your cool threshold. It is obtained by multiplying all the digits found in the input.  The cool threshold could be a huge number, so be mindful.
# An emoji is valid when:
# It is surrounded by 2 characters, either "::" or "**"
# It is at least 3 characters long (without the surrounding symbols)
# It starts with a capital letter
# Continues with lowercase letters only
# Examples of valid emojis: ::Joy::, **Banana**, ::Wink::
# Examples of invalid emojis: ::Joy**, ::fox:es:, **Monk3ys**, :Snak::Es::
# You need to count all valid emojis in the text and calculate their coolness. The coolness of the emoji is determined by summing all the ASCII values of all letters in the emoji.
# Examples: ::Joy:: - 306, **Banana** - 577, ::Wink:: - 409
# You need to print the result of the cool threshold and, after that to take all emojis out of the text, count them and print only the cool ones on the console.
# Input
# On the single input, you will receive a piece of string.
# Output
# On the first line of the output, print the obtained Cool threshold in the format:
# "Cool threshold: {coolThresholdSum}"
# On the following line, print the count of all emojis found in the text in format:
# "{countOfAllEmojis} emojis found in the text. The cool ones are:
# {cool emoji 1}
# {cool emoji 2}
# …
# {cool emoji N}"
# Constraints
# There will always be at least one digit in the text!
#
# Input
# In the Sofia Zoo there are 311 animals in total! ::Smiley:: This includes 3 **Tigers**, 1 ::Elephant:, 12 **Monk3ys**, a **Gorilla::, 5 ::fox:es: and 21 different types of :Snak::Es::. ::Mooning:: **Shy**
#
# Output
# Cool threshold: 540
# 4 emojis found in the text. The cool ones are:
# ::Smiley::
# **Tigers**
# ::Mooning::

import re

line = input()
emoji_list = []
cool_emoji_list = list()
emoji_count = 0

cool_threshold_regex = r"\d"
emoji_regex = r"(\:\:|\*\*)([A-Z][a-z]{2,})\1"

cool_threshold = 1

threshold_matches = re.findall(cool_threshold_regex, line)

for match in threshold_matches:
    cool_threshold *= int(match)

emoji_matches = re.finditer(emoji_regex, line)

for match in emoji_matches:
    emoji_list.append(match.group())
    emoji_count = len(emoji_list)
    emoji_text = match[2]
    emoji_cool_value = 0
    for ch in emoji_text:
        emoji_cool_value += ord(ch)
    if emoji_cool_value >= cool_threshold:
        cool_emoji_list.append(match[0])

print(f"Cool threshold: {cool_threshold}")
print(f"{emoji_count} emojis found in the text. The cool ones are:")
for emoji in cool_emoji_list:
    print(f"{emoji}")
