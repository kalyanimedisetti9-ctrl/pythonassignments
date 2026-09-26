class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

    def display(self):
        print("Account Number:", self.account_number)
        print("Balance:", self.balance)


class SavingsAccount(BankAccount):
    def interest(self):
        print("Savings account gives interest")


class CurrentAccount(BankAccount):
    def overdraft(self):
        print("Current account provides overdraft facility")


savings = SavingsAccount(101, 10000)
current = CurrentAccount(102, 20000)

savings.display()
savings.interest()

print()

current.display()
current.overdraft()