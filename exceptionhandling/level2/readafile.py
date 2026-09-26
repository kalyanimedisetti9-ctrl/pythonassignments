try:
    file = open("student.txt", "r")

except FileNotFoundError:
    print("Error: File not found")

else:
    print("File contents:")
    print(file.read())

finally:
    print("File operation completed")