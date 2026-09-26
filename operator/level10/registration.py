username = input("Enter username: ")
password = input("Enter password: ")
age = int(input("Enter age: "))

registered_users = ["admin", "kalyani", "ravi"]

if username not in registered_users and len(password) >= 6 and age >= 18:
    print("Registration successful")
else:
    print("Registration failed")

    if username in registered_users:
        print("Username already exists")

    if len(password) < 6:
        print("Password must contain at least 6 characters")

    if age < 18:
        print("Age must be 18 or above")