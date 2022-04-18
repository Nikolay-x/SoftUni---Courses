# 2.Number Definer
# Write a program that reads a floating-point number and:
# -prints "zero" if the number is zero.
# -prints "positive" or "negative".
# -adds "small" if the absolute value of the number is less than 1 and it is not 0, or "large" if it exceeds
# 1 000 000.
#
# Input
# 25
#
# Output
# positive

a = float(input())

if a == 0:
    print("zero")
else:
    if a < -1000000:
        print("large negative")
    elif -1000000 <= a <= -1:
        print("negative")
    elif -1 <= a <0:
        print("small negative")
    elif 0 < a < 1:
        print("small positive")
    elif 1 <= a <= 1000000:
        print("positive")
    elif a > 1000000:
        print("large positive")
