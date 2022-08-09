import unittest

from project.train.train import Train


class TrainTests(unittest.TestCase):
    NAME = "Name1"
    CAPACITY = 3
    PASSENGERS = []

    def setUp(self) -> None:
        self.train = Train(self.NAME, self.CAPACITY)

    def test_init(self):
        self.assertEqual(self.NAME, self.train.name)
        self.assertEqual(self.CAPACITY, self.train.capacity)
        self.assertEqual([], self.train.passengers)

    def test_add_train_full(self):
        passengers = ["n1", "n2", "n3"]
        passenger_name = "n4"
        self.train.passengers = passengers
        with self.assertRaises(ValueError) as error:
            self.train.add(passenger_name)
        self.assertIsNotNone(error)
        self.assertEqual("Train is full", str(error.exception))
        self.assertEqual(passengers, self.train.passengers)

    def test_add_p_exists(self):
        passengers = ["n1", "n2"]
        passenger_name = "n1"
        self.train.passengers = passengers
        with self.assertRaises(ValueError) as error:
            self.train.add(passenger_name)
        self.assertIsNotNone(error)
        self.assertEqual("Passenger n1 Exists", str(error.exception))
        self.assertEqual(passengers, self.train.passengers)

    def test_add_p(self):
        passengers = ["n1", "n2"]
        passenger_name = "n3"
        self.train.passengers = passengers

        actual = self.train.add(passenger_name)
        self.assertEqual("Added passenger n3", actual)
        self.assertEqual(["n1", "n2", "n3"], self.train.passengers)

    def test_remove_p_not_exists(self):
        passengers = ["n1", "n2"]
        passenger_name = "n3"
        self.train.passengers = passengers

        with self.assertRaises(ValueError) as error:
            self.train.remove(passenger_name)
        self.assertIsNotNone(error)
        self.assertEqual("Passenger Not Found", str(error.exception))
        self.assertEqual(["n1", "n2"], self.train.passengers)

    def test_remove_p_exists(self):
        passengers = ["n1", "n2", "n3"]
        passenger_name = "n3"
        self.train.passengers = passengers

        actual = self.train.remove(passenger_name)
        self.assertEqual("Removed n3", actual)
        self.assertEqual(["n1", "n2"], self.train.passengers)


if __name__ == "__main__":
    unittest.main()
