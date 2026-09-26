class EmailService:
    def send_email(self, message):
        print("Email sent:", message)


class Order:
    def __init__(self, order_id):
        self.order_id = order_id

    def send_confirmation(self):
        email = EmailService()
        email.send_email(
            f"Order {self.order_id} confirmed successfully."
        )


order = Order(101)
order.send_confirmation()