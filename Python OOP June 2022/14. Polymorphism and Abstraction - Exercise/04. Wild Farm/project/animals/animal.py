from abc import ABC, abstractmethod
from project.food import Food


class Animal(ABC):
    def __init__(self, name, weight, food_eaten=0):
        self.name = name
        self.weight = weight
        self.food_eaten = food_eaten

    @abstractmethod
    def make_sound(self):
        pass

    @property
    @abstractmethod
    def preferred_food(self):
        pass

    @property
    @abstractmethod
    def weight_increase(self):
        pass

    def feed(self, food: Food):
        food_name = food.__class__.__name__
        if food_name not in self.preferred_food:
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"
        self.weight += self.weight_increase * food.quantity
        self.food_eaten += food.quantity


class Bird(Animal, ABC):
    def __init__(self, name, weight, wing_size):
        super().__init__(name, weight)
        self.wing_size = wing_size

    @abstractmethod
    def make_sound(self):
        pass

    def __repr__(self):
        return f"{self.__class__.__name__} [{self.name}, {self.wing_size}, {self.weight}, {self.food_eaten}]"


class Mammal(Animal, ABC):
    def __init__(self, name, weight, living_region):
        super().__init__(name, weight)
        self.living_region = living_region

    @abstractmethod
    def make_sound(self):
        pass

    def __repr__(self):
        return f"{self.__class__.__name__} [{self.name}, {self.weight}, {self.living_region}, {self.food_eaten}]"
