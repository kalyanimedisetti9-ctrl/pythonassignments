name = input("Enter student name: ")

found = False

with open("students.txt", "r") as file:
    for line in file:
        data = line.strip().split(",")

        if data[1].lower() == name.lower():
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