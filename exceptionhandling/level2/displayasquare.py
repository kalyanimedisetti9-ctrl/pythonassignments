try:
    number = int(input("Enter a number: "))

except ValueError:
    print("Error: Please enter a valid number")

else:
    square = number * number
    print("Square:", square)