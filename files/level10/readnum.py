try:
    with open("numbers.txt", "r") as file:
        for line in file:
            try:
                number = int(line.strip())
                print("Number:", number)

            except ValueError:
                print("Invalid data:", line.strip())

except FileNotFoundError:
    print("Error: File not found")