class Employee:
    def __init__(self, daily_salary):
        self.daily_salary = daily_salary

    def calculate_salary(self, working_days):
        return self.daily_salary * working_days

e = Employee(1000)

print("Salary:", e.calculate_salary(25))