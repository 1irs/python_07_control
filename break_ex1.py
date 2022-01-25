from typing import List

numbers: List[int] = [
    2, 3, 7, 0, 11, 14, 17, 0, 12, 234, 0, 234
]

i: int = 0

# Найти ПЕРВЫЙ нулевой элемент.
for number in numbers:
    if number == 0:
        print('Первый нулевой элемент под индексом', i)
        break
    i = i + 1

print('Конец программы')
