# 02. Treasure Hunt
# Submit your solutions in the SoftUni judge system at https://judge.softuni.org/Contests/Practice/Index/1773#1.
# The pirates need to carry a treasure chest safely back to the ship, looting along the way.
# Create a program that manages the state of the treasure chest along the way. On the first line, you will receive the initial loot of the treasure chest, which is a string of items separated by a "|".
# "{loot1}|{loot2}|{loot3} … {lootn}"
# The following lines represent commands until "Yohoho!" which ends the treasure hunt:
# "Loot {item1} {item2}…{itemn}":
# oPick up treasure loot along the way. Insert the items at the beginning of the chest.
# oIf an item is already contained, don't insert it.
# "Drop {index}":
# oRemove the loot at the given position and add it at the end of the treasure chest.
# oIf the index is invalid, skip the command.
# "Steal {count}":
# oSomeone steals the last count loot items. If there are fewer items than the given count, remove as much as there are.
# oPrint the stolen items separated by ", ":
# "{item1}, {item2}, {item3} … {itemn}"
# In the end, output the average treasure gain, which is the sum of all treasure items length divided by the count of all items inside the chest formatted to the second decimal point:
# "Average treasure gain: {averageGain} pirate credits."
# If the chest is empty, print the following message:
# "Failed treasure hunt."
# Input
# On the 1st line, you are going to receive the initial treasure chest (loot separated by "|")
# On the following lines, until "Yohoho!", you will be receiving commands.
# Output
# Print the output in the format described above.
# Constraints
# The loot items will be strings containing any ASCII code.
# The indexes will be integers in the range [-200…200]
# The count will be an integer in the range [1….100]
#
# Input
# Gold|Silver|Bronze|Medallion|Cup
# Loot Wood Gold Coins
# Loot Silver Pistol
# Drop 3
# Steal 3
# Yohoho!
#
# Output
# Medallion, Cup, Gold
# Average treasure gain: 5.40 pirate credits.

treasure_chest = input().split("|")

line = input()
sum = 0

while line != "Yohoho!":
    if "Loot" in line:
        l = line.split(" ")
        for i in range(1, len(l)):
            if l[i] not in treasure_chest:
                treasure_chest.insert(0, l[i])
    if "Drop" in line:
        l = line.split(" ")
        if 0 <= int(l[1]) < len(treasure_chest):
            loot = treasure_chest.pop(int(l[1]))
            treasure_chest.append(loot)
    if "Steal" in line:
        l = line.split(" ")
        count = int(l[1])
        stolen_items = []
        if count <= len(treasure_chest):
            for i in range(count):
                stolen_items.append(treasure_chest[-1])
                treasure_chest.pop(-1)
        else:
            for i in range(len(treasure_chest)):
                stolen_items.append(treasure_chest[-1])
                treasure_chest.pop(-1)
        stolen_items.reverse()
        print(", ".join(stolen_items))

    line = input()

for item in treasure_chest:
    sum += len(item)

if not treasure_chest:
    print("Failed treasure hunt.")
else:
    avg_gain = sum / len(treasure_chest)
    print(f"Average treasure gain: {avg_gain:.2f} pirate credits.")
