from abc import ABC, abstractmethod

class Employee(ABC):
    def __init__(self, name, emp_id):
        self.name = name
        self.emp_id = emp_id

    @abstractmethod
    def calculate_salary(self):
        pass

class Manager(Employee):
    def calculate_salary(self):
        print("Salary of", self.name, "is 50000")

e = Manager("Kalyani", 101)

print("Name:", e.name)
print("Employee ID:", e.emp_id)
e.calculate_salary()