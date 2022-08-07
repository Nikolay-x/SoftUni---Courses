import unittest
from project.library import Library


class LibraryTests(unittest.TestCase):
    NAME = "Name"
    BOOKS = {}
    READERS = {}

    def setUp(self) -> None:
        self.library = Library(self.NAME)

    def test_init(self):
        self.assertEqual(self.NAME, self.library.name)
        self.assertEqual({}, self.library.books_by_authors)
        self.assertEqual({}, self.library.readers)

    def test_name_setter_valid(self):
        name = "Name 2"
        self.library.name = name
        self.assertEqual(name, self.library.name)

    def test_name_setter_invalid(self):
        name = ""
        with self.assertRaises(Exception) as error:
            self.library.name = name
        self.assertIsNotNone(error)
        self.assertEqual("Name cannot be empty string!", str(error.exception))

    def test_add_book_author_not_in_books_by_authors_title_not_in(self):
        books_by_authors = {}
        self.library.books_by_authors = books_by_authors
        author = "A"
        title = "T"
        self.library.add_book(author, title)
        actual = self.library.books_by_authors[author]
        self.assertEqual([title], actual)
        self.assertEqual({'A': ['T']}, self.library.books_by_authors)

    def test_add_book_author_in_books_by_authors_title_not_in(self):
        books_by_authors = {"A": []}
        self.library.books_by_authors = books_by_authors
        author = "A"
        title = "T"
        self.library.add_book(author, title)
        actual = self.library.books_by_authors[author]
        self.assertEqual([title], actual)
        self.assertEqual({'A': ['T']}, self.library.books_by_authors)

    def test_add_book_author_in_books_by_authors_title_in(self):
        books_by_authors = {"A": ["P", "T"]}
        self.library.books_by_authors = books_by_authors
        author = "A"
        title = "T"
        self.library.add_book(author, title)
        actual = self.library.books_by_authors[author]
        self.assertEqual(['P', 'T'], actual)
        self.assertEqual({'A': ['P', 'T']}, self.library.books_by_authors)

    def test_add_reader_name_not_in(self):
        name = "Name1"
        self.library.add_reader(name)
        self.assertEqual([], self.library.readers[name])
        self.assertEqual({'Name1': []}, self.library.readers)

    def test_add_reader_name_in(self):
        name = "Name1"
        self.library.add_reader(name)
        actual = self.library.add_reader(name)
        self.assertEqual(f"{name} is already registered in the {self.library.name} library.", actual)
        self.assertEqual({'Name1': []}, self.library.readers)

    def test_rent_book_reader_not_in_readers(self):
        readers = {}
        self.library.readers = readers
        reader_name = "RN"
        book_author = "BA"
        book_title = "BT"
        actual = self.library.rent_book(reader_name, book_author, book_title)
        expected = f"{reader_name} is not registered in the {self.library.name} Library."
        self.assertEqual(expected, actual)

    def test_rent_book_reader_in_readers_book_author_not_in_books_by_authors(self):
        readers = {"RN": []}
        self.library.readers = readers
        reader_name = "RN"
        book_author = "BA"
        book_title = "BT"
        actual = self.library.rent_book(reader_name, book_author, book_title)
        expected = f"{self.library.name} Library does not have any {book_author}'s books."
        self.assertEqual(expected, actual)

    def test_rent_book_reader_in_readers_book_author_in_books_by_authors_book_title_not_in_books_by_authors(self):
        readers = {"RN": []}
        books_by_authors_book = {"BA": []}
        self.library.readers = readers
        self.library.books_by_authors = books_by_authors_book
        reader_name = "RN"
        book_author = "BA"
        book_title = "BT"
        actual = self.library.rent_book(reader_name, book_author, book_title)
        expected = f"""{self.library.name} Library does not have {book_author}'s "{book_title}"."""
        self.assertEqual(expected, actual)

    def test_rent_book_reader_in_readers_book_author_in_books_by_authors_book_title_in_books_by_authors(self):
        readers = {"RN": []}
        books_by_authors_book = {"BA": ["BT"]}
        self.library.readers = readers
        self.library.books_by_authors = books_by_authors_book
        reader_name = "RN"
        book_author = "BA"
        book_title = "BT"
        self.library.rent_book(reader_name, book_author, book_title)
        actual = self.library.readers
        expected = {'RN': [{'BA': 'BT'}]}
        self.assertEqual(expected, actual)
        self.assertEqual({'BA': []}, self.library.books_by_authors)


if __name__ == "__main__":
    unittest.main()
