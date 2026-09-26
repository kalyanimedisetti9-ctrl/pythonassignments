try:
    number = int(input("Enter a number: "))
    print("Number:", number)

except ValueError:
    print("Error: Invalid input")

finally:
    print("Finally block always executes")