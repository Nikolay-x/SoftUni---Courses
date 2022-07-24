# 3.Vowels
# Create a class called vowels, which should receive a string. Implement the __iter__ and __next__ methods, so the iterator returns only the vowels from the string.
# Note: Submit only the class in the judge system
#
# Test Code
# my_string = vowels('Abcedifuty0o')
# for char in my_string:
#     print(char)
#
# Output
# A
# e
# i
# u
# y
# o

class vowels:
    vowels = 'eyuioa'

    def __init__(self, string):
        self.string = string
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        while self.index < len(self.string):
            if self.string[self.index].lower() in self.vowels:
                value_to_return = self.string[self.index]
                self.index += 1
                return value_to_return
            self.index += 1

        raise StopIteration


my_string = vowels('Abcedifuty0o')
for char in my_string:
    print(char)
