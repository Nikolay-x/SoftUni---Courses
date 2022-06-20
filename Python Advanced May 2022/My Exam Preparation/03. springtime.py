# 03. Springtime
# Spring is the season of new beginnings. Fresh buds bloom, animals awaken and the earth seems to come to life again. Farmers and gardeners plant their seeds and temperatures slowly rise.
# Write a function called start_spring which will receive a different number of keyword arguments.
# Each keyword holds a key with a name of the spring object (string), and each value holds its type (string). For example, dahlia="flower", shrikes="bird", dogwood="tree".
# The function should sort the given spring objects in collections by their type:
# The collections sorted by their number of elements in descending order. If two or more collections have the same number of elements in them, return them in ascending order (alphabetically) by the type's name.
# Each collection's elements should be sorted in ascending order (alphabetically) by the object's name.
# Note: Submit only the function in the judge system
# Input
# There will be no input. Just parameters passed to your function.
# Output
# Return the result, sorted as described above in the format:
# o"{type_one}:
# -{spring_object_of_this_type_one}
# -{spring_object_of_this_type_two}
# …
# -{spring_object_of_this_type_N}
# {type_two}:
# …
# {type_N}:
# …
# -{last_spring_object_of_typeN}"
#
# Test Code
# example_objects = {"Water Lilly": "flower",
#                    "Swifts": "bird",
#                    "Callery Pear": "tree",
#                    "Swallows": "bird",
#                    "Dahlia": "flower",
#                    "Tulip": "flower",}
# print(start_spring(**example_objects))
#
# Output
# flower:
# -Dahlia
# -Tulip
# -Water Lilly
# bird:
# -Swallows
# -Swifts
# tree:
# -Callery Pear

def start_spring(**kwargs):
    result = {}
    output = []

    for spring_object, object_type in kwargs.items():
        if object_type not in result:
            result[object_type] = []
        result[object_type].append(spring_object)

    result = sorted(result.items(), key=lambda x: (-len(x[1]), x[0]))

    for item in result:
        output.append(f"{item[0]}:")
        for obj in sorted(item[1]):
            output.append(f"-{obj}")

    return "\n".join(output)


example_objects = {"Water Lilly": "flower",
                   "Swifts": "bird",
                   "Callery Pear": "tree",
                   "Swallows": "bird",
                   "Dahlia": "flower",
                   "Tulip": "flower"}
print(start_spring(**example_objects))

example_objects = {"Swallow": "bird",
                   "Thrushes": "bird",
                   "Woodpeckers": "bird",
                   "Swallows": "bird",
                   "Warblers": "bird",
                   "Shrikes": "bird"}
print(start_spring(**example_objects))

example_objects = {"Magnolia": "tree",
                   "Swallow": "bird",
                   "Thrushes": "bird",
                   "Pear": "tree",
                   "Cherries": "tree",
                   "Shrikes": "bird",
                   "Butterfly": "insect"}
print(start_spring(**example_objects))
