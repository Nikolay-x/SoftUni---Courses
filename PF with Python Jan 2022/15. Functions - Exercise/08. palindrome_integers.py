# 8.Palindrome Integers
# A palindrome is a number that reads the same backward as forward, such as 323 or 1001. Write a function that receives a list of positive integers, separated by comma and space ", ". The function should check if each integer is a palindrome - True or False. Print the result.
#
# Input
# 123, 323, 421, 121
#
# Output
# False
# True
# False
# True

def palindrome_int(n):
    for num in n:
        if num == num[::-1]:
            print(True)
        else:
            print(False)

nums = list(input().split(", "))
palindrome_int(nums)
