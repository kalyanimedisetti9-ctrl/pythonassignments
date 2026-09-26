from abc import ABC, abstractmethod

class BankAccount(ABC):
    def __init__(self, holder, account_number):
        self.holder = holder
        self.account_number = account_number

    @abstractmethod
    def calculate_interest(self):
        pass

class SavingsAccount(BankAccount):
    def calculate_interest(self):
        print("Interest rate: 5%")

a = SavingsAccount("Kalyani", 123456)

print("Account Holder:", a.holder)
print("Account Number:", a.account_number)
a.calculate_interest()