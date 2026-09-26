from abc import ABC, abstractmethod

class Notification(ABC):
    @abstractmethod
    def send(self):
        pass

class EmailNotification(Notification):
    def send(self):
        print("Notification sent through Email")

class SMSNotification(Notification):
    def send(self):
        print("Notification sent through SMS")

e = EmailNotification()
s = SMSNotification()

e.send()
s.send()