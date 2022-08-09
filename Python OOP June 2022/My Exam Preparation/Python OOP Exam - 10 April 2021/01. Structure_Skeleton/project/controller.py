from project.aquarium.freshwater_aquarium import FreshwaterAquarium
from project.aquarium.saltwater_aquarium import SaltwaterAquarium
from project.decoration.decoration_repository import DecorationRepository
from project.decoration.ornament import Ornament
from project.decoration.plant import Plant
from project.fish.freshwater_fish import FreshwaterFish
from project.fish.saltwater_fish import SaltwaterFish


class Controller:
    def __init__(self):
        self.decorations_repository = DecorationRepository()
        self.aquariums = []

    def add_aquarium(self, aquarium_type: str, aquarium_name: str):
        if aquarium_type == "FreshwaterAquarium":
            aqua = FreshwaterAquarium(aquarium_name)
        elif aquarium_type == "SaltwaterAquarium":
            aqua = SaltwaterAquarium(aquarium_name)
        else:
            return "Invalid aquarium type."

        self.aquariums.append(aqua)
        return f"Successfully added {aquarium_type}."

    def add_decoration(self, decoration_type: str):
        if decoration_type == "Ornament":
            deco = Ornament()
        elif decoration_type == "Plant":
            deco = Plant()
        else:
            return "Invalid decoration type."

        self.decorations_repository.add(deco)
        return f"Successfully added {decoration_type}."

    def insert_decoration(self, aquarium_name: str, decoration_type: str):

        deco = self.decorations_repository.find_by_type(decoration_type)

        if deco == "None":
            return f"There isn't a decoration of type {decoration_type}."

        aqua = self.__find_aqua_by_name(aquarium_name)

        if aqua:
            aqua.add_decoration(deco)
            self.decorations_repository.decorations.remove(deco)
            return f"Successfully added {decoration_type} to {aquarium_name}."

    def add_fish(self, aquarium_name: str, fish_type: str, fish_name: str, fish_species: str, price: float):

        if fish_type == "FreshwaterFish":
            fish = FreshwaterFish(fish_name, fish_species, price)
        elif fish_type == "SaltwaterFish":
            fish = SaltwaterFish(fish_name, fish_species, price)
        else:
            return f"There isn't a fish of type {fish_type}."

        aqua = self.__find_aqua_by_name(aquarium_name)

        if aqua:
            result = aqua.add_fish(fish)
            if result:
                return result
            else:
                return "Water not suitable."

    def feed_fish(self, aquarium_name: str):
        aqua = self.__find_aqua_by_name(aquarium_name)
        if aqua:
            aqua.feed()
            return f"Fish fed: {len(aqua.fish)}"

    def calculate_value(self, aquarium_name: str):
        aqua = self.__find_aqua_by_name(aquarium_name)
        if aqua:
            fish_price = sum(f.price for f in aqua.fish)
            deco_price = sum(d.price for d in aqua.decorations)
            value = fish_price + deco_price
            return f"The value of Aquarium {aquarium_name} is {value:.2f}."

    def report(self):
        result = "\n".join(str(a) for a in self.aquariums)
        return result

    def __find_aqua_by_name(self, aquarium_name):
        for a in self.aquariums:
            if a.name == aquarium_name:
                return a
