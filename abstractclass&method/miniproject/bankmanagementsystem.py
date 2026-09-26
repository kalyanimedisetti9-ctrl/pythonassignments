from abc import ABC, abstractmethod

class Account(ABC):
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    @abstractmethod
    def account_type(self):
        pass

    def show_balance(self):
        print("Account Holder:", self.name)
        print("Balance:", self.balance)

class SavingsAccount(Account):
    def account_type(self):
        print("Account Type: Savings Account")

class CurrentAccount(Account):
    def account_type(self):
        print("Account Type: Current Account")

a1 = SavingsAccount("Kalyani", 50000)
a1.account_type()
a1.show_balance()

a2 = CurrentAccount("Ravi", 75000)
a2.account_type()
a2.show_balance()