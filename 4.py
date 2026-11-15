# 4 masala


def calculate_painting_time(pattern: list) -> int:
    if not pattern:
        return 0

    time = len(pattern) * 2

    for i in range(1, len(pattern)):
        if pattern[i] != pattern[i - 1]:
            time += 1

    return time


n = int(input("Nechta kvadrat bo'yaladi? "))

pattern = []

for i in range(n):
    color = input(f"{i + 1}-kvadrat rangini kiriting: ")
    pattern.append(color)

print("Umumiy vaqt:", calculate_painting_time(pattern), "soniya")
