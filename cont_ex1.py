from typing import List

numbers: List[int] = [
    2, 3, 7, 0, 11, 14, 17, 0, 12, 234, 0, 234
]

i: int = 0

# Напечатать на экран все элементы больше 5
for number in numbers:
    if number < 5:
        continue
    print(number)

print('Конец программы')
