# 4.Odd and Even Sum
# You will receive a single number. You should write a function that returns the sum of all even and all odd digits in a given number. The result should be returned as a single string in the format:
# "Odd sum = {sum_of_odd_digits}, Even sum = {sum_of_even_digits}"
# Print the result of the function on the console.
#
# Input
# 1000435
#
# Output
# Odd sum = 9, Even sum = 4

def sum_even_odd_digits(n):

    even_sum = 0
    odd_sum = 0

    for i in n:
        if i % 2 == 0:
            even_sum += i
        else:
            odd_sum += i

    print(f"Odd sum = {odd_sum}, Even sum = {even_sum}")

num = list(map(int, list(input())))

sum_even_odd_digits(num)
