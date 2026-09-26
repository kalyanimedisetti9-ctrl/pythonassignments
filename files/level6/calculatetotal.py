numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100,
           11, 21, 31, 41, 51, 61, 71, 81, 91, 101]

with open("numbers.txt", "w") as file:
    for number in numbers:
        file.write(str(number) + "\n")

total = sum(numbers)

print("Total:", total)