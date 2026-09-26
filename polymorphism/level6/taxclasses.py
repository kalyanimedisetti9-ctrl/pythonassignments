from abc import ABC, abstractmethod

class Tax(ABC):

    @abstractmethod
    def calculate_tax(self, amount):
        pass


class GST(Tax):
    def calculate_tax(self, amount):
        return amount * 0.18


class IncomeTax(Tax):
    def calculate_tax(self, amount):
        return amount * 0.10


class SalesTax(Tax):
    def calculate_tax(self, amount):
        return amount * 0.05


taxes = [GST(), IncomeTax(), SalesTax()]

for tax in taxes:
    print("Tax:", tax.calculate_tax(10000))