# 1.Books
# Refactor the provided code, so there is a separate class called Library, which contains books and has a method called find_book(title) that returns the book with the given title. Remove the unnecessary code from the Book class.
# Single Responsibility
#
# class Book:
#     def __init__(self, title, author, location):
#         self.title = title
#         self.author = author
#         self.location = location
#         self.page = 0
#
#     def turn_page(self, page):
#         self.page = page

class Book:
    def __init__(self, title, author, location):
        self.title = title
        self.author = author
        self.location = location
        self.page = 0

    def __repr__(self):
        result = "Book details:\n"
        result += f"title - {self.title}\n"
        result += f"author - {self.author}\n"
        result += f"location - {self.location}"
        return result


class Library:
    def __init__(self, books):
        self.books = books

    def find_book(self, title):
        book = [b for b in self.books if b.title == title][0]
        return book


b1 = Book("a", "q", "z")
b2 = Book("b", "s", "q")
b3 = Book("c", "t", "j")
l1 = Library([b1, b2, b3])

print(l1.find_book("c"))
