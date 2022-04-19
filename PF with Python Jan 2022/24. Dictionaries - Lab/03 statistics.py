# 3.Statistics
# You seem to be doing great at your first job, so your boss decides to give you as your next task something more challenging. You have to accept all the new products coming in the bakery and finally gather some statistics.
# You will be receiving key-value pairs on separate lines separated by ": " until you receive the command "statistics". Sometimes you may receive a product more than once. In that case, you have to add the new quantity to the existing one. When you receive the "statistics" command, print the following:
# "Products in stock:
# - {product1}: {quantity1}
# - {product2}: {quantity2}
# …
# - {productN}: {quantityN}
# Total Products: {count_all_products}
# Total Quantity: {sum_all_quantities}"
#
# Input
# bread: 4
# cheese: 2
# ham: 1
# bread: 1
# statistics
#
# Output
# Products in stock:
# - bread: 5
# - cheese: 2
# - ham: 1
# Total Products: 3
# Total Quantity: 8

line = input()
stock = dict()

while line != "statistics":
    line = line.split(": ")
    product = line[0]
    quantity = int(line[1])

    if product not in stock.keys():
        stock[product] = 0

    stock[product] += quantity

    line = input()

print("Products in stock:")

for product in stock:
    print(f"- {product}: {stock[product]}")

# for product, quantity in stock.items():
#     print(f"- {product}: {quantity}")

print(f"Total Products: {len(stock.keys())}")
print(f"Total Quantity: {sum(stock.values())}")
