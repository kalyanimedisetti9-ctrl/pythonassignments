class Teacher:
    def __init__(self, name):
        self.name = name


class Student:
    def __init__(self, name):
        self.name = name


class NotificationService:
    def send(self, message):
        print("Notification:", message)


class School:
    def __init__(self):
        self.teachers = [
            Teacher("Mr. Ravi"),
            Teacher("Ms. Sita")
        ]

        self.students = [
            Student("Kalyani"),
            Student("Rahul")
        ]

    def send_notification(self):
        notification = NotificationService()
        notification.send("Tomorrow is a holiday.")


school = School()
school.send_notification()