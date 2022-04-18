# 4.Sum of a Beach
# Beaches are filled with sand, water, fish, and sun. Given a string, calculate how many times the words "Sand", "Water", "Fish", and "Sun" appear (case insensitive).
#
# Input
# WAtErSlIde
#
# Output
# 1

s = input()

string = s.lower()

count = string.count("sand") + string.count("water") + string.count("fish") + string.count("sun")

print(count)
