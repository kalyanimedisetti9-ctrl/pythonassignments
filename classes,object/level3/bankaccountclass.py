class BankAccount:
    bank_name = "State Bank of India"

    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance

account1 = BankAccount("Kalyani", 50000)
account2 = BankAccount("Ravi", 75000)
account3 = BankAccount("Anitha", 60000)

print(account1.account_holder, "-", account1.bank_name)
print(account2.account_holder, "-", account2.bank_name)
print(account3.account_holder, "-", account3.bank_name)