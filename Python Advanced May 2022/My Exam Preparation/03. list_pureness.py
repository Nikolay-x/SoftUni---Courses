# 03.List Pureness
# Write function called best_list_pureness which will receive a list of numbers and a number K. You have to rotate the list K times (last becomes first) to find the variation of the list with the best pureness (pureness is calculated by summing all the elements in the list multiplied by their indices). For example, in the list [4, 3, 2, 6] with the best pureness is (3 * 0) + (2 * 1) + (6 * 2) + (4 * 3) = 26. At the end the function should return a string containing the highest pureness and the amount of rotations that were made to find this pureness in the following format: "Best pureness {pureness_value} after {count_rotations} rotations". If there is more than one highest pureness, take the first one.
# Note: Submit only the function in the judge system
# Input
# There will be no input, just parameters passed to your function
# Output
# There is no expected output
# The function should return a string in the following format: "Best pureness {pureness_value} after {count_rotations} rotations"
#
# Test Code
# test = ([4, 3, 2, 6], 4)
# result = best_list_pureness(*test)
# print(result)
#
# Output
# Best pureness 26 after 3 rotations

def best_list_pureness(number_list, k):
    pureness_list_values = []
    pureness_list_rotations = []

    pureness = 0
    for j, v in enumerate(number_list):
        pureness += j * v
    pureness_list_values.append(pureness)
    pureness_list_rotations.append(0)

    for i in range(1, k+1):
        pureness = 0
        last_number = number_list.pop()
        number_list.insert(0, last_number)
        for j, v in enumerate(number_list):
            pureness += j * v
        pureness_list_values.append(pureness)
        pureness_list_rotations.append(i)

    best_pureness = max(pureness_list_values)
    index = pureness_list_values.index(best_pureness)
    rotation = pureness_list_rotations[index]
    def_result = f"Best pureness {best_pureness} after {rotation} rotations"

    return def_result


test = ([4, 3, 2, 6], 4)
result = best_list_pureness(*test)
print(result)

test = ([7, 9, 2, 5, 3, 4], 3)
result = best_list_pureness(*test)
print(result)

test = ([1, 2, 3, 4, 5], 10)
result = best_list_pureness(*test)
print(result)
