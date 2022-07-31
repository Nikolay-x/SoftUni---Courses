# 1.Test Worker
# Load provided skeleton in the IDE you use. Add new project Tests.
#
# class Worker:
#
#     def __init__(self, name, salary, energy):
#         self.name = name
#         self.salary = salary
#         self.energy = energy
#         self.money = 0
#
#     def work(self):
#         if self.energy <= 0:
#             raise Exception('Not enough energy.')
#
#         self.money += self.salary
#         self.energy -= 1
#
#     def rest(self):
#         self.energy += 1
#
#     def get_info(self):
#         return f'{self.name} has saved {self.money} money.'
#
# Create a class WorkerTests
# In judge you need to submit just the WokerTests class, with the unittest module imported.
# Create the following tests:
# Test if the worker is initialized with the correct name, salary, and energy
# Test if the worker's energy is incremented after the rest method is called
# Test if an error is raised if the worker tries to work with negative energy or equal to 0
# Test if the worker's money is increased by his salary correctly after the work method is called
# Test if the worker's energy is decreased after the work method is called
# Test if the get_info method returns the proper string with correct values

from lab_tasks.test_worker import Worker
import unittest


class WorkerTests(unittest.TestCase):
    NAME = "Test Worker"
    SALARY = 1024
    ENERGY = 3

    def setUp(self) -> None:
        self.worker = Worker(self.NAME, self.SALARY, self.ENERGY)

    def test__init__when_valid_input_expect_correct_values(self):
        self.assertEqual(self.NAME, self.worker.name)
        self.assertEqual(self.SALARY, self.worker.salary)
        self.assertEqual(self.ENERGY, self.worker.energy)

    def test__rest__expect_energy_incremented(self):
        self.worker.rest()
        self.assertEqual(self.ENERGY + 1, self.worker.energy)

    def test__work_with_negative_energy__expect_to_raise(self):
        self.worker.energy = 0
        with self.assertRaises(Exception) as context:
            self.worker.work()
        self.assertTrue('Not enough energy' in str(context.exception))

        self.worker.energy = -1
        with self.assertRaises(Exception) as context:
            self.worker.work()
        self.assertTrue('Not enough energy' in str(context.exception))

    def test_work__expect_money_increase_with_salary(self):
        self.worker.work()
        self.worker.work()
        self.assertEqual(self.SALARY * 2, self.worker.money)

    def test_work__expect_energy_decrease(self):
        self.worker.work()
        self.assertEqual(self.ENERGY - 1, self.worker.energy)

    def test_get_info__expect_correct_output(self):
        actual_info = self.worker.get_info()
        expected_info = f"{self.worker.name} has saved {self.worker.money} money."
        self.assertEqual(expected_info, actual_info)


if __name__ == "__main__":
    unittest.main()
