from abc import ABC, abstractmethod

class Employee(ABC):

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    @abstractmethod
    def calculate_bonus(self):
        pass

    def show_details(self):
        print("Employee Name:", self.name)
        print("Salary:", self.salary)

class Manager(Employee):

    def calculate_bonus(self):
        return self.salary * 0.20

class Developer(Employee):

    def calculate_bonus(self):
        return self.salary * 0.10

class Tester(Employee):

    def calculate_bonus(self):
        return self.salary * 0.08


employees = [
    Manager("Kalyani", 60000),
    Developer("Ravi", 50000),
    Tester("Anitha", 40000)
]

for employee in employees:
    employee.show_details()
    print("Bonus:", employee.calculate_bonus())
    print("--------------------")