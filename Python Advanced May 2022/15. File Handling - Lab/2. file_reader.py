# 2.File Reader
# You are given a file called numbers.txt with the following content:
#
#     1
#     2
#     3
#     4
#     5
#
# Create a program that reads the numbers from the file. Print on the console the sum of those numbers.

# file = open('numbers.txt', 'r')
# the_sum = 0
#
# for line in file:
#     the_sum += int(line)
#
# print(the_sum)

file_path = './numbers.txt'

file = open(file_path, "r")
numbers_sum = 0

while True:
    line = file.readline()
    if not line:
        break
    numbers_sum += int(line)

print(numbers_sum)
