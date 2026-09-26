class Money:
    def __init__(self, amount):
        self.amount = amount

    def __add__(self, other):
        return Money(self.amount + other.amount)


money1 = Money(1000)
money2 = Money(2500)

money3 = money1 + money2

print("Total Money:", money3.amount)