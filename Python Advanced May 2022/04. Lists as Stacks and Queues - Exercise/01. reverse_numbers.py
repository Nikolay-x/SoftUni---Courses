# 1.Reverse Numbers
# Write a program that reads a string with N integers from the console, separated by a single space, and reverses them using a stack. Print the reversed integers on one line, separated by a single space.
#
# Input
# 1 2 3 4 5
#
# Output
# 5 4 3 2 1

integers_line = input().split(" ")
stack = []

# while integers_line:
#     last_number = integers_line.pop()
#     print(last_number, end=" ")

while integers_line:
    stack.append(integers_line.pop())
print(" ".join(stack))
