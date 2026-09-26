class StringOperations:
    def reverse(self, text):
        return text[::-1]

    def count_vowels(self, text):
        count = 0

        for ch in text:
            if ch.lower() in "aeiou":
                count += 1

        return count

    def palindrome(self, text):
        if text == text[::-1]:
            return True
        else:
            return False

s = StringOperations()

print("Reverse:", s.reverse("hello"))
print("Vowels:", s.count_vowels("hello"))
print("Palindrome:", s.palindrome("madam"))