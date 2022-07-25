# 9.Possible permutations
# Create a generator function called possible_permutations() which should receive a list and return lists with all possible permutations between its elements.
# Note: Submit only the function in the judge system
#
# Test Code
# [print(n) for n in possible_permutations([1, 2, 3])]
#
# Output
# [1, 2, 3]
# [1, 3, 2]
# [2, 1, 3]
# [2, 3, 1]
# [3, 1, 2]
# [3, 2, 1]

from itertools import permutations


def possible_permutations(data_list):
    for permutation in permutations(data_list):
        yield list(permutation)


[print(n) for n in possible_permutations([1, 2, 3])]
