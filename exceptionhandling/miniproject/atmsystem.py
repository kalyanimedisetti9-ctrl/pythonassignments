class InvalidPINError(Exception):
    pass

class InsufficientBalanceError(Exception):
    pass

class InvalidWithdrawalError(Exception):
    pass

class InvalidAccountError(Exception):
    pass


class ATM:
    def __init__(self):
        self.accounts = {
            "1001": {"pin": "1234", "balance": 10000}
        }

    def withdraw(self, account, pin, amount):
        try:
            if account not in self.accounts:
                raise InvalidAccountError("Invalid account")

            if self.accounts[account]["pin"] != pin:
                raise InvalidPINError("Invalid PIN")

            if amount <= 0:
                raise InvalidWithdrawalError("Invalid withdrawal amount")

            if amount > self.accounts[account]["balance"]:
                raise InsufficientBalanceError("Insufficient balance")

            self.accounts[account]["balance"] -= amount

            print("Please collect your cash")
            print("Remaining balance:",
                  self.accounts[account]["balance"])

        except InvalidAccountError as e:
            print("Error:", e)
        except InvalidPINError as e:
            print("Error:", e)
        except InvalidWithdrawalError as e:
            print("Error:", e)
        except InsufficientBalanceError as e:
            print("Error:", e)


atm = ATM()

atm.withdraw("1001", "1234", 2000)
atm.withdraw("1001", "1111", 1000)
atm.withdraw("1001", "1234", 20000)
atm.withdraw("9999", "1234", 1000)