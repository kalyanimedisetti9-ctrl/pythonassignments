import csv


def add_contact():
    with open("contacts.csv", "a", newline="") as file:
        writer = csv.writer(file)

        name = input("Enter name: ")
        phone = input("Enter phone: ")
        email = input("Enter email: ")

        writer.writerow([name, phone, email])

    print("Contact added successfully")


def display_contacts():
    try:
        with open("contacts.csv", "r") as file:
            reader = csv.reader(file)

            for row in reader:
                print("Name:", row[0])
                print("Phone:", row[1])
                print("Email:", row[2])
                print("----------------")

    except FileNotFoundError:
        print("Contact file not found")


def search_contact():
    name = input("Enter name to search: ")

    try:
        with open("contacts.csv", "r") as file:
            reader = csv.reader(file)

            for row in reader:
                if row[0].lower() == name.lower():
                    print("Contact found:", row)
                    return

        print("Contact not found")

    except FileNotFoundError:
        print("File not found")


while True:
    print("\n1. Add Contact")
    print("2. Display Contacts")
    print("3. Search Contact")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_contact()
    elif choice == "2":
        display_contacts()
    elif choice == "3":
        search_contact()
    elif choice == "4":
        break
    else:
        print("Invalid choice")