import unittest
from project.shopping_cart import ShoppingCart


class ShoppingCartTests(unittest.TestCase):
    SHOP_NAME = "Name"
    BUDGET = 0
    PRODUCTS = {}

    def setUp(self) -> None:
        self.shopping_cart = ShoppingCart(self.SHOP_NAME, self.BUDGET)

    def test_init(self):
        self.assertEqual(self.SHOP_NAME, self.shopping_cart.shop_name)
        self.assertEqual(self.BUDGET, self.shopping_cart.budget)
        self.assertEqual({}, self.shopping_cart.products)

    def test_shop_name_getter_setter__invalid_not_alpha(self):
        value = "New name"
        with self.assertRaises(ValueError) as error:
            self.shopping_cart.shop_name = value
        self.assertIsNotNone(error)
        self.assertEqual("Shop must contain only letters and must start with capital letter!", str(error.exception))

    def test_shop_name_getter_setter__invalid_not_capital_letter(self):
        value = "newname"
        with self.assertRaises(ValueError) as error:
            self.shopping_cart.shop_name = value
        self.assertIsNotNone(error)
        self.assertEqual("Shop must contain only letters and must start with capital letter!", str(error.exception))

    def test_shop_name_getter_setter__valid(self):
        value = "Newname"
        self.shopping_cart.shop_name = value
        self.assertEqual(value, self.shopping_cart.shop_name)

    def test_add_to_cart_product_price_gt_100__expect_to_raise(self):
        product_name = "product1"
        product_price = 101
        products = {}
        self.shopping_cart.products = products

        with self.assertRaises(ValueError) as error:
            self.shopping_cart.add_to_cart(product_name, product_price)
        self.assertIsNotNone(error)
        self.assertEqual(f"Product {product_name} cost too much!", str(error.exception))
        self.assertEqual(products, self.shopping_cart.products)

    def test_add_to_cart_product_price_e_100__expect_to_raise(self):
        product_name = "product1"
        product_price = 100
        products = {}
        self.shopping_cart.products = products

        with self.assertRaises(ValueError) as error:
            self.shopping_cart.add_to_cart(product_name, product_price)
        self.assertIsNotNone(error)
        self.assertEqual(f"Product {product_name} cost too much!", str(error.exception))
        self.assertEqual(products, self.shopping_cart.products)

    def test_add_to_cart_product_price_lt_100__expect_to_return(self):
        product_name = "product1"
        product_price = 99
        products = {}
        self.shopping_cart.products = products

        actual = self.shopping_cart.add_to_cart(product_name, product_price)

        self.assertEqual(f"{product_name} product was successfully added to the cart!", actual)
        self.assertEqual({'product1': 99}, self.shopping_cart.products)

    def test_remove_from_cart__product_in__expect_to_return(self):
        product_name = "product1"
        products = {'product1': 99, 'product2': 98, 'product3': 97}
        self.shopping_cart.products = products

        actual = self.shopping_cart.remove_from_cart(product_name)

        self.assertEqual(f"Product {product_name} was successfully removed from the cart!", actual)
        self.assertEqual({'product2': 98, 'product3': 97}, self.shopping_cart.products)

    def test_remove_from_cart__product__not_in__expect_to_raise(self):
        product_name = "product4"
        products = {'product1': 99, 'product2': 98, 'product3': 97}
        self.shopping_cart.products = products

        with self.assertRaises(ValueError) as error:
            self.shopping_cart.remove_from_cart(product_name)
        self.assertIsNotNone(error)
        self.assertEqual(f"No product with name {product_name} in the cart!", str(error.exception))
        self.assertEqual({'product1': 99, 'product2': 98, 'product3': 97}, self.shopping_cart.products)

    def test_add(self):
        products = {'product2': 98, 'product3': 97}
        self.shopping_cart.products = products

        other_shop_name = "Othername"
        other_budget = 3
        other_products = {'product1': 99}
        other_shopping_cart = ShoppingCart(other_shop_name, other_budget)
        other_shopping_cart.products = other_products

        new_shopping_cart = self.shopping_cart.__add__(other_shopping_cart)
        new_shop_name = new_shopping_cart.shop_name
        new_budget = new_shopping_cart.budget
        new_products = new_shopping_cart.products

        self.assertEqual("NameOthername", new_shop_name)
        self.assertEqual(3, new_budget)
        self.assertEqual({'product1': 99, 'product2': 98, 'product3': 97}, new_products)

    def test_buy_products_total_sum_gt_budget__expect_to_raise(self):
        products = {'product1': 3, 'product2': 5, 'product3': 4}
        budget = 10
        self.shopping_cart.products = products
        self.shopping_cart.budget = budget

        with self.assertRaises(ValueError) as error:
            self.shopping_cart.buy_products()
        self.assertIsNotNone(error)
        self.assertEqual(f"Not enough money to buy the products! Over budget with 2.00lv!", str(error.exception))
        self.assertEqual({'product1': 3, 'product2': 5, 'product3': 4}, self.shopping_cart.products)

    def test_buy_products_total_sum_e_budget__expect_to_return(self):
        products = {'product1': 3, 'product2': 5, 'product3': 4}
        budget = 12
        self.shopping_cart.products = products
        self.shopping_cart.budget = budget

        actual = self.shopping_cart.buy_products()

        self.assertEqual(f"Products were successfully bought! Total cost: 12.00lv.", actual)
        self.assertEqual({'product1': 3, 'product2': 5, 'product3': 4}, self.shopping_cart.products)

    def test_buy_products_total_sum_lt_budget__expect_to_return(self):
        products = {'product1': 2, 'product2': 5, 'product3': 4}
        budget = 12
        self.shopping_cart.products = products
        self.shopping_cart.budget = budget

        actual = self.shopping_cart.buy_products()

        self.assertEqual(f"Products were successfully bought! Total cost: 11.00lv.", actual)
        self.assertEqual({'product1': 2, 'product2': 5, 'product3': 4}, self.shopping_cart.products)


if __name__ == "__main__":
    unittest.main()
