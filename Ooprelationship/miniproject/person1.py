class Person:
    def introduce(self):
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


class School:
    def __init__(self):
        self.students = [
            Student(),
            Student()
        ]

        self.teachers = [
            Teacher(),
            Teacher()
        ]

    def send_notification(self):
        notification = NotificationService()
        notification.send("Tomorrow is a holiday")


school = School()

school.students[0].introduce()
school.students[0].study()

school.teachers[0].introduce()
school.teachers[0].teach()

school.send_notification()