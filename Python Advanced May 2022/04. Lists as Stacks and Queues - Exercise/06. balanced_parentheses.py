# 6. Balanced Parentheses
# You will be given a sequence consisting of parentheses. Your job is to determine whether the expression is balanced. A sequence of parentheses is balanced if every opening parenthesis has a corresponding closing parenthesis that occurs after the former. There will be no interval symbols between the parentheses. You will be given three types of parentheses: (), {}, and [].
# {[()]} - Parentheses are balanced.
# (){}[] - Parentheses are balanced.
# {[(])} - Parentheses are NOT balanced.
# Input
# On a single line, you will receive a sequence of parentheses.
# Output
# For each test case, print on a new line "YES" if the parentheses are balanced.
# Otherwise, print "NO"
# Constraints
# 1 ≤ lens ≤ 1000, where the lens is the length of the sequence
# Each character of the sequence will be one of {, }, (, ), [, ]
#
# Input
# {[()]}
#
# Output
# YES

parentheses = input()
parentheses_pairs = {
    "(": ")",
    "{": "}",
    "[": "]"
}
stack = []
is_balanced = True
closing_brackets_counter = 0

for ch in parentheses:
    if ch in "({[":
        stack.append(ch)
    else:
        if not stack:
            is_balanced = False
        closing_brackets_counter += 1
        if stack and parentheses_pairs[stack.pop()] != ch:
            is_balanced = False

if closing_brackets_counter == 0:
    is_balanced = False

if is_balanced:
    print("YES")
else:
    print("NO")
