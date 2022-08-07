from project.astronaut.astronaut import Astronaut


class Biologist(Astronaut):
    DEFAULT_OXYGEN = 70
    _BREATHE_UNITS = 5

    def __init__(self, name: str):
        super().__init__(name, self.DEFAULT_OXYGEN)

    def breathe(self):
        self.oxygen -= 5
        return self.oxygen
