from typing import List

best_students: List[str] = [
    'Vladimir',
    'Vika',
    'Yarik'
]

first_name: str = 'Vika'


# А проверить 2 студента через OR?
is_oleg_best: bool = 'Oleg' in best_students
is_yarik_best: bool = 'Yarik' in best_students

condition: bool = is_oleg_best or is_yarik_best

if condition:
    print('Распечатать сертификат для студента')
else:
    print('Увы, студент не заслуживает сертификат')
