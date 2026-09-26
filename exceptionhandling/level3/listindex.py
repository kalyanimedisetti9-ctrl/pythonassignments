numbers = [10, 20, 30, 40, 50]

try:
    index = int(input("Enter index: "))
    print("Element:", numbers[index])

except ValueError:
    print("Error: Please enter an integer")

except IndexError:
    print("Error: Index is out of range")

except TypeError:
    print("Error: Invalid index type")

except Exception as e:
    print("Unexpected Error:", e)