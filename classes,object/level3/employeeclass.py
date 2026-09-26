class Employee:
    company_name = "TCS"

    def __init__(self, name):
        self.name = name

employee1 = Employee("Ravi")
employee2 = Employee("Anitha")
employee3 = Employee("Kiran")

print(employee1.name, "-", employee1.company_name)
print(employee2.name, "-", employee2.company_name)
print(employee3.name, "-", employee3.company_name)