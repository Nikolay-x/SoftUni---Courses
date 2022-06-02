# 1.Negative vs Positive
# You will receive a sequence of numbers (integers) separated by a single space. Separate the negative numbers from the positive. Find the total sum of the negatives and positives, and print the following:
# On the first line, print the sum of the negatives
# On the second line, print the sum of the positives
# On the third line:
# oIf the absolute negative number is larger than the positive number:
# 	"The negatives are stronger than the positives"
# oIf the positive number is larger than the absolute negative number:
# 	"The positives are stronger than the negatives"
# Note: you will not receive any zeroes in the input.
#
# Input
# 1 2 -3 -4 65 -98 12 57 -84
#
# Output
# -189
# 137
# The negatives are stronger than the positives

def positives_vs_negatives(*args):
    positives = 0
    negatives = 0

    for num in args:
        if num >= 0:
            positives += num
        else:
            negatives += num

    print(negatives)
    print(positives)

    if positives > abs(negatives):
        print("The positives are stronger than the negatives")
    elif positives < abs(negatives):
        print("The negatives are stronger than the positives")


numbers = [int(x) for x in input().split()]
positives_vs_negatives(*numbers)
