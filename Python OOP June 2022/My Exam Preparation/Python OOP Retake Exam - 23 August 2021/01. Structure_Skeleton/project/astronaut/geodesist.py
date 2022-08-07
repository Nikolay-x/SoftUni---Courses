from project.astronaut.astronaut import Astronaut


class Geodesist(Astronaut):
    DEFAULT_OXYGEN = 50

    def __init__(self, name: str):
        super().__init__(name, self.DEFAULT_OXYGEN)

    def breathe(self):
        self.oxygen -= 10
        return self.oxygen
