class Temperature:
    def celsius_to_fahrenheit(self, celsius):
        return (celsius * 9 / 5) + 32

    def fahrenheit_to_celsius(self, fahrenheit):
        return (fahrenheit - 32) * 5 / 9


temperature = Temperature()

celsius = 25
fahrenheit = 77

print("Celsius:", celsius)
print("Fahrenheit:", temperature.celsius_to_fahrenheit(celsius))

print()

print("Fahrenheit:", fahrenheit)
print("Celsius:", temperature.fahrenheit_to_celsius(fahrenheit))