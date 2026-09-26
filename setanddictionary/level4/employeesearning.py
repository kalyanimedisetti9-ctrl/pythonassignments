employees = {
    "Ravi": 45000,
    "Kalyani": 60000,
    "Sita": 55000,
    "Rahul": 40000
}

for name, salary in employees.items():
    if salary > 50000:
        print(name, salary)