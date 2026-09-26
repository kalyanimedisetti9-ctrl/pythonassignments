class BankAccount:
    def __init__(self, account_holder, account_number, balance):
        self.account_holder = account_holder
        self.account_number = account_number
        self.balance = balance

account1 = BankAccount("Kalyani", "1234567890", 50000)
account2 = BankAccount("Ravi", "9876543210", 75000)

print("Account Holder:", account1.account_holder)
print("Account Number:", account1.account_number)
print("Balance:", account1.balance)

print()

print("Account Holder:", account2.account_holder)
print("Account Number:", account2.account_number)
print("Balance:", account2.balance)