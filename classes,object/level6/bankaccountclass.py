class BankAccount:
    def __init__(self, holder, balance):
        self.holder = holder
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self.balance

account = BankAccount("Kalyani", 50000)

print("Initial Balance:", account.balance)

new_balance = account.deposit(10000)

print("Deposited Amount:", 10000)
print("Updated Balance:", new_balance)