# 5.Legendary Farming
# You are playing a game, and your goal is to win a legendary item - any legendary item will be good enough. However, it's a tedious process, and it requires quite a bit of farming. The possible items are:
# "Shadowmourne" - requires 250 Shards
# "Valanyr" - requires 250 Fragments
# "Dragonwrath" - requires 250 Motes
# "Shards", "Fragments", and "Motes" are the key materials 	(case-insensitive), and everything else is junk.
# You will be given lines of input in the format:
# "{quantity1} {material1} {quantity2} {material2} … {quantityN} {materialN}"
# Keep track of the key materials - the first one that reaches 250, wins the race. At that point, you have to print that the corresponding legendary item is obtained.
# In the end, print the remaining shards, fragments, motes in the format:
# "shards: {number_of_shards}
# fragments: {number_of_fragments}
# motes: {number_of_motes}"
# Finally, print the collected junk items in the order of appearance.
#
# Input
# Each line comes in the following format: "{quantity1} {material1} {quantity2} {material2} … {quantityN} {materialN}"
# Output
# On the first line, print the obtained item in the format: "{Legendary item} obtained!"
# On the next three lines, print the remaining key materials
# On the several final lines, print the junk items
# All materials should be printed in the format: "{material}: {quantity}"
# The output should be lowercase, except for the first letter of the legendary
#
# Input
# 3 Motes 5 stones 5 Shards
# 6 leathers 255 fragments 7 Shards
#
# Output
# Valanyr obtained!
# shards: 5
# fragments: 5
# motes: 3
# stones: 5
# leathers: 6

stock_dict = dict()
there_is_legendary_item = False

while True:
    farming_list = input().split(" ")
    for i in range(0, len(farming_list), 2):
        quantity = int(farming_list[i])
        material = farming_list[i+1].lower()

        if material not in stock_dict.keys():
            stock_dict[material] = 0

        stock_dict[material] += quantity

        if material == "shards" and stock_dict[material] >= 250:
            print("Shadowmourne obtained!")
            stock_dict[material] -= 250
            there_is_legendary_item = True
            break
        elif material == "fragments" and stock_dict[material] >= 250:
            print("Valanyr obtained!")
            stock_dict[material] -= 250
            there_is_legendary_item = True
            break
        elif material == "motes" and stock_dict[material] >= 250:
            print("Dragonwrath obtained!")
            stock_dict[material] -= 250
            there_is_legendary_item = True
            break

    if there_is_legendary_item:
        break

if "shards" in stock_dict:
    print(f'shards: {stock_dict.pop("shards")}')
else:
    print(f'shards: 0')
if "fragments" in stock_dict:
    print(f'fragments: {stock_dict.pop("fragments")}')
else:
    print(f'fragments: 0')
if "motes" in stock_dict:
    print(f'motes: {stock_dict.pop("motes")}')
else:
    print(f'motes: 0')

for material, quantity in stock_dict.items():
    print(f"{material}: {quantity}")
