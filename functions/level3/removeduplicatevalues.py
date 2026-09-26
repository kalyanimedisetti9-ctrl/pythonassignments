def remove_duplicates(numbers):
    result = []

    for n in numbers:
        if n not in result:
            result.append(n)

    return result

print("Without duplicates:", remove_duplicates([1, 2, 2, 3, 4, 4, 5]))