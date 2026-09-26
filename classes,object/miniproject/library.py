class Book:
    def __init__(self, book_id, title, author):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.issued = False

    def display(self):
        print(self.book_id, self.title, self.author,
              "Issued:", self.issued)


books = []

books.append(Book(1, "Python Programming", "John"))
books.append(Book(2, "Java Programming", "James"))
books.append(Book(3, "Web Development", "David"))

print("All Books:")
for book in books:
    book.display()

search = input("\nEnter book title to search: ")

for book in books:
    if book.title.lower() == search.lower():
        print("Book Found")
        book.display()

book_id = int(input("\nEnter Book ID to issue: "))

for book in books:
    if book.book_id == book_id:
        if not book.issued:
            book.issued = True
            print("Book issued successfully")
        else:
            print("Book already issued")

book_id = int(input("\nEnter Book ID to return: "))

for book in books:
    if book.book_id == book_id:
        book.issued = False
        print("Book returned successfully")