from project.horse_specification.horse import Horse
from project.horse_specification.appaloosa import Appaloosa
from project.horse_specification.thoroughbred import Thoroughbred
from project.horse_race import HorseRace
from project.jockey import Jockey


class HorseRaceApp:
    def __init__(self):
        self.horses = []
        self.jockeys = []
        self.horse_races = []

    def add_horse(self, horse_type: str, horse_name: str, horse_speed: int):
        if horse_type == "Appaloosa":
            horse = Appaloosa(horse_name, horse_speed)
        elif horse_type == "Thoroughbred":
            horse = Thoroughbred(horse_name, horse_speed)
        else:
            return

        for h in self.horses:
            if h.name == horse_name:
                raise Exception(f"Horse {horse_name} has been already added!")

        if horse:
            self.horses.append(horse)
            return f"{horse_type} horse {horse_name} is added."

    def add_jockey(self, jockey_name: str, age: int):
        for j in self.jockeys:
            if j.name == jockey_name:
                raise Exception(f"Jockey {jockey_name} has been already added!")

        jockey = Jockey(jockey_name, age)
        self.jockeys.append(jockey)
        return f"Jockey {jockey_name} is added."

    def create_horse_race(self, race_type: str):
        for r in self.horse_races:
            if r.race_type == race_type:
                raise Exception(f"Race {race_type} has been already created!")

        race = HorseRace(race_type)
        self.horse_races.append(race)
        return f"Race {race_type} is created."

    def add_horse_to_jockey(self, jockey_name: str, horse_type: str):
        jockey = self.find_jockey_by_name(jockey_name)
        if jockey is None:
            raise Exception(f"Jockey {jockey_name} could not be found!")

        horse = self.find_last_available_horse(horse_type)
        if not horse:
            raise Exception(f"Horse breed {horse_type} could not be found!")

        if jockey.horse is not None:
            return f"Jockey {jockey_name} already has a horse."

        jockey.horse = horse
        horse.is_taken = True
        return f"Jockey {jockey_name} will ride the horse {horse.name}."

    def add_jockey_to_horse_race(self, race_type: str, jockey_name: str):
        race = None
        for r in self.horse_races:
            if r.race_type == race_type:
                race = r
        if race is None:
            raise Exception(f"Race {race_type} could not be found!")

        jockey = self.find_jockey_by_name(jockey_name)
        if jockey not in self.jockeys:
            raise Exception(f"Jockey {jockey_name} could not be found!")

        if jockey.horse is None:
            raise Exception(f"Jockey {jockey_name} cannot race without a horse!")

        if jockey in race.jockeys:
            return f"Jockey {jockey_name} has been already added to the {race_type} race."

        race.jockeys.append(jockey)
        return f"Jockey {jockey_name} added to the {race_type} race."

    def start_horse_race(self, race_type: str):
        race = None
        for r in self.horse_races:
            if r.race_type == race_type:
                race = r
        if race is None:
            raise Exception(f"Race {race_type} could not be found!")

        if len(race.jockeys) < 2:
            raise Exception(f"Horse race {race_type} needs at least two participants!")

        winner = None
        horse = None
        winner_speed = 0
        for j in race.jockeys:
            if j.horse.speed > winner_speed:
                winner = j
                winner_speed = j.horse.speed
                horse = j.horse

        return f"The winner of the {race_type} race, with a speed of {horse.speed}km/h " \
               f"is {winner.name}! Winner's horse: {horse.name}."

    def find_jockey_by_name(self, name):
        for j in self.jockeys:
            if j.name == name:
                return j
        return None

    def find_last_available_horse(self, h_type):
        for i in range(len(self.horses)-1, -1, -1):
            horse = self.horses[i]
            if horse.__class__.__name__ == h_type and not horse.is_taken:
                return horse
        return None
