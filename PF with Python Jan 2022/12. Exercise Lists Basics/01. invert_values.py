# 1.Invert Values
# Write a program that receives a single string containing positive and negative numbers separated by a single space. Print a list containing the opposite of each number.
#
# Input
# 1 2 -3 -3 5
#
# Output
# [-1, -2, 3, 3, -5]

string = input()

# nums = [-num if num > 0 else abs(num) for num in list(map(int, input().split(" ")))]
# print(nums)

list = string.split(" ")
inverted_list = []

for i in range(len(list)):
    inverted_list.append(-1 * int(list[i]))

print(inverted_list)
