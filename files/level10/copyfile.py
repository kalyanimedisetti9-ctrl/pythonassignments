try:
    source = input("Enter source filename: ")
    destination = input("Enter destination filename: ")

    with open(source, "r") as source_file:
        data = source_file.read()

    with open(destination, "w") as destination_file:
        destination_file.write(data)

    print("File copied successfully")

except FileNotFoundError:
    print("Error: Source file not found")

except PermissionError:
    print("Error: Permission denied")

except OSError as e:
    print("File operation error:", e)