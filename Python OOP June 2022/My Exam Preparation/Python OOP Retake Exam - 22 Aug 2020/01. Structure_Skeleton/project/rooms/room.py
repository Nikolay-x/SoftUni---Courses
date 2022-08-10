class Room:
    _APPLIANCES = []
    _ROOM_COST = 0

    def __init__(self, family_name: str, budget: float, members_count: int):
        self.family_name = family_name
        self.budget = budget
        self.members_count = members_count
        self.expenses = 0

        self.room_cost = self.__class__._ROOM_COST

        self.children = []
        self.appliances = []

    @property
    def expenses(self):
        return self.__expenses

    @expenses.setter
    def expenses(self, value):
        if value < 0:
            raise ValueError("Expenses cannot be negative")
        self.__expenses = value

    @property
    def monthly_cost(self):
        return self.__expenses + self.room_cost

    def calculate_expenses(self, *args):
        self.expenses = Room.calculate_items_expenses(*args)

    @staticmethod
    def calculate_items_expenses(*args):
        return sum([el.get_monthly_expense() for arg in args for el in arg])
