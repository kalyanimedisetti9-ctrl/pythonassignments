class Student:
    def __init__(self, name):
        self.name = name

    def display(self):
        print("Student:", self.name)


class College:
    def __init__(self):
        self.students = [
            Student("Kalyani"),
            Student("Ravi"),
            Student("Sita")
        ]

    def display_students(self):
        print("College Students:")
        for student in self.students:
            student.display()


college = College()
college.display_students()