try:
    file = open("numbers.txt", "r")

    for line in file:
        try:
            number = int(line.strip())
            print("Number:", number)

        except ValueError:
            print("Error: Invalid number in file")

    file.close()

except FileNotFoundError:
    print("Error: File not found")

except PermissionError:
    print("Error: Permission denied")

except OSError:
    print("Error: File operation failed")