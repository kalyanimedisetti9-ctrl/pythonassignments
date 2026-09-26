class UPI:
    def pay(self):
        print("Payment processed using UPI")

class CreditCard:
    def pay(self):
        print("Payment processed using Credit Card")

class DebitCard:
    def pay(self):
        print("Payment processed using Debit Card")

class NetBanking:
    def pay(self):
        print("Payment processed using Net Banking")


def process_payment(payment):
    payment.pay()


payments = [UPI(), CreditCard(), DebitCard(), NetBanking()]

for payment in payments:
    process_payment(payment)