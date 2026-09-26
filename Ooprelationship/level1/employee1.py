class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def display(self):
        print("Name:", self.name)
        print("Salary:", self.salary)


class Developer(Employee):
    def coding(self):
        print("Developer writes code")


class Tester(Employee):
    def testing(self):
        print("Tester tests the software")


class Manager(Employee):
    def managing(self):
        print("Manager manages the team")


developer = Developer("Kiran", 50000)
tester = Tester("Ravi", 45000)
manager = Manager("Sita", 60000)

developer.display()
developer.coding()

print()

tester.display()
tester.testing()

print()

manager.display()
manager.managing()