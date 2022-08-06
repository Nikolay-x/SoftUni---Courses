# Workshop HashTable
# In computing, a hash table (hash map) is a data structure that implements an associative array abstract data type, a structure that can map keys to values. A hash table uses a hash function to compute an index, also called a hash code, into an array of buckets or slots, from which the desired value can be found. During lookup, the key is hashed and the resulting hash indicates where the corresponding value is stored.
# 1.Overview
# Create a HashTable class that should have the needed functionality for a hash table, such as:
# hash(key: str) - a function that should figure out where to store the key-value pair
# add(key: str, value: any) - adds a new key-value pair usign the hash function
# get(key: str) - returns the value corresponding to the given key
# additional "magic" methods, that will make the code in the example work correctrly
# The HashTable should have an attribute called array of type: list, where all the values will be stored. Upon initialization the default length of the array should be 4. After each addition of an element if the HashTable gets too populated, double the length of the array and re-add the existing data.
# You are not allowed to inherit any classes. Feel free to implement your own functionality (and unit tests) or to write the methods by yourself.
#
# Test Code
# table = HashTable()
#
# table["name"] = "Peter"
# table["age"] = 25
#
# print(table)
# print(table.get("name"))
# print(table["age"])
# print(len(table))
#
# Result
# <hash_table.HashTable object at 0x00000185F4F08580>
# Peter
# 25
# 4

from copy import copy


class HashTable:
    DEFAULT_CAPACITY = 4

    def __init__(self):
        self.data = [None] * self.DEFAULT_CAPACITY
        self.free_slots = self.DEFAULT_CAPACITY
        self.count = 0

    def add(self, key, value):
        if self.free_slots == 0:
            self.grow_data()

        idx = self.calc_idx(key)
        if self.data[idx] is None:
            self.data[idx] = [(key, value)]
            self.free_slots -= 1
            self.count += 1
            return

        for k, v in self.data[idx]:
            if k == key:
                raise KeyError(f"{key} already exists")

        self.data[idx].append((key, value))
        self.count += 1

    def get(self, key):
        try:
            idx = self.calc_idx(key)
            idx_elements = self.data[idx]
            if idx_elements is None:
                raise KeyError

            for k, v in idx_elements:
                if k == key:
                    return v

            raise KeyError

        except KeyError:
            return "not found"

    def remove(self, key):
        idx = self.calc_idx(key)
        idx_elements = self.data[idx]
        if idx_elements is None:
            raise KeyError(f"{key} does not exist")

        for k, v in idx_elements:
            if k == key:
                self.data[idx].remove((k, v))
                self.count -= 1
                return

        raise KeyError(f"{key} does not exist")

    def items(self):
        result = []
        for slot in self.data:
            if slot is None:
                continue
            result.extend(slot)
        return result

    def __getitem__(self, key):
        return self.get(key)

    def __setitem__(self, key, value):
        try:
            old_value = self.get(key)
            idx = self.calc_idx(key)
            self.data[idx].remove((key, old_value))
            self.data[idx].append((key, value))
        except Exception:
            self.add(key, value)

        # old_value = self.get(key)
        # if old_value != "not found":
        #     idx = self.calc_idx(key)
        #     self.data[idx].remove((key, old_value))
        #     self.data[idx].append((key, value))
        # else:
        #     self.add(key, value)

    def __len__(self):
        return len(self.data)

    def get_number_of_elements(self):
        return self.count

    def get_max_len(self):
        result = float("-inf")
        for slot in self.data:
            if slot is None:
                continue
            if len(slot) > result:
                result = len(slot)
        return result

    def get_table_slots(self):
        result = "\n".join(str(slot) for slot in self.data)
        return result

    def calc_idx(self, key):
        return hash(key) % len(self.data)

    def grow_data(self):
        new_capacity = len(self.data) * 2

        existing_data = copy(self.data)

        self.free_slots = new_capacity
        self.data = [None] * new_capacity
        self.count = 0

        for slot in existing_data:
            for key, value in slot:
                self.add(key, value)


