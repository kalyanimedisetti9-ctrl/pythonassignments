class Employee:
    def __init__(self, name, daily_salary):
        self.name = name
        self.daily_salary = daily_salary

    def calculate_salary(self, working_days):
        return self.daily_salary * working_days

employee = Employee("Ravi", 1000)

working_days = 25

print("Employee:", employee.name)
print("Working Days:", working_days)
print("Salary:", employee.calculate_salary(working_days))