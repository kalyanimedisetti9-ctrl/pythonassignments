class Person:
    def show_person(self):
        print("I am a person")


class Student(Person):
    def study(self):
        print("I am studying")


student = Student()
student.show_person()
student.study()