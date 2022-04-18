# 9.* Moving Target
# You are at the shooting gallery again, and you need a program that helps you keep track of moving targets. On the first line, you will receive a sequence of targets with their integer values, split by a single space. Then, you will start receiving commands for manipulating the targets until the "End" command. The commands are the following:
# "Shoot {index} {power}"
# oShoot the target at the index if it exists by reducing its value by the given power (integer value). A target is considered shot when its value reaches 0.
# oRemove the target if it is shot.
# "Add {index} {value}"
# oInsert a target with the received value at the received index if it exists. If not, print: "Invalid placement!"
# "Strike {index} {radius}"
# oRemove the target at the given index (if such exist) and the ones before and after it depending on the radius.
# oIf any of the indices in the range is invalid, print: "Strike missed!" and skip this command.
#  Example:  "Strike 2 2"
# 	{radius}	{radius}	{strikeIndex}	{radius}	{radius}
#
# "End"
# oPrint the sequence with targets in the following format:
# "{target1}|{target2} … |{targetn}"
# Input / Constraints
# On the first line, you will receive the sequence of targets – integer values [1-10000].
# On the following lines, until the "End", you will be receiving the command described above – strings.
# There will never be a case when the "Strike" command would empty the whole sequence.
# Output
# Print the appropriate message in case of the "Strike" command if necessary.
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

command = input()

while command != "End":
    current_command = command.split(" ")

    if current_command[0] == "Shoot":
        if 0 <= int(current_command[1]) < len(targets):
            targets[int(current_command[1])] -= int(current_command[2])
            if targets[int(current_command[1])] <= 0:
                targets.pop(int(current_command[1]))
    elif current_command[0] == "Add":
        if 0 <= int(current_command[1]) < len(targets):
            targets.insert(int(current_command[1]), int(current_command[2]))
        else:
            print("Invalid placement!")
    elif current_command[0] == "Strike":
        count = 0
        for i in range(int(current_command[1]) - int(current_command[2]),
                       int(current_command[1]) + int(current_command[2]) + 1):
            if 0 <= i < len(targets):
                count += 1
        if count == int(current_command[2]) * 2 + 1:
            for i in range(int(current_command[1]) - int(current_command[2]),
                       int(current_command[1]) + int(current_command[2]) + 1):
                targets.pop(int(current_command[1]) - int(current_command[2]))
        else:
            print("Strike missed!")

    command = input()

print("|".join(map(str, targets)))
