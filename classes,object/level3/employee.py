class Employee:
    company_name = "Infosys"
    employee_count = 0

    def __init__(self, name):
        self.name = name
        Employee.employee_count += 1

employee1 = Employee("Ravi")
employee2 = Employee("Anitha")
employee3 = Employee("Kiran")

print("Company:", Employee.company_name)
print("Employee 1:", employee1.name)
print("Employee 2:", employee2.name)
print("Employee 3:", employee3.name)
print("Total Employees:", Employee.employee_count)