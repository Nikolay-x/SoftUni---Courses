# 7.Group of 10's
# Write a program that receives a sequence of numbers (a string containing integers separated by ", ") and prints the numbers sorted into lists of 10's in the format "Group of {group}'s: {list_of_numbers}".
# Examples:
# The numbers 2, 8, 4, and 10 fall into the group of 10's.
# The numbers 13, 19, 14, and 15 fall into the group of 20's.
# For more clarification, see the examples below.
#
# Input
# 8, 12, 38, 3, 17, 19, 25, 35, 50
#
# Output
# Group of 10's: [8, 3]
# Group of 20's: [12, 17, 19]
# Group of 30's: [25]
# Group of 40's: [38, 35]
# Group of 50's: [50]

numbers = list(map(int, input().split(", ")))

boundary = 0
group = []

while list(set(numbers)) != [0]:
    boundary += 10

    for number in range(len(numbers)):
        if boundary - 10 < numbers[number] <= boundary:
            group.append(numbers[number])
            numbers[number] = 0
    print(f"Group of {boundary}'s: {group}")
    group = []
