# 3.Record Unique Names
# Write a program, which will take a list of names and print only the unique names in the list.
# The order in which we print the result does not matter.
#
# Input
# 8
# Lee
# Joey
# Lee
# Joe
# Alan
# Alan
# Peter
# Joey
#
# Output
# Alan
# Joey
# Lee
# Joe
# Peter

names_count = int(input())
output = set()
for _ in range(names_count):
    name = input()
    output.add(name)
for name in output:
    print(name)
