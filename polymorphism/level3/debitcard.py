class DebitCard:
    def pay(self):
        print("Payment made using Debit Card")

class CreditCard:
    def pay(self):
        print("Payment made using Credit Card")


def card_payment(card):
    card.pay()


card_payment(DebitCard())
card_payment(CreditCard())