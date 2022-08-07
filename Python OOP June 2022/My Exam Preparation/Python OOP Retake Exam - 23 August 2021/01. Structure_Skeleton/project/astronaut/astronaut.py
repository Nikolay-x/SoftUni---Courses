from abc import ABC, abstractmethod


class Astronaut(ABC):
    _BREATHE_UNITS = 10

    def __init__(self, name: str, oxygen: int):
        self.name = name
        self.oxygen = oxygen
        self.backpack = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value is None or value == "" or value.isspace():
            raise ValueError("Astronaut name cannot be empty string or whitespace!")
        self.__name = value

    @abstractmethod
    def breathe(self):
        self.oxygen -= 10
        return self.oxygen

    def increase_oxygen(self, amount: int):
        self.oxygen += amount
        return self.oxygen

    @property
    def breaths_left(self):
        return self.oxygen // self.__class__._BREATHE_UNITS
