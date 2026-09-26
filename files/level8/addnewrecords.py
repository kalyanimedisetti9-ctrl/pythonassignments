import csv

student = [105, "Anjali", "Computer Engineering", 78]

with open("students.csv", "a", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(student)

print("New student added successfully")