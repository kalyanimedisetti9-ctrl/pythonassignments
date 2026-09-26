from abc import ABC, abstractmethod


# Abstract Class
class Payment(ABC):

    @abstractmethod
    def pay(self, amount):
        pass


# Method Overriding
class UPI(Payment):
    def pay(self, amount):
        print("Paid", amount, "using UPI")


class Card(Payment):
    def pay(self, amount):
        print("Paid", amount, "using Card")


# Operator Overloading
class Money:
    def __init__(self, amount):
        self.amount = amount

    def __add__(self, other):
        return Money(self.amount + other.amount)

    def display(self):
        print("Total Money:", self.amount)


# Duck Typing
class Email:
    def send(self):
        print("Email notification sent")


class SMS:
    def send(self):
        print("SMS notification sent")


def send_notification(notification):
    notification.send()


# Polymorphism with Function
def process_payment(payment, amount):
    payment.pay(amount)


# Payment Processing
print("--- Payment System ---")

process_payment(UPI(), 1000)
process_payment(Card(), 2000)


# Duck Typing
print("\n--- Notification System ---")

send_notification(Email())
send_notification(SMS())


# Operator Overloading
print("\n--- Money Calculation ---")

money1 = Money(500)
money2 = Money(1000)

money3 = money1 + money2
money3.display()