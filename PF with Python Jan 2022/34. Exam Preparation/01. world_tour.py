# 01. World Tour
# Submit your solutions in the SoftUni judge system at https://judge.softuni.org/Contests/Practice/Index/2518#0.
#
# You are a world traveler, and your next goal is to make a world tour. To do that, you have to plan out everything first. To start with, you would like to plan out all of your stops where you will have a break.
# On the first line, you will be given a string containing all of your stops. Until you receive the command "Travel", you will be given some commands to manipulate that initial string. The commands can be:
# "Add Stop:{index}:{string}":
# oInsert the given string at that index only if the index is valid
# "Remove Stop:{start_index}:{end_index}":
# oRemove the elements of the string from the starting index to the end index (inclusive) if both indices are valid
# "Switch:{old_string}:{new_string}":
# oIf the old string is in the initial string, replace it with the new one (all occurrences)
# Note: After each command, print the current state of the string
# After the "Travel" command, print the following: "Ready for world tour! Planned stops: {string}"
# Input / Constraints
# JavaScript: you will receive a list of strings
# An index is valid if it is between the first and the last element index (inclusive) in the sequence.
# Output
# Print the proper output messages in the proper cases as described in the problem description
#
# Input
# Hawai::Cyprys-Greece
# Add Stop:7:Rome
# Remove Stop:11:16
# Switch:Hawai:Bulgaria
# Travel
#
# Output
# Hawai::RomeCyprys-Greece
# Hawai::Rome-Greece
# Bulgaria::Rome-Greece
# Ready for world tour! Planned stops: Bulgaria::Rome-Greece

stops_string = input()

while True:
    line = input().split(":")
    if line[0] == "Travel":
        break
    if line[0] == "Add Stop":
        index = int(line[1])
        string = line[2]
        if 0 <= index < len(stops_string):
            stops_string = stops_string[:index] + string + stops_string[index:]
    if line[0] == "Remove Stop":
        start_index = int(line[1])
        end_index = int(line[2])
        if 0 <= start_index <= end_index < len(stops_string):
            stops_string = stops_string[:start_index] + stops_string[end_index+1:]
    if line[0] == "Switch":
        old_string = line[1]
        new_string = line[2]
        stops_string = stops_string.replace(old_string, new_string)

    print(stops_string)

print(f"Ready for world tour! Planned stops: {stops_string}")
