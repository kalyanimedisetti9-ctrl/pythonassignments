class Employee:
    def __init__(self, name, department, salary):
        self.name = name
        self.department = department
        self.salary = salary

employee1 = Employee("Ravi", "IT", 30000)
employee2 = Employee("Anitha", "HR", 35000)
employee3 = Employee("Kiran", "Finance", 40000)
employee4 = Employee("Sita", "Marketing", 32000)
employee5 = Employee("Arjun", "Sales", 28000)

print(employee1.name, employee1.department, employee1.salary)
print(employee2.name, employee2.department, employee2.salary)
print(employee3.name, employee3.department, employee3.salary)
print(employee4.name, employee4.department, employee4.salary)
print(employee5.name, employee5.department, employee5.salary)