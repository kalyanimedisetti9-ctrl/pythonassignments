try:
    text = input("Enter a number: ")

    number = int(text)

    print("Integer value:", number)

except ValueError:
    print("Error: Invalid integer value")