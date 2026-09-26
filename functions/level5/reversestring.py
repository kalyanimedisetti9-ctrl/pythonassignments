def reverse_string(text):
    if text == "":
        return ""
    return reverse_string(text[1:]) + text[0]

print("Reverse:", reverse_string("Python"))