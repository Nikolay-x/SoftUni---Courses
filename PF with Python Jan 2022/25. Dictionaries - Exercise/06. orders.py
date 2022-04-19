# 6.Orders
# Write a program that keeps the information about products and their prices. Each product has a name, a price, and a quantity:
# If the product doesn't exist yet, add it with its starting quantity.
# If you receive a product, which already exists, increases its quantity by the input quantity and if its price is different, replace the price as well.
# You will receive products' names, prices, and quantities on new lines. Until you receive the command "buy", keep adding items. Finally, print all items with their names and the total price of each product.
# Input
# Until you receive "buy", the products will be coming in the format: "{name} {price} {quantity}".
# The product data is always delimited by a single space.
# Output
# Print information about each product in the following format:
# "{product_name} -> {total_price}"
# Format the total price to the 2nd digit after the decimal separator.
#
# Input
# Beer 2.20 100
# IceTea 1.50 50
# NukaCola 3.30 80
# Water 1.00 500
# buy
#
# Output
# Beer -> 220.00
# IceTea -> 75.00
# NukaCola -> 264.00
# Water -> 500.00

orders = dict()
while True:
    item_data = input()
    if item_data == "buy":
        break
    item_data = item_data.split(" ")
    item = item_data[0]
    price = float(item_data[1])
    quantity = int(item_data[2])
    if item not in orders:
        orders[item] = [0.0, 0]
        orders[item][1] = quantity
    else:
        orders[item][1] += quantity
    orders[item][0] = price

for item in orders:
    total_price = orders[item][0] * orders[item][1]
    print(f'{item} -> {total_price:.2f}')
