users = ["kalyani", "ravi", "anu", "suresh"]

username = input("Enter username: ")

if username in users:
    print("Username exists")
else:
    print("Username does not exist")