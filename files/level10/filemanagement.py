import os


class FileManagementSystem:

    def create_file(self):
        try:
            filename = input("Enter filename: ")

            if os.path.exists(filename):
                print("File already exists")
                return

            with open(filename, "w") as file:
                data = input("Enter data: ")
                file.write(data)

            print("File created successfully")

        except PermissionError:
            print("Error: Permission denied")

        except OSError as e:
            print("Error:", e)


    def read_file(self):
        try:
            filename = input("Enter filename: ")

            with open(filename, "r") as file:
                print("\nFile Contents:")
                print(file.read())

        except FileNotFoundError:
            print("Error: File not found")

        except PermissionError:
            print("Error: Permission denied")

        except OSError as e:
            print("Error:", e)


    def write_file(self):
        try:
            filename = input("Enter filename: ")

            with open(filename, "w") as file:
                data = input("Enter new data: ")
                file.write(data)

            print("File overwritten successfully")

        except FileNotFoundError:
            print("Error: File not found")

        except PermissionError:
            print("Error: Permission denied")

        except OSError as e:
            print("Error:", e)


    def append_file(self):
        try:
            filename = input("Enter filename: ")

            with open(filename, "a") as file:
                data = input("Enter data to append: ")
                file.write("\n" + data)

            print("Data appended successfully")

        except FileNotFoundError:
            print("Error: File not found")

        except PermissionError:
            print("Error: Permission denied")

        except OSError as e:
            print("Error:", e)


    def delete_file(self):
        try:
            filename = input("Enter filename: ")

            if not os.path.exists(filename):
                raise FileNotFoundError("File does not exist")

            os.remove(filename)

            print("File deleted successfully")

        except FileNotFoundError as e:
            print("Error:", e)

        except PermissionError:
            print("Error: Permission denied")

        except OSError as e:
            print("Error:", e)


system = FileManagementSystem()


while True:

    print("\n===== FILE MANAGEMENT SYSTEM =====")
    print("1. Create File")
    print("2. Read File")
    print("3. Write File")
    print("4. Append File")
    print("5. Delete File")
    print("6. Exit")

    try:
        choice = int(input("Enter your choice: "))

        if choice == 1:
            system.create_file()

        elif choice == 2:
            system.read_file()

        elif choice == 3:
            system.write_file()

        elif choice == 4:
            system.append_file()

        elif choice == 5:
            system.delete_file()

        elif choice == 6:
            print("Program ended")
            break

        else:
            raise ValueError("Invalid menu choice")

    except ValueError as e:
        print("Error:", e)

    finally:
        print("Operation completed")