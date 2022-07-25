# 3.Countdown Iterator
# Create a class called countdown_iterator. Upon initialization, it should receive a count. Implement the iterator to return each countdown number (from count to 0 inclusive), separated by a single space.
# Note: Submit only the class in the judge system
#
# Test Code
# iterator = countdown_iterator(10)
# for item in iterator:
#     print(item, end=" ")
#
# Output
# 10 9 8 7 6 5 4 3 2 1 0

class countdown_iterator:
    def __init__(self, count):
        self.count = count

    def __iter__(self):
        return self

    def __next__(self):
        if self.count < 0:
            raise StopIteration
        value = self.count
        self.count -= 1
        return value


iterator = countdown_iterator(10)
for item in iterator:
    print(item, end=" ")

print()

iterator = countdown_iterator(0)
for item in iterator:
    print(item, end=" ")
