# List Manipulator
# Write a function called list_manipulator which receives a list of numbers as first parameter and different amount of other parameters. The second parameter might be "add" or "remove". The third parameter might be "beginning" or "end". There might or might not be any other parameters (numbers):
# In case of "add" and "beginning", add the given numbers to the beginning of the given list of numbers and return the new list
# In case of "add" and "end", add the given numbers to the end of the given list of numbers and return the new list
# In case of "remove" and "beginning"
# oIf there is another parameter (number), remove that amount of numbers from the beginning of the list of numbers.
# oIf there are no other parameters, remove only the first element of the list.
# oFinaly, return the new list
# In case of "remove" and "end"
# oIf there is another parameter (number), remove that amount of numbers from the end of the list of numbers.
# oOtherwise if there are no other parameters, remove only the last element of the list.
# oFinaly, return the new list
# For more clarifications, see the examples below.
# Input
# There will be no input
# Parameters will be passed to your function
# Output
# The function should return the new list of numbers
#
# Test Code
# print(list_manipulator([1,2,3], "remove", "end"))
# print(list_manipulator([1,2,3], "remove", "beginning"))
# print(list_manipulator([1,2,3], "add", "beginning", 20))
# print(list_manipulator([1,2,3], "add", "end", 30))
# print(list_manipulator([1,2,3], "remove", "end", 2))
# print(list_manipulator([1,2,3], "remove", "beginning", 2))
# print(list_manipulator([1,2,3], "add", "beginning", 20, 30, 40))
# print(list_manipulator([1,2,3], "add", "end", 30, 40, 50))
#
# Output
# [1, 2]
# [2, 3]
# [20, 1, 2, 3]
# [1, 2, 3, 30]
# [1]
# [3]
# [20, 30, 40, 1, 2, 3]
# [1, 2, 3, 30, 40, 50]

def list_manipulator(numbers_list, *args):
    if args[0] == "add" and args[1] == "beginning":
        for i in range(len(args)-1, 1, -1):
            numbers_list.insert(0, args[i])
        return numbers_list
    elif args[0] == "add" and args[1] == "end":
        for i in range(2, len(args)):
            numbers_list.append(args[i])
        return numbers_list
    elif args[0] == "remove" and args[1] == "beginning":
        if len(args) > 2:
            removed_numbers = args[2]
            for i in range(removed_numbers):
                numbers_list.pop(0)
        else:
            numbers_list.pop(0)
        return numbers_list
    elif args[0] == "remove" and args[1] == "end":
        if len(args) > 2:
            removed_numbers = args[2]
            for i in range(removed_numbers):
                numbers_list.pop()
        else:
            numbers_list.pop()
        return numbers_list


print(list_manipulator([1,2,3], "remove", "end"))
print(list_manipulator([1,2,3], "remove", "beginning"))
print(list_manipulator([1,2,3], "add", "beginning", 20))
print(list_manipulator([1,2,3], "add", "end", 30))
print(list_manipulator([1,2,3], "remove", "end", 2))
print(list_manipulator([1,2,3], "remove", "beginning", 2))
print(list_manipulator([1,2,3], "add", "beginning", 20, 30, 40))
print(list_manipulator([1,2,3], "add", "end", 30, 40, 50))
