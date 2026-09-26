class Email:
    def send(self):
        print("Email notification sent")

class SMS:
    def send(self):
        print("SMS notification sent")

class WhatsApp:
    def send(self):
        print("WhatsApp notification sent")


def send_notification(notification):
    notification.send()


notifications = [Email(), SMS(), WhatsApp()]

for notification in notifications:
    send_notification(notification)