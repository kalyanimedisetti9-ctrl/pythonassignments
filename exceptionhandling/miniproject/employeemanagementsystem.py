class InvalidEmployeeIDError(Exception):
    pass

class InvalidSalaryError(Exception):
    pass

class InvalidDepartmentError(Exception):
    pass


class EmployeeManagement:
    def __init__(self):
        self.employees = {}
        self.departments = ["HR", "IT", "Sales"]

    def add_employee(self, emp_id, name, salary, department):
        try:
            if emp_id <= 0:
                raise InvalidEmployeeIDError("Invalid employee ID")

            if salary <= 0:
                raise InvalidSalaryError("Salary must be greater than zero")

            if department not in self.departments:
                raise InvalidDepartmentError("Invalid department")

            self.employees[emp_id] = {
                "name": name,
                "salary": salary,
                "department": department
            }

            print("Employee added successfully")

        except InvalidEmployeeIDError as e:
            print("Error:", e)
        except InvalidSalaryError as e:
            print("Error:", e)
        except InvalidDepartmentError as e:
            print("Error:", e)


system = EmployeeManagement()

system.add_employee(101, "Kalyani", 30000, "IT")
system.add_employee(-2, "Ravi", 25000, "HR")
system.add_employee(103, "Sita", -5000, "IT")
system.add_employee(104, "Ram", 20000, "Finance")