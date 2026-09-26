with open("numbers.txt", "r") as file:
    numbers = [int(line.strip()) for line in file]

positive = 0
negative = 0
zero = 0

for number in numbers:
    if number > 0:
        positive += 1
    elif number < 0:
        negative += 1
    else:
        zero += 1

print("Positive numbers:", positive)
print("Negative numbers:", negative)
print("Zero values:", zero)