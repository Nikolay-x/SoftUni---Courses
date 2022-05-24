# 2.Matching Parentheses
# You are given an algebraic expression with parentheses. Scan through the string and extract each set of parentheses.
# Print the result back on the console.
#
# Input
# 1 + (2 - (2 + 3) * 4 / (3 + 1)) * 5
#
# Output
# (2 + 3)
# (3 + 1)
# (2 - (2 + 3) * 4 / (3 + 1))

expression = input()
parentheses_stack = []

for i in range(len(expression)):
    if expression[i] == "(":
        parentheses_stack.append(i)
    elif expression[i] == ")":
        start_index = parentheses_stack.pop()
        end_index = i+1
        print(expression[start_index:end_index])
