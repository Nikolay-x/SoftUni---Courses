# 9.* Hello, France
# You want to go to France by train, and the train ticket costs exactly 150$. You do not have enough money, so you decide to buy some items with your budget and then sell them at a higher price – with a 40% markup.
# You will receive a collection of items and a budget in the following format:
# {type->price|type->price|type->price……|type->price}
# {budget}
# The prices for each of the types cannot exceed a specific price, which is given below:
# Type	Maximum Price
# Clothes	50.00
# Shoes	35.00
# Accessories	20.50
# If a price for a particular item is higher than the maximum price, don't buy it. Every time you buy an item, you have to reduce the budget with its price value. If you don't have enough money for it, you can't buy it. Buy as many items as you can.
# Next, you should increase the price of each item you have successfully bought by 40% and then sell it. Calculate if the budget after selling all the items is enough for buying the train ticket.
# Input / Constraints
# On the 1st line, you will receive the items with their prices in the format described above – real numbers in the range [0.00……1000.00]
# On the 2nd line, you are going to be given the budget – a real number in the range [0.0….1000.0]
# Output
# First, print the list with the bought item’s new prices, formatted to the second decimal point in the following format:
# "{price1} {price2} {price3} … {priceN}"
# Second, print the profit, formatted to the second decimal point in the following format:
# "Profit: {profit}"
# Finally:
# oIf the budget is enough for buying the train ticket, print: "Hello, France!"
# oOtherwise, print: "Not enough money."
#
# Input
# Clothes->43.30|Shoes->25.25|Clothes->36.52|Clothes->20.90|Accessories->15.60
# 120
#
# Output
# 60.62 35.35 51.13
# Profit: 42.03
# Hello, France!

items_list = input().split("|")
budget = float(input())

profit = 0
items_total_price = 0
new_prices = []

for item in items_list:
    current_item = item.split("->")
    item_type = current_item[0]
    item_price = float(current_item[1])
    condition = False

    if item_type == "Clothes" and item_price <= 50:
        condition = True

    elif item_type == "Shoes" and item_price <= 35:
        condition = True

    elif item_type == "Accessories" and item_price <= 20.5:
        condition = True

    if condition:
        if budget >= item_price:
            budget -= item_price
            profit += item_price * 0.4
            item_new_price = 1.4 * item_price
            items_total_price += item_new_price
            new_prices.append(f"{item_new_price:.2f}")

print(" ".join(new_prices))
print(f"Profit: {profit:.2f}")

if budget + items_total_price >= 150:
    print("Hello, France!")
else:
    print("Not enough money.")
