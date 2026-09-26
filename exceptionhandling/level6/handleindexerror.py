def access_element(items, index):
    try:
        print("Element:", items[index])
    except IndexError:
        print("Index is out of range")

numbers = [10, 20, 30]
access_element(numbers, 1)
access_element(numbers, 5)