# 1.Shop
# Create a class called Shop. Upon initialization, it should receive a name (string) and items (list). Create a method called get_items_count() which should return the number of items in the store.
#
# Test Code
# shop = Shop("My Shop", ["Apples", "Bananas", "Cucumbers"])
# print(shop.get_items_count())
#
# Output
# 3

class Shop:
    def __init__(self, name, items):
        self.name = name
        self.items = items

    def get_items_count(self):
        return len(self.items)


shop = Shop("My Shop", ["Apples", "Bananas", "Cucumbers"])
print(shop.get_items_count())
