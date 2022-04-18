# 7.* Easter Gifts
# As a good friend, you decide to buy presents for your friends.
# Create a program that helps you plan the gifts for your friends and family. First, you are going to receive the gifts you plan on buying on a single line, separated by space, in the following format:
# "{gift1} {gift2} {gift3}… {giftn}"
# Then you will start receiving commands until you read the "No Money" message. There are three possible commands:
# "OutOfStock {gift}"
# oFind the gifts with this name in your collection, if any, and change their values to "None".
# "Required {gift} {index}"
# oIf the index is valid, replace the gift on the given index with the given gift.
# "JustInCase {gift}"
# oReplace the value of your last gift with this one.
# In the end, print the gifts on a single line, except the ones with value "None", separated by a single space in the following format:
# "{gift1} {gift2} {gift3} … {giftn}"
# Input / Constraints
# On the 1st line,  you will receive the names of the gifts, separated by a single space.
# On the following lines, until the "No Money" command is received, you will be receiving commands.
# The input will always be valid.
# Output
# Print the gifts in the format described above.
#
# Input
# Eggs StuffedAnimal Cozonac Sweets EasterBunny Eggs Clothes
# OutOfStock Eggs
# Required Spoon 2
# JustInCase ChocolateEgg
# No Money
#
# Output
# StuffedAnimal Spoon Sweets EasterBunny ChocolateEgg

gifts_list = input().split(" ")

command = input().split(" ")

while " ".join(command) != "No Money":

    if "OutOfStock" in command:
        for i in range(len(gifts_list)):
            if gifts_list[i] == command[1]:
                gifts_list[i] = "None"

    elif "Required" in command:
        if 0 <= int(command[2]) < len(gifts_list):
                gifts_list[int(command[2])] = command[1]

    elif "JustInCase" in command:
        gifts_list[-1] = command[1]

    command = input().split(" ")

for i in range(len(gifts_list) -1, -1, -1):
    if gifts_list[i] == "None":
        gifts_list.remove(gifts_list[i])

print(" ".join(gifts_list))
