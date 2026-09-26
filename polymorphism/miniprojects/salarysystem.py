class Manager:
    def calculate_salary(self):
        return 60000

class Developer:
    def calculate_salary(self):
        return 50000

class Tester:
    def calculate_salary(self):
        return 40000

class Intern:
    def calculate_salary(self):
        return 20000


def display_salary(employee):
    print("Salary:", employee.calculate_salary())


employees = [Manager(), Developer(), Tester(), Intern()]

for employee in employees:
    display_salary(employee)