student_id = input("Enter student ID: ")

found = False

with open("students.txt", "r") as file:
    for line in file:
        data = line.strip().split(",")

        if data[0] == student_id:
            print("Student found")
            print("ID:", data[0])
            print("Name:", data[1])
            print("Age:", data[2])
            print("Course:", data[3])
            print("Marks:", data[4])
            found = True
            break

if not found:
    print("Student not found")