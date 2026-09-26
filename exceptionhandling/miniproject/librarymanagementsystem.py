class BookUnavailableError(Exception):
    pass

class InvalidBookIDError(Exception):
    pass

class DuplicateBookError(Exception):
    pass


class Library:
    def __init__(self):
        self.books = {
            101: "Python",
            102: "Java"
        }

    def add_book(self, book_id, book_name):
        try:
            if book_id <= 0:
                raise InvalidBookIDError("Invalid book ID")

            if book_id in self.books:
                raise DuplicateBookError("Book already exists")

            self.books[book_id] = book_name
            print("Book added successfully")

        except InvalidBookIDError as e:
            print("Error:", e)
        except DuplicateBookError as e:
            print("Error:", e)

    def issue_book(self, book_id):
        try:
            if book_id not in self.books:
                raise BookUnavailableError("Book is not available")

            print("Book issued:", self.books[book_id])
            del self.books[book_id]

        except BookUnavailableError as e:
            print("Error:", e)


library = Library()

library.add_book(103, "HTML")
library.add_book(101, "Python")
library.issue_book(101)
library.issue_book(101)