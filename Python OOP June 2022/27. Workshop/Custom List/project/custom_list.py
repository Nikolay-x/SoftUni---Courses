# Workshop Custom List
# Overview
# In this workshop, we are going to create a custom data structure, which has similar functionalities as the Python List and create unit tests for its functionalities. It will have the same functionalities as the original List:
# append(value) - Adds a value to the end of the list. Returns the list.
# remove(index) - Removes the value on the index. Returns the value removed.
# get(index) - Returns the value on the index.
# extend(iterable) - Appends the iterable to the list. Returns the new list.
# insert(index, value) - Adds the value on the specific index. Returns the list.
# pop() - Removes the last value and returns it.
# clear() - Removes all values, contained in the list.
# index(value) - Returns the index of the given value.
# count(value) - Returns the number of times the value is contained in the list.
# reverse() - Returns the values of the list in reverse order.
# copy() - Returns a copy of the list.
#
# We will also add our own custom functionalities:
# size() - Returns the length of the list.
# add_first(value) - Adds the value at the beginning of the list
# dictionize() - Returns the list as a dictionary: The keys will be each value on an even position and their values will be each value on an odd position. If the last value on an even position, it’s value will be " " (space)
# move(amount) - Move the first "amount" of values to the end of the list. Returns the list.
# sum() - Returns the sum of the list. If the value is not a number, add the length of the value to the overall number.
# overbound() - Returns the index of the biggest value. If the value is not a number, check it’s length.
# underbound() - Returns the index of the smallest value. If the value is not a number, check it’s length.
#
# Do not inherit List. Feel free to implement your own functionality (and unit tests) or to write the methods by yourself.

from collections.abc import Iterable, Hashable


class CustomList:
    def __init__(self):
        self.data = []

    def append(self, value):
        self.data.append(value)
        return self.data

    def remove(self, index):
        self.validate_index_is_valid(index, self.data)
        value = self.data.pop(index)
        return value

    def get(self, index):
        self.validate_index_is_valid(index, self.data)
        value = self.data[index]
        return value

    def extend(self, iterable):
        self.validate_if_object_is_iterable(iterable)
        self.data.extend(iterable)
        return self.data

    def insert(self, index, value):
        self.validate_index_is_valid_insert(index)
        self.data.insert(index, value)
        return self.data

    def pop(self):
        return self.data.pop()

    def clear(self):
        self.data.clear()

    def index(self, value):
        return self.data.index(value)

    def count(self, value):
        return self.data.count(value)

    def reverse(self):
        reversed_list = list(reversed(self.data))
        return reversed_list

    # def reverse(self):
    #     return self.data[::-1]

    # def reverse(self):
    #     self.data.reverse()
    #     return self.data

    def copy(self):
        copy_list = self.data.copy()
        return copy_list

    def size(self):
        return len(self.data)

    def add_first(self, value):
        self.data.insert(0, value)

    def dictionize(self):
        for el in self.data:
            if not isinstance(el, Hashable):
                return "One or more elements are not hashable."

        last_key = None
        last_value = " "
        if len(self.data) % 2 != 0:
            last_key = self.data[-1]
        result_dict = {}
        for i in range(0, len(self.data)-1, 2):
            result_dict[self.data[i]] = self.data[i+1]
        if last_key:
            result_dict[last_key] = last_value
        return result_dict

    def move(self, amount):
        if not isinstance(amount, int):
            raise TypeError("Amount must be int.")

        if amount > len(self.data):
            raise ValueError(f"There are not {amount} number of elements")

        self.data = self.data[amount:] + self.data[:amount]
        return self.data

    def sum(self):
        result = sum(el if type(el) == int or type(el) == float else len(el) for el in self.data)
        return result

    # def sum(self):
    #     result = 0
    #     for el in self.data:
    #         if type(el) == int:
    #             result += el
    #         elif type(el) == float:
    #             result += el
    #         else:
    #             result += len(el)
    #     return result

    def overbound(self):
        max_value = float("-inf")
        max_value_index = None
        for el in self.data:
            if type(el) == int:
                value = el
            elif type(el) == float:
                value = el
            else:
                if hasattr(el, "__len__"):
                    value = len(el)
                else:
                    raise ValueError("One or more invalid values.")
            if value > max_value:
                max_value = value
                max_value_index = self.data.index(el)
        return max_value_index

    def underbound(self):
        min_value = float("inf")
        min_value_index = None
        for el in self.data:
            if type(el) == int:
                value = el
            elif type(el) == float:
                value = el
            else:
                if hasattr(el, "__len__"):
                    value = len(el)
                else:
                    raise ValueError("One or more invalid values.")
            if value < min_value:
                min_value = value
                min_value_index = self.data.index(el)
        return min_value_index

    @staticmethod
    def validate_index_is_valid(index, input_list):
        if not isinstance(index, int):
            raise TypeError("Index must be integer.")

        if index <= -len(input_list) or index >= len(input_list):
            raise IndexError("Index out of range.")

    @staticmethod
    def validate_if_object_is_iterable(iterable):
        if not isinstance(iterable, Iterable):
            raise TypeError("Object must be iterable.")

    @staticmethod
    def validate_index_is_valid_insert(index):
        if not isinstance(index, int):
            raise TypeError("Index must be integer.")


cl = CustomList()
print(cl)
print(cl.__class__)
print(cl.__class__.__name__)
print()

print(cl.append(1))
print(cl.append(2))
print(cl.remove(1))
print(cl.data)
print()

print(cl.extend([2, 3, {"a": 1, "b": 2}]))
print(cl.insert(2, 4))
print(cl.pop())
print(cl.data)
print(cl.get(2))
print()

cl.clear()
print(cl.data)
print()

print(cl.extend(["abc", 2, 3, {"a": 1, "b": 2}]))
print(cl.append(3))
print(cl.append(3))
print(cl.append(3))
print(cl.index(3))
print(cl.count(3))
print(cl.count(5))
print(cl.data)
print(cl.reverse())
print(f"Copy: {cl.copy()}")
print()

print(cl.size())
print(cl.add_first(6))
print(cl.data)
print(cl.dictionize())
print(cl.remove(4))
print(cl.data)
print(cl.move(3))
print(cl.sum())
print(cl.overbound())
print(cl.underbound())
print()

print(cl.dictionize())
print(cl.data)
