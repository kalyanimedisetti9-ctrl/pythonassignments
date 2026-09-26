with open("numbers.txt", "r") as file:
    numbers = [int(line.strip()) for line in file]

with open("even.txt", "w") as even_file:
    with open("odd.txt", "w") as odd_file:

        for number in numbers:
            if number % 2 == 0:
                even_file.write(str(number) + "\n")
            else:
                odd_file.write(str(number) + "\n")

print("Even and odd numbers separated successfully")