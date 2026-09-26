employees = [
    ("Ravi", "Manager", 60000),
    ("Sita", "Developer", 75000),
    ("Arjun", "Tester", 50000)
]

highest = employees[0]

for employee in employees:
    if employee[2] > highest[2]:
        highest = employee

print("Highest Salary Employee:")
print(highest)