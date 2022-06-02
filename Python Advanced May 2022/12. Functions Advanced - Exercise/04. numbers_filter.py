# 4.Numbers Filter
# Create a function called even_odd_filter() that can receive a different number of named arguments. The keys will be "even" and/or "odd", and the values will be a list of numbers.
# When the key is "odd", you should extract only the odd numbers from its list. When the key is "even", you should extract only the even numbers from its list.
# The function should return a dictionary sorted by the length of the lists in descending order. There will be no case of lists with the same length.
# Submit only your function in the judge system.
#
# Input
# print(even_odd_filter(
#     odd=[1, 2, 3, 4, 10, 5],
#     even=[3, 4, 5, 7, 10, 2, 5, 5, 2],
# ))
#
# Output
# {'even': [4, 10, 2, 2], 'odd': [1, 3, 5]}

# def even_odd_filter(**kwargs):
#     result = {}
#     for key, value in kwargs.items():
#         parity = 0 if key == "even" else 1
#         filtered = [x for x in value if x % 2 == parity]
#         result[key] = filtered
#     return dict(sorted(result.items(), key=lambda x: -len(x[1])))

def even_odd_filter(**kwargs):
    result = {}
    for key in kwargs:
        if key == "even":
            kwargs[key] = [x for x in kwargs[key] if x % 2 == 0]
        if key == "odd":
            kwargs[key] = [x for x in kwargs[key] if x % 2 != 0]
    items = sorted(kwargs.items(), key=lambda x: -len(x[1]))
    for item in items:
        result[item[0]] = item[1]
    return result


print(even_odd_filter(
    odd=[1, 2, 3, 4, 10, 5],
    even=[3, 4, 5, 7, 10, 2, 5, 5, 2],
))
