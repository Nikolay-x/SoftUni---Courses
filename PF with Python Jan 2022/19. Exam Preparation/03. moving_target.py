# 3.Moving Target
# Submit your solutions in the SoftUni judge system at https://judge.softuni.org/Contests/Practice/Index/2305#2.
#
# You are at the shooting gallery again, and you need a program that helps you keep track of moving targets. On the first line, you will receive a sequence of targets with their integer values, split by a single space. Then, you will start receiving commands for manipulating the targets until the "End" command. The commands are the following:
# "Shoot {index} {power}"
# oShoot the target at the index if it exists by reducing its value by the given power (integer value).
# oRemove the target if it is shot. A target is considered shot when its value reaches 0.
# "Add {index} {value}"
# oInsert a target with the received value at the received index if it exists.
# oIf not, print: "Invalid placement!"
# "Strike {index} {radius}"
# oRemove the target at the given index and the ones before and after it depending on the radius.
# oIf any of the indices in the range is invalid, print: "Strike missed!" and skip this command.
#  Example:  "Strike 2 2"
# 	{radius}	{radius}	{strikeIndex}	{radius}	{radius}
#
# "End"
# oPrint the sequence with targets in the following format and end the program:
# "{target1}|{target2}…|{targetn}"
# Input / Constraints
# On the first line, you will receive the sequence of targets – integer values [1-10000].
# On the following lines, until the "End" will be receiving the command described above – strings.
# There will never be a case when the "Strike" command would empty the whole sequence.
# Output
# Print the appropriate message in case of any command if necessary.
# In the end, print the sequence of targets in the format described above.
#
# Input
# 52 74 23 44 96 110
# Shoot 5 10
# Shoot 1 80
# Strike 2 1
# Add 22 3
# End
#
# Output
# Invalid placement!
# 52|100

targets = list(map(int, input().split(" ")))

line = input()

while line != "End":
    line = line.split(" ")
    action = line[0]
    index = int(line[1])
    value = int(line[2])
    if action == "Shoot":
        if 0 <= index < len(targets):
            targets[index] -= value
            if targets[index] <= 0:
                targets.pop(index)
    if action == "Add":
        if 0 <= index < len(targets):
            targets.insert(index, value)
        else:
            print("Invalid placement!")
    if action == "Strike":
        if 0 <= index - value and index + value < len(targets):
            targets = targets[:index - value] + targets[index + value + 1:]
        else:
            print("Strike missed!")
    line = input()

targets = list(map(str, targets))
print("|".join(targets))
