# 1.Rhombus of Stars
# Create a program that reads a positive integer N as input and prints on the console a rhombus with size n:
#
# Input
# 4
#
# Output
#    *
#   * *
#  * * *
# * * * *
#  * * *
#   * *
#    *

def print_row(size, stars_count):
    result = ((size - stars_count) * ' ' + stars_count * '* ').rstrip()
    print(result)


n = int(input())
for i in range(1, n+1):
    print_row(n, i)
for i in range(n-1, 0, -1):
    print_row(n, i)
