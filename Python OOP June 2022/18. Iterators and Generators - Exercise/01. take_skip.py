# 1.Take Skip
# Create a class called take_skip. Upon initialization, it should receive a step (int) and a count (int). Implement the __iter__ and __next__ functions. The iterator should return the count numbers (starting from 0) with the given step. For more clarification, see the examples:
# Note: Submit only the class in the judge system
#
# Test Code
# numbers = take_skip(2, 6)
# for number in numbers:
#     print(number)
#
# Output
# 0
# 2
# 4
# 6
# 8
# 10

class take_skip:
    def __init__(self, step, count):
        self.step = step
        self.count = count
        self.current_count = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current_count == self.count:
            raise StopIteration
        value_to_return = self.current_count * self.step
        self.current_count += 1
        return value_to_return


numbers = take_skip(2, 6)
for number in numbers:
    print(number)

numbers = take_skip(10, 5)
for number in numbers:
    print(number)
