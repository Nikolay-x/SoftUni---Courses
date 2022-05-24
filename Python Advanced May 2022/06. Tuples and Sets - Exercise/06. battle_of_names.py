# 6.Battle of Names
# You will receive a number N. On the following N lines, you will be receiving names. You should sum the ASCII values of each letter in the name and integer divide it to the number of the current row (starting from 1). Save the result to a set of either odd or even numbers, depending on if the resulting number is odd or even. After that, sum the values of each set.
# If the sums of the two sets are equal, print the union of the values, separated by ", ".
# If the sum of the odd numbers is bigger than the sum of the even numbers, print the different values, separated by ", ".
# If the sum of the even numbers is bigger than the sum of the odd numbers, print the symmetric-different values, separated by ", ".
# NOTE: On every operation, the starting set should be the odd set
#
# Input
# 4
# Pesho
# Stefan
# Stamat
# Gosho
#
# Output
# 304, 128, 206, 511

n = int(input())
odd_sums = set()
even_sums = set()

for i in range(1, n+1):
    name = input()

    name_sum = 0
    for ch in name:
        name_sum += ord(ch)
    name_sum = int(name_sum / i)

    # name_sum = sum([ord(x) for x in name]) // i

    if name_sum % 2 != 0:
        odd_sums.add(name_sum)
    else:
        even_sums.add(name_sum)

odd_sums_sum = sum(odd_sums)
even_sums_sum = sum(even_sums)

if odd_sums_sum == even_sums_sum:
    result = odd_sums.union(even_sums)
elif odd_sums_sum > even_sums_sum:
    result = odd_sums.difference(even_sums)
elif odd_sums_sum < even_sums_sum:
    result = odd_sums.symmetric_difference(even_sums)

# print(*result, sep=", ")
print(", ".join(str(x) for x in result))
