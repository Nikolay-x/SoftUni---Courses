# 6.Triples of Latin Letters
# Write a program to read an integer N and print all triples of the first N small Latin letters, ordered alphabetically:
#
# Input
# 2
#
# Output
# aaa
# aab
# aba
# abb
# baa
# bab
# bba
# bbb

n = int(input())

for i in range(n):
    for q in range(n):
        for p in range(n):
            print(f"{chr(97+i)}{chr(97+q)}{chr(97+p)}")
