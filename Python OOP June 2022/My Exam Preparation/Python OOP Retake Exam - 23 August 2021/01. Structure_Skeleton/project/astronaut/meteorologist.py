from project.astronaut.astronaut import Astronaut


class Meteorologist(Astronaut):
    DEFAULT_OXYGEN = 90
    _BREATHE_UNITS = 15

    def __init__(self, name: str):
        super().__init__(name, self.DEFAULT_OXYGEN)

    def breathe(self):
        self.oxygen -= 15
        return self.oxygen
