# 5.Print books
# We want to print books, but before printing the book, we should format it. To accomplish this, we have a class Printer that can print books and a class Formatter which is used by the Printer. Refactor the provided code that breaks the DIP because both Printer and Formatter depend on concretions, not abstractions, by creating abstractions and injecting them wherever needed.
# Dependency Inversion
#
# class Book:
#     def __init__(self, content: str):
#         self.content = content
#
#
# class Formatter:
#     def format(self, book: Book) -> str:
#         return book.content
#
#
# class Printer:
#     def get_book(self, book: Book):
#         formatter = Formatter()
#         formatted_book = formatter.format(book)
#         return formatted_book

class Book:
    def __init__(self, content: str):
        self.content = content


class Formatter:
    @staticmethod
    def format(book, formatted_content: str):
        book.content = formatted_content
        return book.content


class Printer(Formatter):
    @staticmethod
    def get_book(book):
        print(book.content)


book_1 = Book("content 1")
book_2 = Book("content 2")
book_3 = Book("content 3")
formatter = Formatter()
printer = Printer()

printer.get_book(book_1)
formatter.format(book_1, "formatted content")
printer.get_book(book_1)
print()

printer.get_book(book_2)
formatter.format(book_2, "changed content")
printer.get_book(book_2)
print()

printer.get_book(book_3)
formatter.format(book_3, "new content")
printer.get_book(book_3)
