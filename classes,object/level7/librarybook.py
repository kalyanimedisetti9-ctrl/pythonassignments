class LibraryBook:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.issued = False

    def issue_book(self):
        if not self.issued:
            self.issued = True
            print("Book issued successfully")
        else:
            print("Book is already issued")

    def return_book(self):
        if self.issued:
            self.issued = False
            print("Book returned successfully")
        else:
            print("Book was not issued")

    def display(self):
        print("Title:", self.title)
        print("Author:", self.author)
        print("Issued:", self.issued)


book = LibraryBook("Python Programming", "John")

book.display()

book.issue_book()
book.display()

book.return_book()
book.display()