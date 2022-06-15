# 5.Fibonacci Sequence
# Create a module that can create a Fibonacci sequence up to a number (count of numbers in the sequence) and print them, separating them with a single space. The module should also be able to locate a specific number in the sequence. You can read more about the Fibonacci sequence here: https://en.wikipedia.org/wiki/Fibonacci_number
# You will be receiving commands until the "Stop" command. The commands are:
# "Create Sequence {count}". Create a series of numbers up to a specific count and print them in the following format:
#            "{n1} {n2} … {n}"
#
# "Locate {number}"
# Check if the sequence contains the number. If it finds the number, it should print:
# "The number - {number} is at index {index}"
# And if it doesn't find it:
# "The number {number} is not in the sequence"
# Input
# You will be receiving commands until the "Stop" command. All inputs will be valid.
# Output
# Print the output of every command in the format described above.
#
# Input
# Create Sequence 10
# Locate 13
# Create Sequence 3
# Locate 10
# Stop
#
# Output
# 0 1 1 2 3 5 8 13 21 34
# The number - 13 is at index 7
# 0 1 1
# The number 10 is not in the sequence

from fibonacci_sequence.get_sequence_location import create_sequence, locate

a = []

while True:
    line = input().split(" ")
    command = line[0]
    if command == "Stop":
        break
    if command == "Create":
        number = int(line[2])
        a = create_sequence(number)
        print(" ".join([str(x) for x in a]))
    if command == "Locate":
        number = int(line[1])
        locate(number, a)
