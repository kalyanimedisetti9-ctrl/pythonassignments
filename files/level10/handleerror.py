import csv

try:
    with open("students.csv", "r") as file:
        reader = csv.DictReader(file)

        for row in reader:
            try:
                print("ID:", row["Student ID"])
                print("Name:", row["Name"])
                print("Marks:", row["Marks"])
                print("----------------")

            except KeyError:
                print("Error: Invalid CSV columns")

except FileNotFoundError:
    print("Error: CSV file not found")

except PermissionError:
    print("Error: Permission denied")

except csv.Error:
    print("Error: Invalid CSV file")