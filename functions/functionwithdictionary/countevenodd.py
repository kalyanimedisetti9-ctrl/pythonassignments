def count_even_odd(numbers):
    even = 0
    odd = 0

    for n in numbers:
        if n % 2 == 0:
            even += 1
        else:
            odd += 1

    return {"Even": even, "Odd": odd}

numbers = [1, 2, 3, 4, 5, 6, 7]

print(count_even_odd(numbers))