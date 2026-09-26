class Employee:
    def __init__(self, name):
        self.name = name


class Company:
    def __init__(self):
        self.employees = [
            Employee("Ravi"),
            Employee("Kalyani"),
            Employee("Suresh")
        ]

    def show_employees(self):
        for employee in self.employees:
            print(employee.name)


company = Company()
company.show_employees()