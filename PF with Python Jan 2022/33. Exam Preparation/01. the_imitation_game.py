# 01. The Imitation Game
# Submit your solutions in the SoftUni judge system at https://judge.softuni.org/Contests/Practice/Index/2525#0.
#
# During World War 2, you are a mathematician who has joined the cryptography team to decipher the enemy's enigma code. Your job is to create a program to crack the codes.
# On the first line of the input, you will receive the encrypted message. After that, until the "Decode" command is given, you will be receiving strings with instructions for different operations that need to be performed upon the concealed message to interpret it and reveal its true content. There are several types of instructions, split by '|'
# "Move {number of letters}":
# oMoves the first n letters to the back of the string
# "Insert {index} {value}":
# oInserts the given value before the given index in the string
# "ChangeAll {substring} {replacement}":
# oChanges all occurrences of the given substring with the replacement text
# Input / Constraints
# On the first line, you will receive a string with a message.
# On the following lines, you will be receiving commands, split by '|' .
# Output
# After the "Decode" command is received, print this message:
# "The decrypted message is: {message}"
#
# Input
# zzHe
# ChangeAll|z|l
# Insert|2|o
# Move|3
# Decode
#
# Output
# The decrypted message is: Hello

encrypted_message = input()

while True:
    instruction = input()
    if instruction == "Decode":
        break
    instruction = instruction.split("|")
    if instruction[0] == "Move":
        number_of_letters = int(instruction[1])
        last_letters = encrypted_message[:number_of_letters]
        encrypted_message = encrypted_message[number_of_letters:] + last_letters
    if instruction[0] == "Insert":
        index = int(instruction[1])
        value = instruction[2]
        encrypted_message = encrypted_message[:index] + value + encrypted_message[index:]
    if instruction[0] == "ChangeAll":
        substring = instruction[1]
        replacement = instruction[2]
        if substring in encrypted_message:
            encrypted_message = encrypted_message.replace(substring, replacement)

print(f"The decrypted message is: {encrypted_message}")
