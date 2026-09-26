class Notification:
    def send(self):
        print("Sending notification")

class Email(Notification):
    def send(self):
        print("Sending Email notification")

class SMS(Notification):
    def send(self):
        print("Sending SMS notification")

class WhatsApp(Notification):
    def send(self):
        print("Sending WhatsApp notification")


notifications = [Email(), SMS(), WhatsApp()]

for notification in notifications:
    notification.send()