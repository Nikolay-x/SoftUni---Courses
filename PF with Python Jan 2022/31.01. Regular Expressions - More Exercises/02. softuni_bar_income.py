# 2.SoftUni Bar Income
# Let`s take a break and visit the game bar at SoftUni. It is about time for the people behind the bar to go home and you are the person who has to draw the line and calculate the money from the products that were sold throughout the day. Until you receive a line with text "end of shift" you will be given lines of input. But before processing that line you should do some validations first.
# Each valid order should have a customer, product, count and a price:
# Valid customer's name should be surrounded by '%' and must start with a capital letter, followed by lower-case letters
# Valid product contains any word character (not only letters) and must be surrounded by '<' and '>'
# Valid count is an integer, surrounded by '|'
# Valid price is any real number followed by '$'
# The parts of a valid order should appear in the order given: customer, product, count and a price.
# Between each part there can be other symbols, except ('|', '$', '%' and '.')
# For each valid line print on the console: "{customerName}: {product} - {totalPrice}"
# When you receive "end of shift" print the total amount of money for the day rounded to 2 decimal places in the following format: "Total income: {income}".
# Input / Constraints
# Strings that you have to process until you receive text "end of shift".
# Output
# Print all of the valid lines in the format "{customerName}: {product} - {totalPrice}"
# After receiving "end of shift" print the total amount of money for the day rounded to 2 decimal places in the following format: "Total income: {income}"
# Allowed working time / memory: 100ms / 16MB.
#
# Input
# %George%<Croissant>|2|10.3$
# %Peter%<Gum>|1|1.3$
# %Maria%<Cola>|1|2.4$
# end of shift
#
# Output
# George: Croissant - 20.60
# Peter: Gum - 1.30
# Maria: Cola - 2.40
# Total income: 24.30

import re

regex_name = r"(?<=\%)[A-Z][a-z]+(?=\%)"
regex_product = r"(?<=\<)\w+(?=\>)"
regex_count = r"(?<=\|)\d+(?=\|)"
regex_price = r"\d+(\.\d+)?(?=\$)"
total_income = 0

while True:
    is_order_valid = True
    line = input()
    if line == "end of shift":
        break
    name_match = re.findall(regex_name, line)
    if len(name_match) > 0:
        name = name_match[0]
    else:
        is_order_valid = False
    product_match = re.findall(regex_product, line)
    if len(product_match) > 0:
        product = product_match[0]
    else:
        is_order_valid = False
    count_match = re.findall(regex_count, line)
    if len(count_match) > 0:
        count = int(count_match[0])
    else:
        is_order_valid = False
    price_list = []
    price_match = re.finditer(regex_price, line)
    for match in price_match:
        price = float(match.group())
        price_list.append(price)
    if len(price_list) == 0:
        is_order_valid = False
    if is_order_valid:
        total_income += count * price
        print(f"{name}: {product} - {(count * price):.2f}")

print(f"Total income: {total_income:.2f}")
