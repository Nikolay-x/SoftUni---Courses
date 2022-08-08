from project.baked_food.baked_food import BakedFood


class Bread(BakedFood):
    DEFAULT_PORTION_SIZE = 200

    def __init__(self, name: str, price: float):
        super().__init__(name, self.DEFAULT_PORTION_SIZE, price)
