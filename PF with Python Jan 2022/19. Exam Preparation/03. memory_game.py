# Problem 3 - Memory game
# Problem for exam preparation for the Programming Fundamentals Course @SoftUni.
# Submit your solutions in the SoftUni judge system at https://judge.softuni.org/Contests/Practice/Index/2517#1.
#
# Write a program that recreates the Memory game.
# On the first line, you will receive a sequence of elements. Each element in the sequence will have a twin. Until the player receives "end" from the console, you will receive strings with two integers separated by a space, representing the indexes of elements in the sequence.
# If the player tries to cheat and enters two equal indexes or indexes which are out of bounds of the sequence, you should add two matching elements at the middle of the sequence in the following format:
# "-{number of moves until now}a"
# Then print this message on the console:
# "Invalid input! Adding additional elements to the board"
# Input
# On the first line, you will receive a sequence of elements
# On the following lines, you will receive integers until the command "end"
# Output
# Every time the player hit two matching elements, you should remove them from the sequence and print on the console the following message:
# "Congrats! You have found matching elements - ${element}!"
# If the player hit two different elements, you should print on the console the following message:
# "Try again!"
# If the player hit all matching elements before he receives "end" from the console, you should print on the console the following message:
# "You have won in {number of moves until now} turns!"
# If the player receives "end" before he hits all matching elements, you should print on the console the following message:
# "Sorry you lose :(
# {the current sequence's state}"
# Constraints
# All elements in the sequence will always have a matching element.
#
# Input
# 1 1 2 2 3 3 4 4 5 5
# 1 0
# -1 0
# 1 0
# 1 0
# 1 0
# end
#
# Output
# Congrats! You have found matching elements - 1!
# Invalid input! Adding additional elements to the board
# Congrats! You have found matching elements - 2!
# Congrats! You have found matching elements - 3!
# Congrats! You have found matching elements - -2a!
# Sorry you lose :(
# 4 4 5 5

elements = input().split(" ")

move_count = 0
is_win = False

while True:
    str_command = input()
    move_count += 1
    if str_command == "end":
        break
    else:
        command = list(map(int, str_command.split(" ")))
        if 0 <= command[0] < len(elements) and 0 <= command[1] < len(elements) and command[0] != command[1]:
            if elements[command[0]] == elements[command[1]]:
                print(f"Congrats! You have found matching elements - {elements[command[0]]}!")
                elements[command[0]] = "none"
                elements[command[1]] = "none"
                elements.remove("none")
                elements.remove("none")
            elif elements[command[0]] != elements[command[1]]:
                print("Try again!")
        else:
            elements.insert(len(elements)//2, f"-{move_count}a")
            elements.insert(len(elements)//2, f"-{move_count}a")
            print("Invalid input! Adding additional elements to the board")
    if len(elements) == 0:
        print(f"You have won in {move_count} turns!")
        is_win = True
        break
    command = []

if not is_win:
    print("Sorry you lose :(")
    print(" ".join(elements))
