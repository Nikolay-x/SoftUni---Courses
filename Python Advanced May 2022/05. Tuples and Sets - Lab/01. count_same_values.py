# 1.Count Same Values
# You will be given numbers separated by a space. Write a program that prints the number of occurrences of each number in the format "{number} - {count} times". The number must be formatted to the first decimal point.
#
# Input
# -2.5 4 3 -2.5 -5.5 4 3 3 -2.5 3
#
# Output
# -2.5 - 3 times
# 4.0 - 2 times
# 3.0 - 4 times
# -5.5 - 1 times

numbers = [float(x) for x in input().split(" ")]

occurrences = dict()

for num in numbers:
    if num not in occurrences:
        occurrences[num] = 0
    occurrences[num] += 1

for number, count in occurrences.items():
    print(f"{number:.1f} - {count} times")
