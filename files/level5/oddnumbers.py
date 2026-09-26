with open("numbers.txt", "r") as file:
    numbers = file.readlines()

with open("odd.txt", "w") as file:
    for number in numbers:
        number = int(number.strip())

        if number % 2 != 0:
            file.write(str(number) + "\n")

print("Odd numbers written successfully")