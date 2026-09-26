import csv

with open("students.csv", "r") as file:
    reader = csv.DictReader(file)

    total = 0
    count = 0

    for row in reader:
        total += int(row["Marks"])
        count += 1

if count > 0:
    average = total / count
    print("Average marks:", average)
else:
    print("No student records found")