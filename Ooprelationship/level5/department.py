class Department:
    def __init__(self, name):
        self.name = name


class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary


class PayrollService:
    def calculate_salary(self, employee):
        print(f"Salary of {employee.name}: ₹{employee.salary}")


class Company:
    def __init__(self):
        self.departments = [
            Department("IT"),
            Department("HR")
        ]

        self.employees = [
            Employee("Ravi", 30000),
            Employee("Sita", 35000)
        ]

    def process_payroll(self):
        payroll = PayrollService()

        for employee in self.employees:
            payroll.calculate_salary(employee)


company = Company()
company.process_payroll()