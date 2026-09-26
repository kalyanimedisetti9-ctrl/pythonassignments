class Printer:
    def print_details(self, name):
        print("Student Name:", name)


class Student:
    def __init__(self, name):
        self.name = name

    def print_student(self):
        printer = Printer()
        printer.print_details(self.name)


student = Student("Kalyani")
student.print_student()