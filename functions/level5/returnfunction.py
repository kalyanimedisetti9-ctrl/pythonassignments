def outer():
    def inner():
        return "Hello from inner function"

    return inner

function = outer()
print(function())