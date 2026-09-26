class BookUnavailableError(Exception):
    pass


class Library:
    def __init__(self):
        self.books = ["Python", "Java", "HTML"]

    def issue_book(self, book):
        try:
            if book not in self.books:
                raise BookUnavailableError("Book is not available")
            self.books.remove(book)
            print(book, "issued successfully")
        except BookUnavailableError as e:
            print("Error:", e)


library = Library()
library.issue_book("Python")
library.issue_book("C++")