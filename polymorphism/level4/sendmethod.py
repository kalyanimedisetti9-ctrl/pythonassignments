class EmailNotification:
    def send(self):
        print("Email notification sent")

class SMSNotification:
    def send(self):
        print("SMS notification sent")

class WhatsAppNotification:
    def send(self):
        print("WhatsApp notification sent")


def send_notification(notification):
    notification.send()


send_notification(EmailNotification())
send_notification(SMSNotification())
send_notification(WhatsAppNotification())