# 1.Reverse Strings
# Write program that:
# Reads an input string
# Reverses it using a stack
# Prints the result back on the console
#
# Input
# I Love Python
#
# Output
# nohtyP evoL I

# Better solutions
# original_string[::-1]
# original_string.reverse()

# original_string = input()
# s = []
# for c in original_string:
#     s.append(c)
# reversed_string = ""
# while s:
#     reversed_string += s.pop()
# print(reversed_string)

input_string = list(input())
stack = []
for i in range(len(input_string)):
    stack.append(input_string.pop())
print("".join(stack))
