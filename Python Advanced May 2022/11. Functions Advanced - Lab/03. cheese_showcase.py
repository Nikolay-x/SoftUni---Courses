# 3.Cheese Showcase
# White a function called sorting_cheeses that receives keywords arguments:
# The key represents the name of the cheese
# The value is a list of quantities (integers) of the pieces of the given cheese
# The function should return the cheeses and their pieces' quantities sorted by the number of pieces of a cheese kind in descending order. If two or more cheeses have the same number of pieces, sort them by their names in ascending order (alphabetically). For each kind of cheese, return their pieces quantities in descending order.
# For more clarifications, see the examples below.
#
# Input
# print(
#     sorting_cheeses(
#         Parmigiano=[165, 215],
#         Feta=[150, 515],
#         Brie=[150, 125]
#     )
# )
#
# Output
# Brie
# 150
# 125
# Feta
# 515
# 150
# Parmigiano
# 215
# 165

# import os
#
#
# def sorting_cheeses(**kwargs):
#     sorted_cheeses = sorted(
#         kwargs.items(),
#         key=lambda x: (-len(x[1]), x[0]),
#     )
#
#     result = []
#
#     for name, pieces_counts in sorted_cheeses:
#         result.append(name)
#         result.extend(
#             sorted(pieces_counts, reverse=True)
#         )
#
#         # '\n' don't use this!
#         # '\n\r' for Windows
#         # os.linesep
#     return os.linesep.join([str(x) for x in result])
#
#
# print(
#     sorting_cheeses(
#         Parmesan=[102, 120, 135],
#         Camembert=[100, 100, 105, 500, 430],
#         Mozzarella=[50, 125],
#     )
# )

def sorting_cheeses(**kwargs):
    result = []
    kwargs = sorted(kwargs.items(), key=lambda x: (-len(x[1]), x[0]))
    for item in kwargs:
        result.append(item[0])
        for value in sorted(item[1], key=lambda x: -x):
            result.append(value)
    return "\n".join(str(x) for x in result)


# def sorting_cheeses(**cheeses_dict):
#     cheeses_dict = sorted(
#         cheeses_dict.items(),
#         key=lambda x: (-len(x[1]), x[0]))
#
#     result = []
#
#     for (cheese_name, quantities) in cheeses_dict:
#         result.append(cheese_name)
#         quantity_list = sorted(quantities, reverse=True)
#         result += quantity_list
#
#     return "\n".join([str(x) for x in result])


print(
    sorting_cheeses(
        Parmigiano=[165, 215],
        Feta=[150, 515],
        Brie=[150, 125]
    )
)
