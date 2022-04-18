# 5.Multiplication Sign
# You will receive three integer numbers. Write a program that finds if their multiplication (the result) is negative, positive, or zero. Try to do this WITHOUT multiplying the 3 numbers.
#
# Input
# 2
# 3
# -1
#
# Output
# negative

def multiplication_sign(a, b, c):
    count = 0
    is_zero = False

    if a < 0:
        count += 1
    if b < 0:
        count += 1
    if c < 0:
        count += 1
    if a == 0 or b == 0 or c == 0:
        is_zero = True

    if is_zero:
        result = "zero"
    else:
        if count % 2 != 0:
            result = "negative"
        else:
            result = "positive"
    return result

x = int(input())
y = int(input())
z = int(input())

print(multiplication_sign(x, y, z))
