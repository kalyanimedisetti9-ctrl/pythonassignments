class Employee:
    def work(self):
        print("Employee is working")


class Laptop:
    def start(self):
        print("Laptop started")


class Developer(Employee):
    def __init__(self, name):
        self.name = name
        self.laptop = Laptop()

    def code(self):
        self.laptop.start()
        print(self.name, "is coding")


developer = Developer("Ravi")
developer.work()
developer.code()