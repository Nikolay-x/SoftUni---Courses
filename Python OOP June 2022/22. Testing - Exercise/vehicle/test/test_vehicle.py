from project.vehicle import Vehicle
import unittest


class VehicleTests(unittest.TestCase):
    DEFAULT_FUEL_CONSUMPTION = 1.25
    FUEL = 100
    HORSE_POWER = 120

    def setUp(self) -> None:
        self.vehicle = Vehicle(self.FUEL, self.HORSE_POWER)

    def test_init__expect_correct_input(self):
        self.assertEqual(self.FUEL, self.vehicle.fuel)
        self.assertEqual(self.FUEL, self.vehicle.capacity)
        self.assertEqual(self.HORSE_POWER, self.vehicle.horse_power)
        self.assertEqual(self.DEFAULT_FUEL_CONSUMPTION, self.vehicle.fuel_consumption)

    def test_drive__expect_to_raise(self):
        kilometers = 100
        with self.assertRaises(Exception) as error:
            self.vehicle.drive(kilometers)
        self.assertEqual(self.FUEL, self.vehicle.fuel)
        self.assertEqual("Not enough fuel", str(error.exception))

    def test_drive_expect_fuel_reduce(self):
        kilometers = 10
        fuel_needed = self.DEFAULT_FUEL_CONSUMPTION * kilometers
        self.vehicle.drive(kilometers)
        actual_result = self.vehicle.fuel
        expected_result = self.FUEL - fuel_needed
        self.assertEqual(expected_result, actual_result)

    def test_refuel__expect_to_raise(self):
        with self.assertRaises(Exception) as error:
            self.vehicle.refuel(self.vehicle.capacity + 1)
        self.assertEqual("Too much fuel", str(error.exception))

    def test_refuel__expect_fuel_increase(self):
        fuel_amount = 20
        self.vehicle.fuel -= fuel_amount
        self.vehicle.refuel(fuel_amount)
        self.assertEqual(self.FUEL, self.vehicle.fuel)

    def test_str__expect_correct_output(self):
        actual_result = str(self.vehicle)
        expected_result = f"The vehicle has {self.HORSE_POWER} horse power " \
                          f"with {self.vehicle.fuel} fuel left and {self.vehicle.fuel_consumption} fuel consumption"
        self.assertEqual(expected_result, actual_result)


if __name__ == "__main__":
    unittest.main()
