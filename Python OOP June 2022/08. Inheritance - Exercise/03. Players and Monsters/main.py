# 3.Players and Monsters
# Your task is to create the following game hierarchy:
#
# Hero
#     -> Elf
#         -> MuseElf
#     -> Wizard
#         -> DarkWizard
#             -> SoulMaster
#     -> Knight
#         -> DarkKnight
#             -> BladeKnight
#
# Submit in judge a zip file containing a separate file for each of the classes using the structure shown below:
#
#     project
#         __init__.py
#         blade_knight.py
#         dark_knight.py
#         dark_wizard.py
#         elf.py
#         hero.py
#         knight.py
#         muse_elf.py
#         soul_master.py
#         wizard.py
#
# Create a class Hero. It should contain the following attributes:
# username: string
# level: int
# Override the __str__() method of the base class so it returns: "{name} of type {class_name} has level {level}"
#
# Test Code
# hero = Hero("H", 4)
# print(hero.username)
# print(hero.level)
# print(str(hero))
# elf = Elf("E", 4)
# print(str(elf))
# print(elf.__class__.__bases__[0].__name__)
# print(elf.username)
# print(elf.level)
#
# Output
# H
# 4
# H of type Hero has level 4
# E of type Elf has level 4
# Hero
# E
# 4

from project.hero import Hero
from project.elf import Elf
from project.soul_master import SoulMaster

hero = Hero("H", 4)
print(hero.username)
print(hero.level)
print(str(hero))
elf = Elf("E", 4)
print(str(elf))
print(elf.__class__.__bases__[0].__name__)
print(elf.username)
print(elf.level)
soul_master = SoulMaster("S_M", 69)
print(soul_master.__class__.__bases__[0].__name__)
print(soul_master)
