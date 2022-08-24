from project.meals.dessert import Dessert
from project.meals.main_dish import MainDish
from project.meals.meal import Meal
from project.client import Client
from project.meals.starter import Starter


class FoodOrdersApp:
    receipt_id = 0

    def __init__(self):
        self.menu = []
        self.clients_list = []

    def register_client(self, client_phone_number: str):
        for cl in self.clients_list:
            if cl.phone_number == client_phone_number:
                raise Exception("The client has already been registered!")
        client = Client(client_phone_number)
        self.clients_list.append(client)
        return f"Client {client_phone_number} registered successfully."

    def add_meals_to_menu(self, *meals: Meal):
        for meal in meals:
            if meal.__class__.__name__ == "Starter" or \
                    meal.__class__.__name__ == "MainDish" or \
                    meal.__class__.__name__ == "Dessert":
                self.menu.append(meal)

    def show_menu(self):
        if len(self.menu) < 5:
            raise Exception("The menu is not ready!")
        result = ""
        for meal in self.menu:
            result += meal.details() + "\n"
        return result.strip()

    def add_meals_to_shopping_cart(self, client_phone_number: str, **meal_names_and_quantities):
        if len(self.menu) < 5:
            raise Exception("The menu is not ready!")

        client = self.find_client_by_number(client_phone_number)

        if client is None:
            self.register_client(client_phone_number)
        client = self.find_client_by_number(client_phone_number)

        meals_to_order = []
        current_bill = 0

        for meal_name, quantity in meal_names_and_quantities.items():
            menu_meal = self.find_meal_by_name(meal_name)
            if menu_meal is None:
                raise Exception(f"{meal_name} is not on the menu!")

            price = menu_meal.price

            if quantity > menu_meal.quantity:
                raise Exception(f"Not enough quantity of {menu_meal.__class__.__name__}: "
                                f"{meal_name}!")

            meal = None
            if menu_meal.__class__.__name__ == "Starter":
                meal = Starter(meal_name, price, quantity)
            elif menu_meal.__class__.__name__ == "MainDish":
                meal = MainDish(meal_name, price, quantity)
            elif menu_meal.__class__.__name__ == "Dessert":
                meal = Dessert(meal_name, price, quantity)

            meals_to_order.append(meal)
            current_bill += meal.price * quantity

        client.shopping_cart.extend(meals_to_order)
        client.bill += current_bill

        for meal in meals_to_order:
            menu_meal = self.find_meal_by_name(meal.name)
            menu_meal.quantity -= meal.quantity

        return f"Client {client_phone_number} successfully ordered " \
               f"{', '.join([m.name for m in client.shopping_cart])} for " \
               f"{client.bill:.2f}lv."

    def cancel_order(self, client_phone_number: str):
        client = self.find_client_by_number(client_phone_number)
        if len(client.shopping_cart) == 0:
            raise Exception("There are no ordered meals!")

        for meal in client.shopping_cart:
            menu_meal = self.find_meal_by_name(meal.name)
            menu_meal.quantity += meal.quantity

        client.shopping_cart = []
        client.bill = 0
        return f"Client {client_phone_number} successfully canceled his order."

    def finish_order(self, client_phone_number: str):
        client = self.find_client_by_number(client_phone_number)
        if len(client.shopping_cart) == 0:
            raise Exception("There are no ordered meals!")

        total_paid_money = client.bill

        client.shopping_cart = []
        client.bill = 0
        self.receipt_id += 1

        return f"Receipt #{self.receipt_id} with total amount of {total_paid_money:.2f} " \
               f"was successfully paid for {client_phone_number}."

    def __str__(self):
        return f"Food Orders App has {len(self.menu)} meals on the menu and {len(self.clients_list)} clients."

    def find_meal_by_name(self, meal_name):
        for m in self.menu:
            if m.name == meal_name:
                return m
        return None

    def find_client_by_number(self, client_phone_number):
        for c in self.clients_list:
            if c.phone_number == client_phone_number:
                return c
        return None
