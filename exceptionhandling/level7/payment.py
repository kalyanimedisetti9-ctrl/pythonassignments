class InvalidPaymentError(Exception):
    pass


class Payment:
    def make_payment(self, amount):
        try:
            if amount <= 0:
                raise InvalidPaymentError("Payment amount must be greater than zero")
            print("Payment successful")
            print("Amount paid:", amount)
        except InvalidPaymentError as e:
            print("Error:", e)


payment = Payment()
payment.make_payment(1000)
payment.make_payment(-500)