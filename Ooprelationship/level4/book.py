class Book:
    def __init__(self, title):
        self.title = title


class Library:
    def __init__(self):
        self.books = [
            Book("Python"),
            Book("Java"),
            Book("C Programming")
        ]

    def show_books(self):
        for book in self.books:
            print(book.title)


library = Library()
library.show_books()