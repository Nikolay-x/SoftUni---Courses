# 2.Array Modifier
# Submit your solutions in the SoftUni judge system at https://judge.softuni.org/Contests/Practice/Index/2474#1.
#
# You are given an array with integers. Write a program to modify the elements after receiving the following commands:
# "swap {index1} {index2}" takes two elements and swap their places.
# "multiply {index1} {index2}" takes element at the 1st index and multiply it with the element at 2nd index. Save the product at the 1st index.
# "decrease" decreases all elements in the array with 1.
# Input
# On the first input line, you will be given the initial array values separated by a single space.
# On the next lines you will receive commands until you receive the command "end". The commands are as follow:
# "swap {index1} {index2}"
# "multiply {index1} {index2}"
# "decrease"
# Output
# The output should be printed on the console and consist of elements of the modified array – separated by a comma and a single space ", ".
# Constraints
# Elements of the array will be integer numbers in the range [-231...231]
# Count of the array elements will be in the range [2...100]
# Indexes will be always in the range of the array
#
# Input
# 23 -2 321 87 42 90 -123
# swap 1 3
# swap 3 6
# swap 1 0
# multiply 1 2
# multiply 2 1
# decrease
# end
#
# Output
# 86, 7382, 2369942, -124, 41, 89, -3

numbers = list(map(int, input().split(" ")))

line = input()

while line != "end":

    line = line.split(" ")
    action = line[0]

    if action == "decrease":
        numbers = [x-1 for x in numbers]
    else:
        index1 = int(line[1])
        index2 = int(line[2])
        if action == "swap":
            numbers[index1], numbers[index2] = numbers[index2], numbers[index1]
        if action == "multiply":
            numbers[index1] = numbers[index1] * numbers[index2]

    line = input()

output = ", ".join(list(map(str, numbers)))
print(output)
