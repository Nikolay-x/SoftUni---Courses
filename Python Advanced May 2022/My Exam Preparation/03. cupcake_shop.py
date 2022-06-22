# Problem 3 - Cupcake Shop
# Maria is opening a cupcake shop. Help her manage her inventory to improve stock availability.
#
# Write a function called stock_availability which receives:
# an inventory list of boxes with different kinds of cupcake flavours
# "delivery" or "sell" as second parameter
# there might or might not be any other parameters – numbers or strings at the end
#
# In case of "delivery"  to the shop was delivered new boxes with diferent kinds of cupcakes:
# You should add the boxes at the end of the inventory list
# There will be always at least one box delivered
# In case of "sell" Maria has a client and she is selling different boxes with cupcakes:
# If there is a number as another parameter, it means that Maria has sold that many boxes with cupcakes and you should remove them from the beginning of the inventory list
# If there is/are string/s as another parameter/s, it means that Maria has sold ALL cupcake boxes of the ordered flavour/s. Beware that not everything the buyer has ordered might be in stock, so you should check if the order is valid.
# If there are no other parameters, it means that Maria has sold only the first box of cupcakes and you should remove  it of the inventory list
# For more clarifications, see the examples below.
# Input
# There will be no input
# Parameters will be passed to your function
# Output
# The function should return a new inventory list
# All commands will be valid
#
# Test Code
# print(stock_availability(["choco", "vanilla", "banana"], "delivery", "caramel", "berry"))
# print(stock_availability(["chocolate", "vanilla", "banana"], "delivery", "cookie","banana"))
# print(stock_availability(["chocolate", "vanilla", "banana"], "sell"))
# print(stock_availability(["chocolate", "vanilla", "banana"], "sell", 3))
# print(stock_availability(["chocolate", "chocolate", "banana"], "sell", "chocolate"))
# print(stock_availability(["cookie", "chocolate", "banana"], "sell", "chocolate"))
# print(stock_availability(["chocolate", "vanilla", "banana"], "sell", "cookie"))
#
# Output
# ['choco', 'vanilla', 'banana', 'caramel', 'berry']
# ['chocolate', 'vanilla', 'banana', 'cookie', 'banana']
# ['vanilla', 'banana']
# []
# ['banana']
# ['cookie', 'banana']
# ['chocolate', 'vanilla', 'banana']

def stock_availability(inventory_list, command, *args):
    if command == "delivery":
        for arg in args:
            inventory_list.append(arg)
    elif command == "sell":
        if len(args) == 0:
            inventory_list.pop(0)
        else:
            for arg in args:
                if type(arg) == int:
                    for i in range(arg):
                        inventory_list.pop(0)
                else:
                    cupcake = arg
                    if cupcake in inventory_list:

                        for i in range(len(inventory_list) - 1, -1, -1):
                            if inventory_list[i] == cupcake:
                                inventory_list.remove(inventory_list[i])
                        # while cupcake in inventory_list:
                        #     inventory_list.remove(cupcake)

    return inventory_list


print(stock_availability(["choco", "vanilla", "banana"],
                         "delivery", "caramel", "berry"))
print(stock_availability(["chocolate", "vanilla", "banana"],
                         "delivery", "cookie","banana"))
print(stock_availability(["chocolate", "vanilla", "banana"],
                         "sell"))
print(stock_availability(["chocolate", "vanilla", "banana"],
                         "sell", 3))
print(stock_availability(["chocolate", "chocolate", "banana"],
                         "sell", "chocolate"))
print(stock_availability(["cookie", "chocolate", "banana"],
                         "sell", "chocolate"))
print(stock_availability(["chocolate", "vanilla", "banana"],
                         "sell", "cookie"))
