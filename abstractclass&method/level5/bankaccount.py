class BankAccount:
    def __init__(self, holder, account_number, balance):
        self.holder = holder
        self.account_number = account_number
        self.balance = balance

    def display(self):
        print("Account Holder:", self.holder)
        print("Account Number:", self.account_number)
        print("Balance:", self.balance)

a = BankAccount("Kalyani", 123456, 10000)
a.display()