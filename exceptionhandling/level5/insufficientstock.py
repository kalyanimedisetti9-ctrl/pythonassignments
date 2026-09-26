class InsufficientStockError(Exception):
    pass


class Product:
    def __init__(self, name, stock):
        self.name = name
        self.stock = stock

    def purchase(self, quantity):
        if quantity > self.stock:
            raise InsufficientStockError("Insufficient stock")

        self.stock -= quantity
        print("Purchase successful")
        print("Remaining Stock:", self.stock)


try:
    product = Product("Laptop", 10)

    quantity = int(input("Enter quantity: "))

    product.purchase(quantity)

except InsufficientStockError as e:
    print("Error:", e)