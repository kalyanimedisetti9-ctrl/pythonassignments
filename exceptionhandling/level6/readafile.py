def read_file(filename):
    try:
        with open(filename, "r") as file:
            print(file.read())
    except FileNotFoundError:
        print("File not found")
    except PermissionError:
        print("Permission denied")

read_file("sample.txt")