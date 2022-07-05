# 5.Hierarchical Inheritance
# In a folder called project create three files: animal.py, dog.py, and cat.py.
# In each file, create its corresponding class - Animal, Dog, and Cat:
# Animal with a single method eat() that returns: "eating..."
# Dog with a single method bark() that returns: "barking..."
# Cat with a single method meow() that returns: "meowing..."
# Both Dog and Cat should inherit from Animal.
# Submit in Judge a zip file of the folder project.

from project.cat import Cat
from project.dog import Dog

cat = Cat()
dog = Dog()

print(cat.eat())
print(cat.meow())
print()
print(dog.eat())
print(dog.bark())
