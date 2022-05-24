# 2. Stacked Queries
# You have an empty stack. You will receive an integer – N. On the next N lines, you will receive queries. Each query is one of these four types:
# '1 {number}' – push the number (integer) into the stack
# '2' – delete the number at the top of the stack
# '3' – print the maximum number in the stack
# '4' – print the minimum number in the stack
# It is guaranteed that each query is valid.
# After you go through all the queries, print the stack from top to bottom in the following format:
# "{n}, {n1}, {n2}, ... {nn}"
#
# Input
# 9
# 1 97
# 2
# 1 20
# 2
# 1 26
# 1 20
# 3
# 1 91
# 4
#
# Output
# 26
# 20
# 91, 20, 26

stack = []
n = int(input())

for _ in range(n):
    query = input()
    if "1" in query:
        query = query.split(" ")
        number = int(query[1])
        stack.append(number)
    elif "2" in query and stack:
        stack.pop()
    elif "3" in query and stack:
        print(max(stack))
    elif "4" in query and stack:
        print(min(stack))

stack = [str(k) for k in stack]

# reversed_stack = []
# while stack:
#     reversed_stack.append(stack.pop())
# print(", ".join(reversed_stack))

stack = stack[::-1]
print(", ".join(stack))
