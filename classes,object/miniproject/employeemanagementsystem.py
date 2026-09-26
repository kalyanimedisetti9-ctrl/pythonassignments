class Employee:
    company_name = "ABC Technologies"

    def __init__(self, emp_id, name, department, salary):
        self.emp_id = emp_id
        self.name = name
        self.department = department
        self.salary = salary

    def display(self):
        print("ID:", self.emp_id)
        print("Name:", self.name)
        print("Department:", self.department)
        print("Salary:", self.salary)
        print("Company:", Employee.company_name)


employees = []

employees.append(Employee(101, "Kalyani", "IT", 35000))
employees.append(Employee(102, "Ravi", "HR", 30000))
employees.append(Employee(103, "Anitha", "Finance", 40000))

for employee in employees:
    employee.display()
    print("----------------")