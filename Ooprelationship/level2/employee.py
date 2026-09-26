class Employee:
    def __init__(self, name):
        self.name = name

    def display(self):
        print("Employee:", self.name)


class Department:
    def __init__(self):
        self.employees = [
            Employee("Ravi"),
            Employee("Kiran"),
            Employee("Sita")
        ]

    def display_employees(self):
        print("Department Employees:")
        for employee in self.employees:
            employee.display()


department = Department()
department.display_employees()