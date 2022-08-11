import unittest

from project.factory.paint_factory import PaintFactory


class PaintFactoryTests(unittest.TestCase):
    NAME = "Name"
    CAPACITY = 10
    INGREDIENTS = {}
    VALID_INGREDIENTS = ["white", "yellow", "blue", "green", "red"]

    def setUp(self) -> None:
        self.paint_factory = PaintFactory(self.NAME, self.CAPACITY)
        self.valid_ingredients = self.VALID_INGREDIENTS

    def test_init(self):
        self.assertEqual(self.NAME, self.paint_factory.name)
        self.assertEqual(self.CAPACITY, self.paint_factory.capacity)
        self.assertEqual(self.INGREDIENTS, self.paint_factory.ingredients)
        self.assertEqual(self.VALID_INGREDIENTS, self.paint_factory.valid_ingredients)

    def test_can_add_True(self):
        self.paint_factory.capacity = 8
        self.paint_factory.ingredients = {"a": 2, "b": 4}
        actual = self.paint_factory.can_add(2)
        self.assertTrue(actual)

    def test_can_add_False(self):
        self.paint_factory.capacity = 8
        self.paint_factory.ingredients = {"a": 4, "b": 4}
        actual = self.paint_factory.can_add(1)
        self.assertFalse(actual)

    def test_add_ingredient_product_in_valid_ingredients_can_add_product_not_in_ingredients(self):
        self.paint_factory.capacity = 10
        self.paint_factory.ingredients = {"white": 4, "yellow": 4}
        product_type = "blue"
        product_quantity = 2
        self.paint_factory.add_ingredient(product_type, product_quantity)
        actual = self.paint_factory.ingredients
        expected = {'blue': 2, 'white': 4, 'yellow': 4}
        self.assertEqual(expected, actual)

    def test_add_ingredient_product_in_valid_ingredients_can_add_product_in_ingredients(self):
        self.paint_factory.capacity = 10
        self.paint_factory.ingredients = {"white": 4, "yellow": 4}
        product_type = "white"
        product_quantity = 2
        self.paint_factory.add_ingredient(product_type, product_quantity)
        actual = self.paint_factory.ingredients
        expected = {'white': 6, 'yellow': 4}
        self.assertEqual(expected, actual)

    def test_add_ingredient_product_in_valid_ingredients_cannot_add_product_in_ingredients(self):
        self.paint_factory.capacity = 10
        self.paint_factory.ingredients = {"white": 4, "yellow": 4}
        product_type = "white"
        product_quantity = 3
        with self.assertRaises(ValueError) as error:
            self.paint_factory.add_ingredient(product_type, product_quantity)

        self.assertIsNotNone(error)

        actual = self.paint_factory.ingredients
        expected = {'white': 4, 'yellow': 4}
        expected_msg = "Not enough space in factory"

        self.assertEqual(expected_msg, str(error.exception))
        self.assertEqual(expected, actual)

    def test_add_ingredient_product__not_in_valid_ingredients(self):
        self.paint_factory.capacity = 10
        self.paint_factory.ingredients = {"white": 4, "yellow": 4}
        product_type = "black"
        product_quantity = 1
        with self.assertRaises(TypeError) as error:
            self.paint_factory.add_ingredient(product_type, product_quantity)

        self.assertIsNotNone(error)

        actual = self.paint_factory.ingredients
        expected = {'white': 4, 'yellow': 4}
        expected_msg = "Ingredient of type black not allowed in PaintFactory"

        self.assertEqual(expected_msg, str(error.exception))
        self.assertEqual(expected, actual)

    def test_remove_ingredient_product_in_ingredients_product_valid_qty(self):
        self.paint_factory.capacity = 10
        self.paint_factory.ingredients = {"white": 4, "yellow": 4}
        product_type = "white"
        product_quantity = 2
        self.paint_factory.remove_ingredient(product_type, product_quantity)
        actual = self.paint_factory.ingredients
        expected = {'white': 2, 'yellow': 4}
        self.assertEqual(expected, actual)

    def test_remove_ingredient_product_in_ingredients_product_invalid_qty(self):
        self.paint_factory.capacity = 10
        self.paint_factory.ingredients = {"white": 4, "yellow": 4}
        product_type = "white"
        product_quantity = 5
        with self.assertRaises(ValueError) as error:
            self.paint_factory.remove_ingredient(product_type, product_quantity)
        self.assertIsNotNone(error)
        actual = self.paint_factory.ingredients
        expected = {'white': 4, 'yellow': 4}
        expected_msg = "Ingredients quantity cannot be less than zero"
        self.assertEqual(expected_msg, str(error.exception))
        self.assertEqual(expected, actual)

    def test_remove_ingredient_product__not_in_ingredients_product_invalid_qty(self):
        self.paint_factory.capacity = 10
        self.paint_factory.ingredients = {"white": 4, "yellow": 4}
        product_type = "black"
        product_quantity = 3
        with self.assertRaises(KeyError) as error:
            self.paint_factory.remove_ingredient(product_type, product_quantity)
        self.assertIsNotNone(error)
        actual = self.paint_factory.ingredients
        expected = {'white': 4, 'yellow': 4}
        expected_msg = "'No such ingredient in the factory'"
        self.assertEqual(expected_msg, str(error.exception))
        self.assertEqual(expected, actual)

    def test_products(self):
        self.paint_factory.capacity = 10
        self.paint_factory.ingredients = {"white": 4, "yellow": 4}

        actual = self.paint_factory.products
        expected = {'white': 4, 'yellow': 4}
        self.assertEqual(expected, actual)

    def test_repr(self):
        self.paint_factory.capacity = 10
        self.paint_factory.ingredients = {"white": 4, "yellow": 4}
        product_type = "white"
        product_quantity = 2
        self.paint_factory.remove_ingredient(product_type, product_quantity)
        actual = repr(self.paint_factory)
        expected = f"Factory name: {self.NAME} with capacity {self.paint_factory.capacity}.\n" \
                   "white: 2\n" \
                   "yellow: 4\n"
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
