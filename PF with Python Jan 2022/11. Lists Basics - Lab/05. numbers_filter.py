# 5.Numbers Filter
# On the first line, you will receive a single number n. On the following n lines, you will receive integers. After that, you will be given one of the following commands:
# even
# odd
# negative
# positive
# Filter all the numbers that fit in the category (0 counts as a positive and even). Finally, print the result.
#
# Input
# 5
# 33
# 19
# -2
# 18
# 998
# even
#
# Output
# [-2, 18, 998]

n = int(input())

even = []
odd = []
positive = []
negative = []

for i in range(n):
    num = int(input())
    if num % 2 == 0:
        even.append(num)
    else:
        odd.append(num)
    if num >= 0:
        positive.append(num)
    else:
        negative.append(num)

filter = input()

# if filter == "even":
#     print(even)
# if filter == "odd":
#     print(odd)
# if filter == "positive":
#     print(positive)
# if filter == "negative":
#     print(negative)

print(eval(filter))
