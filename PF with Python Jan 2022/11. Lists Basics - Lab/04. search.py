# 4.Search
# On the first line, you will receive a number n. On the second line, you will receive a word. On the following n lines, you will be given some strings. You should add them to a list and print them. After that, you should filter out only the strings that include the given word and print that list too.
#
# Input
# 3
# SoftUni
# I study at SoftUni
# I walk to work
# I learn Python at SoftUni
#
# Output
# ["I study at SoftUni", "I walk to work", "I learn Python at SoftUni"]
# ["I study at SoftUni", "I learn Python at SoftUni"]

n = int(input())
filter_word = input()

list = []
filter_list = []

for i in range(n):
    string = input()
    list.append(string)

# print(list)
#
# for i in range(len(list) - 1, -1, -1):
#     if filter_word not in list[i]:
#         list.remove(list[i])
#
# print(list)

for i in range(len(list)):
    if filter_word in list[i]:
        filter_list.append(list[i])

print(list)
print(filter_list)
