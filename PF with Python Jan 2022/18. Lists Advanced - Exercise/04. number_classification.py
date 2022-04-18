# 4.Number Classification
# Using a list comprehension, write a program that receives numbers, separated by comma and space ", ", and prints all the positive, negative, even, and odd numbers on separate lines as shown below.
# Note: Zero is counted for a positive number
#
# Input
# 1, -2, 0, 5, 3, 4, -100, -20, 12, 19, -33
#
# Output
# Positive: 1, 0, 5, 3, 4, 12, 19
# Negative: -2, -100, -20, -33
# Even: -2, 0, 4, -100, -20, 12
# Odd: 1, 5, 3, 19, -33

numbers = list(map(int, input().split(", ")))

positive = ", ".join(str(number) for number in numbers if number >= 0)
negative = ", ".join(str(number) for number in numbers if number < 0)
even = ", ".join(str(number) for number in numbers if number % 2 == 0)
odd = ", ".join(str(number) for number in numbers if number % 2 != 0)

print(f"Positive: {positive}")
print(f"Negative: {negative}")
print(f"Even: {even}")
print(f"Odd: {odd}")
