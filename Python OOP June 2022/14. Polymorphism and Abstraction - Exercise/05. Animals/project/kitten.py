from project.cat import Cat


class Kitten(Cat):
    GENDER = "Female"

    def __init__(self, name, age, gender=GENDER):
        super().__init__(name, age, gender)

    def make_sound(self):
        return "Meow"
