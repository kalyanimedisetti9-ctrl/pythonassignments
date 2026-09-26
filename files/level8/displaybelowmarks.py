import csv

with open("students.csv", "r") as file:
    reader = csv.DictReader(file)

    print("Students who scored below 40:")

    for row in reader:
        if int(row["Marks"]) < 40:
            print("ID:", row["Student ID"])
            print("Name:", row["Name"])
            print("Marks:", row["Marks"])
            print("------------------")