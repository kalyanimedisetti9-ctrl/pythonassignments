def calculate(a, b):
    return a + b, a - b, a * b, a / b

sum_value, difference, product, division = calculate(20, 5)

print("Sum:", sum_value)
print("Difference:", difference)
print("Product:", product)
print("Division:", division)