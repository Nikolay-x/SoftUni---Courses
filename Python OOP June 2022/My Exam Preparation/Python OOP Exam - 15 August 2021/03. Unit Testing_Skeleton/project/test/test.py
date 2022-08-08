import unittest

from project.pet_shop import PetShop


class PetShopTests(unittest.TestCase):
    NAME = "Name"
    FOOD = {}
    PETS = []

    def setUp(self) -> None:
        self.petshop = PetShop(self.NAME)

    def test_init(self):
        self.assertEqual(self.NAME, self.petshop.name)
        self.assertEqual({}, self.petshop.food)
        self.assertEqual([], self.petshop.pets)

    def test_add_food__qty_negative__raise(self):
        quantity = -5
        with self.assertRaises(ValueError) as error:
            self.petshop.add_food(self.NAME, quantity)
        self.assertIsNotNone(error)
        expected = "Quantity cannot be equal to or less than 0"
        self.assertEqual(expected, str(error.exception))

    def test_add_food__qty_positive_name_not_in_food__raise(self):
        food_name = "Food name"
        quantity = 5.345
        actual = self.petshop.add_food(food_name, quantity)
        expected = f"Successfully added {quantity:.2f} grams of {food_name}."
        self.assertEqual(expected, actual)
        self.assertEqual({'Food name': 5.345}, self.petshop.food)

    def test_add_food__qty_positive_name_in_food__raise(self):
        food_name = "Food name"
        quantity = 5.345
        self.petshop.add_food(food_name, quantity)

        quantity = 1
        actual = self.petshop.add_food(food_name, quantity)
        expected = f"Successfully added {quantity:.2f} grams of {food_name}."
        self.assertEqual(expected, actual)
        self.assertEqual({'Food name': 6.345}, self.petshop.food)

    def test_add_pet__name_not_in_pets(self):
        pet_name = "P"
        actual = self.petshop.add_pet(pet_name)
        expected = f"Successfully added {pet_name}."
        self.assertEqual(expected, actual)
        self.assertEqual(['P'], self.petshop.pets)

    def test_add_pet__name_in_pets__raise(self):
        pet_name = "P"
        self.petshop.add_pet(pet_name)
        with self.assertRaises(Exception) as error:
            self.petshop.add_pet(pet_name)
        self.assertIsNotNone(error)

        expected = f"Cannot add a pet with the same name"
        self.assertEqual(expected, str(error.exception))
        self.assertEqual(['P'], self.petshop.pets)

    def test_feed_pet__pet_name_not_in_pets__raise(self):
        food_name = "F name"
        pet_name = "P name"

        with self.assertRaises(Exception) as error:
            self.petshop.feed_pet(food_name, pet_name)
        self.assertIsNotNone(error)
        expected = f"Please insert a valid pet name"
        self.assertEqual(expected, str(error.exception))

    def test_feed_pet__food_name_not_in_food__return(self):
        food_name = "F name"
        pet_name = "P name"
        self.petshop.add_pet(pet_name)
        actual = self.petshop.feed_pet(food_name, pet_name)
        expected = f'You do not have {food_name}'
        self.assertEqual(expected, actual)

    def test_feed_pet__food_name_in_food_lt_100__return(self):
        food_name = "F name"
        pet_name = "P name"
        qty = 90
        self.petshop.add_food(food_name, qty)
        self.petshop.add_pet(pet_name)
        actual = self.petshop.feed_pet(food_name, pet_name)
        expected = f'Adding food...'
        self.assertEqual(expected, actual)
        self.assertEqual({'F name': 1090.0}, self.petshop.food)

    def test_feed_pet__food_name_in_food_gt_100__return(self):
        food_name = "F name"
        pet_name = "P name"
        qty = 300
        self.petshop.add_food(food_name, qty)
        self.petshop.add_pet(pet_name)
        actual = self.petshop.feed_pet(food_name, pet_name)
        expected = f"{pet_name} was successfully fed"
        self.assertEqual(expected, actual)
        self.assertEqual({'F name': 200}, self.petshop.food)

    def test_repr(self):
        food_name = "F name"
        pet_name = "P name"
        qty = 300
        self.petshop.add_food(food_name, qty)
        self.petshop.add_pet(pet_name)
        self.petshop.feed_pet(food_name, pet_name)
        actual = repr(self.petshop)
        expected = f'Shop {self.petshop.name}:\n' \
               f'Pets: {", ".join(self.petshop.pets)}'
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
