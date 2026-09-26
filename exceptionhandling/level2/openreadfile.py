try:
    file = open("student.txt", "r")

    print("File Contents:")
    print(file.read())

except FileNotFoundError:
    print("Error: The file does not exist")

else:
    print("File read successfully")

finally:
    print("File operation completed")