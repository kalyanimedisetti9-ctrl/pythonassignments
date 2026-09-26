class StringOperations:
    def reverse(self, text):
        return text[::-1]

    def count_vowels(self, text):
        count = 0

        for char in text.lower():
            if char in "aeiou":
                count += 1

        return count

    def is_palindrome(self, text):
        return text.lower() == text.lower()[::-1]


operations = StringOperations()

text = "madam"

print("Original String:", text)
print("Reverse:", operations.reverse(text))
print("Vowels:", operations.count_vowels(text))
print("Palindrome:", operations.is_palindrome(text))