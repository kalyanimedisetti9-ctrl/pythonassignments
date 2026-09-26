class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def __gt__(self, other):
        return self.salary > other.salary


employee1 = Employee("Ravi", 60000)
employee2 = Employee("Kalyani", 50000)

print(employee1 > employee2)