class Employee:
    def __init__(self, name, monthly_salary):
        self.name = name
        self.monthly_salary = monthly_salary
        self.annual_salary = monthly_salary * 12

    def display(self):
        print("Employee Name:", self.name)
        print("Monthly Salary:", self.monthly_salary)
        print("Annual Salary:", self.annual_salary)


employee = Employee("Ravi", 30000)

employee.display()