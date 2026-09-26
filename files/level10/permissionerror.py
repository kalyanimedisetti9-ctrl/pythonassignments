try:
    file = open("sample.txt", "r")
    print(file.read())
    file.close()

except PermissionError:
    print("Error: Permission denied")

except FileNotFoundError:
    print("Error: File not found")