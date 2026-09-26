class BookNotAvailableError(Exception):
    pass


class LibraryBook:
    def __init__(self, title):
        self.title = title
        self.available = True

    def issue_book(self):
        if not self.available:
            raise BookNotAvailableError("Book is not available")

        self.available = False
        print("Book issued successfully")


try:
    book = LibraryBook("Python Programming")

    book.issue_book()
    book.issue_book()

except BookNotAvailableError as e:
    print("Error:", e)