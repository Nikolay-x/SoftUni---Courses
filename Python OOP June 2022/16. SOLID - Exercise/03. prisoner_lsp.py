# 3.Prisoner
# You are provided with a code containing a class Prisoner and a class Person. A prisoner is obviously a person, but since a prisoner is not free to move an arbitrary distance, the Person class can be named FreePerson, then the idea that a Prisoner inherits FreePerson is wrong. Rewrite the code and apply the LSP (Liskov Substitution Principle).
#
# import copy
#
#
# class Person:
#
#     def __init__(self, position):
#         self.position = position
#
#     def walk_north(self, dist):
#         self.position[1] += dist
#
#     def walk_east(self, dist):
#         self.position[0] += dist
#
#
# class Prisoner(Person):
#     PRISON_LOCATION = [3, 3]
#
#     def __init__(self):
#         super(Prisoner, self).__init__(copy.copy(self.PRISON_LOCATION))
#         self.is_free = False
#
#
# prisoner = Prisoner()
# print("The prisoner trying to walk to north by 10 and east by -3.")
#
# try:
#     prisoner.walk_north(10)
#     prisoner.walk_east(-3)
# except:
#     pass
#
# print(f"The location of the prison: {prisoner.PRISON_LOCATION}")
# print(f"The current position of the prisoner: {prisoner.position}")
#
#
# Before
# prisoner = Prisoner()
# print("The prisoner trying to walk to north by 10 and east by -3.")
#
# try:
#     prisoner.walk_north(10)
#     prisoner.walk_east(-3)
# except:
#     pass
#
# print(f"The location of the prison: {prisoner.PRISON_LOCATION}")
# print(f"The current position of the prisoner: {prisoner.position}")
#
# After
# prisoner = Prisoner()
# print("The prisoner trying to walk to north by 10 and east by -3.")
#
# try:
#     prisoner.walk_north(10)
#     prisoner.walk_east(-3)
# except:
#     pass
#
# print(f"The location of the prison: {prisoner.PRISON_LOCATION}")
# print(f"The current position of the prisoner: {prisoner.position}")
#
# Result Before
# The prisoner trying to walk to north by 10 and east by -3.
# The location of the prison: [3, 3]
# The current position of the prisoner: [0, 13]
#
# Result After
# The prisoner trying to walk to north by 10 and east by -3.
# The location of the prison: (3, 3)
# The current position of the prisoner: (3, 3)

import copy


class Person:
    def __init__(self, position, is_free):
        self.position = position
        self.is_free = is_free

    def walk_north(self, dist):
        if self.is_free:
            self.position[0] += dist

    def walk_east(self, dist):
        if self.is_free:
            self.position[1] += dist


class FreePerson(Person):
    def __init__(self, position):
        super().__init__(position, is_free=True)


class Prisoner(Person):
    PRISON_LOCATION = [3, 3]

    def __init__(self):
        super().__init__(position=self.PRISON_LOCATION, is_free=False)


prisoner = Prisoner()
print("The prisoner trying to walk to north by 10 and east by -3.")

try:
    prisoner.walk_north(10)
    prisoner.walk_east(-3)
except:
    pass

print(f"The location of the prison: {prisoner.PRISON_LOCATION}")
print(f"The current position of the prisoner: {prisoner.position}")

# print()
#
# free_person = FreePerson([3, 3])
# print("The free person trying to walk to north by 10 and east by -3.")
# initial_location = f"[{free_person.position[0]}, {free_person.position[1]}]"
#
# try:
#     free_person.walk_north(10)
#     free_person.walk_east(-3)
# except:
#     pass
#
# print(f"The initial location of the free person: {initial_location}")
# print(f"The current position of the free person: {free_person.position}")
