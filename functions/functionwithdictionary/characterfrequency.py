def character_frequency(text):
    frequency = {}

    for ch in text:
        if ch in frequency:
            frequency[ch] += 1
        else:
            frequency[ch] = 1

    return frequency

print(character_frequency("hello"))