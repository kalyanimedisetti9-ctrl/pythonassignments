class Person:
    def introduce(self):
        print("I am a person")


class Course:
    def __init__(self, name):
        self.name = name


class Student(Person):
    def __init__(self, name):
        self.name = name
        self.course = Course("Python Programming")

    def show_details(self):
        print("Student:", self.name)
        print("Course:", self.course.name)


student = Student("Kalyani")
student.introduce()
student.show_details()