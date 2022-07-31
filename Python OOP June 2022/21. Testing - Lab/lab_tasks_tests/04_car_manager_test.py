# 4.Car Manager
# You are provided with a simple project containing only one class - Car. The provided class is simple - its main point is to represent some of the functionality of a Car. Each car contains information about its make, model, fuel consumption, fuel amount, and fuel capacity. Also, each Car can add some fuel to its tank by refueling and can travel distance by driving. In order to be driven, our Car needs to have enough fuel. Everything in the provided skeleton is working perfectly fine, and you mustn't change it.
# Your job now is to write unit tests on the provided project and its functionality. You should test every part of the code inside the Car class:
# You should test the constructor
# You should test all the methods and validations inside the class
# Constraints
# Everything in the provided skeleton is working perfectly fine
# You must not change anything in the project structure
# Any part of validation should be tested
# There is no limit on the tests you can write but keep your attention on the main functionality
# Note: You are not allowed to change the structure of the provided code

from lab_tasks.car_manager import Car
import unittest


class CarTests(unittest.TestCase):

    def setUp(self) -> None:
        self.car = Car("Mercedes", "B-Class", 5, 50)
        self.car.refuel(10)

    def test_init__input__expect_correct_values(self):
        self.assertEqual("Mercedes", self.car.make)
        self.assertEqual("B-Class", self.car.model)
        self.assertEqual(5, self.car.fuel_consumption)
        self.assertEqual(50, self.car.fuel_capacity)
        self.assertEqual(10, self.car.fuel_amount)

    def test_all_attributes_name_mangled(self):
        self.assertTrue(hasattr(self.car, f"_{self.car.__class__.__name__}__make"))
        self.assertTrue(hasattr(self.car, f"_{self.car.__class__.__name__}__model"))
        self.assertTrue(hasattr(self.car, f"_{self.car.__class__.__name__}__fuel_consumption"))
        self.assertTrue(hasattr(self.car, f"_{self.car.__class__.__name__}__fuel_capacity"))
        self.assertTrue(hasattr(self.car, f"_{self.car.__class__.__name__}__fuel_amount"))

    def test_make_getter_and_setter__correct_values(self):
        self.car.make = "GAZ"
        self.assertEqual("GAZ", self.car.make)

    def test_make_setter__empty__expect_to_raise(self):
        with self.assertRaises(Exception) as error:
            self.car.make = ""
        self.assertEqual("Make cannot be null or empty!", str(error.exception))

    def test_model_getter_and_setter__correct_values(self):
        self.car.model = "Chaika"
        self.assertEqual("Chaika", self.car.model)

    def test_model_setter__empty__expect_to_raise(self):
        with self.assertRaises(Exception) as error:
            self.car.model = ""
        self.assertEqual("Model cannot be null or empty!", str(error.exception))

    def test_fuel_consumption_getter_and_setter__correct_values(self):
        self.car.fuel_consumption = 7
        self.assertEqual(7, self.car.fuel_consumption)

    def test_fuel_consumption_setter__zero__expect_to_raise(self):
        with self.assertRaises(Exception) as error:
            self.car.fuel_consumption = 0
        self.assertEqual("Fuel consumption cannot be zero or negative!", str(error.exception))

    def test_fuel_consumption_setter__negative__expect_to_raise(self):
        with self.assertRaises(Exception) as error:
            self.car.fuel_consumption = -3
        self.assertEqual("Fuel consumption cannot be zero or negative!", str(error.exception))

    def test_fuel_capacity_getter_and_setter__correct_values(self):
        self.car.fuel_capacity = 60
        self.assertEqual(60, self.car.fuel_capacity)

    def test_fuel_capacity_setter__zero__expect_to_raise(self):
        with self.assertRaises(Exception) as error:
            self.car.fuel_capacity = 0
        self.assertEqual("Fuel capacity cannot be zero or negative!", str(error.exception))

    def test_fuel_capacity_setter__negative__expect_to_raise(self):
        with self.assertRaises(Exception) as error:
            self.car.fuel_capacity = -6
        self.assertEqual("Fuel capacity cannot be zero or negative!", str(error.exception))

    def test_fuel_amount_getter_and_setter__correct_values(self):
        self.car.fuel_amount = 30
        self.assertEqual(30, self.car.fuel_amount)

    def test_fuel_amount_setter__negative__expect_to_raise(self):
        with self.assertRaises(Exception) as error:
            self.car.fuel_amount = -5
        self.assertEqual("Fuel amount cannot be negative!", str(error.exception))

    def test_refuel__zero__expect_to_raise(self):
        fuel = 0
        with self.assertRaises(Exception) as error:
            self.car.refuel(fuel)
        self.assertEqual("Fuel amount cannot be zero or negative!", str(error.exception))

    def test_refuel__negative__expect_to_raise(self):
        fuel = -8
        with self.assertRaises(Exception) as error:
            self.car.refuel(fuel)
        self.assertEqual("Fuel amount cannot be zero or negative!", str(error.exception))

    def test_refuel__correct_value__expect_correct_value(self):
        fuel = 10
        self.car.refuel(fuel)
        self.assertEqual(20, self.car.fuel_amount)

    def test_refuel__correct_value_greater_than_capacity__expect_correct_capacity(self):
        fuel = 50
        self.car.refuel(fuel)
        self.assertEqual(50, self.car.fuel_capacity)

    def test_drive__impossible_distance__expect_to_raise(self):
        distance = 300
        with self.assertRaises(Exception) as error:
            self.car.drive(distance)
        self.assertEqual("You don't have enough fuel to drive!", str(error.exception))

    def test_drive__possible_distance__expect_correct_fuel_amount(self):
        distance = 200
        self.car.drive(distance)
        self.assertEqual(0, self.car.fuel_amount)


if __name__ == "__main__":
    unittest.main()
