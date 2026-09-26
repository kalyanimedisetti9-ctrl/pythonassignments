class EmailService:
    def send(self):
        print("Message sent through Email")

class SMSService:
    def send(self):
        print("Message sent through SMS")


def send_message(service):
    service.send()


send_message(EmailService())
send_message(SMSService())