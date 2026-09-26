file = None

try:
    file = open("sample.txt", "r")
    print(file.read())

except FileNotFoundError:
    print("Error: File not found")

except PermissionError:
    print("Error: Permission denied")

finally:
    if file is not None:
        file.close()
    print("File operation completed")