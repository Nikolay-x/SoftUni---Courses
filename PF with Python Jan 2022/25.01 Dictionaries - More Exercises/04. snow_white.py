# 4.Snow White
# Snow White loves her dwarfs, but there are so many, and she doesn't know how to order them. Does she order them by name? Or by color of their hat? Or by physics? She can't decide, so it's up to you to write a program that does it for her.
# You will be receiving several input lines which contain data about each dwarf in the following format:
# {dwarf_name} <:> {dwarf_hat_color} <:> {dwarf_physics}
# The "dwarf_name" and the "dwarf_hat_color" are strings. The "dwarf_physics" is an integer.
# You must store the data about the dwarfs in your program. There are several rules though:
# If 2 dwarfs have the same name but different color, they should be considered different dwarfs, and you should store them both.
# If 2 dwarfs have the same name and the same color, store the one with the higher physics.
# When you receive the command "Once upon a time", the input ends. You must order the dwarfs by physics in descending order and then by total count of dwarfs with the same hat color in descending order.
# Then you must print them all.
# Input
# The input will consist of several input lines, containing dwarf data in the format, specified above.
# The input ends when you receive the command "Once upon a time".
# Output
# As output, you must print the dwarfs, ordered in the way, specified above.
# The output format is: "({hat_color}) {name} <-> {physics}"
# Constraints
# The "dwarf_name" will be a string which may contain any ASCII character except ' ' (space), '<', ':', '>'.
# The "dwarf_hat_color" will be a string which may contain any ASCII character except ' ' (space), '<', ':', '>'.
# The "dwarf_physics" will be an integer in range [0, 231 – 1].
# There will be no invalid input lines.
# If all sorting criteria fail, the order should be by order of input.
# Allowed working time / memory: 100ms / 16MB.
#
# Input
# Peter <:> Red <:> 2000
# Teodor <:> Blue <:> 1000
# George <:> Green <:> 1000
# Simon <:> Yellow <:> 4500
# Dopey <:> Simon <:> 1000
# Once upon a time
#
# Output
# (Yellow) Simon <-> 4500
# (Red) Peter <-> 2000
# (Blue) Teodor <-> 1000
# (Green) George <-> 1000
# (Simon) Dopey <-> 1000

# dwarfs = {}
# hat_colours = {}
#
# while True:
#     input_line = input()
#     if input_line == 'Once upon a time':
#         break
#
#     name, colour, physics = input_line.split(' <:> ')
#     key = (name, colour)
#     value = int(physics)
#
#     if key in dwarfs:
#         dwarfs[key] = max(value, dwarfs.get(key))
#     else:
#         dwarfs[key] = value
#
#         if not colour in hat_colours:
#             hat_colours[colour] = 0
#         hat_colours[colour] += 1
#
# sorted_dwarfes = sorted(dwarfs.items(), key=lambda item: (item[1], hat_colours[item[0][1]]), reverse=True)
# for dwarf in sorted_dwarfes:
#     print(f'({dwarf[0][1]}) {dwarf[0][0]} <-> {dwarf[1]}')

dwarf_dict = dict()
dwarf_hat_color_count = dict()

while True:
    line = input()
    if line == "Once upon a time":
        break
    (dwarf_name, dwarf_hat_color, dwarf_physics) = line.split(" <:> ")
    key = (dwarf_hat_color, dwarf_name)
    value = int(dwarf_physics)
    if key not in dwarf_dict:
        dwarf_dict[key] = value
    else:
        if dwarf_dict[key] < int(dwarf_physics):
            dwarf_dict[key] = int(dwarf_physics)

for key in dwarf_dict:
    if key[0] not in dwarf_hat_color_count:
        dwarf_hat_color_count[key[0]] = 1
    else:
        dwarf_hat_color_count[key[0]] += 1

sorted_dwarf_dict = sorted(dwarf_dict.items(), key=lambda item: (item[1], dwarf_hat_color_count[item[0][0]]),
                           reverse=True)

for i in range(len(sorted_dwarf_dict)):
    print(f'({sorted_dwarf_dict[i][0][0]}) {sorted_dwarf_dict[i][0][1]} <-> {sorted_dwarf_dict[i][1]}')
