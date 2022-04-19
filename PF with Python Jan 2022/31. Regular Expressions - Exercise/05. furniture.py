# 5.Furniture
# Write a program that calculates the total cost of bought furniture. You will be given information about each purchase on separate lines until you receive the command "Purchase". Valid information should be in the format: ">>{furniture_name}<<{price}!{quantity}". The price could be a floating-point or integer number. You should store the names of the furniture and the total price.
# In the end, print the name of each bought furniture and the total cost, formatted to the second decimal point:
# "Bought furniture:
# {1st name}
# {2nd name}
# …
# {N name}
# Total money spend: {total_cost}"
#
# Input
# >>Sofa<<312.23!3
# >>TV<<300!5
# >Invalid<<!5
# Purchase
#
# Output
# Bought furniture:
# Sofa
# TV
# Total money spend: 2436.69

import re

regex = r">>(?P<furniture_name>[A-Za-z]+)<<(?P<price>\d+\.*\d+)!(?P<quantity>\d+)"

orders_list = []
total_price = 0

while True:
    line = input()
    if line == "Purchase":
        break

    matches = re.finditer(regex, line)
    for match in matches:

    # match = re.match(regex, line)
    # if match is not None:

        furniture_name = match.group("furniture_name")
        price = float(match.group("price"))
        quantity = int(match.group("quantity"))

        orders_list.append(furniture_name)
        total_price += price * quantity

print("Bought furniture:")

# print("\n".join(orders_list))

for furniture in orders_list:
    print(f"{furniture}")

print(f"Total money spend: {total_price:.2f}")
