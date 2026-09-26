numbers = {}

for num in range(1, 6):
    numbers[num] = num ** 2

print("Numbers and Squares:")

for key, value in numbers.items():
    print(key, ":", value)