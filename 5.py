# 5 masala

def find_nearest_vowel(letter: str) -> str:
    vowels = "aeiou"

    if len(letter) != 1 or letter < "a" or letter > "z":
        return "faqat bitta kichik harf bo‘lishi kerak"

    nearest = vowels[0]
    min_distance = abs(ord(letter) - ord(nearest))

    for vowel in vowels:
        distance = abs(ord(letter) - ord(vowel))

        if distance < min_distance:
            min_distance = distance
            nearest = vowel

    return nearest


letter = input("Bitta kichik harf kiriting: ")
print(find_nearest_vowel(letter))