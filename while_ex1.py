from typing import List

students: List[str] = [
    'Vladimir',
    'Yarik',
    'Vika'
]

i: int = 0

#     i < 3 (i=0, i=1, i=2)
while i < len(students):
    print('Индекс в памяти', i, 'а у нормальных людей', i+1, students[i])
    i = i + 1
