import json

employees = [
    {
        "id": 101,
        "name": "Ravi",
        "department": "IT",
        "salary": 40000
    },
    {
        "id": 102,
        "name": "Sita",
        "department": "HR",
        "salary": 35000
    },
    {
        "id": 103,
        "name": "Ram",
        "department": "Sales",
        "salary": 45000
    }
]

with open("employees.json", "w") as file:
    json.dump(employees, file, indent=4)

print("Employee JSON file created successfully")