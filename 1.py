# 1 masala


def count_passing_students(grades: list[int], passingGrade: int) -> int:
    count = 0

    for grade in grades:
        if grade >= passingGrade:
            count += 1

    return count


grades = list(map(int, input("Talabalar ballarini kiriting: ").split()))

passingGrade = int(input("O'tish balini kiriting: "))

print("Imtihondan o'tgan talabalar soni:", count_passing_students(grades, passingGrade))
