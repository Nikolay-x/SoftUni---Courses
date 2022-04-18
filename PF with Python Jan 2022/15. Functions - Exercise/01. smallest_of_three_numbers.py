# 1.Smallest of Three Numbers
# Write a function that receives three integer numbers and returns the smallest. Print the result on the console. Use an appropriate name for the function.
#
# Input
# 2
# 5
# 3
#
# Output
# 2

def smallest(a, b, c):
    return min(a, b, c)

num1, num2, num3 = int(input()), int(input()), int(input())
result = smallest(num1, num2, num3)

print(result)
