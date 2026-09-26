class NotificationService:
    def send_notification(self, message):
        print("Notification:", message)


class Student:
    def __init__(self, name):
        self.name = name

    def notify(self):
        service = NotificationService()
        service.send_notification(
            f"Hello {self.name}, your exam schedule is available."
        )


student = Student("Kalyani")
student.notify()