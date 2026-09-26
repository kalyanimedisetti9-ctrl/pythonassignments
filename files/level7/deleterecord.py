student_id = input("Enter student ID to delete: ")

with open("students.txt", "r") as file:
    lines = file.readlines()

deleted = False

with open("students.txt", "w") as file:
    for line in lines:
        data = line.strip().split(",")

        if data[0] == student_id:
            deleted = True
            continue

        file.write(line)

if deleted:
    print("Student record deleted successfully")
else:
    print("Student not found")