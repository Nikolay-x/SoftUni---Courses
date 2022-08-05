import unittest

from project.plantation import Plantation


class PlantationTests(unittest.TestCase):
    SIZE = 5
    PLANTS = {}
    WORKERS = []

    def setUp(self) -> None:
        self.plantation = Plantation(self.SIZE)

    def test_init(self):
        self.assertEqual(self.SIZE, self.plantation.size)
        self.assertEqual({}, self.plantation.plants)
        self.assertEqual([], self.plantation.workers)

    def test_size_getter_setter_valid(self):
        value = 10
        self.plantation.size = value
        self.assertEqual(value, self.plantation.size)

    def test_size_getter_setter_invalid(self):
        value = -10
        with self.assertRaises(ValueError) as error:
            self.plantation.size = value
        self.assertIsNotNone(error)
        self.assertEqual("Size must be positive number!", str(error.exception))

    def test_hire_worker_valid(self):
        worker = "Worker"
        expected = f"{worker} successfully hired."
        actual = self.plantation.hire_worker(worker)
        self.assertEqual(expected, actual)

    def test_hire_worker_invalid(self):
        worker = "Worker"
        self.plantation.hire_worker(worker)
        with self.assertRaises(ValueError) as error:
            self.plantation.hire_worker(worker)
        self.assertIsNotNone(error)
        self.assertEqual("Worker already hired!", str(error.exception))

    def test_len(self):
        plants = {"worker1": ["plant1", "plant2"], "worker2": ["plant3"]}
        self.plantation.plants = plants
        actual = len(self.plantation)
        expected = 3
        self.assertEqual(expected, actual)

    def test_planting_valid_worker_not_in_workers_raise(self):
        plants = {"worker1": ["plant1", "plant2"], "worker2": ["plant3"]}
        self.plantation.plants = plants
        worker = "worker3"
        plant = "plant4"

        with self.assertRaises(ValueError) as error:
            self.plantation.planting(worker, plant)
        self.assertIsNotNone(error)
        self.assertEqual(f"Worker with name {worker} is not hired!", str(error.exception))

        expected_plants = {'worker1': ['plant1', 'plant2'], 'worker2': ['plant3']}
        self.assertEqual(expected_plants, self.plantation.plants)

    def test_planting_full_plantation_raise(self):
        size = 3
        self.plantation.size = size
        plants = {"worker1": ["plant1", "plant2"], "worker2": ["plant3"]}
        self.plantation.plants = plants
        worker = "worker2"
        self.plantation.hire_worker(worker)
        plant = "plant4"

        with self.assertRaises(ValueError) as error:
            self.plantation.planting(worker, plant)
        self.assertIsNotNone(error)
        self.assertEqual(f"The plantation is full!", str(error.exception))

        expected_plants = {'worker1': ['plant1', 'plant2'], 'worker2': ['plant3']}
        self.assertEqual(expected_plants, self.plantation.plants)

    def test_planting_valid_worker_not_in_plants(self):
        plants = {"worker1": ["plant1", "plant2"], "worker2": ["plant3"]}
        worker = "worker3"
        self.plantation.hire_worker(worker)
        plant = "plant4"
        self.plantation.plants = plants
        actual = self.plantation.planting(worker, plant)
        expected = "worker3 planted it's first plant4."
        expected_plants = {'worker1': ['plant1', 'plant2'], 'worker2': ['plant3'], 'worker3': ['plant4']}
        self.assertEqual(expected, actual)
        self.assertEqual(expected_plants, self.plantation.plants)

    def test_planting_valid_worker_in_plants(self):
        plants = {"worker1": ["plant1", "plant2"], "worker2": ["plant3"]}
        worker = "worker2"
        self.plantation.hire_worker(worker)
        plant = "plant4"
        self.plantation.plants = plants
        actual = self.plantation.planting(worker, plant)
        expected = "worker2 planted plant4."
        expected_plants = {'worker1': ['plant1', 'plant2'], 'worker2': ['plant3', 'plant4']}
        self.assertEqual(expected, actual)
        self.assertEqual(expected_plants, self.plantation.plants)

    def test_str(self):
        worker1 = "worker1"
        worker2 = "worker2"
        self.plantation.hire_worker(worker1)
        self.plantation.hire_worker(worker2)
        plants = {"worker1": ["plant1", "plant2"], "worker2": ["plant3"]}
        self.plantation.plants = plants
        expected = f"Plantation size: 5\n" \
                   f"worker1, worker2\n" \
                   f"worker1 planted: plant1, plant2\n" \
                   f"worker2 planted: plant3"
        actual = str(self.plantation)
        self.assertEqual(expected, actual)

    def test_repr(self):
        worker1 = "worker1"
        worker2 = "worker2"
        self.plantation.hire_worker(worker1)
        self.plantation.hire_worker(worker2)
        plants = {"worker1": ["plant1", "plant2"], "worker2": ["plant3"]}
        self.plantation.plants = plants
        expected = f'Size: {self.plantation.size}\n' \
                   f'Workers: {", ".join(self.plantation.workers)}'
        actual = repr(self.plantation)
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
