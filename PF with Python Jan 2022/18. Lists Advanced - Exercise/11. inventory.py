# 11.* Inventory
# As a young traveler, you gather items and craft new items.
# You will receive a journal with some Collecting items, separated with ", " (comma and space). After that, until receiving "Craft!" you will be receiving different commands.
# Commands (split by " - "):
# "Collect - {item}" – Receiving this command, you should add the given item to your inventory. If the item already exists, you should skip this line.
# "Drop - {item}" – You should remove the item from your inventory if it exists.
# "Combine Items - {oldItem}:{newItem}" – You should check if the old item exists. If so, add the new item after the old one. Otherwise, ignore the command.
# "Renew – {item}" – If the given item exists, you should change its position and put it last in your inventory.
# Output
# After receiving "Craft!" print the items in your inventory, separated by ", " (comma and space).
#
# Input
# Iron, Wood, Sword
# Collect - Gold
# Drop - Wood
# Craft!
#
# Output
# Iron, Sword, Gold

def collect(x, y):
    if y[1] not in x:
        x.append(y[1])
    return x
def drop(x, y):
    if y[1] in x:
        x.remove(y[1])
    return x
def combine_items(x, y):
    if y[0] == "Combine Items":
        y1 = y[1].split(":")
    for i in range(len(x)):
        if x[i] == y1[0]:
            x.insert(i+1, y1[1])
    return x
def renew(x, y):
    if y[1] in x:
        x.remove(y[1])
        x.append(y[1])
    return x

def inventory(x, y):
    while y != "Craft!":
        current_command = y.split(" - ")

        if current_command[0] == "Collect":
            collect(inventory_list, current_command)
        if current_command[0] == "Drop":
            drop(inventory_list, current_command)
        if current_command[0] == "Combine Items":
            combine_items(inventory_list, current_command)
        if current_command[0] == "Renew":
            renew(inventory_list, current_command)

        y = input()
    return ", ".join(x)

inventory_list = input().split(", ")
command = input()

print(inventory(inventory_list, command))
