from abc import ABC, abstractmethod

from project.baked_food.baked_food import BakedFood
from project.drink.drink import Drink


class Table(ABC):
    _MIN_NUMBER = 1
    _MAX_NUMBER = 100
    _TABLE_CLASS = 'None'

    @abstractmethod
    def __init__(self, table_number: int, capacity: int):
        self.table_number = table_number
        self.capacity = capacity
        self.food_orders = []
        self.drink_orders = []
        self.number_of_people = 0
        self.is_reserved = False

    @property
    def capacity(self):
        return self.__capacity

    @capacity.setter
    def capacity(self, value):
        if value <= 0:
            raise ValueError("Capacity has to be greater than 0!")
        self.__capacity = value

    @property
    def table_number(self):
        return self.__table_number

    @table_number.setter
    def table_number(self, value):
        min_num, max_num = self.__class__._MIN_NUMBER, self.__class__._MAX_NUMBER
        err_msg = f"{self.__class__._TABLE_CLASS} table's number must be between {min_num} and {max_num} inclusive!"
        if self.__class__._MIN_NUMBER > value or value > self.__class__._MAX_NUMBER:
            raise ValueError(err_msg)
        self.__table_number = value

    def reserve(self, number_of_people: int):
        if not self.is_reserved and number_of_people <= self.capacity:
            self.number_of_people = number_of_people
            self.is_reserved = True

    def order_food(self, baked_food: BakedFood):
        self.food_orders.append(baked_food)

    def order_drink(self, drink: Drink):
        self.drink_orders.append(drink)

    def get_bill(self):
        food_bill = sum(f.price for f in self.food_orders)
        drink_bill = sum(d.price for d in self.drink_orders)
        bill = food_bill + drink_bill
        return bill

    def clear(self):
        self.number_of_people = 0
        self.food_orders.clear()
        self.drink_orders.clear()
        self.is_reserved = False

    def free_table_info(self):
        if not self.is_reserved:
            result = f"Table: {self.table_number}" \
                     f"\nType: {self.__class__.__name__}" \
                     f"\nCapacity: {self.capacity}"
            return result
