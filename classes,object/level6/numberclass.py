class Number:
    def __init__(self, number):
        self.number = number

    def is_even(self):
        return self.number % 2 == 0

    def is_odd(self):
        return self.number % 2 != 0

    def is_prime(self):
        if self.number < 2:
            return False

        for i in range(2, int(self.number ** 0.5) + 1):
            if self.number % i == 0:
                return False

        return True

    def is_palindrome(self):
        return str(self.number) == str(self.number)[::-1]


number = Number(121)

print("Number:", number.number)
print("Even:", number.is_even())
print("Odd:", number.is_odd())
print("Prime:", number.is_prime())
print("Palindrome:", number.is_palindrome())