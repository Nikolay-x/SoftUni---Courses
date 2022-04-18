# 6.List Manipulator
# Trifon has finally become a junior developer and has received his first task. It is about manipulating a list of integers. He is not quite happy about it since he hates manipulating lists. They will pay him a lot of money, though, and he is willing to give somebody half of it if to help him do his job. On the other hand, you love lists (and money), so you decide to try your luck.
# The list may be manipulated by one of the following commands:
# "exchange {index}" – splits the list after the given index and exchanges the places of the two resulting sub-lists. E.g., [1, 2, 3, 4, 5] -> "exchange 2" -> result: [4, 5, 1, 2, 3]
# oIf the index is outside the boundaries of the list, print "Invalid index"
# oA negative index is considered invalid
# "max even/odd"– returns the INDEX of the max even/odd element. E.g., [1, 4, 8, 2, 3] -> "max odd" -> print: 4
# "min even/odd" – returns the INDEX of the min even/odd element. E.g. [1, 4, 8, 2, 3] -> "min even" -> print: 3
# oIf there are two or more equal min/max elements, return the index of the rightmost one
# oIf a min/max even/odd element cannot be found, print "No matches"
# "first {count} even/odd" – returns the first count even/odd elements. E.g. [1, 8, 2, 3] -> "first 2 even" -> print [8, 2]
# "last {count} even/odd" – returns the last count even/odd elements. E.g. [1, 8, 2, 3] -> "last 2 odd" -> print [1, 3]
# oIf the count is greater than the list length, print "Invalid count"
# oIf there are not enough elements to satisfy the count, print as many as you can. If there are zero even/odd elements, print an empty list "[]"
# "end" - stop taking input and print the final state of the list
# Input
# The input data should be read from the console.
# On the first line, the initial list is received as a line of integers, separated by a single space.
# On the following lines, until the command "end" is received, you will receive the list manipulation commands.
# The input data will always be valid and in the format described. There is no need to check it explicitly.
# Output
# The output should be printed on the console.
# On a separate line, print the output of the corresponding command.
# On the last line, print the final list in square brackets with its elements separated by a comma and a space.
# See the examples below to get a better understanding of your task.
# Constraints
# The number of input lines will be in the range [2 … 50].
# The list elements will be integers in the range [0 … 1000].
# The number of elements will be in the range [1 .. 50].
# The split index will be an integer in the range [-231 … 231 – 1].
# The first/last count will be an integer in the range [1 … 231 – 1].
# There will not be redundant whitespace anywhere in the input.
# Allowed working time for your program: 0.1 seconds. Allowed memory: 16 MB.
#
# Input
# 1 3 5 7 9
# exchange 1
# max odd
# min even
# first 2 odd
# last 2 even
# exchange 3
# end
#
# Output
# 2
# No matches
# [5, 7]
# []
# [3, 5, 7, 9, 1]

from sys import maxsize

str_numbers = input().split(" ")

numbers = list(map(int, str_numbers))

command = input().split(" ")

max_num = -maxsize
min_num = maxsize

max_even_index = None
max_odd_index = None
min_even_index = None
min_odd_index = None

max_even_count = 0
max_odd_count = 0
min_even_count = 0
min_odd_count = 0

first_even = []
first_odd = []
last_even = []
last_odd = []

first_even_count = 0
first_odd_count = 0
last_even_count = 0
last_odd_count = 0

while command[0] != "end":

    if "exchange" in command:
        if 0 <= int(command[1]) <= len(numbers)-1:
            numbers = numbers[int(command[1]) + 1:] + numbers[:int(command[1]) + 1]
        else:
            print("Invalid index")

    elif "max" in command:

        if command[1] == "even":
            for i in range(len(numbers)):
                if numbers[i] % 2 == 0:
                    max_even_count += 1
                    if numbers[i] >= max_num:
                        max_num = numbers[i]
                        max_even_index = i
            if max_even_count >= 1:
                print(max_even_index)
            else:
                print("No matches")
            max_num = -maxsize
            max_even_count = 0

        elif command[1] == "odd":
            for j in range(len(numbers)):
                if numbers[j] % 2 != 0:
                    max_odd_count += 1
                    if numbers[j] >= max_num:
                        max_num = numbers[j]
                        max_odd_index = j
            if max_odd_count >= 1:
                print(max_odd_index)
            else:
                print("No matches")
            max_num = -maxsize
            max_odd_count = 0

    elif "min" in command:

        if command[1] == "even":
            for p in range(len(numbers)):
                if numbers[p] % 2 == 0:
                    min_even_count += 1
                    if numbers[p] <= min_num:
                        min_num = numbers[p]
                        min_even_index = p
            if min_even_count >= 1:
                print(min_even_index)
            else:
                print("No matches")
            min_num = maxsize
            min_even_count = 0

        elif command[1] == "odd":
            for q in range(len(numbers)):
                if numbers[q] % 2 != 0:
                    min_odd_count += 1
                    if numbers[q] <= min_num:
                        min_num = numbers[q]
                        min_odd_index = q
            if min_odd_count >= 1:
                print(min_odd_index)
            else:
                print("No matches")
            min_num = maxsize
            min_odd_count = 0

    elif "first" in command:

        if command[2] == "even":
            if int(command[1]) > len(numbers):
                print("Invalid count")
            else:
                for u in range(len(numbers)):
                    if numbers[u] % 2 == 0:
                        first_even_count += 1
                        if first_even_count <= int(command[1]):
                            first_even.append(numbers[u])
                print(first_even)
                first_even_count = 0
                first_even = []

        elif command[2] == "odd":
            if int(command[1]) > len(numbers):
                print("Invalid count")
            else:
                for m in range(len(numbers)):
                    if numbers[m] % 2 != 0:
                        first_odd_count += 1
                        if first_odd_count <= int(command[1]):
                            first_odd.append(numbers[m])
                print(first_odd)
                first_odd_count = 0
                first_odd = []

    elif "last" in command:

        if command[2] == "even":
            if int(command[1]) > len(numbers):
                print("Invalid count")
            else:
                for r in range(len(numbers)-1, -1, -1):
                    if numbers[r] % 2 == 0:
                        last_even_count += 1
                        if last_even_count <= int(command[1]):
                            last_even.append(numbers[r])
                last_even.reverse()
                print(last_even)
                last_even_count = 0
                last_even = []

        elif command[2] == "odd":
            if int(command[1]) > len(numbers):
                print("Invalid count")
            else:
                for t in range(len(numbers)-1, -1, -1):
                    if numbers[t] % 2 != 0:
                        last_odd_count += 1
                        if last_odd_count <= int(command[1]):
                            last_odd.append(numbers[t])
                last_odd.reverse()
                print(last_odd)
                last_odd_count = 0
                last_odd = []

    command = input().split(" ")

print(numbers)
