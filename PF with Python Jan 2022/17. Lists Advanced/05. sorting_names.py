# 5.Sorting Names
# Write a program that reads a single string with names separated by comma and space ", ". Sort the names by their length in descending order. If 2 or more names have the same length, sort them in ascending order (alphabetically). Print the resulting list.
#
# Input
# Ali, Marry, Kim, Teddy, Monika, John
#
# Output
# ["Monika", "Marry", "Teddy", "John", "Ali", "Kim"]

names = input().split(", ")

# sorted_names = sorted(names)
# sorted_names = sorted(sorted_names, key=lambda name: -len(name))

# whole_sorted_names = sorted(names, key=lambda name: (-len(name), name))

sorted_names = sorted(names, key=lambda x: (-len(x), x))

# print(whole_sorted_names)

print(sorted_names)
