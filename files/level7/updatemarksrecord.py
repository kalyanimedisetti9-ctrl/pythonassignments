student_id = input("Enter student ID: ")
new_marks = input("Enter new marks: ")

with open("students.txt", "r") as file:
    lines = file.readlines()

updated = False

with open("students.txt", "w") as file:
    for line in lines:
        data = line.strip().split(",")

        if data[0] == student_id:
            data[4] = new_marks
            updated = True

        file.write(",".join(data) + "\n")

if updated:
    print("Marks updated successfully")
else:
    print("Student not found")