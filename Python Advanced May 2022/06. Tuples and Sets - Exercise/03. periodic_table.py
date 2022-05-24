# 3.Periodic Table
# Write a program that keeps all the unique chemical elements. On the first line, you will be given a number n - the count of input lines that you will receive. On the following n lines, you will be receiving chemical compounds separated by a single space. Your task is to print all the unique ones on separate lines (the order does not matter):
#
# Input
# 4
# Ce O
# Mo O Ce
# Ee
# Mo
#
# Output
# Ce
# Ee
# Mo
# O

n = int(input())
result = set()

for _ in range(n):

    # el_list = input().split()
    # for el in el_list:
    #     result.add(el)

    el_set = set(input().split())
    result = result.union(el_set)

# for elem in result:
#     print(elem)

print(*result, sep="\n")
