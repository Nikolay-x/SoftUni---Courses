# 3.Even or Odd
# Create a function called even_odd() that can receive a different quantity of numbers and a command at the end. The command can be "even" or "odd". Filter the numbers depending on the command and return them in a list. Submit only the function in the judge system.
# Submit only your function in the judge system.
#
# Test Code
# print(even_odd(1, 2, 3, 4, 5, 6, "even"))
# print(even_odd(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "odd"))
#
# Output
# [2, 4, 6]
# [1, 3, 5, 7, 9]

# def even_odd(*args):
#     filter_command = args[-1]
#     parity = 0 if filter_command == "even" else 1
#     result = []
#     for i in range(len(args) - 1):
#         number = args[i]
#         if number % 2 == parity:
#             result.append(number)
#     return result
#
#
# print(even_odd(1, 2, 3, 4, 5, 6, "even"))
# print(even_odd(1, 2, 3, 4, 5, 6, 7, 8, 10, "almost_even"))

def even_odd(*args):
    even = []
    odd = []

    for i in range(len(args) - 1):
        if args[i] % 2 == 0:
            even.append(args[i])
        else:
            odd.append(args[i])

    if args[-1] == "even":
        return even
    elif args[-1] == "odd":
        return odd


print(even_odd(1, 2, 3, 4, 5, 6, "even"))
print(even_odd(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "odd"))
