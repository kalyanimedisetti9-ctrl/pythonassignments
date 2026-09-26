class Employee:
    def __init__(self, emp_id, name, department, salary):
        self.emp_id = emp_id
        self.name = name
        self.department = department
        self.salary = salary

e = Employee(101, "Ravi", "IT", 40000)

print("Employee ID:", e.emp_id)
print("Name:", e.name)
print("Department:", e.department)
print("Salary:", e.salary)