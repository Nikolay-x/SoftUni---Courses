# 2.Sets of Elements
# Write a program that prints a set of elements. On the first line, you will receive two numbers - n and m, separated by a single space - representing the lengths of two separate sets. On the next n + m lines, you will receive n numbers, which are the numbers in the first set, and m numbers, which are in the second set. Find all the unique elements that appear in both and print them on separate lines (the order does not matter).
# For example:
# Set with length n = 4: {1, 3, 5, 7}
# Set with length m = 3: {3, 4, 5}
# Set that contains all the elements that repeat in both sets -> {3, 5}
#
# Input
# 4 3
# 1
# 3
# 5
# 7
# 3
# 4
# 5
#
# Output
# 3
# 5

n, m = [int(x) for x in input().split()]
n_set = set()
m_set = set()

for _ in range(n):
    num = input()
    n_set.add(num)

for _ in range(m):
    num = input()
    m_set.add(num)

c = n_set.intersection(m_set)

# print(*c, sep="\n")

for num in c:
    print(num)
