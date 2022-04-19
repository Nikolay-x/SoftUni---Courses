# 7. String Explosion
# Write a program that reads a string from the console that contains:
# Explosions marked with '>'
# Immediately after the mark, there will be an integer x, which signifies the strength of the explosion
# Any other characters
# Your task is to delete x characters, starting after the exploded character ('>'). If you find another explosion mark ('>') while deleting characters, you should add the strength to your previous explosion. You should not delete the explosion character – '>'.
# When all characters are processed, print the final string.
# Constraints
# You will always receive strength for the explosions
# The path will consist only of letters from the Latin alphabet, integers, and the char '>'
# The strength of the punches will be in the interval [0…9]
#
# Input
# abv>1>1>2>2asdasd
#
# Output
# abv>>>>dasd

text = input()
explosion_strength = 0
i = 0

while i < len(text):
    if text[i] == ">":
        explosion_strength += int(text[i+1])
        i += 1
    elif explosion_strength > 0:
        text = text[0:i] + text[i+1:]
        explosion_strength -= 1
    else:
        i += 1

print(text)
