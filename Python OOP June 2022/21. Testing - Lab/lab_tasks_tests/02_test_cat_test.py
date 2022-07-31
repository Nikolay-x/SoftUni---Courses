# 2.Test Cat
#
# class Cat:
#
#   def __init__(self, name):
#     self.name = name
#     self.fed = False
#     self.sleepy = False
#     self.size = 0
#
#   def eat(self):
#     if self.fed:
#       raise Exception('Already fed.')
#
#     self.fed = True
#     self.sleepy = True
#     self.size += 1
#
#   def sleep(self):
#     if not self.fed:
#       raise Exception('Cannot sleep while hungry')
#
#     self.sleepy = False
#
# Create a class CatTests
# In judge you need to submit just the CatTests class, with the unitttest module imported.
# Create the following tests:
# Cat's size is increased after eating
# Cat is fed after eating
# Cat cannot eat if already fed, raises an error
# Cat cannot fall asleep if not fed, raises an error
# Cat is not sleepy after sleeping
# Hints
# Follow the logic of the previous problem

from lab_tasks.test_cat import Cat
import unittest


class CatTests(unittest.TestCase):
    NAME = "Test Cat"

    def setUp(self) -> None:
        self.cat = Cat(self.NAME)

    def test_eat__expect_cat_size_increase(self):
        self.cat.eat()
        self.assertEqual(1, self.cat.size)

    def test_eat__expect_cat_fed_true(self):
        self.cat.eat()
        self.assertTrue(self.cat.fed)

    def test_eat_while_fed__expect_raise_error(self):
        self.cat.eat()
        with self.assertRaises(Exception) as context:
            self.cat.eat()
        self.assertIsNotNone(context)
        self.assertEqual('Already fed.', str(context.exception))

    def test_sleep_while_not_fed__expect_to_raise(self):
        with self.assertRaises(Exception) as context:
            self.cat.sleep()
        self.assertIsNotNone(context)
        self.assertEqual('Cannot sleep while hungry', str(context.exception))

    def test_sleep__expect_sleepy_false(self):
        self.cat.eat()
        self.cat.sleep()
        self.assertFalse(self.cat.sleepy)


if __name__ == "__main__":
    unittest.main()
