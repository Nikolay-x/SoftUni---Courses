# 4.Number Between 1 and 100
# Write a program that reads different floating-point numbers from the console. When it receives a number between 1 and 100 inclusive, the program should stop reading and should print "The number {number} is between 1 and 100".
#
# Input
# -3
# 0.9
# 44
#
# Output
# The number 44.0 is between 1 and 100

a = float(input())

while a < 1 or a > 100:
    a = float(input())

print(f"The number {a} is between 1 and 100")
