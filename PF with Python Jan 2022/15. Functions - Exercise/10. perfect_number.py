# 10.Perfect Number
# A perfect number is a positive integer that is equal to the sum of its proper positive divisors. That is the sum of its positive divisors, excluding the number itself (also known as its aliquot sum).
# Write a function that receives an integer number and returns one of the following messages:
# "We have a perfect number!" - if the number is perfect.
# "It's not so perfect." - if the number is NOT perfect.
# Print the result on the console.
#
# Input
# 6
#
# Output
# We have a perfect number!

def perfect_number(n):
    aliquot_sum = 0
    for i in range(1, n):
        if n % i == 0:
            aliquot_sum += i
    if n == aliquot_sum:
        print("We have a perfect number!")
    else:
        print("It's not so perfect.")

num = int(input())

perfect_number(num)
