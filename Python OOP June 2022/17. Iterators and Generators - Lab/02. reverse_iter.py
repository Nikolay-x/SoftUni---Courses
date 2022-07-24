# 2.Reverse Iter
# Create a class called reverse_iter which should receive an iterable upon initialization. Implement the __iter__ and __next__ methods, so the iterator returns the items of the iterable in reversed order.
# Note: Submit only the class in the judge system
#
# Test Code
# reversed_list = reverse_iter([1, 2, 3, 4])
# for item in reversed_list:
#     print(item)
#
# Output
# 4
# 3
# 2
# 1

class reverse_iter:
    def __init__(self, iterable):
        self.iterable = list(iterable)
        self.index = len(iterable) - 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < 0:
            raise StopIteration
        value_to_return = self.iterable[self.index]
        self.index -= 1
        return value_to_return


reversed_list = reverse_iter([1, 2, 3, 4])
# reversed_list = reverse_iter({1, 2, 3, 4})
for item in reversed_list:
    print(item)
