import json
import os


def load_books():
    if not os.path.exists("library.json"):
        return []

    with open("library.json", "r") as file:
        return json.load(file)


def save_books(books):
    with open("library.json", "w") as file:
        json.dump(books, file, indent=4)


def add_book():
    books = load_books()

    book = {
        "id": input("Enter book ID: "),
        "name": input("Enter book name: "),
        "author": input("Enter author: "),
        "available": True
    }

    books.append(book)
    save_books(books)

    print("Book added successfully")


def display_books():
    books = load_books()

    for book in books:
        print(book)


def issue_book():
    books = load_books()
    book_id = input("Enter book ID: ")

    for book in books:
        if book["id"] == book_id:
            if book["available"]:
                book["available"] = False
                save_books(books)
                print("Book issued successfully")
            else:
                print("Book is already issued")
            return

    print("Book not found")


while True:
    print("\n1. Add Book")
    print("2. Display Books")
    print("3. Issue Book")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_book()
    elif choice == "2":
        display_books()
    elif choice == "3":
        issue_book()
    elif choice == "4":
        break
    else:
        print("Invalid choice")