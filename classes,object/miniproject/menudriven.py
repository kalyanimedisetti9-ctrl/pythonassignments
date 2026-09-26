class Student:
    college_name = "Aditya Polytechnic College"
    student_count = 0

    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course
        Student.student_count += 1

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Course:", self.course)
        print("College:", Student.college_name)


students = []

while True:
    print("\n===== STUDENT MANAGEMENT =====")
    print("1. Add Student")
    print("2. Display Students")
    print("3. Total Students")
    print("4. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        name = input("Enter Name: ")
        age = int(input("Enter Age: "))
        course = input("Enter Course: ")

        student = Student(name, age, course)
        students.append(student)

        print("Student added successfully")

    elif choice == 2:
        if len(students) == 0:
            print("No students available")
        else:
            for student in students:
                student.display()
                print("----------------")

    elif choice == 3:
        print("Total Students:", Student.student_count)

    elif choice == 4:
        print("Thank You!")
        break

    else:
        print("Invalid choice")