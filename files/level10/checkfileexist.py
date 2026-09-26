import os

filename = "sample.txt"

if os.path.exists(filename):
    try:
        with open(filename, "r") as file:
            print(file.read())
    except PermissionError:
        print("Error: Permission denied")
else:
    print("File does not exist")