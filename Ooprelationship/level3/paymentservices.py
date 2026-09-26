class PaymentService:
    def make_payment(self, amount):
        print(f"Payment of ₹{amount} completed")


class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def pay(self, amount):
        payment = PaymentService()
        payment.make_payment(amount)
        self.balance -= amount
        print(f"Remaining Balance: ₹{self.balance}")


account = BankAccount(5000)
account.pay(1000)