# 4.Repeat String
# Write a function that receives a string and a counter n. The function should return a new string – the result of repeating the old string n times. Print the result of the function. Try using lambda.
#
# Input
# abc
# 3
#
# Output
# abcabcabc

string = input()
n = int(input())

repeat = lambda a, b: a * b

# result = repeat(string, n)
# print(result)

print(repeat(string, n))