# hash_table = HashTable()
#
# print("\n" + "-" * 36 + " Hash table overview " + "-" * 36)
# print("\n" + " " * 24 + f" obj - {hash_table}")
#
# print("\n" + "-" * 39 + " adding elements " + "-" * 39 + "\n")
# hash_table.add("a", 15)
# hash_table.add("b", 16)
# hash_table.add("c", 19)
# hash_table.add("d", 23)
# hash_table.add("f", 23)
# hash_table.add("e", 30)
# print(f"Hash table items: {hash_table.items()}")
#
# print("\n" + "-" * 33 + " removing and getting \"e\" " + "-" * 33 + "\n")
# hash_table.remove("e")
# print(f'e: {hash_table.get("e")}')
# print(f"Hash table items: {hash_table.items()}")
#
# print("\n" + "-" * 39 + " setting \"d\" " + "-" * 39 + "\n")
# print(f'd current value: {hash_table.get("d")}')
# hash_table.__setitem__("d", 27)
# print(f'd value after set up: {hash_table.get("d")}')
# print(f"Hash table items: {hash_table.items()}")
#
# print("\n" + "-" * 39 + " getting items " + "-" * 39 + "\n")
# print(f'f: {hash_table.get("f")}')
# print(f'e: {hash_table.get("e")}')
# print(f'x: {hash_table.get("x")}')
# print(f"Hash table items: {hash_table.items()}")
#
# print("\n" + "-" * 39 + " hash table info " + "-" * 39 + "\n")
# print(f"Hash table slots ( with __len__ ) are: {hash_table.__len__()}")
# print(f"Hash table slots ( with len() ) are: {len(hash_table)}")
# print(f"Hash table elements are: {hash_table.get_number_of_elements()}")
# print(f"Max elements per slot are: {hash_table.get_max_len()}")
#
# print("\n" + "-" * 39 + " hash table slots " + "-" * 39 + "\n")
# print(hash_table.get_table_slots())


# hash_table = HashTable()
#
# for i in range(99):
#     hash_table.add(f"{i}", i)
#
# print("\n" + "-" * 36 + " Hash table slots filling " + "-" * 36)
# print("Element can be found with very few iterations, only the iterations needed to cover the needed slot")
# print("    - For 99 elements, max elements per slot are around 8")
# print("    - For 999 elements, max elements per slot are around 10")
# print("    - For 9,999 elements, max elements per slot are around 16")
# print("    - For 99,999 elements, max elements per slot are around 20")
# print("    - For 999,999 elements, max elements per slot are around 23")
#
# print("\n" + "-" * 39 + " hash table info " + "-" * 39 + "\n")
# print(f"Hash table slots are: {len(hash_table)}")
# print(f"Hash table elements are: {hash_table.get_number_of_elements()}")
# print(f"Max elements per slot are: {hash_table.get_max_len()}")
#
# print("\n" + "-" * 33 + " hash table slots " + "-" * 33 + "\n")
# print(hash_table.get_table_slots())


# hash_table = HashTable()
#
# print("\n" + "-" * 36 + " Indices and hash values in hash table " + "-" * 36)
# print("\n" + " " * 24 + f" obj - {hash_table}")
#
# print("\n" + "-" * 39 + " adding elements " + "-" * 39 + "\n")
# hash_table.add("a", 15)
# hash_table.add("b", 16)
# hash_table.add("c", 19)
# hash_table.add("d", 23)
# hash_table.add("f", 23)
# hash_table.add("e", 30)
# print(f"Hash table items: {hash_table.items()}")
#
# print("\n" + "-" * 9 + " element index and hash value change but stay the same during one program run " + "-" * 9 + "\n")
# print(f'Index = {hash_table.calc_idx("b")}')
# print(f'Hash = {hash("b")}')
# print(f'Index = {hash_table.calc_idx("b")}')
# print(f'Hash = {hash("b")}')
# print(f'Index = {hash_table.calc_idx("b")}')
# print(f'Hash = {hash("b")}')


table = HashTable()

table["name"] = "Peter"
table["age"] = 25

print(table)
print(table.get("name"))
print(table["age"])
print(len(table))
