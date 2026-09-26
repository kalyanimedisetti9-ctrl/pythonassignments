salaries = {
    "Ravi": 30000,
    "Anu": 35000,
    "Suresh": 40000,
    "Kalyani": 45000
}

total = 0

for salary in salaries.values():
    total += salary

average = total / len(salaries)

print("Total Salary:", total)
print("Average Salary:", average)