class BankAccount:
    def calculate_interest(self):
        print("Calculating interest")

class SavingsAccount(BankAccount):
    def calculate_interest(self):
        print("Savings Account Interest: 5%")

class CurrentAccount(BankAccount):
    def calculate_interest(self):
        print("Current Account Interest: 2%")


accounts = [SavingsAccount(), CurrentAccount()]

for account in accounts:
    account.calculate_interest()