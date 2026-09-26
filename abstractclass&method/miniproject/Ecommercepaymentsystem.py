from abc import ABC, abstractmethod

class Payment(ABC):
    @abstractmethod
    def pay(self, amount):
        pass

class UPI(Payment):
    def pay(self, amount):
        print("Paid ₹", amount, "using UPI")

class Card(Payment):
    def pay(self, amount):
        print("Paid ₹", amount, "using Credit/Debit Card")

class CashOnDelivery(Payment):
    def pay(self, amount):
        print("₹", amount, "will be paid through Cash on Delivery")

payments = [UPI(), Card(), CashOnDelivery()]

for payment in payments:
    payment.pay(1000)