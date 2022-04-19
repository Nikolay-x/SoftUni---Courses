# 1.Bakery
# Your first task at your new job is to create a table of the stock in a bakery, and you really don't want to fail on your first day at work.
# You will receive a single line containing some food (keys) and quantities (values). They will be separated by a single space (the first element is the key, the second – the value, and so on). Create a dictionary with all the keys and values and print it on the console.
#
# Input
# bread 10 butter 4 sugar 9 jam 12
#
# Output
# {'bread': 10, 'butter': 4, 'sugar': 9, 'jam': 12}

data = input().split(" ")
bakery = {}

for i in range(0, len(data), 2):
    food = data[i]
    quantities = int(data[i+1])
    bakery[food] = quantities

print(bakery)
