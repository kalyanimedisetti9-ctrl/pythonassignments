import json

with open("employees.json", "r") as file:
    employees = json.load(file)

highest = max(employees, key=lambda employee: employee["salary"])

print("Employee with highest salary:")
print("ID:", highest["id"])
print("Name:", highest["name"])
print("Department:", highest["department"])
print("Salary:", highest["salary"])