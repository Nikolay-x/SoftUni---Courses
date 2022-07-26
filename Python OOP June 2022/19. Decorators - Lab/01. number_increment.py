# 1.Number Increment
# Having the following code:
#
# def number_increment(numbers):
#
#     def increase():
#
#         # TODO: Implement
#
#     return increase()
#
# Complete the code, so it works as expected.
#
# Test Code
# print(number_increment([1, 2, 3]))
#
# Output
# [2, 3, 4]

def number_increment(numbers):

    def increase():
        result = [x + 1 for x in numbers]
        return result
    return increase()


print(number_increment([1, 2, 3]))
