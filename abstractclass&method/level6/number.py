class Number:
    def even_odd(self, n):
        if n % 2 == 0:
            return "Even"
        else:
            return "Odd"

    def prime(self, n):
        if n < 2:
            return False

        for i in range(2, n):
            if n % i == 0:
                return False

        return True

    def palindrome(self, n):
        if str(n) == str(n)[::-1]:
            return True
        else:
            return False

n = Number()

print("Even/Odd:", n.even_odd(10))
print("Prime:", n.prime(7))
print("Palindrome:", n.palindrome(121))