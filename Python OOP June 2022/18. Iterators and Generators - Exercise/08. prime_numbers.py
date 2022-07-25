# 8.Prime Numbers
# Create a generator function called get_primes() which should receive a list of integer numbers and return a list containing only the prime numbers from the initial list. You can learn more about prime numbers from here:
# Note: Submit only the function in the judge system
#
# Test Code
# print(list(get_primes([2, 4, 3, 5, 6, 9, 1, 0])))
#
# Output
# [2, 3, 5]

def prime_check(n):
    is_prime = True
    for i in range(2, n):
        if n % i == 0:
            is_prime = False
            break
    return is_prime


def get_primes(numbers):
    for number in numbers:
        if number > 1:
            if prime_check(number):
                yield number


print(list(get_primes([2, 4, 3, 5, 6, 9, 1, 0])))
print(list(get_primes([-2, 0, 0, 1, 1, 0])))
