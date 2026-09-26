class Printer:
    def print_details(self, details):
        print(details)


class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show_details(self):
        printer = Printer()
        printer.print_details(f"Name: {self.name}, Age: {self.age}")


student = Student("Kalyani", 18)
student.show_details()