# 5.Can't Sleep? Count Sheep
# If you can't fall asleep, try counting sheep! You will be given a positive integer, 3, for example. You should return a string with a murmur: "1 sheep...2 sheep...3 sheep...". Input will always be valid, i.e., integers greater than 0.
#
# Input
# 5
#
# Output
# 1 sheep...2 sheep...3 sheep...4 sheep...5 sheep...

number = int(input())

for i in range(number):
    print(f"{i + 1} sheep...", end = "")
