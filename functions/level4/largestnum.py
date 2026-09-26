def largest(*args):
    result = args[0]

    for n in args:
        if n > result:
            result = n

    return result

print("Largest:", largest(10, 50, 20, 40, 30))