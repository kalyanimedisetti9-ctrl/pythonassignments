class Person:
    def show_role(self):
        print("I am a person")


class Librarian(Person):
    def manage_library(self):
        print("Librarian manages the library")


class Book:
    def __init__(self, title):
        self.title = title


class SearchService:
    def search(self, title):
        print("Searching for:", title)


class Library:
    def __init__(self):
        self.books = [
            Book("Python"),
            Book("Java"),
            Book("C Programming")
        ]

    def search_book(self, title):
        search = SearchService()
        search.search(title)

    def show_books(self):
        for book in self.books:
            print(book.title)


librarian = Librarian()
librarian.show_role()
librarian.manage_library()

library = Library()
library.show_books()
library.search_book("Python")