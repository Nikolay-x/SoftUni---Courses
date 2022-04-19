# 5.Dragon Army
# Heroes III is the best game ever. Everyone loves it and everyone plays it all the time. Simon is no exclusion to this rule. His favorite units in the game are all types of dragons – black, red, gold, azure etc. He likes them so much that he gives them names and keeps logs of their stats: damage, health, and armor. The process of aggregating all the data is quite tedious, so he would like to have a program doing it. Since he is no programmer, it's your task to help him.
# You need to categorize dragons by their type. For each dragon, identified by name, keep information about his stats (damage, health, and armor). Type is preserved as in the order of input, but dragons are sorted alphabetically by their name. For each type, you should also print the average damage, health, and armor of the dragons. For each dragon, print his own stats.
# There may be missing stats in the input, though. If a stat is missing you should assign it default values. Default values are as follows: health 250, damage 45, and armor 10. Missing stat will be marked by "null".
# The input is in the following format "{type} {name} {damage} {health} {armor}".
# The "type" and the "name" are strings. The "damage", the "health", and the "armor" are integers. Any of the integers may be assigned "null" value. See the examples below for better understanding of your task.
# If the same dragon is added a second time, the new stats should overwrite the previous ones. Two dragons are considered equal if they match by both name and type.
# Input
# On the first line, you are given number N -> the number of dragons to follow.
# On the next N lines, you are given input in the above-described format. There will be a single space separating each element.
# Output
# Print the aggregated data on the console.
# For each type, print average stats of its dragons in format "{type}::({damage}/{health}/{armor})".
# Damage, health, and armor should be rounded to two digits after the decimal separator.
# For each dragon, print its stats in format "-{Name} -> damage: {damage}, health: {health}, armor: {armor}".
# Constraints
# N is in range [1…100].
# The dragon type and name are one word only, starting with capital letter.
# Damage health and armor are integers in range [0 … 100000] or null.
#
# Input
# 5
# Red Bazgargal 100 2500 25
# Black Dargonax 200 3500 18
# Red Obsidion 220 2200 35
# Blue Kerizsa 60 2100 20
# Blue Algordox 65 1800 50
#
# Output
# Red::(160.00/2350.00/30.00)
# -Bazgargal -> damage: 100, health: 2500, armor: 25
# -Obsidion -> damage: 220, health: 2200, armor: 35
# Black::(200.00/3500.00/18.00)
# -Dargonax -> damage: 200, health: 3500, armor: 18
# Blue::(62.50/1950.00/35.00)
# -Algordox -> damage: 65, health: 1800, armor: 50
# -Kerizsa -> damage: 60, health: 2100, armor: 20

# dragons = {}
# dtypes = []
# default_stats = (45, 250, 10)
#
# for _ in range(int(input())):
#     dtype, name, dmg, hp, ac = input().split(' ')
#     dmg, hp, ac = (default_stats[i] if x == 'null' else int(x) for i, x in enumerate((dmg, hp, ac)))
#
#     key = (dtype, name)
#     value = (dmg, hp, ac)
#     dragons[key] = value
#
#     if dtype not in dtypes:
#         dtypes.append(dtype)
#
# for dtype in dtypes:
#     stats = [v for k, v in dragons.items() if k[0] == dtype]
#     dmg, hp, ac = [sum(item) / len(item) for item in zip(*stats)]
#     print(f'{dtype}::({dmg:.2f}/{hp:.2f}/{ac:.2f})')
#
#     filtered_dragons = {k[1]: v for k, v in dragons.items() if k[0] == dtype}
#     output = {k: v for k, v in sorted(filtered_dragons.items(), key=lambda item: item[0])}
#     for k, v in output.items():
#         print(f'-{k} -> damage: {v[0]}, health: {v[1]}, armor: {v[2]}')

dragon_number = int(input())
default_stats = (45, 250, 10)
dragons_dict = dict()
dragons_avg_dict = list()

for i in range(dragon_number):

    (dr_type, name, damage, health, armor) = input().split(" ")
    damage, health, armor = (default_stats[i] if x == 'null' else int(x) for i, x in enumerate((damage, health, armor)))

    key = (dr_type, name)
    value = (int(damage), int(health), int(armor))
    dragons_dict[key] = value

    if dr_type not in dragons_avg_dict:
        dragons_avg_dict.append(dr_type)

for dr_type in dragons_avg_dict:
    stats = [v for k, v in dragons_dict.items() if k[0] == dr_type]
    damage, health, armor = [sum(item) / len(item) for item in zip(*stats)]
    print(f'{dr_type}::({damage:.2f}/{health:.2f}/{armor:.2f})')

    sorted_dragons = {k[1]: v for k, v in dragons_dict.items() if k[0] == dr_type}
    output = {key: value for key, value in sorted(sorted_dragons.items(), key=lambda item: item[0])}
    for key, value in output.items():
        print(f'-{key} -> damage: {value[0]}, health: {value[1]}, armor: {value[2]}')
