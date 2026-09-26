class Employee:
    def calculate_salary(self):
        print("Employee salary")

class Manager(Employee):
    def calculate_salary(self):
        print("Manager salary: 60000")

class Developer(Employee):
    def calculate_salary(self):
        print("Developer salary: 50000")


employees = [Manager(), Developer()]

for employee in employees:
    employee.calculate_salary()