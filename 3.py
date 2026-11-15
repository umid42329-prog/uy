# 3 masala


def find_top_three_numbers_sorted(data: list) -> list:
    result = []

    for tup in data:
        top_three = sorted(tup, reverse=True)[:3]
        result.append(tuple(top_three))

    return result


data = []

n = int(input("Nechta tuple kiritasiz? "))

for i in range(n):
    numbers = tuple(map(int, input(f"{i + 1}-tuple sonlarini kiriting: ").split()))
    data.append(numbers)

print("Natija:", find_top_three_numbers_sorted(data))
