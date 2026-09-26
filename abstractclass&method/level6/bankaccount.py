class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def deposit(self, amount):
        self.balance = self.balance + amount
        return self.balance

a = BankAccount(10000)

print("Balance after deposit:", a.deposit(5000))