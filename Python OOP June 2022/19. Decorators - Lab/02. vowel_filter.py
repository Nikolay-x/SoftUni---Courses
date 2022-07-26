# 2.Vowel Filter
# Having the following code:
#
# def vowel_filter(function):
#
#     def wrapper():
#
#         # TODO: Implement
#
#     return wrapper
#
# Complete the code, so it works as expected:
#
# Test Code
# @vowel_filter
# def get_letters():
#     return ["a", "b", "c", "d", "e"]
#
# print(get_letters())
#
# Output
# ["a", "e"]

def vowel_filter(function):
    def wrapper():
        result = function()
        vowels = [x for x in result if x.lower() in "aeiou"]
        return vowels
    return wrapper


@vowel_filter
def get_letters():
    return ["a", "b", "c", "d", "e"]


print(get_letters())
