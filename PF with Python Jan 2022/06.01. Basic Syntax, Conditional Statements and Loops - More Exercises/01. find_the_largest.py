# 1.Find the Largest
# You will be given a number. Print the largest number that can be formed from the digits of the given number.
#
# Input
# 213
#
# Output
# 321

num = input()

count = [0 for x in range(10)]

string = str(num)

for i in range(len(string)):
    count[int(string[i])] = count[int(string[i])] + 1

result = 0
multiplier = 1

for i in range(10):
    while count[i] > 0:
        result = result + (i * multiplier)
        count[i] = count[i] - 1
        multiplier = multiplier * 10

print(result)
