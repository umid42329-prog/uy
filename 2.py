# 2 masala


def ends_with_gram(words: list[str]) -> list[str]:
    result = []

    for word in words:
        if word.lower().endswith("gram"):
            result.append(word)

    return result


words = input("So'zlarni probel bilan ajratib kiriting: ").split()

print(ends_with_gram(words))
