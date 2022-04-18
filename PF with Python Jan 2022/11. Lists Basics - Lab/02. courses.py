# 2.Courses
# On the first line, you will receive a single number n. On the following n lines, you will receive names of courses. You should create a list of courses and print it.
#
# Input
# 2
# PB Python
# PF Python
#
# Output
# ['PB Python', 'PF Python']

n = int(input())

list = []
# list = list()

for i in range(n):
    course = input()
    list.append(course)

print(list)
