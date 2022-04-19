# 8.* Vehicle
# Create a class Vehicle. The __init__ method should receive a type, a model, and a price. You should also set an owner to None. The class should have the following methods:
# buy(money: int, owner: str)
# oIf the person has enough money and the vehicle has no owner, returns: "Successfully bought a {type}. Change: {change}" and sets the owner to the given one
# oIf the money is not enough, return: "Sorry, not enough money"
# oIf the car already has an owner, return: "Car already sold"
# sell()
# oIf the car has an owner, set it to None again.
# oOtherwise, return: "Vehicle has no owner"
# __repr__()
# oIf the vehicle has an owner, returns: "{model} {type} is owned by: {owner}".
# oOtherwise, return: "{model} {type} is on sale: {price}"
#
# Test Code
# vehicle_type = "car"
# model = "BMW"
# price = 30000
# vehicle = Vehicle(vehicle_type, model, price)
# print(vehicle.buy(15000, "Peter"))
# print(vehicle.buy(35000, "George"))
# print(vehicle)
# vehicle.sell()
# print(vehicle)
#
# Output
# Sorry, not enough money
# Successfully bought a car. Change: 5000.00
# BMW car is owned by: George
# BMW car is on sale: 30000

class Vehicle:
    def __init__(self, car_type, model, price):
        self.type = car_type
        self.model = model
        self.price = price
        self.owner = None

    def buy(self, money: int, owner: str):
        if money >= self.price:
            if self.owner is None:
                self.owner = owner
                return f"Successfully bought a {self.type}. Change: {(money- self.price):.2f}"
            else:
                return "Car already sold"
        else:
            return "Sorry, not enough money"

    def sell(self):
        if self.owner is not None:
            self.owner = None
        else:
            return "Vehicle has no owner"

    def __repr__(self):
        if self.owner is not None:
            return f"{self.model} {self.type} is owned by: {self.owner}"
        else:
            return f"{self.model} {self.type} is on sale: {self.price}"


vehicle_type = "car"
input_model = "BMW"
input_price = 30000
vehicle = Vehicle(vehicle_type, input_model, input_price)
print(vehicle.buy(15000, "Peter"))
print(vehicle.buy(35000, "George"))
print(vehicle)
vehicle.sell()
print(vehicle)
