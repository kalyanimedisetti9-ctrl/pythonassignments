from abc import ABC, abstractmethod

class LibraryItem(ABC):
    def __init__(self, title):
        self.title = title

    @abstractmethod
    def display(self):
        pass

class Book(LibraryItem):
    def display(self):
        print("Book:", self.title)

class Magazine(LibraryItem):
    def display(self):
        print("Magazine:", self.title)

class Newspaper(LibraryItem):
    def display(self):
        print("Newspaper:", self.title)

items = [
    Book("Python Programming"),
    Magazine("Technology Today"),
    Newspaper("The Hindu")
]

for item in items:
    item.display()