class InsufficientStockError(Exception):
    pass


class Product:
    def __init__(self, name, stock):
        self.name = name
        self.stock = stock

    def purchase(self, quantity):
        try:
            if quantity > self.stock:
                raise InsufficientStockError("Insufficient stock")
            self.stock -= quantity
            print("Product:", self.name)
            print("Purchase successful")
            print("Remaining stock:", self.stock)
        except InsufficientStockError as e:
            print("Error:", e)


product = Product("Laptop", 10)
product.purchase(4)
product.purchase(8)