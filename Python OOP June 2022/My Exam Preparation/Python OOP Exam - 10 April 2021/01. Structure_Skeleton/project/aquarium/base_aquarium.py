from abc import ABC, abstractmethod


class BaseAquarium(ABC):
    @abstractmethod
    def __init__(self, name: str, capacity: int):
        self.name = name
        self.capacity = capacity
        self.decorations = []
        self.fish = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value == "":
            raise ValueError("Aquarium name cannot be an empty string.")
        self.__name = value

    def calculate_comfort(self):
        comfort = sum(d.comfort for d in self.decorations)
        return comfort

    def add_fish(self, fish):
        if fish.__class__.__name__ == "FreshwaterFish" or fish.__class__.__name__ == "SaltwaterFish":
            if fish.habitat == self.__class__.__name__:
                if self.capacity > len(self.fish):
                    self.fish.append(fish)
                    return f"Successfully added {fish.__class__.__name__} to {self.__name}."
                else:
                    return "Not enough capacity."

    def remove_fish(self, fish):
        if fish in self.fish:
            self.fish.remove(fish)

    def add_decoration(self, decoration):
        self.decorations.append(decoration)

    def feed(self):
        for fish in self.fish:
            fish.eat()

    def __str__(self):
        result = f"{self.name}:\n"
        if self.fish:
            result += f'Fish: {" ".join(f.name for f in self.fish)}\n'
        else:
            result += "Fish: none\n"
        result += f"Decorations: {len(self.decorations)}\n"
        aquarium_comfort = self.calculate_comfort()
        result += f"Comfort: {aquarium_comfort}"

        return result
