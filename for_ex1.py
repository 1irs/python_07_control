from typing import List

grades: List[int] = [
    5, 5, 4, 3, 4, 3, 2, 2, 5
]

grade_5 = 0
grade_4 = 0
grade_3 = 0
grade_2 = 0

for grade in grades:
    if grade == 5:
        grade_5 = grade_5 + 1
    elif grade == 4:
        grade_4 = grade_4 + 1
    elif grade == 3:
        grade_3 = grade_3 + 1
    elif grade == 2:
        grade_2 = grade_2 + 1

print('Пятерок', grade_5)
print('Четверок', grade_4)
print('Троек', grade_3)
print('Двоек', grade_2)
