# 3.Treasure Finder
# Write a program that decrypts a message by a given key and gathers information about hidden treasure type and its coordinates. On the first line, you will receive a key (sequence of numbers separated by a space). On the next few lines, you will receive lines with strings until you get the command "find".
# You should loop through every string and decrease the ASCII code of each character with a corresponding number of the key sequence. You choose a key number from the sequence by just looping through it. If the length of the key sequence is less than the string sequence, you should continue looping from the beginning.
# For more clarification, see the example below.
# After decrypting the message, you will get a type of treasure and its coordinates. The type will be between the symbol "&", and the coordinates - between the symbols "<' and '>'.
# For each line print the type and the coordinates in the format "Found {type} at {coordinates}".
#
# Input
# 1 2 1 3
# ikegfp'jpne)bv=41P83X@
# ujfufKt)Tkmyft'duEprsfjqbvfv=53V55XA
# find
#
# Output
# Found gold at 10N70W
# Found Silver at 32S43W

key_sequence = [int(x) for x in input().split(" ")]

while True:
    line = input()
    decrypted_message = ""
    resource = ""
    coordinates = ""
    count = 0

    if line == "find":
        break
    for i in range(len(line)):
        if i < len(key_sequence):
            q = i
        else:
            q = i % len(key_sequence)
        decrypted_message += chr(ord(line[i]) - key_sequence[q])
    for i, ch in enumerate(decrypted_message):
        if ch == "&" and count == 0:
            start_resource = i + 1
            count += 1
        if ch == "<":
            start_coordinates = i + 1

    while decrypted_message[start_resource] != "&":
        resource += decrypted_message[start_resource]
        start_resource += 1
    while decrypted_message[start_coordinates] != ">":
        coordinates += decrypted_message[start_coordinates]
        start_coordinates += 1

    print(f'Found {resource} at {coordinates}')
