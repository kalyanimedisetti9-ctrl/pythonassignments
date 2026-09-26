import csv
import os


def add_employee():
    with open("employees.csv", "a", newline="") as file:
        writer = csv.writer(file)

        if os.path.getsize("employees.csv") == 0:
            writer.writerow(["ID", "Name", "Department", "Salary"])

        emp_id = input("Enter employee ID: ")
        name = input("Enter name: ")
        department = input("Enter department: ")
        salary = input("Enter salary: ")

        writer.writerow([emp_id, name, department, salary])

    print("Employee added successfully")


def display_employees():
    try:
        with open("employees.csv", "r") as file:
            reader = csv.DictReader(file)

            for employee in reader:
                print(employee)

    except FileNotFoundError:
        print("Employee file not found")


def search_employee():
    emp_id = input("Enter employee ID: ")

    try:
        with open("employees.csv", "r") as file:
            reader = csv.DictReader(file)

            for employee in reader:
                if employee["ID"] == emp_id:
                    print("Employee found:", employee)
                    return

        print("Employee not found")

    except FileNotFoundError:
        print("File not found")


while True:
    print("\n1. Add Employee")
    print("2. Display Employees")
    print("3. Search Employee")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_employee()
    elif choice == "2":
        display_employees()
    elif choice == "3":
        search_employee()
    elif choice == "4":
        break
    else:
        print("Invalid choice")