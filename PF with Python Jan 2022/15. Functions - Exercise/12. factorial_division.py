# 12.* Factorial Division
# Write a function that receives two integer numbers. Calculate the factorial of each number.
# Divide the first result by the second and print the division formatted to the second decimal point.
#
# Input
# 5
# 2
#
# Output
# 60.00

def factorial_division(m, n):
    m_factorial = 1
    n_factorial = 1
    for i in range(1, m + 1):
        m_factorial *= i
    for j in range(1, n + 1):
        n_factorial *= j
    result = m_factorial / n_factorial
    return result

num1 = int(input())
num2 = int(input())

print(f"{factorial_division(num1, num2):.2f}")
