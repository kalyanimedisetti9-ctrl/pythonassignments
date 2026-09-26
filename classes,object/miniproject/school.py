class Student:
    def __init__(self, name, roll_no):
        self.name = name
        self.roll_no = roll_no

    def display(self):
        print("Student:", self.name)
        print("Roll No:", self.roll_no)


class Teacher:
    def __init__(self, name, subject):
        self.name = name
        self.subject = subject

    def display(self):
        print("Teacher:", self.name)
        print("Subject:", self.subject)


class Course:
    def __init__(self, course_name, duration):
        self.course_name = course_name
        self.duration = duration

    def display(self):
        print("Course:", self.course_name)
        print("Duration:", self.duration)


student = Student("Kalyani", 101)
teacher = Teacher("Ramesh", "Python")
course = Course("Computer Engineering", "3 Years")

student.display()
print()
teacher.display()
print()
course.display()