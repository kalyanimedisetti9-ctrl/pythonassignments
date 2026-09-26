from abc import ABC, abstractmethod

class Employee(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def calculate_salary(self):
        pass

class FullTimeEmployee(Employee):
    def calculate_salary(self):
        print(self.name, "Salary: ₹50,000")

class PartTimeEmployee(Employee):
    def calculate_salary(self):
        print(self.name, "Salary: ₹25,000")

class Intern(Employee):
    def calculate_salary(self):
        print(self.name, "Stipend: ₹15,000")

employees = [
    FullTimeEmployee("Kalyani"),
    PartTimeEmployee("Ravi"),
    Intern("Anitha")
]

for employee in employees:
    employee.calculate_salary()