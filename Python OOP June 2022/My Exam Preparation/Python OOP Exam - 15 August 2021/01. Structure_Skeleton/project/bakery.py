from project.baked_food.bread import Bread
from project.baked_food.cake import Cake
from project.drink.tea import Tea
from project.drink.water import Water
from project.table.inside_table import InsideTable
from project.table.outside_table import OutsideTable


class Bakery:
    def __init__(self, name: str):
        self.name = name
        self.food_menu = []
        self.drinks_menu = []
        self.tables_repository = []
        self.total_income = 0

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value == "" or value.isspace():
            raise ValueError("Name cannot be empty string or white space!")
        self.__name = value

    def add_food(self, food_type: str, name: str, price: float):
        if food_type in ("Bread", "Cake"):
            for f in self.food_menu:
                if f.name == name:
                    raise Exception(f"{food_type} {name} is already in the menu!")

            food = None
            if food_type == "Bread":
                food = Bread(name, price)
            elif food_type == "Cake":
                food = Cake(name, price)

            self.food_menu.append(food)
            return f"Added {name} ({food_type}) to the food menu"

    def add_drink(self, drink_type: str, name: str, portion: float, brand: str):
        if drink_type in ("Tea", "Water"):
            for d in self.drinks_menu:
                if d.name == name:
                    raise Exception(f"{drink_type} {name} is already in the menu!")

            drink = None
            if drink_type == "Tea":
                drink = Tea(name, portion, brand)
            elif drink_type == "Water":
                drink = Water(name, portion, brand)

            self.drinks_menu.append(drink)
            return f"Added {name} ({brand}) to the drink menu"

    def add_table(self, table_type: str, table_number: int, capacity: int):
        if table_type in ("InsideTable", "OutsideTable"):
            for t in self.tables_repository:
                if t.table_number == table_number:
                    raise Exception(f"Table {table_number} is already in the bakery!")

            table = None
            if table_type == "InsideTable":
                table = InsideTable(table_number, capacity)
            elif table_type == "OutsideTable":
                table = OutsideTable(table_number, capacity)

            self.tables_repository.append(table)
            return f"Added table number {table_number} in the bakery"

    def reserve_table(self, number_of_people: int):
        table = self.get_free_table(number_of_people)
        if table:
            table.reserve(number_of_people)
            return f"Table {table.table_number} has been reserved for {number_of_people} people"

        return f"No available table for {number_of_people} people"

    def order_food(self, table_number: int, *food_names):
        table = None
        for t in self.tables_repository:
            if t.table_number == table_number:
                table = t

        if not table:
            return f"Could not find table {table_number}"

        not_available_foods = []
        for food_name in food_names:
            food = self.find_food_by_name(food_name)
            if food:
                table.order_food(food)
            else:
                not_available_foods.append(food_name)

        result = f"Table {table_number} ordered:\n"
        result += "\n".join(repr(f) for f in table.food_orders) + "\n"
        result += f"{self.name} does not have in the menu:\n"
        result += "\n".join(f for f in not_available_foods)

        return result.strip()

    def order_drink(self, table_number: int, *drink_names):
        table = None
        for t in self.tables_repository:
            if t.table_number == table_number:
                table = t

        if not table:
            return f"Could not find table {table_number}"

        not_available_drinks = []
        for drink_name in drink_names:
            drink = self.find_drink_by_name(drink_name)
            if drink:
                table.order_drink(drink)
            else:
                not_available_drinks.append(drink_name)

        result = f"Table {table_number} ordered:\n"
        result += "\n".join(repr(d) for d in table.drink_orders) + "\n"
        result += f"{self.name} does not have in the menu:\n"
        result += "\n".join(d for d in not_available_drinks)

        return result.strip()

    def leave_table(self, table_number: int):
        table = None
        for t in self.tables_repository:
            if t.table_number == table_number:
                table = t

        bill = table.get_bill()
        self.total_income += bill
        table.clear()

        result = f"Table: {table_number}\n"
        result += f"Bill: {bill:.2f}"
        return result

    def get_free_tables_info(self):
        result = ""
        for t in self.tables_repository:
            if not t.is_reserved:
                result += t.free_table_info() + "\n"
        return result.strip()

    def get_total_income(self):
        return f"Total income: {self.total_income:.2f}lv"

    def find_food_by_name(self, food_name):
        for food in self.food_menu:
            if food.name == food_name:
                return food

    def find_drink_by_name(self, drink_name):
        for drink in self.drinks_menu:
            if drink.name == drink_name:
                return drink

    def get_free_table(self, number_of_people):
        for table in self.tables_repository:
            if table.capacity >= number_of_people and not table.is_reserved:
                return table
