# 2.Dictionary Iterator
# Create a class called dictionary_iter. Upon initialization, it should receive a dictionary object. Implement the iterator to return each key-value pair of the dictionary as a tuple of two elements (the key and the value).
# Note: Submit only the class in the judge system
#
# Test Code
# result = dictionary_iter({1: "1", 2: "2"})
# for x in result:
#     print(x)
#
# Output
# (1, '1')
# (2, '2')

class dictionary_iter:
    def __init__(self, obj_dict):
        self.obj_list = list(((key, pair) for key, pair in obj_dict.items()))
        # self.obj_list = list(obj_dict.items())
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index > len(self.obj_list) - 1:
            raise StopIteration
        value = self.obj_list[self.index]
        self.index += 1
        return value


result = dictionary_iter({1: "1", 2: "2"})
for x in result:
    print(x)

result = dictionary_iter({"name": "Peter", "age": 24})
for x in result:
    print(x)
