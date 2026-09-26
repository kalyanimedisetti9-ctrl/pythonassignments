numbers = [10, 20, 30, 40, 50]

try:
    index = int(input("Enter index: "))
    print("Element:", numbers[index])

except ValueError:
    print("Error: Enter a valid index")

except IndexError:
    print("Error: Index is out of range")

finally:
    print("List operation completed")