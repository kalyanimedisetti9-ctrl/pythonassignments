from abc import ABC, abstractmethod

class Payment(ABC):
    @abstractmethod
    def pay(self):
        pass

class UPIPayment(Payment):
    def pay(self):
        print("Payment made using UPI")

class CardPayment(Payment):
    def pay(self):
        print("Payment made using Card")

u = UPIPayment()
c = CardPayment()

u.pay()
c.pay()