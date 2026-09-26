class InvalidSalaryError(Exception):
    pass


class Employee:
    def __init__(self, name):
        self.name = name

    def set_salary(self, salary):
        try:
            if salary <= 0:
                raise InvalidSalaryError("Salary must be greater than zero")
            print("Employee:", self.name)
            print("Salary:", salary)
        except InvalidSalaryError as e:
            print("Error:", e)


employee = Employee("Ravi")
employee.set_salary(30000)
employee.set_salary(-5000)