class Person:
    def show_role(self):
        print("I am a person")


class Student(Person):
    def study(self):
        print("Student is studying")


class Teacher(Person):
    def teach(self):
        print("Teacher is teaching")


class NotificationService:
    def send(self, message):
        print("Notification:", message)


class CertificateService:
    def generate(self, student, course):
        print("Certificate generated for", student)
        print("Course:", course)


class Course:
    def __init__(self, name):
        self.name = name
        self.teacher = Teacher()
        self.students = [
            Student(),
            Student()
        ]

    def notify_students(self):
        notification = NotificationService()
        notification.send("New lesson is available")

    def give_certificate(self):
        certificate = CertificateService()
        certificate.generate("Kalyani", self.name)


course = Course("Python Programming")

course.teacher.teach()
course.students[0].study()

course.notify_students()
course.give_certificate()