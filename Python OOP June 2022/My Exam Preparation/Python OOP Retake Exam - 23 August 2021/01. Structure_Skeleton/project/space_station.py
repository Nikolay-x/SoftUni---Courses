from project.astronaut.biologist import Biologist
from project.astronaut.geodesist import Geodesist
from project.astronaut.meteorologist import Meteorologist
from project.planet.planet import Planet
from project.planet.planet_repository import PlanetRepository
from project.astronaut.astronaut_repository import AstronautRepository


class SpaceStation:
    def __init__(self):
        self.planet_repository = PlanetRepository()
        self.astronaut_repository = AstronautRepository()
        self.successful_missions = 0
        self.not_completed_missions = 0

    def add_astronaut(self, astronaut_type: str, name: str):
        for a in self.astronaut_repository.astronauts:
            if a.name == name:
                return f"{name} is already added."

        astronaut = None
        if astronaut_type == "Biologist" or \
                astronaut_type == "Geodesist" or \
                astronaut_type == "Meteorologist":

            if astronaut_type == "Biologist":
                astronaut = Biologist(name)
            elif astronaut_type == "Geodesist":
                astronaut = Geodesist(name)
            elif astronaut_type == "Meteorologist":
                astronaut = Meteorologist(name)

        else:
            raise Exception("Astronaut type is not valid!")

        if astronaut is not None:
            self.astronaut_repository.add(astronaut)
        return f"Successfully added {astronaut_type}: {name}."

    def add_planet(self, name: str, items: str):
        for p in self.planet_repository.planets:
            if p.name == name:
                return f"{name} is already added."

        items_list = items.split(", ")
        planet = Planet(name)
        planet.items.extend(items_list)

        self.planet_repository.add(planet)

        return f"Successfully added Planet: {name}."

    def retire_astronaut(self, name: str):
        astronaut = self.astronaut_repository.find_by_name(name)

        if astronaut not in self.astronaut_repository.astronauts:
            raise Exception(f"Astronaut {name} doesn't exist!")

        self.astronaut_repository.astronauts.remove(astronaut)

        return f"Astronaut {name} was retired!"

    def recharge_oxygen(self):
        for a in self.astronaut_repository.astronauts:
            a.oxygen += 10

    def send_on_mission(self, planet_name: str):

        planet = self.planet_repository.find_by_name(planet_name)

        if not planet:
            raise Exception("Invalid planet name!")

        mission_astronauts = self.astronaut_repository.find_top_five("oxygen")

        if len(mission_astronauts) == 0:
            raise Exception("You need at least one astronaut to explore the planet!")

        items = planet.items
        sent_to_explore = 0
        while mission_astronauts and items:
            current_astronaut = mission_astronauts.pop(0)
            sent_to_explore += 1
            while current_astronaut.breaths_left > 0 and items:
                item = items.pop()
                current_astronaut.backpack.append(item)
                current_astronaut.breathe()

        if items:
            self.not_completed_missions += 1
            return "Mission is not completed."

        self.successful_missions += 1
        return f"Planet: {planet_name} was explored. {sent_to_explore} " \
               f"astronauts participated in collecting items."

    def report(self):
        result = f"{self.successful_missions} successful missions!\n"
        result += f"{self.not_completed_missions} missions were not completed!\n"
        result += "Astronauts' info:\n"

        for a in self.astronaut_repository.astronauts:
            result += f"Name: {a.name}\n"
            result += f"Oxygen: {a.oxygen}\n"

            if a.backpack:
                result += f"Backpack items: {', '.join(str(x) for x in a.backpack)}\n"
            else:
                result += f'Backpack items: none\n'

        return result.strip()
