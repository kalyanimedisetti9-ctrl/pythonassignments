class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        return a / b

calculator = Calculator()

print("Addition:", calculator.add(20, 10))
print("Subtraction:", calculator.subtract(20, 10))
print("Multiplication:", calculator.multiply(20, 10))
print("Division:", calculator.divide(20, 10))