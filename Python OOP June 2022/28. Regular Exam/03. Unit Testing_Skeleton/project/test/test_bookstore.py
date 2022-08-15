import unittest
from project.bookstore import Bookstore


class BookstoreTests(unittest.TestCase):
    BOOKS_LIMIT = 12
    AVAILABILITY_IN_STORE_BY_BOOK_TITLES = {}
    TOTAL_SOLD_BOOKS = 0

    def setUp(self) -> None:
        self.bookstore = Bookstore(self.BOOKS_LIMIT)

    def test_init(self):
        self.assertEqual(self.BOOKS_LIMIT, self.bookstore.books_limit)
        self.assertEqual({}, self.bookstore.availability_in_store_by_book_titles)
        self.assertEqual(self.TOTAL_SOLD_BOOKS, self.bookstore.total_sold_books)

    def test_getter_total_sold_books(self):
        self.assertEqual(0, self.bookstore.total_sold_books)

    def test_getter_setter__books_limit__valid(self):
        value = 5
        self.bookstore.books_limit = value
        self.assertEqual(value, self.bookstore.books_limit)

    def test_getter_setter__books_limit__invalid_negative(self):
        value = -5
        with self.assertRaises(ValueError) as error:
            self.bookstore.books_limit = value
        self.assertIsNotNone(error)
        expected_msg = f"Books limit of {value} is not valid"
        self.assertEqual(expected_msg, str(error.exception))

    def test_getter_setter__books_limit__invalid_zero(self):
        value = 0
        with self.assertRaises(ValueError) as error:
            self.bookstore.books_limit = value
        self.assertIsNotNone(error)
        expected_msg = f"Books limit of {value} is not valid"
        self.assertEqual(expected_msg, str(error.exception))

    def test_len(self):
        avbl_in_store_by_book_titles = {"Book1": 5, "Book2": 6}
        self.bookstore.availability_in_store_by_book_titles = avbl_in_store_by_book_titles
        self.assertEqual(11, len(self.bookstore))

    def test_len_zero(self):
        avbl_in_store_by_book_titles = {}
        self.bookstore.availability_in_store_by_book_titles = avbl_in_store_by_book_titles
        self.assertEqual(0, len(self.bookstore))

    def test_receive_book__exceeding_books_limit(self):
        avbl_in_store_by_book_titles = {"Book1": 5, "Book2": 6}
        self.bookstore.availability_in_store_by_book_titles = avbl_in_store_by_book_titles

        book_title = "Book4"
        books_number = 2

        with self.assertRaises(Exception) as error:
            self.bookstore.receive_book(book_title, books_number)
        self.assertIsNotNone(error)
        expected_msg = "Books limit is reached. Cannot receive more books!"
        self.assertEqual(expected_msg, str(error.exception))
        self.assertEqual(avbl_in_store_by_book_titles, self.bookstore.availability_in_store_by_book_titles)

    def test_receive_book__not_exceeding_books_limit_book_not_in(self):
        avbl_in_store_by_book_titles = {"Book1": 3, "Book2": 3}
        self.bookstore.availability_in_store_by_book_titles = avbl_in_store_by_book_titles

        book_title = "Book3"
        books_number = 6

        actual = self.bookstore.receive_book(book_title, books_number)
        expected = "6 copies of Book3 are available in the bookstore."

        self.assertEqual(expected, actual)
        self.assertEqual({'Book1': 3, 'Book2': 3, 'Book3': 6}, self.bookstore.availability_in_store_by_book_titles)

    def test_receive_book__not_exceeding_books_limit_book_in(self):
        avbl_in_store_by_book_titles = {"Book1": 3, "Book2": 3}
        self.bookstore.availability_in_store_by_book_titles = avbl_in_store_by_book_titles

        book_title = "Book1"
        books_number = 6

        actual = self.bookstore.receive_book(book_title, books_number)
        expected = "9 copies of Book1 are available in the bookstore."

        self.assertEqual(expected, actual)
        self.assertEqual({'Book1': 9, 'Book2': 3}, self.bookstore.availability_in_store_by_book_titles)

    def test_sell_book__book_title_not_in__raise(self):
        avbl_in_store_by_book_titles = {'Book1': 3, 'Book2': 3, 'Book3': 2}
        self.bookstore.availability_in_store_by_book_titles = avbl_in_store_by_book_titles

        book_title = "Book4"
        books_number = 2
        with self.assertRaises(Exception) as error:
            self.bookstore.sell_book(book_title, books_number)
        self.assertIsNotNone(error)
        expected_msg = "Book Book4 doesn't exist!"
        self.assertEqual(expected_msg, str(error.exception))
        self.assertEqual({'Book1': 3, 'Book2': 3, 'Book3': 2}, self.bookstore.availability_in_store_by_book_titles)

    def test_sell_book__book_title_in_not_enough_books__raise(self):
        avbl_in_store_by_book_titles = {'Book1': 3, 'Book2': 3, 'Book3': 2}
        self.bookstore.availability_in_store_by_book_titles = avbl_in_store_by_book_titles

        book_title = "Book1"
        books_number = 4
        with self.assertRaises(Exception) as error:
            self.bookstore.sell_book(book_title, books_number)
        self.assertIsNotNone(error)
        expected_msg = "Book1 has not enough copies to sell. Left: 3"
        self.assertEqual(expected_msg, str(error.exception))
        self.assertEqual({'Book1': 3, 'Book2': 3, 'Book3': 2}, self.bookstore.availability_in_store_by_book_titles)

    def test_sell_book__book_title_in_enough_books__sell(self):
        avbl_in_store_by_book_titles = {'Book1': 3, 'Book2': 3, 'Book3': 2}
        self.bookstore.availability_in_store_by_book_titles = avbl_in_store_by_book_titles

        book_title = "Book1"
        books_number = 3
        actual = self.bookstore.sell_book(book_title, books_number)
        expected = "Sold 3 copies of Book1"
        self.assertEqual(expected, actual)
        self.assertEqual({'Book1': 0, 'Book2': 3, 'Book3': 2}, self.bookstore.availability_in_store_by_book_titles)
        self.assertEqual(3, self.bookstore.total_sold_books)

    def test_sell_book__book_title_in_enough_books__sell_2_times(self):
        avbl_in_store_by_book_titles = {'Book1': 3, 'Book2': 3, 'Book3': 2}
        self.bookstore.availability_in_store_by_book_titles = avbl_in_store_by_book_titles

        book_title = "Book1"
        books_number = 3
        actual = self.bookstore.sell_book(book_title, books_number)

        book_title = "Book2"
        books_number = 3
        actual = self.bookstore.sell_book(book_title, books_number)

        expected = "Sold 3 copies of Book2"
        self.assertEqual(expected, actual)
        self.assertEqual({'Book1': 0, 'Book2': 0, 'Book3': 2}, self.bookstore.availability_in_store_by_book_titles)
        self.assertEqual(6, self.bookstore.total_sold_books)

    def test_str(self):
        avbl_in_store_by_book_titles = {'Book1': 3, 'Book2': 3, 'Book3': 2}
        self.bookstore.availability_in_store_by_book_titles = avbl_in_store_by_book_titles
        actual = str(self.bookstore)
        expected = "Total sold books: 0\nCurrent availability: 8\n" \
                   " - Book1: 3 copies\n - Book2: 3 copies\n - Book3: 2 copies"
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
