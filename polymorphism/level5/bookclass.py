class Book:
    def __init__(self, title, price):
        self.title = title
        self.price = price

    def __gt__(self, other):
        return self.price > other.price


book1 = Book("Python", 500)
book2 = Book("Java", 400)

print(book1 > book2)