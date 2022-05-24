# 1.Numbers
# First, you will be given two sequences of integers values on different lines. The values of the sequences are separated by a single space between them.
# Keep in mind that each sequence should contain only unique values.
# Next, you will receive a number - N. On the next N lines, you will receive one of the following commands:
# "Add First {numbers, separated by a space}" - add the given numbers at the end of the first sequence of numbers.
# "Add Second {numbers, separated by a space}" - add the given numbers at the end of the second sequence of numbers.
# "Remove First {numbers, separated by a space}" - remove only the numbers contained in the first sequence.
# "Remove Second {numbers, separated by a space}" - remove only the numbers contained in the second sequence.
# "Check Subset" - check if any of the given sequences are a subset of the other. If it is, print "True". Otherwise, print "False".
# In the end, print the final sequences, separated by a comma and a space ", ". The values in each sequence should be sorted in ascending order.
#
# Input
#
# 5 4 2 9 9 5 4
# 1 1 1 5 6 5
# 4
# Add First 5 6 9 3
# Add Second 1 2 3 3 3
# Check Subset
# Remove Second 1 2 3 4 5
#
# Output
#
# False
# 2, 3, 4, 5, 6, 9
# 6

first = set([int(x) for x in input().split()])
second = set([int(x) for x in input().split()])
n = int(input())

for i in range(n):
    command = input().split()
    instruction = command[0]
    seq_set = command[1]
    numbers = set(int(x) for x in command[2:])

    if instruction == "Add":
        if seq_set == "First":
            first = first.union(numbers)
        elif seq_set == "Second":
            second = second.union(numbers)
    if instruction == "Remove":
        if seq_set == "First":
            first = first.difference(numbers)
        elif seq_set == "Second":
            second = second.difference(numbers)
    if instruction == "Check":
        print(first.issubset(second) or second.issubset(first))

# print(*sorted(first), sep=', ')
# print(*sorted(second), sep=', ')

print(", ".join(str(x) for x in sorted(first)))
print(", ".join(str(x) for x in sorted(second)))
