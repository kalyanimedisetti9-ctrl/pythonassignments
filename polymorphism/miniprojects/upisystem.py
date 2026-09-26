class UPI:
    def pay(self, amount):
        print("Paid", amount, "using UPI")

class CreditCard:
    def pay(self, amount):
        print("Paid", amount, "using Credit Card")

class DebitCard:
    def pay(self, amount):
        print("Paid", amount, "using Debit Card")

class NetBanking:
    def pay(self, amount):
        print("Paid", amount, "using Net Banking")


def make_payment(payment, amount):
    payment.pay(amount)


make_payment(UPI(), 1000)
make_payment(CreditCard(), 2000)
make_payment(DebitCard(), 1500)
make_payment(NetBanking(), 3000)