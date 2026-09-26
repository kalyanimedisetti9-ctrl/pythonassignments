from abc import ABC, abstractmethod

class Payment(ABC):
    def __init__(self, amount, transaction_id):
        self.amount = amount
        self.transaction_id = transaction_id

    @abstractmethod
    def pay(self):
        pass

class UPI(Payment):
    def pay(self):
        print("Payment through UPI")

class Card(Payment):
    def pay(self):
        print("Payment through Card")

u = UPI(1000, "TXN101")
c = Card(2000, "TXN102")

print("Amount:", u.amount)
print("Transaction ID:", u.transaction_id)
u.pay()

print("Amount:", c.amount)
print("Transaction ID:", c.transaction_id)
c.pay()