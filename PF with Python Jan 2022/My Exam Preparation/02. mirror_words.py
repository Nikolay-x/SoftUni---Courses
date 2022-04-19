# Problem 2 - Mirror words
# Problem for exam preparation for the Programming Fundamentals Course @SoftUni.
# Submit your solutions in the SoftUni judge system at https://judge.softuni.org/Contests/Practice/Index/2307#1.
#
# The SoftUni Spelling Bee competition is here. But it`s not like any other Spelling Bee competition out there. It`s different and a lot more fun! You, of course, are a participant, and you are eager to show the competition that you are the best, so go ahead, learn the rules and win!
# On the first line of the input, you will be given a text string. To win the competition, you have to find all hidden word pairs, read them, and mark the ones that are mirror images of each other.
# First of all, you have to extract the hidden word pairs. Hidden word pairs are:
# Surrounded by "@" or "#" (only one of the two) in the following pattern #wordOne##wordTwo# or @wordOne@@wordTwo@
# At least 3 characters long each (without the surrounding symbols)
# Made up of letters only
# If the second word, spelled backward, is the same as the first word and vice versa (casing matters!), they are a match, and you have to store them somewhere. Examples of mirror words:
# #Part##traP# @leveL@@Level@ #sAw##wAs#
# If you don`t find any valid pairs, print: "No word pairs found!"
# If you find valid pairs print their count: "{valid pairs count} word pairs found!"
# If there are no mirror words, print: "No mirror words!"
# If there are mirror words print:
# "The mirror words are:
# {wordOne} <=> {wordtwo}, {wordOne} <=> {wordtwo}, … {wordOne} <=> {wordtwo}"
# Input / Constraints
# You will recive a string.
# Output
# Print the proper output messages in the proper cases as described in the problem description.
# If there are pairs of mirror words, print them in the end, each pair separated by ", ".
# Each pair of mirror word must be printed with " <=> " between the words.
#
# Input
# @mix  # tix3dj#poOl##loOp#wl@@bong&song%4very$long@thong#Part##traP##@@leveL@@Level@##car#rac##tu@pack@@ckap@#rr#sAw##wAs#r#@w1r
#
# Output
# 5 word pairs found!
# The mirror words are:
# Part <=> traP, leveL <=> Level, sAw <=> wAs

import re

line = input()

first_words_list = []
second_words_list = []
mirror_pairs_list = list()

regex = r"(@|#)([A-Za-z]{3,})\1\1([A-Za-z]{3,})\1"

words_matches = re.finditer(regex, line)

for match in words_matches:
    first_words_list.append(match[2])
    second_words_list.append(match[3])

for i in range(len(first_words_list)):
    if first_words_list[i] == second_words_list[i][::-1]:
        mirror_pairs_list.append(f"{first_words_list[i]} <=> {second_words_list[i]}")

if len(first_words_list) == 0:
    print("No word pairs found!")
else:
    print(f"{len(first_words_list)} word pairs found!")

if len(mirror_pairs_list) == 0:
    print("No mirror words!")
else:
    print("The mirror words are:")
    print(", ".join(mirror_pairs_list))
