# Problem 3 - The Pianist
# Problem for exam preparation for the Programming Fundamentals Course @SoftUni.
# Submit your solutions in the SoftUni judge system at https://judge.softuni.org/Contests/Practice/Index/2525#2.
#
# You are a pianist, and you like to keep a list of your favorite piano pieces. Create a program to help you organize it and add, change, remove pieces from it!
# On the first line of the standard input, you will receive an integer n – the number of pieces you will initially have. On the next n lines, the pieces themselves will follow with their composer and key, separated by "|" in the following format: "{piece}|{composer}|{key}".
# Then, you will be receiving different commands, each on a new line, separated by "|", until the "Stop" command is given:
# "Add|{piece}|{composer}|{key}":
# oYou need to add the given piece with the information about it to the other pieces and print:
# "{piece} by {composer} in {key} added to the collection!"
# oIf the piece is already in the collection, print:
# "{piece} is already in the collection!"
# "Remove|{piece}":
# oIf the piece is in the collection, remove it and print:
# "Successfully removed {piece}!"
# oOtherwise, print:
# "Invalid operation! {piece} does not exist in the collection."
# "ChangeKey|{piece}|{new key}":
# oIf the piece is in the collection, change its key with the given one and print:
# "Changed the key of {piece} to {new key}!"
# oOtherwise, print:
# "Invalid operation! {piece} does not exist in the collection."
# Upon receiving the "Stop" command, you need to print all pieces in your collection in the following format:
# "{Piece} -> Composer: {composer}, Key: {key}"
# Input/Constraints
# You will receive a single integer at first – the initial number of pieces in the collection
# For each piece, you will receive a single line of text with information about it.
# Then you will receive multiple commands in the way described above until the command "Stop".
# Output
# All the output messages with the appropriate formats are described in the problem description.
#
# Input
# 3
# Fur Elise|Beethoven|A Minor
# Moonlight Sonata|Beethoven|C# Minor
# Clair de Lune|Debussy|C# Minor
# Add|Sonata No.2|Chopin|B Minor
# Add|Hungarian Rhapsody No.2|Liszt|C# Minor
# Add|Fur Elise|Beethoven|C# Minor
# Remove|Clair de Lune
# ChangeKey|Moonlight Sonata|C# Major
# Stop
#
# Output
# Sonata No.2 by Chopin in B Minor added to the collection!
# Hungarian Rhapsody No.2 by Liszt in C# Minor added to the collection!
# Fur Elise is already in the collection!
# Successfully removed Clair de Lune!
# Changed the key of Moonlight Sonata to C# Major!
# Fur Elise -> Composer: Beethoven, Key: A Minor
# Moonlight Sonata -> Composer: Beethoven, Key: C# Major
# Sonata No.2 -> Composer: Chopin, Key: B Minor
# Hungarian Rhapsody No.2 -> Composer: Liszt, Key: C# Minor

pieces_number = int(input())
songs_dict = dict()

for i in range(pieces_number):
    line = input().split("|")
    piece = line[0]
    composer = line[1]
    key = line[2]
    songs_dict[piece] = [composer, key]

while True:
    command = input().split("|")
    if command[0] == "Stop":
        break
    piece = command[1]
    if command[0] == "Add":
        composer = command[2]
        key = command[3]
        if piece not in songs_dict:
            songs_dict[piece] = [composer, key]
            print(f"{piece} by {composer} in {key} added to the collection!")
        else:
            print(f"{piece} is already in the collection!")
    if command[0] == "Remove":
        if piece in songs_dict:
            del songs_dict[piece]
            print(f"Successfully removed {piece}!")
        else:
            print(f"Invalid operation! {piece} does not exist in the collection.")
    if command[0] == "ChangeKey":
        new_key = command[2]
        if piece in songs_dict:
            songs_dict[piece][1] = new_key
            print(f"Changed the key of {piece} to {new_key}!")
        else:
            print(f"Invalid operation! {piece} does not exist in the collection.")

for piece in songs_dict:
    print(f"{piece} -> Composer: {songs_dict[piece][0]}, Key: {songs_dict[piece][1]}")
