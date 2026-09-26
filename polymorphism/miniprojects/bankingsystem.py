class SavingsAccount:
    def calculate_interest(self, amount):
        return amount * 0.05

class CurrentAccount:
    def calculate_interest(self, amount):
        return amount * 0.02

class FixedDeposit:
    def calculate_interest(self, amount):
        return amount * 0.07


def show_interest(account, amount):
    print("Interest:", account.calculate_interest(amount))


accounts = [
    SavingsAccount(),
    CurrentAccount(),
    FixedDeposit()
]

for account in accounts:
    show_interest(account, 10000)