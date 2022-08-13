class Person:
    def __init__(self, name, age):
        self.name = name
        self.__age = age

    def __str__(self):
        return f"I am {self.name}, {self.__age} old."

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    def dif_inside_outside(self):
        return f"The difference between age inside class and age outside class is: {self.__age - self.age}"


print(f"{'-' * 18} General class info {'-' * 18}")

person = Person("Nikolay", 27)
print(person)
print(person.__class__)
print(person.__class__.__name__)
print()


print(f"{'-' * 18} Name and age change {'-' * 18}")
print(f"{'-' * 6} name is private attr with getter and setter {'-' * 6}")
print(f"{'-' * 12} age is private attr set with __ {'-' * 12}")
print(f"{person.name} - before change")

# print(f"{person.__age} - before change")  # AttributeError: 'Person' object has no attribute '__age'
# print(person.age)  # AttributeError: 'Person' object has no attribute 'age'
print(f"{person._Person__age} - before change")
person.name = "Ivan"
person.age = 24
# person._Person__age = 33
print(f"First way 'person.name': {person.name} - after change")
print(f"Second way 'person._Person__name': {person._Person__name} - after change")
print(f"{person._Person__age} - after change")
print()


print(f"{'-' * 18} __age vs age set outside class  {'-' * 18}")

print(f"{person._Person__age} inside class age vs {person.age} outside class age")
print(person.dif_inside_outside())
print()
