class Person:
    def show_person(self):
        print("I am a person")


class Customer(Person):
    def __init__(self, name):
        self.name = name
        self.cart = ShoppingCart()

    def show_customer(self):
        print("Customer:", self.name)


class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class Electronics(Product):
    def show_product(self):
        print("Electronic:", self.name)


class Clothing(Product):
    def show_product(self):
        print("Clothing:", self.name)


class ShoppingCart:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def show_products(self):
        for product in self.products:
            print(product.name, "₹", product.price)

    def total_price(self):
        return sum(product.price for product in self.products)


class PaymentService:
    def pay(self, amount):
        print("Payment successful: ₹", amount)


class DeliveryService:
    def deliver(self, address):
        print("Order delivered to:", address)


class Order:
    def __init__(self, cart):
        self.cart = cart

    def checkout(self):
        total = self.cart.total_price()

        payment = PaymentService()
        payment.pay(total)

        delivery = DeliveryService()
        delivery.deliver("Rajahmundry")


# Create customer
customer = Customer("Kalyani")

customer.show_person()
customer.show_customer()

# Add products to customer's cart
laptop = Electronics("Laptop", 50000)
shirt = Clothing("Shirt", 1000)

customer.cart.add_product(laptop)
customer.cart.add_product(shirt)

# Show cart
print("\nShopping Cart:")
customer.cart.show_products()

print("Total: ₹", customer.cart.total_price())

# Create order
order = Order(customer.cart)

# Checkout
print("\nCheckout:")
order.checkout()