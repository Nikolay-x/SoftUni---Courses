# 6.Even Numbers
# Write a program that reads a single string with numbers separated by comma and space ", ". Print the indices of all even numbers.
#
# Input
# 3, 2, 1, 5, 8
#
# Output
# [1, 4]

str_numbers = input().split(", ")

numbers = list(map(int, str_numbers))

# numbers = list(map(int, input().split(", ")))


even_numbers_indices = []

for i in range(len(numbers)):
    if numbers[i] % 2 == 0:
        even_numbers_indices.append(i)

print(even_numbers_indices)
