class ReportGenerator:
    def generate_report(self, name, salary):
        print("Employee Report")
        print("Name:", name)
        print("Salary:", salary)


class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def create_report(self):
        report = ReportGenerator()
        report.generate_report(self.name, self.salary)


employee = Employee("Ravi", 30000)
employee.create_report()