# 7.Min Max and Sum
# Write a program that receives a sequence of numbers (integers) separated by a single space. It should print the min and max values of the given numbers and the sum of all the numbers in the list. Use min(), max() and sum().
# The output should be as follows:
# On the first line: "The minimum number is {minimum number}"
# On the second line: "The maximum number is {maximum number}"
# On the third line: "The sum number is {sum of all numbers}"
#
# Input
# 2 4 6
#
# Output
# The minimum number is 2
# The maximum number is 6
# The sum number is: 12

def min_max_sum(n):
    print(f"The minimum number is {min(n)}")
    print(f"The maximum number is {max(n)}")
    print(f"The sum number is: {sum(n)}")

nums = list(map(int, input().split(" ")))

min_max_sum(nums)
