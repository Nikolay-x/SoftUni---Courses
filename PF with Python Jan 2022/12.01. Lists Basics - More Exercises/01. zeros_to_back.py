# 1.Zeros to Back
# Write a program that receives a single string (integers separated by a comma and space ", "), finds all the zeros, and moves them to the back without messing up the other elements. Print the resulting integer list.
#
# Input
# 1, 0, 1, 2, 0, 1, 3
#
# Output
# [1, 1, 2, 1, 3, 0, 0]

numbers_list = input().split(", ")

int_numbers = []

for num in numbers_list:
    int_numbers.append(int(num))

# int_numbers = list(map(int, numbers_list))

for i in range(len(int_numbers) -1, -1, -1):
    if int_numbers[i] == 0:
        int_numbers.remove(int_numbers[i])
        int_numbers.append(0)

print(int_numbers)
