# 5.Orders
# Write a function that calculates the total price of an order and returns it. The function should receive one of the following products: "coffee", "coke", "water", or "snacks", and a quantity of the product. The prices for a single piece of each product are:
# coffee - 1.50
# water - 1.00
# coke - 1.40
# snacks - 2.00
#
# Print the result formatted to the second decimal place.
#
# Input
# water
# 5
#
# Output
# 5.00

def orders(product, quantity):
    result = None
    if product == "coffee":
        result = quantity * 1.5
    elif product == "coke":
        result = quantity * 1.4
    elif product == "water":
        result = quantity * 1
    elif product == "snacks":
        result = quantity * 2
    return f'{result:.2f}'

input_product = input()
q = int(input())

print(orders(input_product, q))
