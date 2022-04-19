# Problem 1 - Activation Keys
# Problem for exam preparation for the Programming Fundamentals Course @SoftUni.
# Submit your solutions in the SoftUni judge system at https://judge.softuni.org/Contests/Practice/Index/2302#0.
#
# You are about to make some good money, but first, you need to think of a way to verify who paid for your product and who didn't. You have decided to let people use the software for a free trial period and then require an activation key to continue using the product. Before you can cash out, the last step is to design a program that creates unique activation keys for each user. So, waste no more time and start typing!
# The first line of the input will be your raw activation key. It will consist of letters and numbers only.
# After that, until the "Generate" command is given, you will be receiving strings with instructions for different operations that need to be performed upon the raw activation key.
# There are several types of instructions, split by ">>>":
# "Contains>>>{substring}":
# oIf the raw activation key contains the given substring, prints: "{raw activation key} contains {substring}".
# oOtherwise, prints: "Substring not found!"
# "Flip>>>Upper/Lower>>>{startIndex}>>>{endIndex}":
# oChanges the substring between the given indices (the end index is exclusive) to upper or lower case and then prints the activation key.
# oAll given indexes will be valid.
# "Slice>>>{startIndex}>>>{endIndex}":
# oDeletes the characters between the start and end indices (the end index is exclusive) and prints the activation key.
# oBoth indices will be valid.
# Input
# The first line of the input will be a string consisting of letters and numbers only.
# After the first line, until the "Generate" command is given, you will be receiving strings.
# Output
# After the "Generate" command is received, print:
# o"Your activation key is: {activation key}"
#
# Input
# abcdefghijklmnopqrstuvwxyz
# Slice>>>2>>>6
# Flip>>>Upper>>>3>>>14
# Flip>>>Lower>>>5>>>7
# Contains>>>def
# Contains>>>deF
# Generate
#
# Output
# abghijklmnopqrstuvwxyz
# abgHIJKLMNOPQRstuvwxyz
# abgHIjkLMNOPQRstuvwxyz
# Substring not found!
# Substring not found!
# Your activation key is: abgHIjkLMNOPQRstuvwxyz

raw_key = input()

while True:
    line = input().split(">>>")
    if line[0] == "Generate":
        break
    if line[0] == "Contains":
        substring = line[1]
        if substring in raw_key:
            print(f"{raw_key} contains {substring}")
        else:
            print(f"Substring not found!")
    if line[0] == "Flip":
        instruction = line[1]
        start_index = int(line[2])
        end_index = int(line[3])
        if instruction == "Upper":
            substitution = raw_key[start_index:end_index].upper()
            raw_key = raw_key[:start_index] + substitution + raw_key[end_index:]
            print(raw_key)
        elif instruction == "Lower":
            substitution = raw_key[start_index:end_index].lower()
            raw_key = raw_key[:start_index] + substitution + raw_key[end_index:]
            print(raw_key)
    if line[0] == "Slice":
        start_index = int(line[1])
        end_index = int(line[2])
        raw_key = raw_key[:start_index] + raw_key[end_index:]
        print(raw_key)

print(f"Your activation key is: {raw_key}")
