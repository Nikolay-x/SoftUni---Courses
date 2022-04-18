# 3.List Statistics
# On the first line, you will receive a number n. On the following n lines, you will receive integers. You should create and print two lists:
# One with all the positives (including 0) numbers
# One with all the negatives numbers
# Finally, print the following message:
# "Count of positives: {count_positives}
# Sum of negatives: {sum_of_negatives}"
#
# Input
# 5
# 10
# 3
# 2
# -15
# -4
#
# Output
# [10, 3, 2]
# [-15, -4]
# Count of positives: 3
# Sum of negatives: -19

n = int(input())

positives = []
negatives = []
count_positives = 0
sum_of_negatives = 0

for i in range(n):
    num = int(input())
    if num >= 0:
        positives.append(num)
        count_positives += 1
    else:
        negatives.append(num)
        sum_of_negatives += num

print(positives)
print(negatives)

# print(f"Count of positives: {len(positives)}")
# print(f"Sum of negatives: {sum(negatives)}")

print(f"Count of positives: {count_positives}")
print(f"Sum of negatives: {sum_of_negatives}")
