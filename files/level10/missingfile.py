filename = input("Enter filename: ")

try:
    with open(filename, "r") as file:
        print("\nFile contents:")
        print(file.read())

except FileNotFoundError:
    print("Error: File does not exist")

except PermissionError:
    print("Error: Permission denied")