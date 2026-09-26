def register():
    username = input("Enter username: ")
    password = input("Enter password: ")

    try:
        with open("users.txt", "r") as file:
            for line in file:
                old_username = line.strip().split(",")[0]

                if old_username == username:
                    print("Username already exists")
                    return
    except FileNotFoundError:
        pass

    with open("users.txt", "a") as file:
        file.write(f"{username},{password}\n")

    print("Registration successful")


def login():
    username = input("Enter username: ")
    password = input("Enter password: ")

    try:
        with open("users.txt", "r") as file:
            for line in file:
                data = line.strip().split(",")

                if data[0] == username and data[1] == password:
                    print("Login successful")
                    return

        print("Invalid username or password")

    except FileNotFoundError:
        print("No registered users")


while True:
    print("\n1. Register")
    print("2. Login")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        register()
    elif choice == "2":
        login()
    elif choice == "3":
        break
    else:
        print("Invalid choice")