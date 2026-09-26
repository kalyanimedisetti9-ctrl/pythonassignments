class Account:
    def __init__(self, balance):
        self.balance = balance

    def show_balance(self):
        print("Balance:", self.balance)


class SavingsAccount(Account):
    def add_interest(self):
        self.balance += 500
        print("Interest added")


class Customer:
    def __init__(self, name):
        self.name = name


class PaymentService:
    def make_payment(self, amount):
        print("Payment of ₹", amount, "successful")


class Bank:
    def __init__(self):
        self.customers = [
            Customer("Kalyani"),
            Customer("Ravi")
        ]

    def make_payment(self, amount):
        payment = PaymentService()
        payment.make_payment(amount)


account = SavingsAccount(5000)
account.show_balance()
account.add_interest()
account.show_balance()

bank = Bank()
bank.make_payment(1000)