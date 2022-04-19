# 1.Extract Person Information
# Write a program that reads N lines of strings and extracts the name and the age of a given person:
# The person's name will be surrounded by "@" and "|" in the format "@{name}|".
# The person's age will be surrounded by "#" and "*" in the format "#{age}*".
# Example: "Hello my name is @Peter| and I am #20* years old."
# For each found name-age pair, print a line in the following format "{name} is {age} years old."
#
# Input
# 2
# Here is a name @George| and an age #18*
# Another name @Billy| #35* is his age
#
# Output
# George is 18 years old.
# Billy is 35 years old.

n = int(input())

for i in range(n):
    line = input()
    name = ""
    age = ""

    for q, ch in enumerate(line):
        if ch == "@":
            name_starting_index = q + 1
        if ch == "#":
            age_starting_index = q + 1

    while line[name_starting_index] != "|":
        name += line[name_starting_index]
        name_starting_index += 1

    while line[age_starting_index] != "*":
        age += line[age_starting_index]
        age_starting_index += 1

    print(f'{name} is {age} years old.')
