class Book:
    def __init__(self, title):
        self.title = title


class SearchService:
    def search(self, book_name):
        print("Searching for:", book_name)


class Library:
    def __init__(self):
        self.books = [
            Book("Python"),
            Book("Java"),
            Book("C Programming")
        ]

    def search_book(self, name):
        search_service = SearchService()
        search_service.search(name)


library = Library()
library.search_book("Python")