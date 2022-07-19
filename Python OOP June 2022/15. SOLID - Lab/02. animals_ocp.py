# 2.Animals
# Refactor the provided code, so you do not need to make any changes in it when you want to add new species to the animals' list
# Open/Closed
#
# class Animal:
#     def __init__(self, species):
#         self.species = species
#
#     def get_species(self):
#         return self.species
#
#
# def animal_sound(animals: list):
#     for animal in animals:
#         if animal.species == 'cat':
#             print('meow')
#         elif animal.species == 'dog':
#             print('woof-woof')
#
#
# animals = [Animal('cat'), Animal('dog')]
# animal_sound(animals)
#
# ## добавете ново животно и рефакторирайте кода да работи без да се налага да се правят промени по него
# ## при добавяне на нови животни
# # animals = [Animal('cat'), Animal('dog'), Animal('chicken')]

class Animal:
    def __init__(self, species):
        self.species = species
        self.sounds = {
            "cat": 'meow',
            "dog": 'woof-woof',
            "chicken": 'bwak'
        }

    def sound(self, name):
        return self.sounds[name]

    def get_species(self):
        return self.species


def animal_sound(class_animals: list):
    for animal in class_animals:
        if animal.species in animal.sounds:
            print(animal.sound(animal.species))


# animals = [Animal('cat'), Animal('dog')]
animals = [Animal('cat'), Animal('dog'), Animal('chicken')]

animal_sound(animals)
