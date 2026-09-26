class InsufficientBalanceError(Exception):
    pass

class InvalidAmountError(Exception):
    pass

class InvalidAccountError(Exception):
    pass


class BankingSystem:
    def __init__(self):
        self.accounts = {
            "1001": 5000,
            "1002": 10000
        }

    def withdraw(self, account_no, amount):
        try:
            if account_no not in self.accounts:
                raise InvalidAccountError("Invalid account number")

            if amount <= 0:
                raise InvalidAmountError("Invalid withdrawal amount")

            if amount > self.accounts[account_no]:
                raise InsufficientBalanceError("Insufficient balance")

            self.accounts[account_no] -= amount
            print("Withdrawal successful")
            print("Remaining balance:", self.accounts[account_no])

        except InvalidAccountError as e:
            print("Error:", e)
        except InvalidAmountError as e:
            print("Error:", e)
        except InsufficientBalanceError as e:
            print("Error:", e)


bank = BankingSystem()

bank.withdraw("1001", 2000)
bank.withdraw("1001", 5000)
bank.withdraw("9999", 1000)
bank.withdraw("1001", -500)