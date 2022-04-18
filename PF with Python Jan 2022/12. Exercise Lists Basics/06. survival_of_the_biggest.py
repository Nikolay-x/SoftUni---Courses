# 6.Survival of the Biggest
# Write a program that receives a list of integer numbers (separated by a single space) and a number n. The number n represents the count of numbers to remove from the list. You should remove the smallest ones, and then, you should print all the numbers that are left in the list, separated by a comma and a space ", ".
#
# Input
# 10 9 8 7 6 5
# 3
#
# Output
# 10, 9, 8

numbers_string = input().split(" ")
count = int(input())

# numbers = list(map(int, numbers_string))

numbers = []

for str_num in numbers_string:
    numbers.append(int(str_num))

for i in range(count):
    min_num = min(numbers)
    numbers.remove(min_num)
    numbers_string.remove(str(min_num))

print(", ".join(numbers_string))
