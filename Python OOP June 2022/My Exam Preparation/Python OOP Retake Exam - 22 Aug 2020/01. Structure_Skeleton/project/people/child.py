class Child:
    def __init__(self, food_cost: int, *toys_cost):
        self.cost = food_cost + sum(toys_cost)

    def get_monthly_expense(self):
        monthly_cost = self.cost * 30
        return monthly_cost
